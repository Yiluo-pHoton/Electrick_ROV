
int p1 = A0;
int p2 = A1;
int p3 = A2;
int p4 = A3;
int p5 = A4;
int p6 = A5;
int p7 = A6;
int p8 = A7;


int pin11  = 2;
int pin12  = 3;
int pin21  = 4;
int pin22  = 5;
int pin31  = 6;
int pin32  = 7;
int pin41  = 8;
int pin42  = 9;

int outPin[ ] = {pin11, pin12, pin21, pin22, pin31, pin32, pin41, pin42};
int sizeOut = 8;
int inPin[ ]  = {p1, p2, p3, p4, p5, p6, p7, p8};
int sizeIn  = 8;

int frames = 10;

void setup() {
  // initialize all outPins
  for (int i = 0; i < sizeOut; i = i + 1) {
    pinMode(outPin[i], OUTPUT);
  }
  Serial.begin(9600);

}

void loop() {

  float vin = 5;
  for (int i = 0; i < sizeOut; i = i + 2) {
    Serial.println("Set voltage pair ...");
    analogWrite(outPin[i], vin / 5.0 * 255);
    analogWrite(outPin[i + 1], 0);

    // switch off the other 4 electro
    pinMode(outPin[(i + 2) % sizeOut], INPUT);
    pinMode(outPin[(i + 3) % sizeOut], INPUT);
    pinMode(outPin[(i + 4) % sizeOut], INPUT);
    pinMode(outPin[(i + 5) % sizeOut], INPUT);
    pinMode(outPin[(i + 6) % sizeOut], INPUT);
    pinMode(outPin[(i + 7) % sizeOut], INPUT);
    //INPUT has 100Mohm impedance

    // stablizing
    delay(100);

    // read
    Serial.println("Read electrodes ...");
    for (int k = 0; k < frames; k = k + 1) {
      float v1 = analogRead(inPin[i]) * 5.0 / 1023;
      float v2 = analogRead(inPin[i + 1]) * 5.0 / 1023;
      float v3 = analogRead(inPin[(i + 2) % sizeOut]) * 5.0 / 1023;
      float v4 = analogRead(inPin[(i + 3) % sizeOut]) * 5.0 / 1023;
      float v5 = analogRead(inPin[(i + 4) % sizeOut]) * 5.0 / 1023;
      float v6 = analogRead(inPin[(i + 5) % sizeOut]) * 5.0 / 1023;

      // print
      int precise = 4;
      Serial.print("V"); Serial.print(i); Serial.print(" = ");
      Serial.print(v1, precise); //Serial.print("Volts");
      Serial.print(" | ");
      Serial.print("V"); Serial.print(i + 1); Serial.print(" = ");
      Serial.print(v2, precise); //Serial.print("Volts");
      Serial.print(" | ");
      Serial.print("V"); Serial.print((i + 2) % sizeOut); Serial.print(" = ");
      Serial.print(v3, precise); //Serial.print("Volts");
      Serial.print(" | ");
      Serial.print("V"); Serial.print((i + 3) % sizeOut); Serial.print(" = ");
      Serial.print(v4, precise); //Serial.print("Volts");
      Serial.print(" | ");
      Serial.print("V"); Serial.print((i + 4) % sizeOut); Serial.print(" = ");
      Serial.print(v5, precise); //Serial.print("Volts");
      Serial.print(" | ");
      Serial.print("V"); Serial.print((i + 5) % sizeOut); Serial.print(" = ");
      Serial.println(v6, precise); //Serial.println("Volts");

      // 200Hz sampling rate
      delay(50);
    }

    pinMode(outPin[(i + 2) % sizeOut], OUTPUT);
    pinMode(outPin[(i + 3) % sizeOut], OUTPUT);
    pinMode(outPin[(i + 4) % sizeOut], OUTPUT);
    pinMode(outPin[(i + 5) % sizeOut], OUTPUT);
    pinMode(outPin[(i + 6) % sizeOut], OUTPUT);
    pinMode(outPin[(i + 7) % sizeOut], OUTPUT);

    // wait 1 sec
    delay(1000);

  }



}
