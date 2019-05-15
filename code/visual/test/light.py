import numpy as np
import serial
import matplotlib
matplotlib.use("TKAgg")  # for conda env
import matplotlib.pyplot as plt
import time

ser = serial.Serial('/dev/cu.usbmodem14501', 115200)

def visualize(readIn):
    readIn = np.array(list(map(float, readIn)))
    readIn = readIn.reshape((40, 8))
    readIn = list(map(lambda x: np.sqrt(np.mean(np.array(x)**2)), list(readIn.transpose())))

    print(readIn)

    visual_matrix = np.zeros((8, 8))
    voltage_coordinates = [(0,2), (0,5), (2,7), (5,7), (7,5), (7,2), (5,0), (2,0)]  # (y,x)

    for i in range(len(readIn)):
        visual_matrix[voltage_coordinates[i]] = readIn[i]

    return visual_matrix
light = 0
fig = plt.plot(time.time(), light, cmap='seismic')

while True:
    readIn = ser.readline().decode("utf-8").split()
    visual_matrix readIn

    plt.pause(1e-16)

