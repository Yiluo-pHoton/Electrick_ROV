import numpy as np
import serial
import matplotlib.pyplot as plt
import lib.train as tr

k, modem, baud = input("k, modem, baud:\n").split()
train = tr.Train(int(k), modem, baud)
theta = train.start()
ini_val = []
ini_val_recorded = False

ser = serial.Serial('/dev/cu.usbmodem'+modem, int(baud))

plt.figure()
plt.xlim(0, 30.1)
plt.ylim(0, 29.8)
scat = plt.scatter(1, 1, c='b', s=20, marker='.')

while True:
    if not ini_val_recorded:
        try:
            readIn = ser.readline().decode('utf-8').split()
        except UnicodeDecodeError:
            continue
        readIn = np.array(list(map(float, readIn)))
        readIn = readIn.reshape((40, 32))
        readIn = list(map(lambda x: np.sqrt(np.mean(np.arrau(x)**2)), list(readIn.transpose())))
        readIn.insert(0, 1)
        init_val_recorded = True
    else:
        try:
            readIn = ser.readline().decode('utf-8').split()
        except UnicodeDecodeError:
            continue
        readIn = np.array(list(map(float, readIn)))
        readIn = readIn.reshape((40, 32)) # 40 measurements, 32 features
        readIn = list(map(lambda x: np.sqrt(np.mean(np.array(x)**2)), list(readIn.transpose())))
        readIn.insert(0, 1)

        Y = np.array(readIn) * theta
        print(Y)
        scat.set_offsets(Y)
        plt.pause(1e-10)

plt.show()
