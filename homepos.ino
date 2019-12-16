#define Motor1A 1
#define Motor1B 2
#define Enable 0
#define Interrupter 4

void setup() {
  // put your setup code here, to run once:
  pinMode (Motor1A, OUTPUT);
  pinMode (Motor1B, OUTPUT);
  pinMode (Enable, OUTPUT);
  pinMode (Interrupter, INPUT);

  Serial.begin(9600);

  attachInterrupt(4, homePos, LOW);
  digitalWrite(Enable, HIGH);
  digitalWrite(Motor1A, LOW);
  digitalWrite(Motor1B, HIGH);

}

void loop() {
  // put your main code here, to run repeatedly:

}

void homePos() {
  digitalWrite(Motor1A, LOW);
  digitalWrite(Motor1B, LOW);
  digitalWrite(Enable, LOW);
}

