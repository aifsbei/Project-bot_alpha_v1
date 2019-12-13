from PIL import ImageGrab
#import os
import time
#import win32api
#import win32con
#from PIL import ImageOps
#from PIL import Image
import numpy as np
import ctypes
import cv2
import win32com.client
import foos
import pyautogui


awareness = ctypes.c_int() # correcting DPI
ctypes.windll.shcore.SetProcessDpiAwareness(2) # setting DPI to high

# Globals:

my_hp_3d = (384, 401, 950, 1020)
my_hp_2d = (439, 473, 899, 1016)
center_x = 970
center_y = 570

# ------------

attack_speed = 2
enemy_color = (204, 0, 0)
low_color = (203, 0, 0)
high_color = (204, 0, 0)
low_hpbar_color = (45, 200, 35)
high_hpbar_color = (54, 228, 40)

# ------------


def find_enemy(im, color):
    for x in range(1920):
        for y in range(1080):
            r, g, b = im.getpixel((x, y))
            if r == color[0] and g == color[1] and b == color[2]:
                foos.mousePos((x + 20, y - 80))
                foos.leftClick()
                quit(0)


def fast_find_enemy(low, high):
    image = ImageGrab.grab()
    ima = np.array(image)
    ima[717:1021, 1526:1883] = (0, 0, 0)
    ima[0:220, 0:1920] = (0, 0, 0)
    ima[932:1080, 0:1920] = (0, 0, 0)
    hsv = cv2.cvtColor(ima, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(ima, low, high)
    coord = cv2.findNonZero(mask)
    try:
        return (coord[0][0][0], coord[0][0][1])
    except TypeError:
        return None


def aim(coord):
    if coord is not None:
        print('get aimed... but... cuz coord = {}'.format(coord))
        foos.mousePos((coord[0] + 45, coord[1] - 75))
        foos.leftClick()
#        if coord[0] > center_x and coord[1] > center_y:
#            foos.mousePos((coord[0] - 15, coord[1] - 135))
#            foos.leftClick()
#            foos.mousePos((coord[0] - 75, coord[1] - 195))
#            foos.leftClick()
#            foos.mousePos((coord[0] - 135, coord[1] - 255))
#            foos.leftClick()
#            foos.mousePos((coord[0] - 195, coord[1] - 315))
#            foos.leftClick()
#        elif coord[0] > center_x and coord[1] < center_y:
#            foos.mousePos((coord[0] - 15, coord[1] - 15))
#            foos.leftClick()
#            foos.mousePos((coord[0] - 75, coord[1] + 45))
#            foos.leftClick()
#            foos.mousePos((coord[0] - 135, coord[1] + 105))
#            foos.leftClick()
#            foos.mousePos((coord[0] - 195, coord[1] + 165))
#            foos.leftClick()
#        elif coord[0] < center_x and coord[1] > center_y:
#            foos.mousePos((coord[0] + 105, coord[1] - 135))
#            foos.leftClick()
#            foos.mousePos((coord[0] + 165, coord[1] - 195))
#            foos.leftClick()
#            foos.mousePos((coord[0] + 225, coord[1] - 255))
#            foos.leftClick()
#            foos.mousePos((coord[0] + 285, coord[1] - 315))
#            foos.leftClick()
#        elif coord[0] < center_x and coord[1] < center_y:
#            foos.mousePos((coord[0] + 105, coord[1] - 15))
#            foos.leftClick()
#            foos.mousePos((coord[0] + 165, coord[1] + 45))
#            foos.leftClick()
#            foos.mousePos((coord[0] + 225, coord[1] + 105))
#            foos.leftClick()
#            foos.mousePos((coord[0] + 285, coord[1] + 165))
#            foos.leftClick()

#        foos.mousePos((coord[0] + 0, coord[1] - 55))
#        foos.leftClick()
#        foos.mousePos((coord[0] + 0, coord[1] - 155))
#        foos.leftClick()
#        foos.mousePos((coord[0] + 160, coord[1] - 65))
#        foos.leftClick()
#        foos.mousePos((coord[0] + 130, coord[1] - 155))
#        foos.leftClick()
    else:
        return False


def shoot():
    shell = win32com.client.Dispatch('WScript.Shell')
    shell.SendKeys('^')
#    time.sleep(.01)
#    pyautogui.keyDown('ctrl')
#    time.sleep(.02)
#    pyautogui.keyUp('ctrl')


def attack():
    it = 1
#    shoot()
    while True:
        it += 1
        print(it)
###        image = ImageGrab.grab()
#        image = foos.screenGrab()
        if aim(fast_find_enemy(low_color, high_color)) == False:
            print('no enemies here...')
            return
#        aim(fast_find_enemy(image, low_color, high_color))
        time.sleep(.1)
        shoot()
#        time.sleep(attack_speed)
###        image = ImageGrab.grab()
        image = foos.screenGrab()
        while enemy_alive(image, low_hpbar_color, high_hpbar_color):
#            time.sleep(attack_speed / 10)
###            image = ImageGrab.grab()
            image = foos.screenGrab()


def attack_light():
    shoot()
    image = foos.screenGrab()
    while enemy_alive(image, low_hpbar_color, high_hpbar_color):
        image = foos.screenGrab()


def enemy_alive(image, low, high):
#    ima2 = np.array(image)
#    arr2im = Image.fromarray(ima2)
#    arr2im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    ima = np.array(image)
#    arr2im = Image.fromarray(ima)
#    arr2im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    ima[my_hp_2d[0]:my_hp_2d[1], my_hp_2d[2]:my_hp_2d[3]] = (0, 0, 0)
#    arr2im = Image.fromarray(ima)
#    arr2im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    hsv = cv2.cvtColor(ima, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(ima, low, high)
    coord = cv2.findNonZero(mask)
    try:
        temp = coord[0][0][0], coord[0][0][1]
#        foos.mousePos(temp)
        print('still alive')
        return True
    except TypeError:
        print('hes dead')
#        arr2im = Image.fromarray(mask)
#        arr2im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
        return False


if __name__ == '__main__':
    print('attack main')
    while True:
        attack()