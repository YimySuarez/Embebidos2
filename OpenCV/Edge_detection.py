from matplotlib import pyplot as plt
import numpy as np
import cv2
image = cv2.imread('./image/monedas.jpg')
cv2.imshow("Original", image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 7)
(T, binary) = cv2.threshold(blur, 230, 255, cv2.THRESH_BINARY_INV)
canny = cv2.Canny(binary, 100, 200)

cv2.imshow("detec", canny)
cv2.waitKey(0)
