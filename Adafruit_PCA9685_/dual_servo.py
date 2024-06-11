import time
import Adafruit_PCA9685
import argparse

# Set frequency to 60hz, good for servos.
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

xaxis_pin = 15
yaxis_pin = 14
# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
def reset_x(angle=59):
    duty = int(float(angle) * 2.17 + 102)
    # reverse
    duty = 594 - duty
    print('x reset angle is', f' {angle}' 'duty is' f' {duty}')
    return duty #self.pwm.set_pwm(self.xaxis_pin, 0, duty)

def reset_y(angle=159):
    duty = int(float(angle) * 2.17 + 102)
    print('y reset angle is', f' {angle}' 'duty is' f' {duty}')
    return duty
        # self.pwm.set_pwm(self.yaxis_pin, 0, duty)
        #time.sleep(0.1)

def xaxis_calibrate(angle):
    duty = int(float(angle) * 2.17 + 102)
    # reverse
    duty = 594 - duty
    print('xaxis angle is', f' {angle}' 'duty is' f' {duty}')
    return duty # pwm.set_pwm(self.xaxis_pin, 0, duty)

def yaxis_calibrate(angle):
    duty = int(float(angle) * 2.17 + 102 )
    print('y-axis, angle is', f' {angle}' 'duty is' f' {duty}')
    return duty # pwm.set_pwm(self.yaxis_pin, 0, duty)
        #time.sleep(0.1)

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
    opt = parser.parse_args()
    return opt 

opt = get_parser()
#def calibrate(opt):
pwm = Adafruit_PCA9685.PCA9685()
# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)
xaxis_pin = 15
yaxis_pin = 14
print('start cycle')
    
xduty0 = reset_x(opt.x_defalut)
pwm.set_pwm(xaxis_pin, 0, xduty0)
yduty0 = reset_y(opt.y_defalut)
pwm.set_pwm(xaxis_pin, 0, yduty0)
xduty1 = 102 #xaxis_calibrate(opt.x_min)
xduty2 = 492 # xaxis_calibrate(opt.x_max)
yduty1 = 102 #yaxis_calibrate(opt.y_min)
yduty2 = 492 #yaxis_calibrate(opt.y_max)
# x-default => xmax=> xmin => y-default => ymax => ymin
time.sleep(3)
while True:
    # x-max
    pwm.set_pwm(xaxis_pin, 0, xduty1)
    time.sleep(3)
    print('1st clear')
    # x-min
    pwm.set_pwm(xaxis_pin, 0, xduty2)
    time.sleep(3)
    print('2st clear')
    # y-max
    pwm.set_pwm(xaxis_pin, 0, yduty1)
    time.sleep(3)
    print('3st clear')
    # y-min
    pwm.set_pwm(xaxis_pin, 0, yduty2)
    time.sleep(3)
    print('4st clear')
    #self.reset_x(opt.x_defalut)
    #self.reset_y(opt.y_defalut)
