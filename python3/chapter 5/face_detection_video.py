import cv2

face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')


camera = cv2.VideoCapture('./Клоун Бебей танцует под Вангеров.mp4')
size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)), int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWrite = cv2.VideoWriter('./outputVideo.avi', cv2.VideoWriter.fourcc('I', '4', '2', '0'), camera.get(cv2.CAP_PROP_FPS), size)

while (cv2.waitKey(1) == -1):
    ret, frame = camera.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.03, 5, minSize=(120, 120))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5, minSize=(40, 40))
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(frame, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)
        cv2.imshow('Video', frame)
        videoWrite.write(frame)