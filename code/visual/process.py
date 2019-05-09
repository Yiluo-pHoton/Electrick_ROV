import numpy as np
import serial
import matplotlib.pyplot as plt

k, modem, baud = input("k, modem, baud:\n").split()
train = Train(int(k), modem, baud)
theta = train.start()

ser = serial.Serial('/dev/cu.usbmodem'+modem, int(baud))

plt.figure()
plt.xlim(0, 30.1)
plt.ylim(0, 29.8)
scat = plt.scatter(0, 0, c='b', s=10, marker='.')

while True:
    readIn = ser.readline().decode('utf-8').split()
    readIn = np.array(list(map(float, readIn)))
    readIn = list(map(lambda x: np.sqrt(np.mean(np.array(x)**2)), list(readIn.transpose())))

    Y = np.array(readIn) * theta

    scat.set_offsets(Y)
    plt.pause(1e-10)

plt.show()
