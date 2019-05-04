import numpy as np
import serial
import matplotlib
matplotlib.use("TKAgg")  # for conda env
import matplotlib.pyplot as plt

ser = serial.Serial('/dev/cu.usbmodem14501', 115200)
ini_val = []
ini_val_recorded = False

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

visual_matrix = np.zeros((8,8))
fig = plt.imshow(visual_matrix, cmap='seismic')
plt.clim(-0.3,0.3)
plt.colorbar()

i = 0

while True:
    # readIn = (str(i) + " ") * 320
    # readIn = readIn[:-1].split()
    if not ini_val_recorded:
        for i in range(4):
            readIn = ser.readline().decode("utf-8").split()
            ini_val.append(visualize(readIn))
            ini_val_recorded = True
    else:
        readIn = ser.readline().decode("utf-8").split()
        visual_matrix = visualize(readIn)
        fig.set_data(visual_matrix-ini_val[i])
    # fig.draw()

    i = (i+1)%4

    plt.pause(1e-16)
