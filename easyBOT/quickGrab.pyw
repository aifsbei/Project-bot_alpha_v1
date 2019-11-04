from PIL import ImageGrab
import os
import time

# Globals:
# ------------

x_pad = -1
y_pad = 87

# ------------


def screenGrab():
    box = (x_pad + 1, y_pad + 1, x_pad + 1920, y_pad + 942)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    


def main():
    screenGrab()


if __name__ == '__main__':
    main()