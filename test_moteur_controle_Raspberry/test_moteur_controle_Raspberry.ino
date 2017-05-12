const int PWMA = 6;
const int DIRA = 7;
const int PWMB = 5;
const int DIRB = 4;

int message = 0;

void setup() {

  pinMode(DIRA, OUTPUT);
  pinMode(DIRB, OUTPUT);
  pinMode(PWMA, OUTPUT);
  pinMode(PWMB, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()){
    message = Serial.read()-'0';
    switch(message){
      case 1:
        avancer(1000);
        break;
      case 2:
        reculer(1000);
        break;
      case 3:
        tournerG(1000);
        break;
      case 4:
        tournerD(1000);
        break;
      case 5:
        avancer(2000);
        break;
      case 6:
        reculer(2000);
        break;
         
    }
    
   }
  
}

void avancer(int temp){
  digitalWrite(DIRA, HIGH);
  digitalWrite(DIRB, HIGH);
  digitalWrite(PWMA, HIGH);
  digitalWrite(PWMB, HIGH);
  delay(temp);
  digitalWrite(PWMA, LOW);
  digitalWrite(PWMB, LOW);
}

void reculer(int temp){
  digitalWrite(DIRA, LOW);
  digitalWrite(DIRB, LOW);
  digitalWrite(PWMA, HIGH);
  digitalWrite(PWMB, HIGH);
  delay(temp);
  digitalWrite(PWMA, LOW);
  digitalWrite(PWMB, LOW);
}

void tournerG(int temp){
  digitalWrite(DIRA, HIGH);
  digitalWrite(DIRB, LOW);
  digitalWrite(PWMA, HIGH);
  digitalWrite(PWMB, HIGH);
  delay(temp);
  digitalWrite(PWMA, LOW);
  digitalWrite(PWMB, LOW);
}

void tournerD(int temp){
  digitalWrite(DIRA, LOW);
  digitalWrite(DIRB, HIGH);
  digitalWrite(PWMA, HIGH);
  digitalWrite(PWMB, HIGH);
  delay(temp);
  digitalWrite(PWMA, LOW);
  digitalWrite(PWMB, LOW);
}
