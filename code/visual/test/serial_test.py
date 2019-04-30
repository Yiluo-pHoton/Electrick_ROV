import serial

while True:
    ser = serial.Serial('/dev/cu.usbmodem14101', 9600)
    read = str(ser.readline()).decode("utf-8")
    print(read)
