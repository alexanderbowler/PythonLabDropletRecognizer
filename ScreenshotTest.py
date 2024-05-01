import pyautogui
import time
import os

time.sleep(3)
myscreenshot = pyautogui.screenshot()
directory = os.getcwd()
print(directory)
myscreenshot.save(directory+'/ScreenshotTest.png')