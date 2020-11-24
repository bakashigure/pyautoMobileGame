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
    def __init__(self):
        self.img_type='JPG'
        self.game_hwnd=0
        
        
    def images(self,*_image_list,prefix=''):
        """
        Full name of image files like ``['D://img1.jpg','D://img2.jpg']`` OR
        ``['img1.jpg','img2.jpg']`` with ``prefix='D://'``
        """
        pass

    def find_title(self,title):
        hwnd_title = dict()
        self.title = title
        def getAllHwnd(hwnd,mouse):
            if (
                win32gui.IsWindow(hwnd)
                and win32gui.IsWindowEnabled(hwnd)
                and win32gui.IsWindowVisible(hwnd)
            ):
                hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
        win32gui.EnumWindows(getAllHwnd, 0)
        match_title="([0-9]*)(.*) "+str(self.title)+"(.*)"
        for k,w in hwnd_title.items():
            # TODO
            pass



    def locate(self,image,type=''):
        type=self.img_type
        # TODO
        pass



    def sendkey(self,image,key:str,times=1,interval=0.1):
        """
        Send specified key to the matched image.

        Parameter:
            - image: image to be matched
            - key: send mouse click or press from keyboard
            - times: click times
        """
        pass

    def sendkeys(self,*_image_list:list,key:str,times=1,interval=0.1):
        """
        Send same key to all matched images.

        Parameter:
            - _image_list: list of images
            - key: send mouse click or press sth
            - times: each matched image click frequency
            - interval: send key interval
        """

        pass

class IDIMG():
    _game_times=0
