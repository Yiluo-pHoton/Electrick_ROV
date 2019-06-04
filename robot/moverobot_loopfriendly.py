from pyfirmata import Arduino, util
import time
board = Arduino('/dev/cu.usbmodem14401')

#initial values
global initial_time
initlal_time = time.perf_counter()
global control_num
control_num = 0
global pausetime
pausetime = 0
global forward
forward = 1 # 1 is forward, 2 is backward

def sleeptime(distance):
    distance = abs(distance)
    if distance > 11.5:
        return (distance - 5.71)/(30.31)
    else:
        return 0.2
# same function as move robot

# put this in initialization
print('sleepy time over')

board.digital[5].write(1)
board.digital[6].write(1)

# below are the lines to be added to the main loop
distance = 10

def goforward():
    if control_num == 0 and distance != 0:
        pausetime = sleeptime(distance)
        if distance > 0 :
            board.digital[5].write(0)
            initial_time = time.perf_counter()
            forward = 1
            control_num = 1
            print("go forward!")
        else :
            board.digital[6].write(0)
            initial_time = time.perf_counter()
            forward = 2
            control_num = 1
    else:
        time_now = time.perf_counter()
        if time_now - initial_time >= pausetime:
            if forward == 1:
                board.digital[5].write(1)
                control_num = 0
                distance = 0
            else:
                board.digital[6].write(1)
                control_num = 0
                distance = 0
        
