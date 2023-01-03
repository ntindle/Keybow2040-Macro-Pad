# Initalize the encoders
import board
from lib.adafruit_seesaw import seesaw, rotaryio, digitalio, neopixel
from rainbowio import colorwheel
from adafruit_debouncer import Button

try:
    from typing import Tuple
except ImportError:
    pass

class Encoder:
    def __init__(self, i2c, address=0x36, color=(0, 0, 0)):
        self.seesaw = seesaw.Seesaw(i2c, 0x36)
        self.seesaw.pin_mode(24, self.seesaw.INPUT_PULLUP)
        self._button = digitalio.DigitalIO(self.seesaw, 24)
        self.button = Button(self._button)

        self.all_press_function = None
        self.single_press_function = None
        self.double_press_function = None
        self.long_press_function = None
        self.release_function = None

        self.encoder_increase_function = None
        self.encoder_decrease_function = None
        self.encoder_change_function = None

        self._color = color

        self.pixel = neopixel.NeoPixel(self.seesaw, 6, 1)
        self.pixel.brightness = .05

        self.encoder = rotaryio.IncrementalEncoder(self.seesaw)
        self.last_position = self.encoder.position

    def get_position(self):
        return self.encoder.position * -1

    def set_color(self, color: Tuple[int, int, int]):
        self._color = color
        self.pixel.fill(color)

    def set_brightness(self, brightness: float):
        self.pixel.brightness = brightness

    def update(self):
        self.button.update()
        if self.button.pressed and self.all_press_function:
            self.all_press_function()
        if self.button.released and self.release_function:
            self.release_function()
        if self.button.long_press and self.long_press_function:
            self.long_press_function()
        if self.button.short_count==1 and self.single_press_function:
            self.single_press_function()
        if self.button.short_count==2 and self.double_press_function:
            self.double_press_function()

        # Update the encoder position and run the appropriate function if necessary
        if self.position != self.last_position:
            if self.position > self.last_position:
                if self.encoder_increase_function:
                    self.encoder_increase_function()
            else:
                if self.encoder_decrease_function:
                    self.encoder_decrease_function()
            if self.encoder_change_function:
                self.encoder_change_function()
            self.last_position = self.position

    def on_release(self, handler=None):
        # Attaches a release function to the encoder button, via a decorator. This is stored as
        # `encoder.release_function` in the encoders's attributes, and run if necessary
        # as part of the key's update function . It can be attached as follows:

        # @encoder.on_release()
        # def release_handler(key, pressed):
        #     if pressed:
        #         do something
        #     else:
        #         do something else

        def attach_handler(handler):
            self.release_function = handler

        if handler is not None:
            attach_handler(handler)
        else:
            return attach_handler

    def on_all_press(self, handler=None):
        # Attaches a press function to the encoder button, via a decorator. This is stored as
        # `encoder.all_press_function` in the encoders's attributes, and run if necessary
        # as part of the key's update function . It can be attached as follows:

        # @encoder.on_all_press()
        # def press_handler(key, pressed):
        #     if pressed:
        #         do something
        #     else:
        #         do something else

        def attach_handler(handler):
            self.all_press_function = handler

        if handler is not None:
            attach_handler(handler)
        else:
            return attach_handler

    def on_single_press(self, handler=None):
        # Attaches a press function to the encoder button, via a decorator. This is stored as
        # `encoder.single_press_function` in the encoders's attributes, and run if necessary
        # as part of the key's update function . It can be attached as follows:

        # @encoder.on_single_press()
        # def press_handler(key, pressed):
        #     if pressed:
        #         do something
        #     else:
        #         do something else

        def attach_handler(handler):
            self.single_press_function = handler

        if handler is not None:
            attach_handler(handler)
        else:
            return attach_handler

    def on_double_press(self, handler=None):
        # Attaches a press function to the encoder button, via a decorator. This is stored as
        # `encoder.double_press_function` in the encoders's attributes, and run if necessary
        # as part of the key's update function . It can be attached as follows:

        # @encoder.on_double_press()
        # def press_handler(key, pressed):
        #     if pressed:
        #         do something
        #     else:
        #         do something else

        def attach_handler(handler):
            self.double_press_function = handler

        if handler is not None:
            attach_handler(handler)
        else:
            return attach_handler

    def on_long_press(self, handler=None):
        # Attaches a press function to the encoder button, via a decorator. This is stored as
        # `encoder.long_press_function` in the encoders's attributes, and run if necessary
        # as part of the key's update function . It can be attached as follows:

        # @encoder.on_long_press()
        # def press_handler(key, pressed):
        #     if pressed:
        #         do something
        #     else:
        #         do something else

        def attach_handler(handler):
            self.long_press_function = handler

        if handler is not None:
            attach_handler(handler)
        else:
            return attach_handler

    def on_increase(self, handler=None):
        # Attaches a press function to the encoder, via a decorator. This is stored as
        # `encoder.encoder_increase_function` in the encoders's attributes, and run if necessary
        # as part of the key's update function . It can be attached as follows:

        # @encoder.on_increase()
        # def press_handler(key, pressed):
        #     if pressed:
        #         do something
        #     else:
        #         do something else

        def attach_handler(handler):
            self.encoder_increase_function = handler

        if handler is not None:
            attach_handler(handler)
        else:
            return attach_handler

    def on_decrease(self, handler=None):
        # Attaches a press function to the encoder, via a decorator. This is stored as
        # `encoder.encoder_decrease_function` in the encoders's attributes, and run if necessary
        # as part of the key's update function . It can be attached as follows:

        # @encoder.on_decrease()
        # def press_handler(key, pressed):
        #     if pressed:
        #         do something
        #     else:
        #         do something else

        def attach_handler(handler):
            self.encoder_decrease_function = handler

        if handler is not None:
            attach_handler(handler)
        else:
            return attach_handler

    @property
    def color(self):
        return self._color

    @property
    def position(self):
        return self.get_position()

    @property
    def brightness(self):
        return self.pixel.brightness