import os
import time
while True:
    ret = os.popen('python ./dh11.py')
    print(ret.read())
    time.sleep(5)
