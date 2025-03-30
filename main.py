import time
import threading
import pyautogui
from pynput import keyboard

autoclicking = False

def clicker():
    global autoclicking
    while True:
        if autoclicking:
            pyautogui.click()
            time.sleep(0.02)  # Change the values to set the delay (in seconds)

def on_press(key):
    global autoclicking
    try:
        if key == keyboard.Key.f6:  # Change the values to set keyboard shortcut for on/off
            autoclicking = not autoclicking
            print("Autoclick:", "ON" if autoclicking else "OFF")
    except AttributeError:
        pass

click_thread = threading.Thread(target=clicker, daemon=True)
click_thread.start()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
