from matplotlib import pyplot as plt
import numpy as np
import cv2
image = cv2.imread('./image/campus.jpg')
cv2.imshow("Original", image)
cv2.waitKey(0)
#BLUR
blur = cv2.blur(image, (7, 7))
cv2.imshow("Blur", blur)
cv2.waitKey(0)
#GAUSS
gauss = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow("Gauss", gauss)
cv2.waitKey(0)

#MEDIAN BLUR
gauss = cv2.medianBlur(image, 11)
cv2.imshow("Median", gauss)
cv2.waitKey(0)

#BILATERAL
bilat = cv2.bilateralFilter(image, 9, 41, 41)
cv2.imshow("Bilateral", bilat)
cv2.waitKey(0)
