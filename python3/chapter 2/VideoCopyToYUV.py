import cv2

videoCapture = cv2.VideoCapture('MyInputVid.avi')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWrite = cv2.VideoWriter('MyOutputVid.avi', cv2.VideoWriter.fourcc('I', '4', '2', '0'), fps, size)

success, frame = videoCapture.read()
while success:
    videoWrite.write(frame)
    success, frame = videoCapture.read()