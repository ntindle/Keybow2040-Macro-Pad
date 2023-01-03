import board
import displayio
import terminalio
i2c = board.I2C()  # uses board.SCL and board.SDA
# Initalize the encoders
from lib.adafruit_seesaw import seesaw, rotaryio, digitalio, neopixel
from rainbowio import colorwheel
seesaw = seesaw.Seesaw(i2c, 0x36)
seesaw.pin_mode(24, seesaw.INPUT_PULLUP)
button = digitalio.DigitalIO(seesaw, 24)
button_held = False

pixel = neopixel.NeoPixel(seesaw, 6, 1)
pixel.brightness = 0.5

encoder = rotaryio.IncrementalEncoder(seesaw)
last_position = None

print(pixel.fill(colorwheel(45)))

while True:
    print(encoder.position * -1 )
    pixel.fill(colorwheel(encoder.position * -1))
    print(button.value)

