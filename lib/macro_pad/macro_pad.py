import board
import time
from rainbowio import colorwheel
from lib.macro_pad import data
from lib.macro_pad import screen
from lib.macro_pad import encoder
from lib.macro_pad import keypad
from lib.macro_pad import colors
from lib.macro_pad import control

class MacroPad:
    def __init__(self, i2c=board.I2C()):
        self.i2c = i2c
        self.data = data.Data()
        self.encoder = encoder.Encoder(i2c)
        self.screen = screen.Screen(128, 64, i2c)
        self.keypad = keypad.Keypad()
        self.control = control.Control()
        self.layer = 0
        self.last_layer = self.layer


        try:
            self.encoder.set_color(self.data.get_layer_color(self.layer))
            colors = self.data.get_layer_keymap_colors(self.layer)
            for i, key in enumerate(self.keypad.keys):
                key.set_led(*colors[i])
            self.screen.show_grid(self.data.get_layer_keymap_labels_list_by_4(self.layer))
        except Exception as e:
            print(e)
            self.screen.print("Error loading layer")

        self.set_decorators()


    def set_decorators(self):
        @self.encoder.on_long_press
        def on_long_press():
            print("Long Press")
            self.encoder.set_color(colors.green)

        @self.encoder.on_single_press
        def on_single_press():
            print("Single Press")
            self.layer = (self.layer + 1) % self.data.layer_count
            print(f"Layer: {self.layer}")
            self.encoder.set_color(colors.red)

        @self.encoder.on_double_press
        def on_double_press():
            print("Double Press")
            self.encoder.set_color(colors.blue)

        @self.encoder.on_increase
        def on_increase():
            self.encoder.set_color(colors.yellow)
            print(self.encoder.position)
            print(f"ACTION: {self.data.get_layer_encoder_up_action(self.layer)}")
            command = control.Command.from_dict(self.data.get_layer_encoder_up_action(self.layer))
            print(command)
            # Press as there is no release automatically
            self.control.press(command)

        @self.encoder.on_decrease
        def on_decrease():
            self.encoder.set_color(colors.cyan)
            print(self.encoder.position)
            print(f"ACTION: {self.data.get_layer_encoder_down_action(self.layer)}")
            command = control.Command.from_dict(self.data.get_layer_encoder_down_action(self.layer))
            print(command)
            # Press as there is no release automatically
            self.control.press(command)

        for key in self.keypad.keys:
            @self.keypad.on_press(key)
            def press_handler(key):
                print("Key {} pressed".format(key.number))
                print(f"Action: {self.data.get_layer_keymap_action(self.layer, key.number)}")
                command = control.Command.from_dict(self.data.get_layer_keymap_action(self.layer, key.number))
                print(command)
                self.control.send(command)
                # key.set_led(*colors.blue)

            @self.keypad.on_release(key)
            def release_handler(key):
                print("Key {} released".format(key.number))
                print(f"Action: {self.data.get_layer_keymap_action(self.layer, key.number)}")
                command = control.Command.from_dict(self.data.get_layer_keymap_action(self.layer, key.number))
                print(command)
                self.control.release(command)
                # key.set_led(*colors.white)


    def update(self):
        if self.last_layer != self.layer:
            self.last_layer = self.layer
            try:
                self.screen.print(self.data.get_layer_name(self.layer))
                self.encoder.set_color(self.data.get_layer_color(self.layer))
                colors = self.data.get_layer_keymap_colors(self.layer)
                for i, key in enumerate(self.keypad.keys):
                    key.set_led(*colors[i])
                self.screen.show_grid(self.data.get_layer_keymap_labels_list_by_4(self.layer))
            except Exception as e:
                print(e)
                self.screen.print("Error Loading Layer")
        self.encoder.update()
        self.keypad.update()

    def print_data(self):
        print("Data", data)
        print(f"All Layers: {data.layers}")
        print(f"By Index: {data.get_layer_by_index(self.layer)}")
        print(f"By Name: {data.get_layer_by_name('General')}")
        print(f"Keymap: {data.get_layer_keymap(self.layer)}")
        print(f"Colors: {data.get_layer_keymap_colors(self.layer)}")
        print(f"Labels: {data.get_layer_keymap_labels(self.layer)}")
        print(f"Up action {data.get_layer_encoder_up_action(self.layer)}")