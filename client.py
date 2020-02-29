#!/usr/bin/python3
import socket
import json
import datetime
import threading
import time

# 从配置文件中读取信息
f = open("./config.json", "r", encoding="UTF-8")
config_dict = json.load(f)
print(config_dict)
hostname = config_dict['netty-server-host']
port = config_dict['netty-server-port']

deviceInfo = json.dumps({
    'type': 1,
    'data':{
        'name': config_dict['device-name'],
        'describe': config_dict['device-describe'],
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

def recvMsg():
    while 1:
        data = s.recv(1024)
        if data == 'exit':
            print('if not data')
            s.close()
            break
        print('aa',data.encode('utf-8'))
 
 
if __name__ == '__main__':
    threading.Thread(target=sendMsg).start()
    threading.Thread(target=recvMsg).start()
