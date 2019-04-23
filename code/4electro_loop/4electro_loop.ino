
int p1 = A0;
int p2 = A1;
int p3 = A2;
int p4 = A3;


int pin11  = 9;
int pin12  = 10;
int pin21  = 5;
int pin22  = 6;

int outPin[ ] = {pin11, pin12, pin21, pin22};
int sizeOut = 4;
int inPin[ ]  = {p1, p2, p3, p4};
int sizeIn  = 4;

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
  for (int i = 0; i <= sizeOut/2; i = i + 2) {
    Serial.println("Set voltage pair ...");
    analogWrite(outPin[i], vin / 5.0 * 255);
    analogWrite(outPin[i+1], 0);

    // switch off the other 2 electro
    pinMode(outPin[(i+2) % sizeOut], INPUT);
    pinMode(outPin[(i+3) % sizeOut], INPUT); 
    //INPUT has 100Mohm impedance
    
    // stablizing
    delay(100);

    // read
    Serial.println("Read electrodes ...");
    for (int k = 0; k < frames; k = k + 1) {
      float v1 = analogRead(inPin[i])*5.0/1023;
      float v2 = analogRead(inPin[i+1])*5.0/1023;

      // print
      Serial.print("V"); Serial.print(i+1); Serial.print(" = ");
      Serial.print(v1,4); Serial.print("Volts");
      Serial.print(" | ");
      Serial.print("V"); Serial.print(i+2); Serial.print(" = ");
      Serial.print(v2,4); Serial.println("Volts");

      // 200Hz sampling rate
      delay(50);
    }

    pinMode(outPin[(i+2) % sizeOut], OUTPUT);
    pinMode(outPin[(i+3) % sizeOut], OUTPUT);

    // wait 1 sec
    delay(1000);

  }



}
