# Automatic Door Based on Deeplearning and Ultrasonic

### Repo Collaborators

**Trung Kien Pham**, **Quy Dung Nguyen**, **Dinh Vinh Nguyen**, **Tien Manh Pham** and **Huy Anh Nguyen**.

# Status

**Ongoing**

## Directory Tree

```
.
├── face_recognition/
│   ├── knew_faces/
│   │   └── face_images
│   ├── recognition
│   │   ├── Add_face.py
│   │   └── Face_recognition.py
│   ├── check
│   │   ├── check_camera.py
│   │   └── check_serial_communication.py
│   └── main.py
├── src/
│   ├── check
│   │   ├── check_keypad.cpp
│   │   ├── check_servo.cpp
│   │   └── check_serial_communication.cpp
│   └── main.cpp
├── requirements.txt
└── README.md
```

## Dirdirectory Description

- **face_recognition/**: Face recognition and adding a face upon receiving a signal from Arduino.
- **src/**: Controlling hardware via Arduino.
- **requirements.txt**: requirements python packages.

# Description

## Feature
- A keypad for entering the passcode.
- Integration of a sensor to detect people in front of the door.
- Real-time face recognition using a camera.
- Adding faces through the camera.
- Opening the door via Arduino and a servo motor.

## Hardware
- Ardurino UNO R3
- Ultrasonic HC-SR04
- Servo MG996R
- Keypad 3x4

# Usage-CLI
- Clone the project.

```bash
git clone https://github.com/trung-kien-pham/Introduction_to_mechatronic.git
```

- Install requirement packages.

```bash
pip install requirements.txt
```

- Upload the code to Arduino. 

```bash
pio run --target upload
```

- Run Python to recognize the face when receiving a signal from Arduino.

```bash
python main.py
```
Note: <br>If using an external camera, the user needs to modify line 17 in the `main.py` file.