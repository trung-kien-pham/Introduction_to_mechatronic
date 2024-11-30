// #include <Arduino.h>
// #include <Keypad.h>

// const String openCode = "8386";
// const String addFaceCode = "1314";
// String enteredCode = "";
 
// const byte rows = 4;
// const byte columns = 3;
 
// int holdDelay = 500;
// int n = 3; 
// int state = 0;
// char key = 0;
// char lastKey = 0;
 
// char keys[rows][columns] =
// {
//   {'1', '2', '3'},
//   {'4', '5', '6'},
//   {'7', '8', '9'},
//   {'*', '0', '#'},
// };
 
// byte rowPins[rows] = {2, 3, 4, 5};
// byte columnPins[columns] = {6, 7, 8};
 
// Keypad keypad = Keypad(makeKeymap(keys), rowPins, columnPins, rows, columns);
// void setup() {
//   Serial.begin(9600);
 
// }
// void loop() {  
//   char tempKey = keypad.getKey();
  
//   if (tempKey) {  // If a key is pressed
//     // Serial.print(tempKey);
//     if (tempKey != lastKey) {  // New key press detected
//       key = tempKey;
//       state = 0;  // Reset state for a new key press
//       lastKey = key;
//     }
    
//     if (keypad.isPressed(key)) {  // Check if the key is still being held
//       state++;
//       state = constrain(state, 1, n - 1);
//       delay(holdDelay);
//     }
//   }

//   if (tempKey == NO_KEY && lastKey != 0) {  // Key released
//     if (key == '#') {
//       if (enteredCode == openCode) {
//         // Serial.println("Correct code! Opening door.");
//         Serial.println("open");
//         delay(5000);
//         Serial.println("close");
//         delay(5000);
//       } 
//       else if (enteredCode == addFaceCode) {
//         // Serial.println("Correct code! Adding face.");
//         Serial.println("add_face");
//       }
//       enteredCode = "";
//     } else {
//       enteredCode += key;  // Append the key to the entered code
//     }    
//     // Reset key tracking variables
//     key = 0;
//     lastKey = 0;
//     state = 0;
//   }
//   // Serial.print(enteredCode);
//   delay(100);
// }