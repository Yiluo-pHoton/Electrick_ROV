import numpy as np
import serial
import matplotlib
matplotlib.use("TKAgg")  # for conda env
import matplotlib.pyplot as plt
import lib.train_vdiff as tr
from pyfirmata import Arduino, util
import time

def sleeptime(distance):
    distance = abs(distance)
    if distance > 11.5:
        return (distance - 5.71)/(30.31)
    else:
        return 0.2

def goforward(distance):
    global initial_time
    global control_num
    global pausetime
    global forward
    global position
    if control_num == 0 and distance-position != 0:
        pausetime = sleeptime(distance-position)
        if distance-position > 0 :
            board.digital[5].write(0)
            initial_time = time.perf_counter()
            forward = 1
            control_num = 1
            print("go forward!" + str(distance - position))
            position = distance
            return
        else :
            print("Going backward" + str(distance-position))
            board.digital[6].write(0)
            initial_time = time.perf_counter()
            forward = 2
            control_num = 1
            position = distance
            return
    else:
        time_now = time.perf_counter()
        if time_now - initial_time >= pausetime:
            if forward == 1:
                board.digital[5].write(1)
                control_num = 0
                distance = 0
                return
            else:
                board.digital[6].write(1)
                control_num = 0
                distance = 0
                return


k = input("number of samples:\n")
elec_port = '14501'
robot_port = '14301'
baud = '115200'
train = tr.Train(int(k), elec_port, baud)
theta = train.start()
ini_val = []
ini_val_recorded = False

# initialize board and serial

board = Arduino('/dev/cu.usbmodem'+robot_port)
ser = serial.Serial('/dev/cu.usbmodem'+elec_port, int(baud))

# initialize robot
#initial values
global initial_time
initlal_time = time.perf_counter()
global control_num
control_num = 0
global pausetime
pausetime = 0
global forward
global position
position = 0
forward = 1 # 1 is forward, 2 is backward
print('Robot Control Ready...')
board.digital[5].write(1)
board.digital[6].write(1)


plt.figure()
plt.xlim(0, 40)
plt.ylim(0, 2.)
scat = plt.scatter(1, 1, c='b', s=510, marker='o')



while True:
    if not ini_val_recorded:
        try:
            readIn = ser.readline().decode('utf-8').split()
        except UnicodeDecodeError:
            continue
        readIn = np.array(list(map(float, readIn)))
        readIn = readIn.reshape((40, 5))
        # readIn = list(map(lambda x: np.sqrt(np.mean(np.arrau(x)**2)), list(readIn.transpose())))
        readIn = readIn.mean()
        readIn = np.array([0, readIn])
        ini_val = readIn
        ini_val_recorded = True
        print(ini_val)
        print(ini_val_recorded)
    else:
        try:
            readIn = ser.readline().decode('utf-8').split()
        except UnicodeDecodeError:
            continue
        readIn = np.array(list(map(float, readIn)))
        readIn = readIn.reshape((40, 5)) # 40 measurements, 32 features
        # readIn = list(map(lambda x: np.sqrt(np.mean(np.array(x)**2)), list(readIn.transpose())))
        readIn = readIn.mean()
        readIn = np.array([1, readIn])

        Y = np.array(readIn - ini_val) * theta
        print(Y)
        distance = Y[0,0]/40*11.5
        goforward(distance)
        scat.set_offsets(Y)
        plt.pause(1e-10)

plt.show()


