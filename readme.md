# ConnectEd Code Demo Wrappers

## An simple example wrapper
You can have a look at [analogInput.py](analogInput.py) to see an example of a simple wrapper.

It lets students create an analog input, and read from it using two different methods.

It also changes the pin supplied to upper case, to prevent a common frustration.

## A more complex wrapper
The file [potentiometer.py](potentiometer.py) contains a wrapper that builds on the AnalogInput class. Like with any other project, inheritance and composition can be used to simplify various wrappers, and keep them consistent.

Our method here uses default arguments so that students can have start using the method with as little hassle as possible, and it can be introduced later.

## Bundling them together
To prevent having multiple lines of inputs, an easy source of errors, we have a single file [connectedcode.py](connectedcode.py), which bundles the various wrappers together. It also has a few imports of its own to pass things along (such as the face buttons of the Kookaberry) without adding complexity.

These functions can hide the complexity of some wrappers, or can let you intoduce students to specific components by their actual names, even if they might be using the same wrapper.

## Precompiled files
In the [precompiled](precompiled) folder exist a small collection of `.mpy` files. These are some additional wrappers that are free to be used[^1]. These wrappers are designed for Kookaberries, but you _might_ be able to get them working on Micro:Bits or other devices. I make no promises, but I'd love to hear about it if you do.

### Reference:
Here's a quick reference guide to the precompiled wrappers. These are all available with `from connectedcode import *`

#### Radio

| Method | Description |
| :---: | :--- |
| `radio = start_radio()` | Initialises the radio. No arguments needed. |
| `radio.set_channel(channel)` | Sets the radio's channel to `channel`. |
| `radio.send_message(message)` | Broadcasts `message`. If `message` is too long, it prints a message to console, but does not raise an error. |
| `radio.get_message()` | Returns any message received on the radio, or `None` if none available. |

#### Digital Input

| Method | Description |
| :---: | :--- |
| `my_input = connect_digital_input(pin)` | Initialises the digital input. Pin takes the ID of the pin. e.g. `"P1"` or `"P4"`. Can be set to pull-up with the kwarg `pull="up"`. Default or other value results in pull-down. |
| `my_input.is_pressed()` | Equivalent to normal `is_pressed()`. Returns current state of the input. |
| `my_input.was_pressed()` | Equivalent to normal `was_pressed()`. Returns if the state has been high since the last time `was_pressed` was called. |

#### Analog Input

| Method | Description |
| :---: | :--- |
| `my_input = connect_analog_input(pin)` | Initialises the analog input. Pin takes the ID of the pin. e.g. `"P1"` or `"P4"`. |
| `my_input.read()` | Returns the raw value of the pin as a 16-bit integer (range from 0 to 65535) |
| `my_input.read_percentage()` | Reads the value then converts it to a percentage value. |

#### Potentiometer
Subclasses from [Analog Input](#### Analog Input)

| Method | Description |
| :---: | :--- |
| `pot = connect_potentiometer(pin)` | Initialises the potentiometer. Pin takes the ID of the pin. e.g. `"P1"` or `"P4"`. |
| `my_input.read_step()` | Reads the value and then converts it to a range from 1-20. Can have an alternate number of steps with the kwarg `steps=50`. `steps` must be an integer > 1. |

#### NeoPixel Bar Light

This wrapper is vastly over-engineered. While not 100% foolproof, these methods can receive a colour in almost any RGB-based format, and any python format, and will handle it. If you find a format that doesn't work, let me know! I'd love to make it even more robust!

| Method | Description |
| :---: | :--- |
| `bar = connect_bar_light(pin)` | Initialises an 8-pixel NeoPixel module. Pin takes the ID of the pin. e.g. `"P1"` or `"P4"`. |
| `my_input.fill(red, green, blue)` | Sets all neopixels to the given RGB colour. `red`, `green`, and `blue` can be separate arguments, or a single tuple or list. |
| `my_input.set_pixel(pixel, red, green, blue)` | Sets a specific neopixel to the given RGB colour. `pixel` is an integer 0-7. `red`, `green`, and `blue` can be separate arguments, or a single tuple or list. |
| `my_input.clear()` | Turns off all the neopixels. |

[^1]: All work is provided ​“AS IS”. ConnectedCode makes no other warranties, express or implied, and hereby disclaims all implied warranties, including any warranty of merchantability and warranty of fitness for a particular purpose.