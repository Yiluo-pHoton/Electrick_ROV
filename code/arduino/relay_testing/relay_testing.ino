#include <math.h>

const int node1PinOut = 2;
const int node0PinIn = A0;
const int node1PinIn = A1;
const int node2PinIn = A2;

int node1Out = 100;
int node1In = 0;
int node2In = 0;
  
void setup() {
  Serial.begin(9600);
}

void loop() {
  digitalWrite(node1PinOut, HIGH);
  
  int node2In = analogRead(node2PinIn);
  int node1In = analogRead(node1PinIn);
  int node0In = analogRead(node0PinIn);
  float node2InVoltage = node2In * (3.3 / 1023.0);
  float node1InVoltage = node1In * (3.3 / 1023.0);
  float node0InVoltage = node0In * (3.3 / 1023.0);
  Serial.println("A0: " + (String)node0InVoltage + "   A1: " + (String)node1InVoltage + "   A2: " + (String)node2InVoltage);
}
