String test;
const int dirPin1 = 4;
const int stepPin1 = 5;//Pwm pins are 3, 5, 6, 9, 10, 11
const int dirPin2 = 7;
const int stepPin2 = 6;
const int dirPin3 = 8;
const int stepPin3 = 9;
const int dirPin4 = 10;
const int stepPin4 = 11;
const int stepsPerRevolution = 200;
const int stepWidthmax = 4000;
const int stepWidthmin = 300;
int stepWidth = (stepWidthmax+stepWidthmin)/2; //between 300 and 4000

void setup()
{
  Serial.begin(28800);
  pinMode(stepPin1, OUTPUT);
  pinMode(dirPin1, OUTPUT);
  pinMode(stepPin2, OUTPUT);
  pinMode(dirPin2, OUTPUT);
  pinMode(stepPin3, OUTPUT);
  pinMode(dirPin3, OUTPUT);
  pinMode(stepPin4, OUTPUT);
  pinMode(dirPin4, OUTPUT);
}

void loop() {
if (Serial.available() > 0) {
  test = Serial.readStringUntil('\n');
  
  if (test == "1") {
    digitalWrite(dirPin1, HIGH); // Right only
    for(int x = 0; x < 100*stepsPerRevolution; x++)
    {
      digitalWrite(stepPin1, HIGH);
      delayMicroseconds(stepWidth);
      digitalWrite(stepPin1, LOW);
      delayMicroseconds(stepWidth);
      if (Serial.available() > 0) {
        test = Serial.readStringUntil('\n'); //READING TAKES SOME TIME AND PWM IS NOT THAT NICE BECAUSE OF THAT
        if (test != "1") {
          break;
        }
      }
    }
  }
  if (test == "2") {
    digitalWrite(dirPin1, LOW); // Left only
    for(int x = 0; x < 100*stepsPerRevolution; x++)
    {
      digitalWrite(stepPin1, HIGH);
      delayMicroseconds(stepWidth);
      digitalWrite(stepPin1, LOW);
      delayMicroseconds(stepWidth);
      if (Serial.available() > 0) {
        test = Serial.readStringUntil('\n');
        if (test != "2") {
          break;
        }
        }
    }
  }
  if (test == "3") {
    digitalWrite(dirPin2, HIGH); // up only
    digitalWrite(dirPin3, LOW);
    for(int x = 0; x < 100*stepsPerRevolution; x++)
    {
      digitalWrite(stepPin2, HIGH);
      digitalWrite(stepPin3, HIGH);
      delayMicroseconds(stepWidth);
      digitalWrite(stepPin2, LOW);
      digitalWrite(stepPin3, LOW);
      delayMicroseconds(stepWidth);
      if (Serial.available() > 0) {
        test = Serial.readStringUntil('\n');
        if (test != "3") {
          break;
        }
        }
    }
  }
  if (test == "4") {
    digitalWrite(dirPin2, LOW); // down only
    digitalWrite(dirPin3, HIGH);
    for(int x = 0; x < 100*stepsPerRevolution; x++)
    {
      digitalWrite(stepPin2, HIGH);
      digitalWrite(stepPin3, HIGH);
      delayMicroseconds(stepWidth);
      digitalWrite(stepPin2, LOW);
      digitalWrite(stepPin3, LOW);
      delayMicroseconds(stepWidth);
      if (Serial.available() > 0) {
        test = Serial.readStringUntil('\n');
        if (test != "4") {
          break;
        }
        }
    }
  }
  if (test == "5") {
    digitalWrite(dirPin2, HIGH); // Right and up
    digitalWrite(dirPin3, LOW);
    digitalWrite(dirPin1, HIGH);
    for(int x = 0; x < 100*stepsPerRevolution; x++)
    {
      digitalWrite(stepPin1, HIGH);
      digitalWrite(stepPin2, HIGH);
      digitalWrite(stepPin3, HIGH);
      delayMicroseconds(stepWidth);
      digitalWrite(stepPin1, LOW);
      digitalWrite(stepPin2, LOW);
      digitalWrite(stepPin3, LOW);
      delayMicroseconds(stepWidth);
      if (Serial.available() > 0) {
        test = Serial.readStringUntil('\n');
        if (test != "5") {
          break;
        }
        }
    }
  }
  if (test == "6") {
    digitalWrite(dirPin2, LOW); // Right and down
    digitalWrite(dirPin3, HIGH);
    digitalWrite(dirPin1, HIGH);
    for(int x = 0; x < 100*stepsPerRevolution; x++)
    {
      digitalWrite(stepPin1, HIGH);
      digitalWrite(stepPin2, HIGH);
      digitalWrite(stepPin3, HIGH);
      delayMicroseconds(stepWidth);
      digitalWrite(stepPin1, LOW);
      digitalWrite(stepPin2, LOW);
      digitalWrite(stepPin3, LOW);
      delayMicroseconds(stepWidth);
      if (Serial.available() > 0) {
        test = Serial.readStringUntil('\n');
        if (test != "6") {
          break;
        }
        }
    }
  }
  if (test == "7") {
    digitalWrite(dirPin2, HIGH); // Left and up
    digitalWrite(dirPin3, LOW);
    digitalWrite(dirPin1, LOW);
    for(int x = 0; x < 100*stepsPerRevolution; x++)
    {
      digitalWrite(stepPin1, HIGH);
      digitalWrite(stepPin2, HIGH);
      digitalWrite(stepPin3, HIGH);
      delayMicroseconds(stepWidth);
      digitalWrite(stepPin1, LOW);
      digitalWrite(stepPin2, LOW);
      digitalWrite(stepPin3, LOW);
      delayMicroseconds(stepWidth);
      if (Serial.available() > 0) {
        test = Serial.readStringUntil('\n');
        if (test != "7") {
          break;
        }
        }
    }
  }
  if (test == "8") {
    digitalWrite(dirPin2, LOW); // Left and down
    digitalWrite(dirPin3, HIGH);
    digitalWrite(dirPin1, LOW);
    for(int x = 0; x < 100*stepsPerRevolution; x++)
    {
      digitalWrite(stepPin1, HIGH);
      digitalWrite(stepPin2, HIGH);
      digitalWrite(stepPin3, HIGH);
      delayMicroseconds(stepWidth);
      digitalWrite(stepPin1, LOW);
      digitalWrite(stepPin2, LOW);
      digitalWrite(stepPin3, LOW);
      delayMicroseconds(stepWidth);
      if (Serial.available() > 0) {
        test = Serial.readStringUntil('\n');
        if (test != "8") {
          break;
        }
        }
    }
  }
  if (test == "12") {
    digitalWrite(dirPin4, HIGH); // Contact up
    for(int x = 0; x < 1*stepsPerRevolution; x++)
    {
      digitalWrite(stepPin4, HIGH);
      delayMicroseconds(stepWidth);
      digitalWrite(stepPin4, LOW);
      delayMicroseconds(stepWidth);
    }
  }
  if (test == "13") {
    digitalWrite(dirPin4, LOW); // Contact down
    for(int x = 0; x < 1*stepsPerRevolution; x++)
    {
      digitalWrite(stepPin4, HIGH);
      delayMicroseconds(stepWidth);
      digitalWrite(stepPin4, LOW);
      delayMicroseconds(stepWidth);
    }
  }
  if (test == "10") {
    change_step_width();
  }
}
delay(3);
}
void change_step_width() {
  while(test!="out") {
    if (Serial.available() > 0) {
      test = Serial.readStringUntil('\n');
      if (test!="11"){
        stepWidth = test.toInt();
      }
      else{
        test = "out";
      }
    }
  }
}
