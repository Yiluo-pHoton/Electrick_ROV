import matplotlib.pyplot as plt
import numpy as np
import serial

# ser = serial.Serial('/dev/cu.usbmodem14101', 9600)

def visualize(readIn):
    readIn = np.array(list(map(float, readIn)))
    readIn = readIn.reshape((40, 8))
    readIn = list(map(lambda x: np.sqrt(np.mean(np.array(x)**2)), list(readIn.transpose())))

    print(readIn)

    visual_matrix = np.zeros((8, 8))
    voltage_coordinates = [(2,7), (5,7), (7,5), (7,2), (5,0), (2,0), (0,2), (0,5)]

    for i in range(len(readIn)):
        visual_matrix[voltage_coordinates[i]] = readIn[i]

    return visual_matrix

visual_matrix = np.zeros((8,8))
fig = plt.imshow(visual_matrix, cmap='plasma')
plt.clim(0,5)
plt.colorbar()

while True:
    readIn = ser.readline().decode("utf-8").split()
    # readIn = (str(i) + " ") * 320
    # readIn = readIn[:-1].split()
    visual_matrix = visualize(readIn)

    fig.set_data(visual_matrix)
    # fig.draw()

    plt.pause(0.05)
    i += 1
