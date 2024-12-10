import os
import cv2
import numpy


def read_images(path, image_size):
    names = []
    trainings_images, training_labels = [], []
    labels = 0

    for dirname, subdirnames, filenames in os.walk(path):
        for subdirname in subdirnames:
            names.append(subdirname)
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                img = cv2.imread(os.path.join(subject_path, filename), cv2.IMREAD_GRAYSCALE)
                if img is None:
                    continue
                img = cv2.resize(img, image_size)
                trainings_images.append(img)
                training_labels.append(labels)
            labels += 1
        print(training_labels.count(0))
        training_images = numpy.array(trainings_images)
        training_labels = numpy.array(training_labels)
        return names, training_images, training_labels

path_to_training_images = '../data/at'
training_image_size = (300, 300)
names, training_images, training_labels = read_images(path_to_training_images, training_image_size)


model = cv2.face.EigenFaceRecognizer().create()
model.train(training_images, training_labels)

face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)
while cv2.waitKey(1) == -1:
    success, frame = camera.read()
    if success:
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            roi_gray = gray[x:x+w, y:y+h]
            if roi_gray.shape == 0:
                continue
            roi_gray = cv2.resize(roi_gray, training_image_size)
            label, confidence = model.predict(roi_gray)
            text = '%s, confidence=%.2f' % (names[label], confidence)
            cv2.putText(frame, text, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Video', frame)