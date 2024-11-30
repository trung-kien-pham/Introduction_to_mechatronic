# Code Python
import serial
import time

# Kết nối Serial với Arduino
arduino = serial.Serial(port='COM6', baudrate=9600, timeout=1)  # Thay 'COM3' bằng cổng kết nối Arduino

def send_data(data):
    arduino.write(f"{data}\n".encode())  # Gửi dữ liệu đến Arduino
    time.sleep(0.05)

def receive_data():
    data = arduino.readline().decode().strip()  # Đọc dữ liệu từ Arduino
    return data if data else None

# Kiểm tra dữ liệu nhận được và phản hồi lại Arduino
while True:
    received = receive_data()
    if received:
        print(f"Received from Arduino: {received}")

        # Kiểm tra nếu nhận được ký tự "1"
        if received == "1":
            send_data("OK")
            print("Sent to Arduino: OK")
        else:
            send_data("NO")
            print("Sent to Arduino: NO")
    
    time.sleep(1)