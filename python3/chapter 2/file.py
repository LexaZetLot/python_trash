import cv2
import numpy

img = numpy.zeros((3, 3), dtype=numpy.uint8)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img)

img = cv2.imread('MyPic.png')
cv2.imwrite('MyPic.png', img)

grayImg = cv2.imread('MyPic.png', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('MyPicGray.png', grayImg)