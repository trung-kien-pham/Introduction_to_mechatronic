import cv2
import screeninfo

screen = screeninfo.get_monitors()[0]
screen_width = screen.width
screen_height = screen.height

cap = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Không thể mở camera")

video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, screen_width)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, screen_height)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Không thể nhận khung hình (frame). Kết thúc.")
        break
    
    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()