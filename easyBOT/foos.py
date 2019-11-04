from PIL import ImageGrab
#import os
import time
import win32api
import win32con
#from PIL import ImageOps
#import numpy as np
import ctypes
#import cv2
#import win32com.client

awareness = ctypes.c_int() # correcting DPI
ctypes.windll.shcore.SetProcessDpiAwareness(2) # setting DPI to high

# Globals:
# ------------

x_pad = 0
y_pad = 0

# ------------


#class Cord:



def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print('click')


def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    print('left Down')


def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    print('left Up')


def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


def print_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x, y)


def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    return x, y


def screenGrab():
    b1 = (x_pad + 1, y_pad + 1, x_pad + 1920, y_pad + 942)
    im = ImageGrab.grab()
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


def check():
    im = screenGrab()
    print_cords()
    print(im.getpixel(get_cords()))
    time.sleep(3)


if __name__ == '__main__':
    for i in range(4):
        check()