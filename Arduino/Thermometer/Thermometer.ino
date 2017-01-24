int sensorPin = A5; // select the input pin for the potentiometer
 
void setup() {
 Serial.begin(9600);
}
 
void loop() {
 int readVal = analogRead(sensorPin);
 
 Serial.println(readVal);  // display tempature
 
 delay(1000);
}

