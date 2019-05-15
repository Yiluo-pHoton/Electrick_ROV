int pin = A10;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(pin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(analogRead(pin) * 5.0 / 1023, 4);
}
