from PIL import ImageGrab
#import os
import time
#import win32api
#import win32con
#from PIL import ImageOps
import numpy as np
import ctypes
import cv2
#import win32com.client
import pyautogui
import random
import foos
import attack
import os

awareness = ctypes.c_int() # correcting DPI
ctypes.windll.shcore.SetProcessDpiAwareness(2) # setting DPI to high

# Globals:
# ------------

low_color = (230, 223, 190) # may cause an error
high_color = (232, 225, 191)
#enemy_color = (198, 10, 10)
enemy_color_low = (190, 0, 0)
enemy_color_high = (210, 12, 12)
minimap_square_32 = ((1637, 885), (1787, 885), (1637, 960), (1787, 960))
minimap_square_33 = ((1637, 900), (1787, 900), (1637, 960), (1787, 960))

# ------------


def fly():
    if find_enemy_on_minimap(enemy_color_low, enemy_color_high) != None:
        #print(find_enemy_on_minimap(enemy_color_low, enemy_color_high)[0], find_enemy_on_minimap(enemy_color_low, enemy_color_high)[1])
#        x = find_enemy_on_minimap(enemy_color_low, enemy_color_high)
        x, y = find_enemy_on_minimap(enemy_color_low, enemy_color_high)
    else:
        x = random.randint(minimap_square_33[0][0], minimap_square_33[1][0])
        y = random.randint(minimap_square_33[0][1], minimap_square_33[2][1])
    foos.mousePos((x, y))
    foos.leftClick()
    for i in range(2):
        image = foos.screen_shot()
###        if attack.aim(attack.fast_find_enemy(attack.low_color, attack.high_color)):
        if attack.fast_find_enemy(attack.low_color, attack.high_color) != None:
#            attack.attack_light()
            return
        print(i + 1, '...')
        time.sleep(1)


def find_minimap(image, low, high):
    ima = np.array(image)
    hsv = cv2.cvtColor(ima, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(ima, low, high)
    coord = cv2.findNonZero(mask)
    try:
        return (coord[-1][-1][-2], coord[-1][-1][-1])
    except TypeError:
        return None


def place_minimap(coord):
    if coord == None:
        foos.mousePos((368, 121))
        foos.leftClick()
    else:
        print('found at {}'.format(coord))
        foos.mousePos(coord)
        pyautogui.mouseDown()
        pyautogui.dragTo(1670, 809, button='left')
        pyautogui.mouseUp()
        #mousePos((1670, 809))
        #leftUp()


def find_enemy_on_minimap(low, high):
    box = (minimap_square_33[0][0], minimap_square_33[0][1],
           minimap_square_33[2][0], minimap_square_33[2][1])
    image = foos.screenGrab()
    ima = np.array(image)
    ima[845:870, 1730:1756] = (0, 0, 0)
    hsv = cv2.cvtColor(ima, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(ima, low, high)
    coord = cv2.findNonZero(mask)
    try:
        print('found enemy on minimap!')
        return (coord[-1][-1][-2], coord[-1][-1][-1])
    except TypeError:
        return None


def main():
    print('navi main')
    im = foos.screenGrab()
    minimap_coords = find_minimap(im, low_color, high_color)
    place_minimap(minimap_coords)
    time.sleep(1)
#    for i in range(5):
#       fly()


if __name__ == '__main__':
    main()