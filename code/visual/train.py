import numpy as np
import const as _c
import serial

class Train():
    def __init__(self, k, modem, baud):
        self.k = k
        self.X = []
        self.Y = _c.POS[:k, :]
        ser = serial.Serial('/dev/cu.usbmodem'+modem, int(baud))

    def start(self):
        for i in range(k):
            self.X += [np.array(self.collect())]
            pause = input("Press Enter for next point.")
        X = self.X
        Y = self.Y
        theta = (X.T*X)*X.T*Y
        ser.close()
        return theta

    def collect(self):
        readIn = ser.readlin().decode('utf-8').split()

        if len(readIn) != 320:
            return self.collect()
        else:
            readIn = np.array(list(float, readIn))
            readIn = readIn.reshape((40, 8))
            readIn = list(map(lambda x: np.sqrt(np.mean(np.array(x)**2)), list(readIn.transpose())))
            return readIn
