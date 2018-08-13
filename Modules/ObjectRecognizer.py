#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ********************************************
# Object Recognition Model v1
# for feeding robot arm
# By Ye Liu
# Aug 9 2018
# ********************************************

import cv2
import serial
from time import sleep


class ObjectRecognizer(object):

    def __init__(self, window_name, camera_idx, port):
        self.color = (0, 255, 0)
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.window_name = window_name
        self.camera_idx = camera_idx

        self.faceClassfier = cv2.CascadeClassifier(
            '/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml')
        self.breadClassfier = cv2.CascadeClassifier(
            '/Volumes/Data/Git/Feeding-Robot-Demo/Modules/cascade_bread_11stages.xml')
        self.classifier = self.faceClassfier

        self.ser = serial.Serial(port, 9600)

    def catchUsbVideo(self):
        cv2.namedWindow(self.window_name, 0)
        # cv2.resizeWindow(self.window_name, 100, 100)

        cap = cv2.VideoCapture(self.camera_idx)
        count = 0

        while cap.isOpened():
            ok, frame = cap.read()
            if not ok:
                print('frame not found')
                break

            # Create gray level image
            grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            with open('/Volumes/Data/Git/Feeding-Robot-Demo/Modules/queue.txt', 'r+') as f:
                # Read command from file
                command = f.read()

                if command:
                    # Change classifier
                    if command == 'bread':
                        self.classifier = self.breadClassfier
                        print('bread')
                    else:
                        self.classifier = self.faceClassfier

                    # Clear temp file
                    f.seek(0, 0)
                    f.truncate()

            # Object recognition
            if self.classifier:
                faceRects = self.classifier.detectMultiScale(
                    grey, scaleFactor=1.1, minNeighbors=3, minSize=(150, 150))

                if len(faceRects):
                    (x, y, w, h) = faceRects[0]
                    center_x = int(x + w / 2)
                    center_y = int(y + h / 2)

                    if self.classifier == self.breadClassfier:
                        if center_x > 570 and center_x < 700:
                            count += 1
                            if count >= 20:
                                self.ser.write('p'.encode())
                                sleep(2)
                                self.ser.write('g'.encode())
                                sleep(2)
                                self.classifier = self.faceClassfier
                        else:
                            count = 0

                    # Send serial data
                    coordinate = 'c' + str(center_x) + \
                        ',' + str(center_y) + 'q'
                    self.ser.write(coordinate.encode())
                    # print('Send:', coordinate)

                    # Receive serial data
                    # res = self.ser.readline()
                    # print('Receive:', res.decode())

                    cv2.putText(frame, '(%d,%d)' % (center_x, center_y),
                                (10, 30), self.font, 1, (255, 0, 255), 3)

                    cv2.rectangle(frame, (x - 10, y - 10),
                                  (x + w + 10, y + h + 10), self.color, 2)

                    cv2.putText(frame, 'Size: %d%%' % int(
                        100 * h / frame.shape[0]), (x + 5, y + 30), self.font, 1, (255, 0, 255), 3)

            # Show image
            cv2.imshow(self.window_name, frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def switchClassfier(self, classifier):
        if classifier == 'face':
            self.classifier = self.faceClassfier
        elif classifier == 'bread':
            self.classifier = self.breadClassfier


if __name__ == '__main__':
    # 0 for original camera, 1 for webcam
    detector = ObjectRecognizer(
        'ObjectRecognition', 0, '/dev/cu.usbmodem14341')
    detector.catchUsbVideo()
