import pyautogui
import time
time.sleep(4)
count = 0
while count<=20:
    pyautogui.typewrite("Happy Birthday Modi")
    pyautogui.typewrite("🥳🎂🎂")
    pyautogui.press("enter")
    count = count+1

