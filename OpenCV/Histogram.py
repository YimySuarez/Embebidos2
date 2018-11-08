from matplotlib import pyplot as plt
import numpy as np
import cv2
image = cv2.imread('./image/tux.jpeg')
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
plt.figure()
plt.title("Histograma RGB")
plt.xlabel("Int")
plt.ylabel("Pix")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)