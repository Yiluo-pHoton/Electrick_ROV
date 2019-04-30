import serial
from time import sleep

ser = serial.Serial('/dev/cu.usbmodem14101', 9600)
fps = 3

class Queue():
    def __init__(self):
        self.queue = []
        self.length = fps

    def add(self, val):
        self.queue.append(val)

        if len(self.queue) > 3:
            self.pop()

    def pop(self):
        if self.queue:
            self.queue = self.queue[1:]

data_history = Queue()

while True:
    data = ser.readline().decode("utf-8").split()
    data = np.reshape((4, 8))

    data_history.add(data)

    print(data_history)
