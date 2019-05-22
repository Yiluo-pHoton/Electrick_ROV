from pyfirmata import Arduino, util
import time
board = Arduino('/dev/cu.usbmodem146201')
# The address is subject to change when using different port or different adaptors.
# Connect it to matlab first and fetch the address from matlab.

def time(distance):
    distance = abs(distance)
    if distance > 11.5:
        return (distance - 5.71)/(30.31)
    else:
        return 0.2
# function acquired from fitting the data, minimum movement is 11.5 cm.

def goforward(coordinate):
    # coordinate goes from 0 to 23 cm
    # to avoid minumum movement issue let 1 cm coordinate -> 11.5 cm distance
    distance = coordinate*12
    if distance = 0 :
        # do nothing
    elif distance > 0 :
        board.digital[5].write(0)
        time.sleep(time(distance))
        board.digital[5].write(1)
        # go forward
    else :
        board.digital[6].write(0)
        time.sleep(time(distance))
        board.digital[6].write(1)
        # go backwards
