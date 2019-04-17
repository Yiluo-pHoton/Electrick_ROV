void setup() {
  const int lowestPin = 2;
  const int highestPin = 10;
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int thisPin = lowestPin; thisPin < highestPin; thisPin++) {
    pinMode(thisPin, OUTPUT);
  }
}
