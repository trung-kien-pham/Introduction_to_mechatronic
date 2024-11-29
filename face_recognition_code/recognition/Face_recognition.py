import cv2
import os
import time
from deepface import DeepFace

class FaceRecognition:

    def __init__(self, face_folder, frame):
        self.face_folder = face_folder
        self.frame = frame

    def face_recognition(self):
        # print("Opening camera...")
        # video_capture = cv2.VideoCapture(0)
        
        # time.sleep(1)
        
        # ret, person_image = video_capture.read()
        # video_capture.release()

        # if not ret:
        #     print("Failed to capture image from webcam.")
        #     return False

        match_found = False

        for image_name in os.listdir(self.face_folder):
            image_path = os.path.join(self.face_folder, image_name)
            known_image = cv2.imread(image_path)
            result = DeepFace.verify(self.frame, known_image, threshold=0.3, model_name="Facenet512", enforce_detection=False)

            if result["verified"]:
                match_found = True
                break

        return match_found


if __name__ == "__main__":
    face_recognition = FaceRecognition('python_code/knew_face')
    match = face_recognition.face_recognition()
    # print(match)