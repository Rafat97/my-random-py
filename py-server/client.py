import socket
import json
import pyautogui
import sys
import os
import cv2
import cv2
import base64
import matplotlib.pyplot as plt
import numpy as nm
import PIL
import io
from PIL import Image
import time


HOST = '192.168.123.101'  # The server's hostname or IP address
PORT = 28280        # The port used by the server
# a Python object (dict):
x = {
  "name": "John",
  "age": {
      "1":30,
      "2":30,
  },
  "city": "New York",
}

# convert into JSON:
jsonToString = json.dumps(x)

# the result is a JSON string:
# print(jsonToString)
sendData = jsonToString
print(type(sendData.encode('utf-8')))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for x in range(100):
        # sendData = str(x) + " Hello, world sdf " 
        seconds = time.time() 
        sendData = jsonToString
        s.sendall(sendData.encode('utf-8'))


        # count = 0
        # filename = "img/"+str(count) + "_img.jpg"
        # myScreenshot = pyautogui.screenshot()
        # myScreenshot.save(filename)

        # xbash = open(filename, "rb").read()
        # s.sendall(xbash)


        data = s.recv(1024)
        seconds = time.time() - seconds 
        print(seconds)
        pass

print('Received', repr(data))
