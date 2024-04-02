# Bin Mate

Bin Mate is a multi-MCU (ESP32, RPi Pico, more soon) bin reminder tool. Initially for Ballarat in Victoria AU but hopefully rolling out to more cities soon. It is an open source software/hardware project connecting to local council APIs to remind you which bins to put out on which days.

The project can be as simple as buying an RPi Pico + a click-on e-Paper hat (see "[/RPi Pico](https://github.com/senwerks/Bin-Mate/tree/main/RPi%20Pico)"), up to a fully-custom PCB you can self-solder (Soon™) or buy as a kit (Soon™) that runs for months on a rechargeable battery or can be plugged in to any USB power.

## Raspberry Pi Pico W + Waveshare Pico e-Paper 2.13in Hat

This is the easiest way to get started with this project, using just an [RPi Pico W](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html) (WiFi model) and a [Waveshare Pico e-Paper 2.13in Hat](https://www.waveshare.com/pico-epaper-2.13.htm).

- Install MicroPython onto the RPi Pico using Thonny (or your tool of choice)
- Create a file called "secrets.py" and put the following code into it:

```
ADDRESS = "123 Sturt Street Ballarat Central"
SSID = "WiFiSSID"
PASS = "Password!"
```

- Copy the code onto the Pico.
- 3D print the included case, or bonus brownie points if you design/make your own
- Plug it into any USB plug for power (or if you're RPi-savvy, wire up some batteries)
  .. and you're up!

If you do create this project, please share it with me either via Mastadon (https://hackerspace.au/@sen) or post it in an [Issue here](https://github.com/obsoletenerd/Bin-Mate/issues).

## ESP32 + 2.9" e-Paper Module

For a version of the project that can run off a single battery for many months, we're developing a custom PCB with an ESP32 onboard utilising all the deep sleep trickery, along with a cheap 2.9" e-Paper module, that you will be able to order assembled or solder together yourself. It will throw up its own Wifi AP with a dashboard for configuration and customisation. PCB designs and code will all be open-sourced and added here soon.

## Notes

### Creating New Graphics

The project now uses PBM files for the graphics. You can do direct-replacement of my graphics by creating 3 BMP images that are 64px wide and 220 high (they're displayed sideways). Put the BMP files in the same folder as my [BMP-to-PBM script](https://github.com/senwerks/BMP-to-PBM) and run the script as per the instructions. Copy those outputted PBM files onto the RPi Pico in the /gfx folder, using the same names as the files already in there.
