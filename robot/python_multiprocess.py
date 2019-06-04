from multiprocessing import Process
import time

def loop_a():
    while 1:
        print("a")
        #time.sleep(0.5)
        

def loop_b():
    while 1:
        print("b")
        #time.sleep(0.5)

if __name__ == '__main__':
        Process(target=loop_a).start()
        Process(target=loop_b).start()
