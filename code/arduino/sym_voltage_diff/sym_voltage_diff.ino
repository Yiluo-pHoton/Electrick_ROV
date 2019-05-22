// This version is easier for python to read the voltages at each frame
// For each frame (1-pair as source, 3-pair for measuring), the program takes sampleNum(40) mesurements.
// All results will be printed on one line. There will be (8*40 = 320) data points.
// Compared with the old version, where the input voltage running around (i.e. the voltage on the right side of the current output pair is always the first on the printing list),
// this version fixes the output of each point.
// The measurement for the next frame will be printed on the next line and so on.
// created by David Wang

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

// number of samples needed for each frame
int sampleNum = 40;

// precision of voltage reading
int digit = 6;

// input voltage in V
int vin = 5;

// stub voltage
int vGND = 0;

void setup() {
  // initialize all outPins
  for (int i = 0; i < sizeOut; i = i + 1) {
    pinMode(outPin[i], OUTPUT);
  }
  Serial.begin(115200);

}

void loop() {

  for (int i = 0; i < 1; i = i + 2) {
    analogWrite(outPin[i], vin / 5.0 * 255);
    analogWrite(outPin[i + 1], 0);
    // switch off the other 6 electros
    for (int j = 2; j < sizeOut; j = j + 1) {
      pinMode(outPin[(i + j) % sizeOut], INPUT);
    }
    // wait 1 ms to stablize
    delayMicroseconds(100);

    // read
    for (int k = 0; k < sampleNum; k = k + 1) {
      int p = 2;
      float v3 = analogRead(inPin[p]);
      float v5 = analogRead(inPin[p + 2]);
      float v7 = analogRead(inPin[p + 4]);
      float v4 = analogRead(inPin[p + 3]);
      float v6 = analogRead(inPin[p + 5]);
      float v8 = analogRead(inPin[p + 7]);
      Serial.print((v3 - v4) * 5.0 / 1023, digit); Serial.print(" ");
      Serial.print((v5 - v6) * 5.0 / 1023, digit); Serial.print(" ");
      Serial.print((v7 - v8) * 5.0 / 1023, digit); Serial.print(" ");
      //delay(2000);
    }

    // switch to the next frame
    for (int j = 2; j < sizeOut; j = j + 1) {
      pinMode(outPin[(i + j) % sizeOut], OUTPUT);
    }

  }
  Serial.println();
}
