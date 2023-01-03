import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

try:
    from typing import Tuple
except ImportError:
    pass


class Command(object):
    def __init__(self, label: str, type: str, color: Tuple[int, int, int], keys, control: str, text: str):
        self.label = label
        self.type = type
        self.color = color
        self.keys = keys
        self.keys_parsed = []
        self.text = text
        self.control = control
        self.control_parsed = None

    def __repr__(self) -> str:
        return f"Command(label={self.label}, type={self.type}, color={self.color}, keys={self.keys}, control={self.control}, text={self.text})"
    
    def __str__(self) -> str:
        return self.__repr__()

    @staticmethod
    def from_dict(d: dict):
        print(f"Creating command from dict: {d}")
        command =  Command(
            d.get('label', 'Unknown'),
            d.get('type', None),
            d.get('color', (0, 0, 0)),
            d.get('keys', None),
            d.get('control', None),
            d.get('text', None)
        )

        if command.type == 'key':
            if command.keys is None:
                raise Exception(f"Key command must have keys defined: {command}")
            for key in command.keys:
                if not hasattr(Keycode, key):
                    raise Exception(f"Invalid key: {key}")
                else:
                    command.keys_parsed.append(getattr(Keycode, key))
                    print(f"Converted key: {key} to {getattr(Keycode, key)}")
        if command.type == 'text':
            if command.text is None:
                raise Exception(f"Text command must have text defined: {command}")
        if command.type == 'control':
            if command.control is None:
                raise Exception(f"Control command must have control defined: {command}")
            if not hasattr(ConsumerControlCode, command.control):
                raise Exception(f"Invalid control: {command.control}")
            else:
                command.control_parsed = getattr(ConsumerControlCode, command.control)
        return command


class Control:
    def __init__(self):
        # Set up the keyboard and layout
        self.keyboard = Keyboard(usb_hid.devices)
        self.layout = KeyboardLayoutUS(self.keyboard)

        # Set up consumer control (used to send media key presses)
        self.consumer_control = ConsumerControl(usb_hid.devices)

    def send(self, command):
        if command.type == 'key':
            self.keyboard.press(*command.keys_parsed)
        elif command.type == 'text':
            self.layout.write(command.text)
        elif command.type == 'control':
            self.consumer_control.send(command.control_parsed)
        else:
            print(f"Send Control not implemented: {command}")
        
    def press(self, command):
        print(f"Pressing command: {command}")
        if command.type == 'key':
            print(f"Pressing key: {command.keys_parsed}")
            self.keyboard.send(*command.keys_parsed)
        elif command.type == 'text':
            self.layout.write(command.text)
        elif command.type == 'control':
            self.consumer_control.send(command.control_parsed)
        else:
            print(f"Press Control not implemented: {command}")

    def release(self, command):
        print(f"Releasing command: {command}")
        if command.type == 'key':
            print(f"Releasing key: {command.keys_parsed}")
            self.keyboard.release(*command.keys_parsed)
        elif command.type == 'text':
            pass
        elif command.type == 'control':
            pass
        else:
            print(f"Release Control not implemented: {command}")