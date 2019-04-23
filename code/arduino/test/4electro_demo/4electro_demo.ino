
int p1 = A0;
int p2 = A1;
int p3 = A2;
int p4 = A3;


int pin11  = 9; //pwm pin
int pin12  = 10;
int pin21  = 5;
int pin22  = 6; //as ground pin


void setup() {
  // put your setup code here, to run once:
  pinMode(pin11, OUTPUT);
  pinMode(pin12, OUTPUT);
  pinMode(pin21, OUTPUT);
  pinMode(pin22, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  float vin = 5;
  analogWrite(pin11, vin/5*255);
  analogWrite(pin12, 0);
//  pinMode(pin21, INPUT_PULLUP);
//  pinMode(pin22, INPUT_PULLUP);
  pinMode(pin21, INPUT);
  pinMode(pin22, INPUT);
  // stablizing
  delay(10);
  
  float v1_raw = analogRead(p1);
  float v2_raw = analogRead(p2);

  float v1 = v1_raw*5/1023;
  float v2 = v2_raw*5/1023;
  
  Serial.print("V1 potential: ");
  Serial.print(v1,3); 
  Serial.print("V | V2 potential: ");
  Serial.print(v2,3);
  Serial.println("V ");
  
  delay(500);
  
}
