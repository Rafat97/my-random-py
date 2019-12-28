import cv2
import os
import matplotlib.pyplot as plt


image = cv2.imread("img/ball_1.jpg")
print(image)
image_rgba = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
#
# image_gray = cv2.cvtColor(image_rgba, cv2.COLOR_RGBA2GRAY)
# image_hsv = cv2.cvtColor(image_rgba, cv2.COLOR_BGR2HSV)

plt.imshow(image_rgba)
plt.show()