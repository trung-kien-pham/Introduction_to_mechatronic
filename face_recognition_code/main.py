import serial
import time
from recognition.Face_recognition import FaceRecognition
from recognition.Add_face import AddFace

arduino = serial.Serial('COM6', 9600)
time.sleep(2)

face_folder = 'python_code/knew_face'

while True:

    if arduino.in_waiting > 0:
        message = arduino.readline().decode('utf-8').strip()
        # message = "recognize_face"
        # print(message=="recognize_face")
        print(f"message: {message}")
        if message == "recognize_face":
            # arduino.write(b"open\n")
            print("True")  
            face_recognition = FaceRecognition(face_folder)
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

            add_face_obj = AddFace(face_folder=face_folder)
            add_face_obj.add_face()

            pass