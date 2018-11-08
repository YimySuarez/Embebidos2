from matplotlib import pyplot as plt
import numpy as np
import cv2

def plot_histogram(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    cv2.imshow("Original", image)
    plt.figure()
    plt.title("Histograma")
    plt.xlabel("Int")
    plt.ylabel("Pix")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()


image = cv2.imread('./image/fig.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 3)

#plot_histogram(blur)

(T, binary) = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY_INV)
edge = cv2.Canny(binary, 100, 200)
(cnts, parm) = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print (len(cnts))
cv2.imshow("binary", edge)
cv2.waitKey(0)
