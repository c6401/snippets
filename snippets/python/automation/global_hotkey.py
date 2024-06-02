from pynput import keyboard

def on_activate():
    print('ok')

with keyboard.GlobalHotKeys({'<ctrl>+<alt>+s': on_activate}) as handler:
    handler.join()