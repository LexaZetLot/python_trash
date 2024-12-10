import cv2
import numpy as np

xi, yi = 0, 0
new_rec = False

def funcMaus(event, x, y, flags, param):
    global xi, yi, new_rec
    if event == cv2.EVENT_LBUTTONDOWN:

        xi = x
        yi = y
        new_rec = True

img = cv2.imread('women_in_hayfield_detected.png')
cv2.namedWindow('image')
split = cv2.split(img)
histSize = 256
histRange = (0, histSize)
accumulate = False

bHist = cv2.calcHist(split, [0], None, [histSize], histRange, accumulate=accumulate)
gHist = cv2.calcHist(split, [1], None, [histSize], histRange, accumulate=accumulate)
rHist = cv2.calcHist(split, [2], None, [histSize], histRange, accumulate=accumulate)



hist_w = 512
hist_h = 400
bin_w = int(round( hist_w/histSize ))
histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)

cv2.normalize(bHist, bHist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
cv2.normalize(gHist, gHist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
cv2.normalize(rHist, rHist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)


for i in range(1, histSize):
    cv2.line(histImage, ( bin_w*(i-1), hist_h - int(bHist[i-1]) ),
            ( bin_w*(i), hist_h - int(bHist[i]) ),
            ( 255, 0, 0), thickness=2)
    cv2.line(histImage, ( bin_w*(i-1), hist_h - int(gHist[i-1]) ),
            ( bin_w*(i), hist_h - int(gHist[i]) ),
            ( 0, 255, 0), thickness=2)
    cv2.line(histImage, ( bin_w*(i-1), hist_h - int(rHist[i-1]) ),
            ( bin_w*(i), hist_h - int(rHist[i]) ),
            ( 0, 0, 255), thickness=2)

cv2.imshow('histImage', histImage)
cv2.imshow('image', img)
cv2.setMouseCallback('image', funcMaus)

buf = img.copy()
while True:
    if new_rec:
        buf = img.copy()
        cv2.rectangle(buf, (xi - 6, yi - 6), (xi + 6, yi + 6), (0, 255, 0), 1)
        subText = f'({xi}, {yi})'
        cv2.putText(buf, subText, (xi - 6, yi - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        bufPoint = buf[xi, yi]
        bufPointT = bufPoint[0] + bufPoint[1] + bufPoint[2] / 3
        subText = f'{bufPointT}'
        cv2.putText(buf, subText, (xi - 6, yi - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        sig = ((bufPoint[2] - bufPoint[1]) + (bufPoint[2] - bufPoint[0])) /  ((bufPoint[2] - bufPoint[1]) ** 2 + (bufPoint[2] - bufPoint[0]) * (bufPoint[0] - bufPoint[1]))
        subText = f'{sig}'
        cv2.putText(buf, subText, (xi - 6, yi - 35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        new_rec = False

    cv2.imshow('image', buf)

    if cv2.waitKey(1) == 27:
        break