import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    f = np.fft.fft2(frame)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift))

    cv2.imshow('frame', fshift)

    if cv2.waitKey(1) == 27:
        break