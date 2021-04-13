String test;
const int dirPin = 4;
const int stepPin = 5;
const int stepsPerRevolution = 200;
const int stepWidth = 600; //between 300 and 4000

void setup()
{
  Serial.begin(9600);
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
}

void loop() {
if (Serial.available() > 0) {
  test = Serial.readStringUntil('\n');

  if (test == "1") {
    digitalWrite(dirPin, HIGH); // CW
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(stepWidth);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(stepWidth);
  }
  if (test == "2") {
    digitalWrite(dirPin, LOW); // CCW
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(stepWidth);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(stepWidth);
  }
  if (test == "0") {
    digitalWrite(dirPin, LOW); // Stop
    digitalWrite(stepPin, LOW);
  }
}
delay(3);
}
