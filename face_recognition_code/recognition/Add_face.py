import os
import cv2
import uuid
import time
from mtcnn import MTCNN

class AddFace:

    def __init__(self, face_folder, frame):
        self.face_folder = face_folder
        os.makedirs(self.face_folder, exist_ok=True)
        self.frame = frame

    def add_face(self):
        detector = MTCNN()

        # Open the camera and capture an image
        # print("Opening camera...")
        # cap = cv2.VideoCapture(0)
        # time.sleep(1)
        # print("Capturing image from frontal angle...")
        # time.sleep(3)
        # ret, frame = cap.read()
        # cap.release()

        faces = detector.detect_faces(self.frame)
        if faces:
            print("Face(s) detected. Processing the face(s)...")
            
            # Find the face with the largest bounding box
            largest_face = max(faces, key=lambda face: face['box'][2] * face['box'][3])
            x, y, w, h = largest_face['box']
            detected_face = self.frame[y:y+h, x:x+w]

            # Save the detected largest face to the specified folder
            face_img_path = f"{self.face_folder}/{uuid.uuid4()}.jpg"
            cv2.imwrite(face_img_path, detected_face)
            print(f"Face saved: {face_img_path}")
        else:
            print("No face detected in the captured image.")

if __name__ == "__main__":
    add_face_obj = AddFace()
    add_face_obj.add_face()
