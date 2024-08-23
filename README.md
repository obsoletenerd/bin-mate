# Bin Mate

**Bin Mate** is a multi-MCU (ESP32, RPi Pico, more soon) bin reminder tool. Initially for Ballarat in Victoria AU but hopefully rolling out to more cities soon. It is an open source software/hardware project connecting to local council APIs to remind you which bins to put out on which days.

The project can be as simple as buying an RPi Pico + a click-on e-Paper hat (see "[/RPi Pico](https://github.com/senwerks/Bin-Mate/tree/main/RPi%20Pico)"), up to a fully-custom PCB you can self-solder or buy as a kit (Soon™).

## Current Status

- **DIY Pico version** works and is "finished" (but will get updates as I think of things)
- **DIY ESP32 version** has been prototyped and is being worked on now (mid 2024)
- **ESP32 Kit version** will come Soon™

## Raspberry Pi Pico DIY Version

![Photo of the Bin-Mate "DIY Pico" version](https://github.com/senwerks/Bin-Mate/blob/main/RPi%20Pico%20Assets/bin-mate-pico.jpg?raw=true)

#### Ingredients
This is the easiest way to get started with this project, using just:
- [RPi Pico W](https://core-electronics.com.au/raspberry-pi-pico-w-wireless-wifi.html) (WiFi model)
- [Waveshare Pico e-Paper 2.13in Hat](https://core-electronics.com.au/waveshare-2-13inch-e-paper-module-for-raspberry-pi-pico-250x122-black-white.html).
- 3D printed case ([Base](https://github.com/senwerks/Bin-Mate/blob/main/RPi%20Pico%20Assets/Bin-Mate%20Pico%20Case%20(Base).3mf) and [Top](https://github.com/senwerks/Bin-Mate/blob/main/RPi%20Pico%20Assets/Bin-Mate%20Pico%20Case%20(Top).3mf))

#### Instructions
- [Install MicroPython](https://core-electronics.com.au/guides/how-to-setup-a-raspberry-pi-pico-and-code-with-thonny/) onto the RPi Pico using [Thonny](https://thonny.org) (or your tool of choice)
- Create a file called "secrets.py" in the [project folder](https://github.com/senwerks/Bin-Mate/tree/main/RPi%20Pico) and put the following code into it (with your address):

```
ADDRESS = "123 Sturt Street Ballarat Central"
SSID = "WiFiSSID"
PASS = "Password!"
```

- Copy the [project folder](https://github.com/senwerks/Bin-Mate/tree/main/RPi%20Pico) onto the Pico.
- 3D print the [included case](https://github.com/senwerks/Bin-Mate/tree/main/RPi%20Pico%20Assets), or bonus brownie points if you design/make your own
- Plug it into any USB plug for power (or if you're RPi-savvy, wire up some batteries)
  .. and you're up!

The first WiFi connection can take 10-20 seconds (then it caches your details), and the e-Paper display can take a few seconds to update, so be patient. e-Paper is incredibly technology but it's not fast.

If you do create this project, please share it with me either via Mastadon (https://hackerspace.au/@sen) or post it in an [Issue here](https://github.com/obsoletenerd/Bin-Mate/issues).

#### Creating New Graphics

The project now uses PBM files for the graphics. You can do direct-replacement of the included graphics by creating 3 BMP images that are 60px wide and 200 high (they're displayed sideways). Put the BMP files in the same folder as my [BMP-to-PBM script](https://github.com/senwerks/BMP-to-PBM) and run the script as per the instructions (or use an online converter). Copy those outputted PBM files onto the RPi Pico in the /gfx folder, using the same names as the files already in there. If they look inverted, use the [invert-pbm.py](https://github.com/senwerks/BMP-to-PBM/blob/main/invert-pbm.py) script to flip the black/white bits.


## ESP32 Versions

For a version of the project that can run off batteries for many months, we're developing both DIY and custom-PCB versions using an ESP32 and utilising all the deepsleep/low-power trickery, along with larger multi-colour e-Paper displays.

You will be able to order them pre-built, or solder together yourself. Both the DIY and custom-PCB versions have been prototyped and are in progress, and will be published when there's something functional to share.

