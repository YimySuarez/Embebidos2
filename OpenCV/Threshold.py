from matplotlib import pyplot as plt
import numpy as np
import cv2
image = cv2.imread('./image/monedas.jpg')
cv2.imshow("Original", image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 7)
(T, binary) = cv2.threshold(blur, 230, 255, cv2.THRESH_BINARY_INV)
detec = cv2.bitwise_and(image, image, mask=binary)

cv2.imshow("detec", detec)
cv2.waitKey(0)

