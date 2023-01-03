from lib.macro_pad import data
from lib.pmk import PMK
from pmk.platform.keybow2040 import Keybow2040
class Keypad(PMK):
    def __init__(self):
        super().__init__(Keybow2040())

    def update_all(self):
        return self.update()