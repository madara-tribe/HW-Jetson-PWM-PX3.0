#!/usr/bin/env python


import Jetson.GPIO as GPIO
import time
import threading
import sys

output_pin1 = 32 
output_pin2 = 33 
t=2
GPIO.setmode(GPIO.BOARD)
GPIO.setup(output_pin1, GPIO.OUT, initial=GPIO.HIGH)
p1 = GPIO.PWM(output_pin1, 50)

GPIO.setup(output_pin2, GPIO.OUT, initial=GPIO.HIGH)
p2 = GPIO.PWM(output_pin2, 50)
def p1_loop():
    while flag:
        sita1=7.25
        p1.start(sita1)
        print("p1 angle {}".format(sita1))
        time.sleep(t)
        sita2=2.5
        p1.start(sita2)
        print("p1 angle {}".format(sita2))
        time.sleep(t)
        sita3=12
        p1.start(sita3)
        print("p1 angle {}".format(sita3))
        time.sleep(t)
        sita4=8
        p1.start(sita4)
        print("p1 angle {}".format(sita4))
        time.sleep(t)

def p2_loop():
    while flag:
        beta1=7.25
        p2.start(beta1)
        print("p2 angle {}".format(beta1))
        time.sleep(t)
        beta2=2.5
        p2.start(beta2)
        print("p2 angle {}".format(beta2))
        time.sleep(t)
        beta3=12
        p2.start(beta3)
        print("p2 angle {}".format(beta3))
        time.sleep(t)
        beta4=7.25
        p2.start(beta4)
        print("p2 angle {}".format(beta4))
        time.sleep(t)
        

if __name__ == '__main__':
    flag = True
    c=0
    th1 = threading.Thread(target=p1_loop)
    th1.start()
    th2 = threading.Thread(target=p2_loop)
    th2.start()
    while True:
        c +=1
        if c==100:
            flag =False
            th1.join()
            th2.join()
            p1.stop()
            p2.stop()
            GPIO.cleanup()
            sys.exit(1)
    GPIO.cleanup()
