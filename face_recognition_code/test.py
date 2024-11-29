import cv2
import serial
import time
from recognition.Face_recognition import FaceRecognition
from recognition.Add_face import AddFace

arduino = serial.Serial('COM6', 9600)
time.sleep(2)

face_folder = 'face_recognition_code/knew_faces'

video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Can't open camera!")

while True:

    ret, frame = video_capture.read()
    
    cv2.imshow('Camera', frame)

    if arduino.in_waiting > 0:
        message = arduino.readline().decode('utf-8').strip()
        # message = "recognize_face"
        # print(message=="recognize_face")
        print(f"message: {message}")
        if message == "recognize_face":
            # arduino.write(b"open\n")
            print("True")
            time.sleep(2)
            ret, frame = video_capture.read()
            face_recognition = FaceRecognition(face_folder=face_folder, frame=frame)
            verify_image = face_recognition.face_recognition()

            if verify_image:
                arduino.write(b"open\n")
                print('Match face. Opening door...')
                time.sleep(2)
                pass
            else:
                arduino.write(b"recognition_complete\n")
                print('No match face')
                pass

        if message == "add_face":

            time.sleep(2)
            ret, frame = video_capture.read()
            add_face_obj = AddFace(face_folder=face_folder, frame=frame)
            add_face_obj.add_face()

            pass

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()