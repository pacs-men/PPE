//Arduino PWM Speed Control

int E1 = 6;
int M1 = 7;
int E2 = 5;
int M2 = 4;
void setup(){ 
  pinMode(M1, OUTPUT);
  pinMode(M2, OUTPUT); 
} 
void loop(){ 
  int value;

  digitalWrite(M1,HIGH);
  digitalWrite(M2, HIGH);
  analogWrite(E1, 100);
  //PWM Speed Control
  analogWrite(E2, 100);
  //PWM Speed Control
  delay(3000);
  
  digitalWrite(M1, LOW);
  digitalWrite(M2, LOW);
  analogWrite(E1, 100);
  //PWM Speed Control
  analogWrite(E2, 100);
  //PWM Speed Control
  delay(3000);
 
}

void avancer(int temp){
  digitalWrite(M1,HIGH);
  digitalWrite(M2, HIGH);
  analogWrite(E1, 100);
  //PWM Speed Control
  analogWrite(E2, 100);
  //PWM Speed Control
  delay(temp);
  analogWrite(E1, 0);
  analogWrite(E2, 0);
}

void reculer(int temp){
  digitalWrite(M1,LOW);
  digitalWrite(M2, LOW);
  analogWrite(E1, 100);
  //PWM Speed Control
  analogWrite(E2, 100);
  //PWM Speed Control
  delay(temp);
  analogWrite(E1, 0);
  analogWrite(E2, 0);
}

void tournerG(int temp){
  digitalWrite(M1,LOW);
  digitalWrite(M2, HIGH);
  analogWrite(E1, 100);
  //PWM Speed Control
  analogWrite(E2, 100);
  //PWM Speed Control
  delay(temp);
  analogWrite(E1, 0);
  analogWrite(E2, 0);
}

void tournerD(int temp){
  digitalWrite(M1,HIGH);
  digitalWrite(M2, LOW);
  analogWrite(E1, 100);
  //PWM Speed Control
  analogWrite(E2, 100);
  //PWM Speed Control
  delay(temp);
  analogWrite(E1, 0);
  analogWrite(E2, 0);
}
