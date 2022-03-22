import threading
from themeToggler import toggleOSThemeColor
from pynput import keyboard

pressed = set()

COMBINATIONS = [
    {
        "keys": [
            {keyboard.Key.cmd, keyboard.KeyCode(char="z")},
            {keyboard.Key.cmd, keyboard.KeyCode(char="Z")},
        ],
        "command": toggleOSThemeColor,
    },
]

def on_press(key):
    pressed.add(key)
    for c in COMBINATIONS:
        for keys in c["keys"]:
            if keys.issubset(pressed):
                threading.Thread(target=c["command"]).start()

def on_release(key):
    if key in pressed:
        pressed.remove(key)

if __name__ == '__main__':
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()