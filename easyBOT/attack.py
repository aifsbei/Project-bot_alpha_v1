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

awareness = ctypes.c_int() # correcting DPI
ctypes.windll.shcore.SetProcessDpiAwareness(2) # setting DPI to high

# Globals:


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


def fast_find_enemy(image, low, high):
    ima = np.array(image)
    ima[717:1021, 1526:1883] = (0, 0, 0)
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
    else:
        return False


def shoot():
    shell = win32com.client.Dispatch('WScript.Shell')
    shell.SendKeys('^')


def attack():
    it = 1
    while True:
        it += 1
        print(it)
        image = ImageGrab.grab()
        if aim(fast_find_enemy(image, low_color, high_color)) == False:
            print('no enemies here...')
            return
#        aim(fast_find_enemy(image, low_color, high_color))
        time.sleep(.5)
        shoot()
#        time.sleep(attack_speed)
        image = ImageGrab.grab()
        while enemy_alive(image, low_hpbar_color, high_hpbar_color):
#            time.sleep(attack_speed / 10)
            image = ImageGrab.grab()


def enemy_alive(image, low, high):
#    ima2 = np.array(image)
#    arr2im = Image.fromarray(ima2)
#    arr2im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    ima = np.array(image)
#    arr2im = Image.fromarray(ima)
#    arr2im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    ima[439:473, 899:1016] = (0, 0, 0)
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
    attack()