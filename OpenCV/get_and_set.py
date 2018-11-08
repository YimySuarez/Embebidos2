import numpy
import cv2
image = cv2.imread('./image/tux.jpeg')
cv2.imshow("Original", image)
(x, y, z) = image.shape
print x, y, z
for pix_y in xrange(y):
   for pix_x in xrange(x):
       if(image[pix_x, pix_y][0] > 230 and image[pix_x, pix_y][1] > 230 and image[pix_x, pix_y][2] > 230):
           image[pix_x, pix_y] = (0,0,0)

cv2.imshow("Update", image)
cv2.waitKey(0)
