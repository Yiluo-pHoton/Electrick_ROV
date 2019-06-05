import numpy as np
import const as _c
import serial

class Train():
    def __init__(self, k, modem, baud):
        self.k = k
        self.X = []
        self.Y = _c.POS[:,:]
        self.initialized = False
        self.ser = serial.Serial('/dev/cu.usbmodem'+modem, int(baud))
        self.ini_val = np.array(self.collect())
        print("Done initializing")

    def start(self):
        for i in range(self.k):
            pause = input("Press Enter to collect for point " + str(i+1))
            self.X += [np.array(self.collect())-self.ini_val]
        X = np.matrix(self.X)
        Y = np.matrix(self.Y)
        print(X)
        theta = np.linalg.inv(X.T*X)*X.T*Y
        self.ser.close()
        print(X*theta)
        return theta

    def collect(self):
        try:
            readIn = self.ser.readline().decode('utf-8').split()
        except UnicodeDecodeError:
            return self.collect()

        if len(readIn) != 4*40:
            return self.collect()
        else:
            readIn = np.array(list(map(float, readIn))) ** 2
            readIn = readIn.reshape((40, 4))  # 40 times, 32 features
            # readIn = list(map(lambda x: np.sqrt(np.mean(np.array(x)**2)), list(readIn.transpose())))
            readIn = readIn.mean()
            readIn = np.array([2 if self.initialized else 1, readIn])
            self.initialized = 1
            return readIn
