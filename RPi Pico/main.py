#   .-------------.---------------------------------------------.
#   | Project     |   Bin Mate / main.py                        |
#   | Author      |   SenWerks - senwerks.com                   |
#   | Description |   Which bins are being collected next?      |
#   | Source      |   https://github.com/senwerks/Bin-Mate      |
#   |-------------|---------------------------------------------|
#   | Version     |   V0.9                                      |
#   | Release     |   2023-02-24                                |
#   | Updated     |   2024-03-26                                |
#   '-------------'---------------------------------------------'

# TODO: Replicate basic functionality of ESP32 WiFi manager using https://github.com/miguelgrinberg/microdot
#       Eg:
#        - If no internet, throw up an AP with kiosk webpage to config wifi, show AP on display
#        - If yes internet, serve webpage on local IP to edit address/wifi/etc and see debug info
#        - Any other errors, show on the display (address not found, API down, etc)
# TODO: Create final graphics/layout now that it all basically works

from machine import Pin, SPI, lightsleep, RTC
import framebuf
import utime
import network
import urequests

from pico_epaper import EPD_2in13
import secrets  # WiFi and User Details from secrets.py

# Show the user we're doing work now...
led = Pin("LED", Pin.OUT)


def do_wifi(epd):
    rp2.country("AU")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(pm=0xA11140)  # WiFi power-saving mode off if needed
    try:
        wlan.connect(secrets.SSID, secrets.PASS)
        for _ in range(100):  # Wait for 10 seconds max
            if wlan.isconnected():
                return wlan  # Successfully connected
            utime.sleep(0.1)
        else:
            # Connection failed
            raise RuntimeError("WiFi connection failed")
    except Exception as e:
        # Show errors in console
        print(f"WiFi Error: {e}")
        # Show errors on the ePaper display
        show_error(epd, message1="WiFi Error:", message2=e)
        return None


def pbm_draw(x_pos, y_pos, file, epd, white):
    with open(file, "rb") as f:
        # Skip the 'P4\n' part of the header
        f.readline()
        # Read and process the dimensions
        dimensions = f.readline().decode("utf-8").strip()
        width, height = map(int, dimensions.split())

        # Read the image data
        data = bytearray(f.read())

    # Create a frame buffer from the binary data
    fbuf = framebuf.FrameBuffer(data, width, height, framebuf.MONO_HLSB)

    # Use the blit method to draw the image at the specified position
    # Note: Ensure 'epd' and 'white' are correctly defined in your context
    epd.blit(fbuf, x_pos, y_pos, white)


def show_results(day, date, bin1, bin2, epd):
    bin1logo = "/gfx/" + bin1.lower() + ".pbm"
    bin2logo = "/gfx/" + bin2.lower() + ".pbm"

    epd.fill(0xFF)
    epd.text("Next Pick-Up:", 4, 4, 0x00)
    epd.text(f"{day} {date}", 4, 16, 0x00)

    print(f"----- Drawing {bin1logo}")
    pbm_draw(0, 28, bin1logo, epd, 0xFF)
    print(f"----- Drawing {bin2logo}")
    pbm_draw(64, 28, bin2logo, epd, 0xFF)

    epd.display(epd.buffer)


def show_error(epd, message1="", message2=""):
    epd.fill(0xFF)
    epd.text("ERROR:", 4, 8, 0x00)
    epd.text(message1, 4, 18, 0x00)
    epd.text(message2, 4, 28, 0x00)
    epd.display(epd.buffer)


def main():
    epd = EPD_2in13()
    epd.init(epd.full_update)

    wlan = do_wifi(epd)
    if wlan is None:
        return  # Stop execution if WiFi connection failed

    status = wlan.ifconfig()
    msg_network_status = 1
    msg_device_ip = status[0]
    print("----- Device IP: " + msg_device_ip)

    address = secrets.ADDRESS.replace(" ", "%20")

    # Get the JSON Data from the Ballarat Council API
    bin_data_url = (
        "https://data.ballarat.vic.gov.au/api/records/1.0/search/?sort=propnum&q="
        + address
        + "&rows=100&dataset=waste-collection-days&timezone=Australia/Melbourne&lang=en"
    )
    print("----- Pulling JSON from:")
    print(bin_data_url)

    try:
        r = urequests.get(bin_data_url)
        if r.status_code == 200:
            print("----- Data fetched successfully")
            bin_data_json = r.json()
        else:
            # Handle non-200 responses appropriately
            raise Exception(
                "Failed to fetch data: HTTP status code " + str(r.status_code)
            )
    finally:
        r.close()  # Ensure the request is closed even if an error occurs

    print("----- Raw JSON data pulled from API:")
    print(bin_data_json)

    address_hits = bin_data_json["nhits"]
    if address_hits == 1:
        # Confirm we found a single matching address
        msg_address_found = bin_data_json["records"][0]["fields"]["address"].replace(
            "%20", " "
        )
        print(f"----- Found Address: {msg_address_found}")

        # Get the pickup day
        msg_collectionday = bin_data_json["records"][0]["fields"]["collectionday"]

        # Get the individual bin pickup dates
        msg_waste_data = bin_data_json["records"][0]["fields"]
        msg_dates = {
            "Green": msg_waste_data["nextgreen"],
            "Waste": msg_waste_data["nextwaste"],
            "Recycle": msg_waste_data["nextrecycle"],
        }
        # Which date is the next collection day
        soonest_date = min(msg_dates.values())
        soonest_bin = [
            bin_type for bin_type, date in msg_dates.items() if date == soonest_date
        ][0]

        msg_collectionday = msg_collectionday[:3]
        print(
            f"----- The next {soonest_bin} bin pickup is on {msg_collectionday} {soonest_date}."
        )

        sorted_bins = sorted(msg_dates.items(), key=lambda x: x[1])[:2]
        bin1_type, bin1_date = sorted_bins[0]
        bin2_type, bin2_date = sorted_bins[1]
        show_results(msg_collectionday, bin1_date, bin1_type, bin2_type, epd)
    else:
        show_error(epd, message1="Error:", message2="Address Not Found")
        print("ERROR: Address Not Found, or found more than 1 match!")

    epd.delay_ms(2000)
    epd.sleep()

    # Properly disconnect WiFi and prepare for sleep
    wlan.disconnect()
    wlan.active(False)

    # Turn off LED to indicate we're done
    led.off()

    # Go to light sleep for 3 hours
    print("..zzZZZzz.. Going to sleep for 3 hours ..zzZZZzz.. ")
    lightsleep(3 * 60 * 60 * 1000)  # 3 hours in milliseconds


# Run the main function
if __name__ == "__main__":
    while True:
        main()
