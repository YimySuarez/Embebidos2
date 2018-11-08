from matplotlib import pyplot as plt
import numpy as np
import cv2
image = cv2.imread('./image/campus.jpg')
cv2.imshow("Original", image)
cv2.waitKey(0)

gray =  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

equal = cv2.equalizeHist(gray)

cv2.imshow("Ecualizada", equal)
cv2.waitKey(0)

#(B, G, R) = cv2.split(image)
hist_B = cv2.calcHist([gray], [0], None, [256], [0, 256])
hist_G = cv2.calcHist([equal], [0], None, [256], [0, 256])

plt.figure()
plt.title("Histograma RGB")
plt.xlabel("Int")
plt.ylabel("Pix")

plt.plot(hist_B)
plt.plot(hist_G)

plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)