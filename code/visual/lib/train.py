import numpy as np
import const as _c
import serial

class Train():
    def __init__(self, k, modem, baud):
        #outter = [8, 9, 10, 11, 12, 15, 16, 19, 20, 21, 22, 23]
        self.k = k
        self.X = []
        #self.Y = _c.POS[outter, :]
        self.Y = _c.POS[:,:]
        self.ser = serial.Serial('/dev/cu.usbmodem'+modem, int(baud))
        self.ini_val = np.array(self.collect())
        print("Done initializing")

    def start(self):
        for i in range(self.k):
            pause = input("Press Enter to collect for point " + str(i+1))
            self.X += [np.array(self.collect())-self.ini_val]
        X = np.matrix(self.X)
        Y = np.matrix(self.Y)
        theta = np.linalg.inv(X.T*X)*X.T*Y
        self.ser.close()
        print(X*theta)
        return theta

    def collect(self):
        try:
            readIn = self.ser.readline().decode('utf-8').split()
        except UnicodeDecodeError:
            return self.collect()

        if len(readIn) != 320 * 4:
            return self.collect()
        else:
            readIn = np.array(list(map(float, readIn)))
            readIn = readIn.reshape((40, 32))  # 40 times, 32 features
            # readIn = list(map(lambda x: np.sqrt(np.mean(np.array(x)**2)), list(readIn.transpose())))
            readIn = readIn.mean(axis=0)
            np.insert(readIn, 0, 1)
            return readIn
