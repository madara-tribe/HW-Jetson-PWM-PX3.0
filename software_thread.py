from multiprocessing import Queue
import time

def xaxis_calibrate(angle):
    duty = int(float(angle) * 2.17 + 102)
    # reverse
    duty = 594 - duty
    print('xaxis angle is', f' {angle}' 'duty is' f' {duty}')
    return duty
    
def yaxis_calibrate(angle):
    duty = int(float(angle) * 2.17 + 102)
    print('y-axis, angle is', f' {angle}' 'duty is' f' {duty}')
    return duty
    
    
def sw_thread(q:Queue, opt):
    x_max = opt.x_max
    x_min = opt.x_min
    y_min = opt.y_min
    y_max = opt.y_max
    print("x calibrating")
    for x in range(x_min, x_max):
        xduty = xaxis_calibrate(x)
        time.sleep(opt.timer)
        q.put(["x", xduty])
        
    print("y calibrating")
    for y in range(y_min, y_max):
        yduty = yaxis_calibrate(y)
        time.sleep(opt.timer)
        q.put(["y", yduty])
