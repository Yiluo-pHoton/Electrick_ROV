import time

#initial values
initial_time = time.perf_counter()
control_num = 0
pausetime = 0
forward = 1 # 1 is forward, 2 is backward

def sleeptime(distance):
    distance = abs(distance)
    if distance > 11.5:
        return (distance - 5.71)/(30.31)
    else:
        return 0.2
#same function as move robot

# below are the lines to be added to the main loop
while True:
    if control_num == 0:
        pausetime = sleeptime(distance)
        if distance > 0 :
            board.digital[5].write(0)
            initial_time = time.perf_counter()
            forward = 1
            control_num = 1
        else :
            board.digital[6].write(0)
            initial_time = time.perf_counter()
            forward = 2
            control_num = 1
    else:
        time_now = time.perf_counter()
        if time_now - initial_time >= pausetime:
            if forward == 1:
                board.digital[5].write(1)
                control_num = 0
            else:
                board.digital[6].write(1)
                control_num = 0
                
        
