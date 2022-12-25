import threading
from time import sleep
import keyboard as kb


def handle_start_button(window) -> None:
    elem_handlers = window.gui.element_handlers
    words = elem_handlers["text_words"].get("1.0", "end")
    tbm = float(elem_handlers["entry_tbm"].get())
    tufm = float(elem_handlers["entry_tufm"].get())
    itercnt = int(elem_handlers["entry_itercnt"].get())
    sleep(tufm)
    for i in range(itercnt):
        kb.write(words)
        kb.press_and_release("enter")
        sleep(tbm)


def handle_commands(window, command) -> None:
    handler_thread = threading.Thread(
        target=command,
        args=(window,)
    )
    handler_thread.start()
