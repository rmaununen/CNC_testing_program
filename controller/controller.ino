String test;
const int dirPin = 4;
const int stepPin = 5;
const int stepsPerRevolution = 200;
const int stepWidth = 800; //between 300 and 4000

void setup()
{
  Serial.begin(28800);
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
}

void loop() {
if (Serial.available() > 0) {
  test = Serial.readStringUntil('\n');
  
  if (test == "1") {
    digitalWrite(dirPin, HIGH); // CW
    for(int x = 0; x < 10*stepsPerRevolution; x++)
    {
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(stepWidth);
      digitalWrite(stepPin, LOW);
      delayMicroseconds(stepWidth);
      if (Serial.available() > 0) {
        test = Serial.readStringUntil('\n'); //READING TAKES SOME TIME AND PWM IS NOT THAT NICE BECAUSE OF THAT
        if (test == "0" || test == "2") {
          break;
        }
      }
    }
  }
  if (test == "2") {
    digitalWrite(dirPin, LOW); // CCW
    for(int x = 0; x < 100*stepsPerRevolution; x++)
    {
      digitalWrite(stepPin, HIGH);
      delayMicroseconds(stepWidth);
      digitalWrite(stepPin, LOW);
      delayMicroseconds(stepWidth);
      if (Serial.available() > 0) {
        test = Serial.readStringUntil('\n');//READING TAKES SOME TIME AND PWM IS NOT THAT NICE BECAUSE OF THAT
        if (test == "0" || test == "1") {
          break;
        }
        }
    }
  }
  if (test == "0") {
    digitalWrite(dirPin, LOW); // Stop
    digitalWrite(stepPin, LOW);
  }
}
delay(3);
}
