# Bin Mate
### by BallaratMade

 
 
Bin Mate is a multi-MCU (ESP32, RPi Pico, more soon) bin reminder. Initially for Ballarat in Victoria AU but hopefully rolling out to more cities soon. It is an open sourcesoftware/hardware project connecting to local council APIs to remind you which bins to put out on which days.

The project can be as simple as buying an RPi Pico + a click-on e-Paper hat, up to a fully-custom PCB you can self-solder or buy as a kit that runs for months on a coin cell battery and sticks to your fridge with a magnet.

## Raspberry Pi Pico W + Waveshare Pico e-Paper 2.13in Hat

![image](https://user-images.githubusercontent.com/46561474/231915121-d6996989-cdba-4584-a00a-9060e527b8db.png)

This is the easiest way to get started with this project, using just an [RPi Pico W](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html) (WiFi model) and a [Waveshare Pico e-Paper 2.13in Hat](https://www.waveshare.com/pico-epaper-2.13.htm). Install MicroPython onto the RPi Pico, add your address and wifi details to the code, then copy the code onto the Pico. Plug it into any USB plug for power (or if you're RPi-savvy, wire up some batteries) and you're running.

We have also designed a few different 3D printable cases or a laser-cut wooden case to pretty the project up, both of which take a magnet on the back to stick to your fridge or use double-sided tape to put it up wherever you want.

(Link here when tested/working)
 
 

## ESP32 + 2.9" e-Paper Module

For a version of the project that can run off a coin-cell battery for many months, we're developing a custom PCB with an ESP32 onboard utilising all the deep sleep trickery, along with a cheap 2.9" e-Paper module, to create a device that can stick to your fridge or back door and requires no wiring. PCB designs and code will all be open-sourced and added here when we have it working.
