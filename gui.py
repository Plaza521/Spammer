import io_handlers
from functools import partial
import json
import tkinter as tk


class Graphic:
    def __init__(self, window):
        with open("ui.json") as f:
            self.elements_data = json.load(f)['Elements']
        for element in self.elements_data:
            self.elements_data[element]['type'] = \
                getattr(tk, self.elements_data[element]['type'])
            if 'command' in self.elements_data[element]['param']:
                elem_callable = getattr(
                    io_handlers,
                    self.elements_data[element]['param']['command']
                )
                self.elements_data[element]['param']['command'] = \
                    partial(io_handlers.handle_commands, window, elem_callable)

        self.element_handlers = {}

    def draw(self, frame: tk.Frame):
        esd = self.elements_data
        for element in esd:
            esd_elem = esd[element]
            self.element_handlers[element] = \
                esd_elem['type'](frame, **esd_elem['param'])
            self.element_handlers[element].grid(**esd_elem['place'])
