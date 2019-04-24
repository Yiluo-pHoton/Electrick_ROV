import serial
from time import sleep

ser = serial.Serial('/dev/tty.usbmodem1d11', 9600)

class Queue():
    def __init__(self):
        self.queue = []
        self.length = 3

    def add(self, val):
        self.queue.append(val)

        if len(self.queue) > 3:
            self.pop()

    def pop(self):
        if self.queue:
            self.queue = self.queue[1:]

data_history = Queue()

while True:
    data = ser.readline().split()
    data = np.reshape((4, 6))

    data_history.add(data)

    print(data_history)
