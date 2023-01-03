import board

from .switches.gpio import GPIO as Switches
from .display.keybow2040 import Keybow2040 as Display

from . import PMK

# These are the 16 switches on Keybow, with their board-defined names.
# indexed from the bottom left, going up, then across
# _PINS = [board.SW0,
#         board.SW1,
#         board.SW2,
#         board.SW3,
#         board.SW4,
#         board.SW5,
#         board.SW6,
#         board.SW7,
#         board.SW8,
#         board.SW9,
#         board.SW10,
#         board.SW11,
#         board.SW12,
#         board.SW13,
#         board.SW14,
#         board.SW15]

# indexed from the top left, going across, then down
_PINS = [
        board.SW3, 
        board.SW7, 
        board.SW11, 
        board.SW15, 
        board.SW2, 
        board.SW6, 
        board.SW10,
        board.SW14, 
        board.SW1, 
        board.SW5, 
        board.SW9,
        board.SW13, 
        board.SW0, 
        board.SW4, 
        board.SW8, 
        board.SW12 
    ]

class Keybow2040(PMK):
    def __init__(self):
        self._i2c = board.I2C()
        self._switches = Switches(_PINS)
        self._display = Display(self._i2c)
