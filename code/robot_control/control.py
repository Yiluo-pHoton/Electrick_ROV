from pyfirmata import Arduino, util
import time
import pdb
modem = '14501'
board = Arduino('/dev/cu.usbmodem'+modem)


def Time(distance):
    distance = abs(distance)
    if distance > 11.5:
        return (distance - 5.71)/(30.31)
    else:
        return 0.2
# function acquired from fitting the data, minimum movement is 11.5 cm.

def goforward(coordinate):
    # use pins 12 and 13
    # coordinate goes from 0 to 23 cm
    # to avoid minumum movement issue let 1 cm coordinate -> 11.5 cm distance
    distance = coordinate*12
    if distance == 0 :
        return
        # do nothing
    elif distance > 0 :
        board.digital[12].write(0)
        time.sleep(Time(distance))
        board.digital[12].write(1)
        # go forward
    else :
        board.digital[13].write(0)
        time.sleep(Time(distance))
        board.digital[13].write(1)
        # go backwards
board.digital[12].write(1)
board.digital[13].write(1)

pdb.set_trace()

