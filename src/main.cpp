#include <Arduino.h>
#include <Keypad.h>
#include <Servo.h>

Servo servo1;
Servo servo2;

const String openCode = "8386";
const String addFaceCode = "1314";
String enteredCode = "";

const byte ROWS = 4;
const byte COLS = 3;

int holdDelay = 500;
int n = 3;
int state = 0;
char key = 0;
char lastKey = 0;

char keys[ROWS][COLS] = {
  {'1', '2', '3'},
  {'4', '5', '6'},
  {'7', '8', '9'},
  {'*', '0', '#'}
};

byte rowPins[ROWS] = {2, 3, 4, 5};
byte colPins[COLS] = {6, 7, 8};

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

const int trigPin = 11;
const int echoPin = 12;

bool faceRecognitionInProgress = false;

void setup() {
  Serial.begin(9600);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  servo1.attach(9);
  servo2.attach(10);
  servo1.write(30);
  servo2.write(30);
}

long readUltrasonicDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);
  long distance = duration * 0.034 / 2;
  return distance;
}

void openDoor() {
  servo1.write(120);
  servo2.write(120);
}

void closeDoor() {
  servo1.write(30);
  servo2.write(30);
}

void loop() {
  if (!faceRecognitionInProgress) {
    long distance = readUltrasonicDistance();

    if (distance > 0 && distance < 5) {
      faceRecognitionInProgress = true;
      Serial.println("recognize_face");
    }
  }

  char tempKey = keypad.getKey();
  
  if (tempKey) {
    if (tempKey != lastKey) {
      key = tempKey;
      state = 0;
      lastKey = key;
    }
    
    if (keypad.isPressed(key)) {
      state++;
      state = constrain(state, 1, n - 1);
      delay(holdDelay);
    }
  }

  if (tempKey == NO_KEY && lastKey != 0) {
    if (key == '#') {
      if (enteredCode == openCode) {
        openDoor();
        delay(5000);
        closeDoor();
        delay(5000);
      } 
      else if (enteredCode == addFaceCode) {
        Serial.println("add_face");
      }
      enteredCode = "";
    } else {
      enteredCode += key;
    }
    
    key = 0;
    lastKey = 0;
    state = 0;
  }

  if (Serial.available() > 0) {

    String command = Serial.readString();
    if (command == "open\n") {
      openDoor();
      delay(5000);
      closeDoor();
      delay(5000);
      faceRecognitionInProgress = false;
    } else {
      faceRecognitionInProgress = false;
    }
  }

  delay(100);
}