#include <avr/interrupt.h>
#include <stdlib.h>

char sinetable [32];

int V = 2;
int GND = 3;
volatile int wave0 = 0;

#define maxWaveform 4
#define maxSamplesNum 120
static int waveformsTable[maxWaveform][maxSamplesNum] = {
  // Sin wave
  {
    0x7ff, 0x86a, 0x8d5, 0x93f, 0x9a9, 0xa11, 0xa78, 0xadd, 0xb40, 0xba1,
    0xbff, 0xc5a, 0xcb2, 0xd08, 0xd59, 0xda7, 0xdf1, 0xe36, 0xe77, 0xeb4,
    0xeec, 0xf1f, 0xf4d, 0xf77, 0xf9a, 0xfb9, 0xfd2, 0xfe5, 0xff3, 0xffc,
    0xfff, 0xffc, 0xff3, 0xfe5, 0xfd2, 0xfb9, 0xf9a, 0xf77, 0xf4d, 0xf1f,
    0xeec, 0xeb4, 0xe77, 0xe36, 0xdf1, 0xda7, 0xd59, 0xd08, 0xcb2, 0xc5a,
    0xbff, 0xba1, 0xb40, 0xadd, 0xa78, 0xa11, 0x9a9, 0x93f, 0x8d5, 0x86a,
    0x7ff, 0x794, 0x729, 0x6bf, 0x655, 0x5ed, 0x586, 0x521, 0x4be, 0x45d,
    0x3ff, 0x3a4, 0x34c, 0x2f6, 0x2a5, 0x257, 0x20d, 0x1c8, 0x187, 0x14a,
    0x112, 0xdf, 0xb1, 0x87, 0x64, 0x45, 0x2c, 0x19, 0xb, 0x2,
    0x0, 0x2, 0xb, 0x19, 0x2c, 0x45, 0x64, 0x87, 0xb1, 0xdf,
    0x112, 0x14a, 0x187, 0x1c8, 0x20d, 0x257, 0x2a5, 0x2f6, 0x34c, 0x3a4,
    0x3ff, 0x45d, 0x4be, 0x521, 0x586, 0x5ed, 0x655, 0x6bf, 0x729, 0x794
  }
};

void arraysetup(void) {
    sinetable[0] = 127; // Put 32 step 8 bit sine table into array.
    sinetable[1] = 152;
    sinetable[2] = 176;
    sinetable[3] = 198;
    sinetable[4] = 217;
    sinetable[5] = 233;
    sinetable[6] = 245;
    sinetable[7] = 252;
    sinetable[8] = 254;
    sinetable[9] = 252;
    sinetable[10] = 245;
    sinetable[11] = 233;
    sinetable[12] = 217;
    sinetable[13] = 198;
    sinetable[14] = 176;
    sinetable[15] = 152;
    sinetable[16] = 128;
    sinetable[17] = 103;
    sinetable[18] = 79;
    sinetable[19] = 57;
    sinetable[20] = 38;
    sinetable[21] = 22;
    sinetable[22] = 10;
    sinetable[23] = 3;
    sinetable[24] = 0;
    sinetable[25] = 3;
    sinetable[26] = 10;
    sinetable[27] = 22;
    sinetable[28] = 38;
    sinetable[29] = 57;
    sinetable[30] = 79;
    sinetable[31] = 103;
  }

  void setup() {
    pinMode(V, OUTPUT);
    pinMode(GND, INPUT);
    Serial.begin(9600);
  }

  void loop() {
//    for (int i = 0; i < 32; i = i++) {
//      analogWrite(V, waveformsTable[wave0][i]);
//      if (i == 31) {
//        i = 0;
//      }
//      delay(1000);
//      // delayMicroseconds(5000000);
//      Serial.println("hi hi ");
//    }
//
//    analogWrite(V, 255);
//    delay(5);
    analogWrite(V, 0);
    delay(5);

    //  for (int i = 0; i < 256; i = i++) {
    //  analogWrite(V, i);
    //  delay(1000);
    //  }
    //  for (int i = 255; i >= 0; i = i--) {
    //  analogWrite(V, i);
    //  delay(1000);
    //  }

  }
