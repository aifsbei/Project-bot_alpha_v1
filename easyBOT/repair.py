import foos
import numpy as np
from PIL import ImageOps, ImageGrab
import time
import pyautogui

dead_sum = 2241378
tp_from_31_to_32 = 76805


def is_dead():
    box = (636, 769, 1282, 849)
    image = ImageOps.grayscale(ImageGrab.grab(box))
    a = np.array(image)
    a = a.sum()
    if a == dead_sum:
        return True
    else:
        return False


def repair():
    foos.mousePos((961, 800))
    foos.leftClick()
    time.sleep(5)
    foos.mousePos((1627, 853))
    foos.leftClick()
    box = (1631, 807, 1693, 821)
    while True:
        image = ImageOps.grayscale(ImageGrab.grab(box))
        a = np.array(image)
        a = a.sum()
        if a == tp_from_31_to_32:
            pyautogui.keyUp('J')
            pyautogui.keyDown('J')
            time.sleep(5)
            return


if __name__ == '__main__':
    repair()