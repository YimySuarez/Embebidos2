import numpy as np
import cv2
image = cv2.imread('./image/tux.jpeg')
cv2.imshow("Original", image)
plantilla = np.zeros(image.shape[:2], dtype="uint8")
(B, G, R) = cv2.split(image)
#cv2.imshow("Blue", B)
#cv2.imshow("Green", G)
#cv2.imshow("Red", R)

cv2.imshow("Blue_Color", cv2.merge([B, plantilla, plantilla]))
cv2.imshow("Green_Color", cv2.merge([plantilla, G, plantilla]))
cv2.imshow("Red_Color", cv2.merge([plantilla, plantilla, R]))
cv2.waitKey(0)