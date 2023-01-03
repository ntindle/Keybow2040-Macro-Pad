import displayio
import terminalio
from adafruit_display_text import label, wrap_text_to_lines
from adafruit_displayio_layout.layouts.grid_layout import GridLayout
import adafruit_displayio_ssd1306

try:
    from typing import Tuple
except ImportError:
    pass

class Screen:
    def __init__(self, width, height, i2c, address=0x3d):
        # Initalize the display
        displayio.release_displays()
        self.width = width
        self.height = height
        self.display_bus = displayio.I2CDisplay(i2c, device_address=address)
        self.display = adafruit_displayio_ssd1306.SSD1306(self.display_bus, width=self.width, height=self.height)

    def print(self, text: str):
        # Make the display context
        splash = displayio.Group()
        self.display.show(splash)

        color_bitmap = displayio.Bitmap(self.width, self.height, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = 0xFFFFFF

        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
        splash.append(bg_sprite)

        # Draw a smaller inner rectangle
        inner_bitmap = displayio.Bitmap(self.width - 10, self.height - 10, 1)
        inner_palette = displayio.Palette(1)
        inner_palette[0] = 0x000000  # Black
        inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=4)
        splash.append(inner_sprite)

        text = "\n".join(wrap_text_to_lines(text, 15))

        text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=28, y=15)
        splash.append(text_area)

    def clear(self):
        splash = displayio.Group()
        self.display.show(splash)

    def show_grid(self, content: Tuple[Tuple[str, str, str, str], Tuple[str, str, str, str], Tuple[str, str, str, str], Tuple[str, str, str, str]]):
        main_group = displayio.Group()
        self.display.show(main_group)

        layout = GridLayout(
            x=0,
            y=0,
            width=self.width,
            height=self.height,
            grid_size=(4, 4),
            cell_padding=1,
            divider_lines=True,
        )
        _labels = []

        for row in range(0, 4):
            for col in range(0, 4):
                _labels.append(
                    label.Label(
                        terminalio.FONT, x=0, y=0, text=content[row][col], background_color=0x770077
                    )
                )
                layout.add_content(_labels[-1], grid_position=(col, row), cell_size=(1, 1))

        main_group.append(layout)

