import threading
import time
from rgb_new import rgbThread
from queue import Queue

thread1 = rgbThread(100, 0, 0)
thread1.start()

print("等待 5s")
time.sleep(5)

thread1.stop()


        