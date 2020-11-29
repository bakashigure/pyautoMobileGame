# HELLO

__version__ = "0.0.1"


import base64
import ctypes
import datetime
import os
import re
import sys
import time
from io import BytesIO, TextIOWrapper
import pyscreeze
import win32api
import win32con
import win32gui
import win32ui
import jieba
from PIL import Image


class PyautoMobileGameException(Exception):
    """
    Raise Exception here.
    """
    pass


class ImageNotFoundError(PyautoMobileGameException):
    """
    This exception is raised when the image given by the user 
    is not found. 
    """
    pass


class PyautoMobileGame():
    """
    HAHAHA
    """

    def __init__(self):
        self.img_type = 'JPG'
        self.game_hwnd = 0
        self.game_times = 0
        self.process_list = []
        self.game_list = []
        self.x = 0
        self.y = 0
        print("Init success.")

    def images(self, *_image_list, prefix=''):
        """
        Full name of image files like 
         ['D://img1.jpg','D://img2.jpg'] 
          OR
         ['img1.jpg','img2.jpg'] with prefix='D://'
        """
        pass

    def listAllHwnd(self):
        pass

    def findTitle(self, title, mode=0):
        """
        - Parameter: 
                mode:0 list all matched titles and receive a user input.
                mode:1 choose the first matched title as game_hwnd
        """
        hwnd_title = dict()
        self.title = title

        def getAllHwnd(hwnd, mouse):
            if (
                win32gui.IsWindow(hwnd)
                and win32gui.IsWindowEnabled(hwnd)
                and win32gui.IsWindowVisible(hwnd)
            ):
                hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
        win32gui.EnumWindows(getAllHwnd, 0)
        match_title = "([0-9]*)(.*)    "+str(self.title)+"(.*)"

        for h, t in hwnd_title.items():
            if t != '':
                c = f"{h}    {t}"
                self.process_list.append(c)
                result = re.match(match_title, c)
                if result != None:
                    self.game_list.append(result)

        if len_game_list := len(self.game_list) == 0:
            print(f"""WARNING: There`s none process match the title '{title}',
    Do you want to list all processes and select manaual (y/n) or rescan process(r)""")
            user_input=input()
            if user_input in ['y', 'Y']:
                for item in self.process_list:
                    print(item)
            elif user_input in ['n','N']:
                print('done')
            elif user_input in ['r','R']:
                return self.findTitle(title)

        elif len_game_list >= 1 and mode == 0:
            for items in self.game_list:
                print(items)
            # TODO user input here

    def getAppScreenshot(self):
        hwnd = int(self.game_hwnd)
        left, top, right, bot = win32gui.GetWindowRect(hwnd)
        width = right - left
        height = bot - top
        hWndDC = win32gui.GetWindowDC(hwnd)
        mfcDC = win32ui.CreateDCFromHandle(hWndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
        saveDC.SelectObject(saveBitMap)
        saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)
        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)
        im_PIL = Image.frombuffer(
            "RGB",
            (bmpinfo["bmWidth"], bmpinfo["bmHeight"]),
            bmpstr,
            "raw",
            "BGRX",
            0,
            1,
        )
        return im_PIL, left, width, top

    def locate(self, image, type='', **kwargs):
        if type == "base64":
            needle_image = BytesIO(base64.b64decode(image))
        else:
            needle_image = Image.open(image)

        haystack_image, _left, _width, _top = self.getAppScreenshot()

        if res := pyscreeze.locate(needle_image, haystack_image) != None:
            position = []
            self.x = pyscreeze.center(res)[0]
            self.y = pyscreeze.center(res)[1]
            position.append(pyscreeze.center(res)[0])
            position.append(pyscreeze.center(res)[1])
            return True
        return False

    def sendkey(self, image, key: str, times=1, interval=0.1):
        """
        Send specified key to the matched image.

        Parameter:
            - image: image to be matched
            - key: send mouse click or press from keyboard
            - times: click times
        """
        pass

    def sendkeys(self, *_image_list: list, key: str, times=1, interval=0.1):
        """
        Send same key to all matched images.

        Parameter:
            - _image_list: list of images
            - key: send mouse click or press sth
            - times: each matched image click frequency
            - interval: send key interval
        """

        pass
