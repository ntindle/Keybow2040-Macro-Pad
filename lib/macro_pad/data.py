import json
import storage
from math import ceil
class Data:
    def __init__(self):
        self.content = {}
        try: 
            with open('maps.json') as f:
                self.content = json.load(f)
        except Exception as e:
            print(e)
            pass

    def __repr__(self) -> str:
        return self.content
    
    @property
    def layers(self):
        return self.content['layers']

    def get_layer_name(self, layer: int):
        return self.content['layers'][layer]['name']

    def get_layer_count(self):
        return len(self.content['layers'])

    
    def get_layer_color(self, layer: int):
        return self.content['layers'][layer]['color']
    
    @property
    def layer_count(self):
        return self.get_layer_count()

    def get_layer_by_index(self, layer: int):
        return self.content['layers'][layer]

    def get_layer_by_name(self, name: str):
        for layer in self.content['layers']:
            if layer['name'] == name:
                return layer

    def get_layer_keymap(self, layer: int):
        return self.content['layers'][layer]['keymap']

    def get_layer_keymap_labels(self, layer: int):
        labels = {}
        for i, key in enumerate(self.content['layers'][layer]['keymap']):
            try:
                labels[i] = key['label']
            except Exception as e:
                print(e)
                pass
        return labels

    def get_layer_keymap_labels_list_by_4(self, layer: int):
        labels = []
        size = 4
        for i, key in enumerate(self.content['layers'][layer]['keymap']):
            try:
                labels.append(key['label'])
            except Exception as e:
                print(e)
                pass
            
        return [
            labels[i * size:(i * size) + size]
            for i in range(ceil(len(labels) / size))
        ]
    
    def get_layer_keymap_action(self, layer: int, key: int):
        return self.content['layers'][layer]['keymap'][key]

    def get_layer_encoder_up_action(self, layer: int):
        return self.content['layers'][layer]['encoder_up_action']

    def get_layer_encoder_down_action(self, layer: int):
        return self.content['layers'][layer]['encoder_down_action']

    def get_layer_keymap_colors(self, layer: int):
        colors = {}
        for i, key in enumerate(self.content['layers'][layer]['keymap']):
            try:
                colors[i] = key['color']
            except Exception as e:
                print(e)
                pass
        return colors
    
    def get_layer_encoder_up_action(self, layer: int):
        return self.content['layers'][layer]['encoder_up_action']

    def get_layer_encoder_down_action(self, layer: int):
        return self.content['layers'][layer]['encoder_down_action']
