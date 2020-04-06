# -*- coding: utf-8 -*
#!/usr/bin/python3
import socket
import json
import datetime
import threading
import time
import re
from dht11 import getTempHum
from relay import switch
from rgb import rgbThread

# 从配置文件中读取信息
f = open("./config.json", "r", encoding="UTF-8")
config_dict = json.load(f)
print(config_dict)
hostname = config_dict['netty-server-host']
port = config_dict['netty-server-port']

deviceInfo = json.dumps({
    'type': 1,
    'data':{
        'id': config_dict['device-id'],
        'status': True,
        'positionX': 126.627938,
        'positionY': 45.715051,
        'connTime': datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S'),
        'userId': config_dict['device-owner-id']
    }
})

print(deviceInfo)
print(type(deviceInfo))

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
except socket.error as msg:
    print(msg)
    s.close()
    sys.exit(1)

def sendMsg():
    s.send(bytes(deviceInfo +'\n', "UTF-8"))
    while True:
        res = getTempHum()
        if(res != None ):
            tempHum = json.dumps({
                'type': 2,
                'data': {
                    'temp': res[0],
                    'humidity': res[1],
                    'time': datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S'),
                    'deviceId': config_dict['device-id']
                    }
                })
            s.send(bytes(tempHum+'\n', 'UTF-8'))
        time.sleep(5)

def recvMsg():
    rgb_thread = rgbThread(100, 0, 0)
    rgb_thread.start()
    while 1:
        data = str(s.recv(1024), encoding='utf-8')
        print('aa',data)
        if data == 'exit':
            print('查询无此设备，请检查 device-id 配置')
            s.close()
            break
        else:
            ctrl = data.split('_')
            if ctrl[0] == 'switch':
                print('switch')
                if ctrl[1] == '1':
                    switch(True)
                else:
                    switch(False)
            elif ctrl[0] == 'rgb':
                rgb_thread.stop()
                rgb_thread = None
                pattern = re.compile(r'[(](.*?)[)]')
                rgbStr =  pattern.findall(ctrl[1])
                r,g,b = list(map(int, rgbStr[0].split(',')))
                print("rgb=",r,g,b)
                time.sleep(0.5)
                print('--------')
                rgb_thread = rgbThread(r, g, b)
                rgb_thread.start()
 
 
if __name__ == '__main__':
    threading.Thread(target=sendMsg).start()
    threading.Thread(target=recvMsg).start()
