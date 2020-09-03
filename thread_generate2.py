# Modules
import time, threading, os
print("you have ", len(os.sched_getaffinity(0)), " available in your system")

os.sched_setaffinity(0, {0})

# Thread-Function
def show():
    print("Start Thread")
    for i in range(5):
        print(i, time.time())
        time.sleep(1.5)
    print("End Thread")

# main program
print("Start main program")
t = threading.Thread(target=show)
t.start()
time.sleep(10)
print("End main program")
