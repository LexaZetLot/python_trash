import cv2
import depth
import filters
from managers import WindowManager, CaptureManager

class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)
        self._curveFilter = filters.BGRPortraCurveFilter()

    def run(self):
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            if frame is not None:
                filters.strokeEdges(frame, frame)
                self._curveFilter.apply(frame, frame)
            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):
        if keycode == 32:
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9:
            if not self._captureManager.isWritingVideo:
                self._captureManager.statrWritingVideo('screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27:
            self._windowManager.destroyWindow()

class CameoDepth(Cameo):
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        device = cv2.CAP_OPENNI2
        #device = cv2.CAP_OPENNI_ASUS
        self._captureManager = CaptureManager(cv2.VideoCapture(device), self._windowManager, True)
        self._curveFilter = filters.BGRPortraCurveFilter()

    def run(self):
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            self._captureManager.channel = cv2.CAP_OPENNI_DISPARITY_MAP
            disparityMap = self._captureManager.frame
            self._captureManager.channel = cv2.CAP_OPENNI_VALID_DEPTH_MASK
            validDepthMap = self._captureManager.frame
            self._captureManager.channel = cv2.CAP_OPENNI_BGR_IMAGE
            frame = self._captureManager.frame

            if frame is None:
                self._captureManager.channel = cv2.CAP_OPENNI_BGR_IMAGE
                frame = self._captureManager.frame

            if frame is not None:
                mask = depth.createMedianMask(disparityMap, validDepthMap)
                frame[mask == 0] = 0
                if self._captureManager.channel == cv2.CAP_OPENNI_BGR_IMAGE:
                    filters.strokeEdges(frame, frame)
                    self._curveFilter.apply(frame, frame)
            self._captureManager.exitFrame()
            self._windowManager.processEvents()


if __name__ == '__main__':
    CameoDepth().run()