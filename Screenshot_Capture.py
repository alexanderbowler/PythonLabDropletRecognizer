import pyautogui
import time
import os
from datetime import datetime




class ScrnShot:
    def __init__(self, placementPath):
        self.dir = placementPath

    def takeScreenshot(self):
        myscreenshot = pyautogui.screenshot(region=(0,0, 300,400))
        curDateTime = datetime.now()
        name = "/Screenshot"+str(curDateTime.month)+str(curDateTime.day)+str(curDateTime.hour)+str(curDateTime.minute)+str(curDateTime.second)+".png"
        myscreenshot.save(self.dir+name)








# time.sleep(3)
# myscreenshot = pyautogui.screenshot()
# directory = os.getcwd()
# print(directory)
# myscreenshot.save(directory+'/ScreenshotTest.png')