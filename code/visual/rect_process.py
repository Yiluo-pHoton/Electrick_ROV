import numpy as np
import serial
import matplotlib
matplotlib.use("TKAgg")  # for conda env
import matplotlib.pyplot as plt
import lib.train_rec as tr

k = input("number of samples:\n")
modem = '14501'
baud = '115200'
train = tr.Train(int(k), modem, baud)
theta = train.start()
ini_val = []
ini_val_recorded = False

ser = serial.Serial('/dev/cu.usbmodem'+modem, int(baud))

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
        readIn = readIn.reshape((40, 24))
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
        readIn = readIn.reshape((40, 24)) # 40 measurements, 32 features
        # readIn = list(map(lambda x: np.sqrt(np.mean(np.array(x)**2)), list(readIn.transpose())))
        readIn = readIn.mean()
        readIn = np.array([1, readIn])

        Y = np.array(readIn - ini_val) * theta
        print(Y)
        scat.set_offsets(Y)
        plt.pause(1e-10)

plt.show()
