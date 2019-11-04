from PIL import ImageGrab
#import os
#import time
#import win32api
#import win32con
#from PIL import ImageOps
#import numpy as np
import ctypes
#import cv2
#import win32com.client
#import foos
import attack
import navigation
import threading
#import win32event

awareness = ctypes.c_int() # correcting DPI
ctypes.windll.shcore.SetProcessDpiAwareness(2) # setting DPI to high

# Globals:
# ------------

status = 'inactive'

# ------------


#def main():
#    global status
#    image = ImageGrab.grab()
#    fly_thread = threading.Thread(target=navigation.fly(), daemon=True)
#    attack_thread = threading.Thread(target=attack.attack(image), daemon=True)
#    if status == 'inactive':
#        fly_thread.start()
#        status = 'roaming'
#    elif status == 'roaming':
#        attack_thread.start()
#        status = 'fighting'
#    elif status == 'fighting':
#        if not attack_thread.is_alive():
#            status = 'inactive'
#        else:
#            if fly_thread.is_alive():
#                fly_thread.join()
#    print(status, time.ctime())


class fly_thread_class(threading.Thread):



    def run(self):
        global status
        status = 'roaming'
        navigation.fly()


class attack_thread_class(threading.Thread):



    def run(self):
        global status
        status = 'under attack'
        attack.attack()


def main():
    global status

#    fly_thread = threading.Thread(target=navigation.fly(), daemon=True)
#    attack_thread = threading.Thread(target=attack.attack(), daemon=True)
#    attack_thread.start()
#    f = open('as', 'r')
#    if status == 'inactive':
#        fly_thread.start()
#        status = 'roaming'
#    elif f.read() == 'under attack':
#        fly_thread.join()
#        status = 'fighting'
#    elif status == 'fighting':
#        if attack_thread.is_alive() == False:
#            status = 'roaming'
#            fly_thread.start()
    stop_signal = threading.Event()


    while True:
        image = ImageGrab.grab()
        if status == 'inactive':
    #        print(status)
            fly_thread = fly_thread_class(daemon=True)
            fly_thread.start()
        elif status == 'roaming':
            if fly_thread.is_alive() is True:
                print('fly is ALIVE!!!')
                stop_signal.set()
                fly_thread.join()
    #        print(status)
            attack_thread = attack_thread_class(daemon=True)
            attack_thread.start()
        elif status == 'under attack':
            if attack_thread.is_alive() is True:
                print('attack is ALIVE!!!')
                stop_signal.set()
                attack_thread.join()
    #        print(status)
            fly_thread = fly_thread_class(daemon=True)
            fly_thread.start()
        print(status)



if __name__ == '__main__':
    iter = 0
    iter += 1
    print('iter {}'.format(iter))
    main()