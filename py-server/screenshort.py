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

count = 0
filename = "img/"+str(count) + "_img.jpg"
myScreenshot = pyautogui.screenshot()
myScreenshot.save(filename)

#### USING FILE READ ####

# xbash = open(filename, "rb").read()
# print(type(xbash))
# print(type("sad".encode('utf-8')))
# print(str(xbash).encode('utf-8'))

#### USING OPENCV ####

# image = cv2.imread(filename)
# encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
# retval, buffer = cv2.imencode('.jpg', image, encode_param)
# jpg_as_text = base64.b64encode(buffer)
# #jpg_original = base64.b64decode(jpg_as_text)


#### USING PIL ####

# baseheight = 560
# img = Image.open(filename)
# hpercent = (baseheight / float(img.size[1]))
# wsize = int((float(img.size[0]) * float(hpercent)))
# img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
# img.save("resized_image.jpg")
# img = Image.open("resized_image.jpg")
# byteIO = io.BytesIO()
# img.save(byteIO, format='PNG')
# byteArr = byteIO.getvalue()
# print(type(byteArr))



# print('Press Ctrl-C to quit.')
# try:
#     while TruHello world!e:HelloHello world! world!
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')


# while True:
#     filename = "img/"+str(count) + "_img.png"
#     myScreenshot = pyautogui.screenshot()
#     pyautogui.lo
#     myScreenshot.save(filename)
#     print(myScreenshot)

#     count = count + 1
#     pass
