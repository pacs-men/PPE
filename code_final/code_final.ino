#include <Wire.h>
#include <LIDARLite.h>

LIDARLite myLidarLite;


const int CW_CCW = 3;
const int INH = 2;
float angle_lidar = 0.0;
int message;
//controle de moteurs
const int DIRA = 7;
const int DIRB = 4;
const int PWMB = 5;
const int PWMA = 6;

//connecte to clock (port 5 de l'arduino)
// Ground carte connecté au ground arduino
// Ground carte et 24V carte coneecté a des piles

int posx = 0
int posy = 0

void setup() {
  // communication
  Serial.begin(9600);
  // moteur pas a pas 
  pinMode(INH, OUTPUT);
  digitalWrite(INH, HIGH);
  // Lidar I2c
  myLidarLite.begin(0, true);
  myLidarLite.configure(0);
  // moteurs
  pinMode(DIRA, OUTPUT);
  pinMode(DIRB, OUTPUT);
  pinMode(PWMA, OUTPUT);
  pinMode(PWMB, OUTPUT);

}

void loop()
{
  if (Serial.available())
  {
    message = Serial.read()-'0';
    if(message == 1)
    {
      Serial.println(get_distance());
    }
    else if(message == 2)
    {
      angle = tourner_lidar(angle_lidar);
      Serial.println(angle_lidar);
    }
    else if(message == 3)
    {
       avancer(1000)
    }
    else if(message == 4)
    {
       reculer(1000)
    }
    else if(message == 5)
    {
       tournerD(1000)
    }
    else if(message == 6)
    {
       tournerG(1000)
    }
    
    
  }
}

float tourner_lidar(float angle){
  digitalWrite(INH, LOW);
  delay(10);
  digitalWrite(INH, HIGH);
  angle = angle + 7.5;
  return angle;
}

int get_distance(){
  return myLidarLite.distance();
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

float remise_a_z_lidar(float angle){
  while angle 
}


