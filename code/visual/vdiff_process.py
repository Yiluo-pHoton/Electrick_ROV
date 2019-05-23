import numpy as np
import serial
import matplotlib
matplotlib.use("TKAgg")  # for conda env
import matplotlib.pyplot as plt
import lib.train_vdiff as tr
from pyfirmata import Arduino, util
import time

def Time(distance):
    distance = abs(distance)
    if distance > 11.5:
        return (distance - 5.71)/(30.31)
    else:
        return 0.2
# function acquired from fitting the data, minimum movement is 11.5 cm.

def goforward(coordinate):
    # use pins 12 and 13
    # coordinate goes from 0 to 23 cm
    # to avoid minumum movement issue let 1 cm coordinate -> 11.5 cm distance
    distance = coordinate*12
    if distance == 0 :
        return
        # do nothing
    elif distance > 0 :
        board.digital[12].write(0)
        time.sleep(Time(distance))
        board.digital[12].write(1)
        # go forward
    else :
        board.digital[13].write(0)
        time.sleep(Time(distance))
        board.digital[13].write(1)
        # go backwards


k = input("number of samples:\n")
elec_port = '14501'
robot_port = '14601'
baud = '115200'
train = tr.Train(int(k), elec_port, baud)
theta = train.start()
ini_val = []
ini_val_recorded = False

# initialize board and serial

board = Arduino('/dev/cu.usbmodem'+robot_port)
ser = serial.Serial('/dev/cu.usbmodem'+elec_port, int(baud))


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
        scat.set_offsets(Y)
        plt.pause(1e-10)

plt.show()


