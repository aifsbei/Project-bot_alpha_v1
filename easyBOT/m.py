from PIL import ImageGrab
import os
import time
import win32api
import win32con
from PIL import ImageOps
import numpy as np
import ctypes
import cv2
import win32com.client

awareness = ctypes.c_int() # correcting DPI
ctypes.windll.shcore.SetProcessDpiAwareness(2) # setting DPI to high

# Globals:
# ------------

attack_speed = 2
x_pad = 0
y_pad = 0
enemy_color = (204, 0, 0)
low_color = (203, 0, 0)
high_color = (204, 0, 0)

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


def find_enemy(im, color):
    for x in range(1920):
        for y in range(1080):
            r, g, b = im.getpixel((x, y))
            if r == color[0] and g == color[1] and b == color[2]:
                mousePos((x + 20, y - 80))
                leftClick()
                quit(0)


def fast_find_enemy(im, low, high):
    ima = np.array(im)
    hsv = cv2.cvtColor(ima, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(ima, low, high)
    coord = cv2.findNonZero(mask)
    try:
        return (coord[0][0][0], coord[0][0][1])
    except TypeError:
        return None


def aim(im, coord):
    if coord is not None:
        mousePos((coord[0] + 50, coord[1] - 80))
        leftClick()


def shoot():
    shell = win32com.client.Dispatch('WScript.Shell')
    shell.SendKeys('^')


def main():
    im = screenGrab()
    aim(im, fast_find_enemy(im, low_color, high_color))
#    shoot()
    time.sleep(attack_speed)



if __name__ == '__main__':
    while True:
        main()