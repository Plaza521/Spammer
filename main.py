from gui import Graphic
import schemas
import json
import tkinter as tk
import jsonschema


class Window:
    def __init__(self):
        with open("ui.json") as f:
            jsonschema.validate(
                instance=json.load(f),
                schema=schemas.ui_schema
            )
        with open("ui.json") as f:
            self.settings = json.load(f)['MainSettings']

        self.win = tk.Tk()
        self.win.geometry(
            f"{self.settings['width']}x{self.settings['height']}"
        )
        self.win.title(self.settings['title'])
        self.win.resizable(False, False)

        self.gui = Graphic(self)
        self.frame = tk.Frame(
            self.win,
            padx=10,
            pady=10
        )

    def run(self) -> None:
        self.frame.pack(expand=True)
        self.gui.draw(self.frame)
        self.win.mainloop()


def main() -> None:
    window = Window()
    window.run()


if __name__ == '__main__':
    main()
