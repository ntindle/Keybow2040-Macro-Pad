
<Center>
<h1>KEYBOW 2040 MACRO PAD</h1>
<h3>This repo contains all the code for turning a Keybow 2040 into a fully fledged data-driven macropad.</h3>
    <div>
        <img src="./.github/img.jpg"/>
    </div>
    Special thanks to <a href= "https://www.printables.com/social/1358-manelto/models">ManelTo</a> for the designs!

    Huge thanks to the many software devs that contributed to this project:
    Neradoc for the Control Codes
    A lot of Adafruit Devs for the CircuitPython Libraries
    ManelTo for the starting source code
</Center>

<h2>Requirements</h2>

### Hardware
- [Keybow 2040 by Pimoroni](https://shop.pimoroni.com/products/keybow-2040?variant=32399559589971)
- [I2C Stemma QT Rotary Encoder Breakout with NeoPixel - STEMMA QT / Qwiic](https://www.adafruit.com/product/4991)
- [Monochrome 0.96" 128x64 OLED Graphic Display - STEMMA QT](https://www.adafruit.com/product/326)
- [A Rotery Encoder with Push Button](https://www.adafruit.com/product/377)
- [SparkFun Qwiic Cable Kit](https://www.sparkfun.com/products/15081)
- [10mm M2 Hex Bolts](https://www.amazon.com/dp/B07W5HBRMP)
- [M2.5 Flat Top Screws](https://www.amazon.com/dp/B089QX453K)
- [USB C Cable](https://pine64.com/product/usb-type-c-to-usb-type-c-silicone-power-charging-cable-1-5-meter-length/)
- [Knob](https://www.alibaba.com/product-detail/Factory-machinig-solid-anodized-aluminum-knurled_62498933495.html?spm=a2700.galleryofferlist.normal_offer.d_title.f19016dbZNflhI)

### Tools
- [3D Printer](https://www.creality3dofficial.com/products/official-creality-ender-3-3d-printer)
- [Screwdriver](https://www.ifixit.com/products/repair-business-toolkit)
- [Soldering Iron](https://pine64.com/product/pinecil-smart-mini-portable-soldering-iron/)
- [Solder](https://www.microcenter.com/product/659263/chip-quick-solder-wire-no-clean-0020-1-oz)
- [Flux](https://www.microcenter.com/product/657250/caig-laboratories-deoxit-brand-no-clean-rma-soldering-flux-in-syringe-applicator)
- [Solder Stand](https://www.microcenter.com/product/659033/eclipse-enterprise-mini-soldering-stand-with-sponge)

### 3D Prints
- [Keybow2040 MacroPad with display and encoder](https://www.printables.com/model/228327-keybow2040-macropad-with-display-and-encoder)


<h2>Printing</h2>

Print the [files](https://www.printables.com/model/228327-keybow2040-macropad-with-display-and-encoder/files) ManelTo created. The file names are in Spanish but you will need to print:

- cajaKeyBow-Anexos.stl
- cajaKeyBow-Caja.stl

If you would like a tilt-stand, one of:

- cajaKeyBow.FCStd (10 mm foot)
- cajaKeyBow-pie5mm.stl (5mm foot)

<h2>Assembly</h2>

Once the prints are completed, remove the plugs from the various holes in the prints. There are two holes on the right side that are a bit of a challenge to remove. I ended up using tweezers to pull the plugs out. It took some time. 

Next, set your soldering iron to just above the melting temperature of the filament you used. Then align a 2.5 mm insert for 12 pegs on the front and back cases and push them in with the soldering iron.

If you are confused on the process, watch [this video](https://www.youtube.com/watch?v=ba4TdnjzdjI).

Solder a cut off QT stemma connector to the pins on the KEYBOW 2040. You will need a good amount of space so I recommend using the 200mm or 150mm cables. The breakout of the connectors is:

| Black | Red | Blue | Yellow |
| ----- | --- | ---- | ------ |
GND | 3.3V | SDA | SCL

Secure everything down with the appropriate screws, then hook it all up with the cables from the kit. It'll be a tight fit inside so be careful and don't use too much force. THere are paths to run cables around the various pieces if you are patient.

<h2>Programming</h2>

First, update your Keybow 2040 to CircuitPython 7.3.3 using the firmware found [here](https://circuitpython.org/board/pimoroni_keybow2040/).

Next, copy all the files in this repo (except the `.github` folder) onto the board, replace any existing files. 

Finally, customize the `maps.json` as you see fit. 


<h3><kbd>maps.json</kbd></h3>
The `maps.json` file is what drives the macro pad. It is a json object made of one or more layers. 

```json
{
    "layers": [
        ...
    ]
}
```

<h4><kbd>layers</kbd></h4>
A layer is defined by a few things.

- "name": "The short name of the layer shown when switching layers"
  ```json
  "name": "General",
  ```
- "description": "A internally unused description of the layer that can be longer"
  ```json
  "description": "General Keybinds",
  ```
- "color": An RGB Color code split into a 3 segment array that sets the encoder color
  ```json
  "color": [
                255,
                255,
                0
            ],
  ```
- "keymap": A 16 length array of control commands. This value must be exactly 16 commands. Leave the others listed as unused as described below if needed.
    <details>
    <summary>
    Example Keymap
    </summary>

    ```json
    "keymap": [
                    {
                        "label": "Ins.",
                        "type":"key",
                        "keys": [
                            "INSERT"
                        ],
                        "color": [ 0, 0 , 255]
                    },
                    {
                        "label": "Home",
                        "type":"key",
                        "keys": [
                            "HOME"
                        ]
                        ,
                        "color": [ 0, 0 , 255]
                    },
                    {
                        "label": "PgUp",
                        "type":"key",
                        "keys": [
                            "PAGE_UP"
                        ],
                        "color": [ 0, 0 , 255]
                    },
                    {
                        "label": "()",
                        "type": "text",
                        "text": "()",
                        "color": [ 255, 0, 0]
                    },
                    {
                        "label": "Del",
                        "type": "key",
                        "keys": [
                            "DELETE"
                        ],
                        "color": [ 0, 0 , 255]
                    },
                    {
                        "label": "End",
                        "type": "key",
                        "keys": [
                            "END"
                        ],
                        "color": [ 0, 0, 255]
                    },
                    {
                        "label": "PgDn",
                        "type": "key",
                        "keys": [
                            "PAGE_DOWN"
                        ],
                        "color": [ 0, 0 , 255]
                    },
                    {
                        "label": "Win",
                        "type": "key",
                        "keys": [
                            "GUI"
                        ],
                        "color": [ 0, 0 , 255]
                    },
                    {
                        "label": "Ctrl",
                        "type": "key",
                        "keys": [
                            "CONTROL"
                        ],
                        "color": [ 0, 0 , 255]
                    },
                    {
                        "label": "Alt",
                        "type": "key",
                        "keys": [
                            "ALT"
                        ],
                        "color": [ 0, 0, 255]
                    },
                    {
                        "label": "ArrUp",
                        "type": "key",
                        "keys": [
                            "UP_ARROW"
                        ],
                        "color": [ 255, 255, 255]
                    },
                    {
                        "label": "Pause",
                        "type": "key",
                        "keys": [
                            "PAUSE"
                        ],
                        "color": [ 0, 0, 255]
                    },
                    {
                        "label": "Shift",
                        "type": "key",
                        "keys": [
                            "SHIFT"
                        ],
                        "color": [ 0, 0, 255]
                    },
                    {
                        "label": "LftAr",
                        "type": "key",
                        "keys": [
                            "LEFT_ARROW"
                        ],
                        "color": [ 255, 255, 255]
                    },
                    {
                        "label": "DwnAr",
                        "type": "key",
                        "keys": [
                            "DOWN_ARROW"
                        ],
                        "color": [ 255, 255, 255]
                    },
                    {
                        "label": "RigAr",
                        "type": "key",
                        "keys": [
                            "RIGHT_ARROW"
                        ],
                        "color": [ 255, 255, 255]
                    }
                ],
    ```
    </details>

- "encoder_down_action": A control command with the `type` and required pair (`keys`, `text` or `control`) that is run when the knob is turned counter-clockwise
  ```json
  "encoder_down_action": {
                "type": "control",
                "control": "VOLUME_DOWN"
            }
  ```

- "encoder_up_action": A control command with the `type` and required pair (`keys`, `text` or `control`) that is run when the knob is turned clockwise
  ```json
  "encoder_up_action": {
                "type": "control",
                "control": "VOLUME_UP"
            }
  ```

## Control Commands
A control command is defined in `lib/macro_pad/control.py`. I encourage you to take a look. 

A control command is composed of a few parts.

- `label`: The label shown when the command is displayed on the OLED screen
- `type`: one of `key`, `text`, or `control`
  - `key` will any number of keys and release them when the key is released
  - `text` will type the message as if it is the keyboard
  - `control` will send a ConsumerControl HID code.
- `color`: The color the interaction will change a key to when pressed
- `keys`: Required for `type=key`. An array of keys that can be pressed. The valid options are listed in `lib/adafruit_hid/keycode.py`. These keys will act as if they were typed on a US_en keyboard. (If you need something else, look into using [Neradoc's library](https://github.com/Neradoc/Circuitpython_Keyboard_Layouts)).

  A parentheses `(` could be typed with the `keys`
  ```json
   "keys": [
        "SHIFT",
        "NINE"
   ]
  ```
- `text`: Required for `type=text`. A string of text to be sent by the macropad
  ```json
  "text": "Hello world"
  ```
- `control`: Required for `type=control`. A Consumer control code as found in `lib/adafruit_hid/consumer_control_code.py`. There are more of them not listed in that file, if you find one you need, feel free to open a PR. The [HID Usage Tables for Universal Serial Bus (USB)](https://www.usb.org/sites/default/files/hut1_22.pdf) if needed.
  ```json
  "control": "VOLUME_DOWN"
  ```


## Debugging
Open a serial connection with baud `9600` to the device and you can see error messages get printed 