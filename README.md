# 🖱️ Python Autoclicker

A simple Python-based autoclicker that uses `pyautogui` and `pynput` to simulate mouse clicks with a toggle hotkey.

## 🔧 Features

- Clicks the mouse automatically every 0.02 seconds
- Toggle on/off with a keyboard shortcut (`F6` by default)
- Lightweight and easy to use

## 🧠 How It Works

- Press `F6` to start or stop the autoclicker
- While active, it will click continuously with a short delay (can be customized)

## 📦 Requirements

Make sure you have the following Python packages installed:

```bash
pip install pyautogui pynput
```

🚀 Running the Autoclicker

Simply run the script:
```
python autoclicker.py
```
Then press F6 to toggle autoclicking.

⚙️ Configuration

Change the clicking speed by modifying the time.sleep(0.02) line
Change the toggle key by updating if key == keyboard.Key.f6 in the on_press function
⚠️ Warning

Use responsibly. Some games or applications may restrict or ban the use of autoclickers.