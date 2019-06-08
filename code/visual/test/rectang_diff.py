import numpy as np
import serial
import matplotlib
matplotlib.use("TKAgg")  # for conda env
import matplotlib.pyplot as plt

port = '14501'
ser = serial.Serial('/dev/cu.usbmodem'+port, 115200)
ini_val = []
ini_val_recorded = False

def visualize(readIn):
    readIn = np.array(list(map(float, readIn)))
    readIn = readIn.reshape((40, 5))
    readIn = readIn.mean(axis=0)
    #readIn = list(map(lambda x: np.sqrt(np.mean(np.array(x)**2)), list(readIn.transpose())))

    print(readIn)

    visual_matrix = np.zeros((4, 10))
    voltage_coordinates = [ (0,4), (3,4), (0,7), (3,7), (1,9)]  # (y,x)
    #voltage_coordinates = [(0,0), (3,0), (0,3), (3,3), (0,6), (3,6), (0,9), (3,9)]  # (y,x)


    for i in range(len(readIn)):
        visual_matrix[voltage_coordinates[i]] = readIn[i]

    return visual_matrix

visual_matrix = np.zeros((4,10))
fig = plt.imshow(visual_matrix, cmap='seismic')
plt.clim(-0.007,0.007)
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