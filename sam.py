import pyautogui
import time

# Delay for a few seconds (in case you need to focus on the input field)
time.sleep(5)

# Type "Hello"
for i range(1000):
    pyautogui.typewrite("Hello")

    # Press Enter
    pyautogui.press("enter")
