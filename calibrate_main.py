import argparse
import os
from tkinter import Tk
from Adafruit_PCA9685_.pan_tilt import App
#from Adafruit_PCA9685_.dual_servo import calibrate

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--gui', action='store_true', help='calibrate gui mode')
    parser.add_argument('-c', '--command', action='store_true', help='calibrate command line mode')
    parser.add_argument('--x_max', type=int, default=180, help='x angle max')
    parser.add_argument('--x_min', type=int, default=0, help='x angle min')
    parser.add_argument('--y_max', type=int, default=180, help='y angle max')
    parser.add_argument('--y_min', type=int, default=0, help='y angle min')
    parser.add_argument('--y_defalut', type=int, default=169, help='y default angle')
    parser.add_argument('--x_defalut', type=int, default=66, help='x default angle')
    parser.add_argument('--set_time', type=int, default=1, help='set timer')
    opt = parser.parse_args()
    return opt


def main(opt):
    if opt.gui:
        root = Tk()
        root.wm_title('Servo Control')
        app = App(root)
        root.geometry("220x120+0+0")
        root.mainloop()
    elif opt.command:
        os.system('python3 Adafruit_PCA9685_/dual_servo.py')


if __name__=='__main__':
    opt = get_parser()
    main(opt)
