#include <Wire.h>
#include <LIDARLite.h>

LIDARLite myLidarLite;


const int CW_CCW = 6;
const int INH = 2;
float angle = 0.0;
int message;

//connecte to clock (port 5 de l'arduino)
// Ground carte connecté au ground arduino
// Ground carte et 24V carte coneecté a des piles

void setup() {
  // communication
  Serial.begin(9600);
  // moteur pas a pas 
  pinMode(INH, OUTPUT);
  digitalWrite(INH, HIGH);
  // Lidar I2c
  myLidarLite.begin(0, true);
  myLidarLite.configure(1);
}

void loop()
{
  if (Serial.available())
  {
    message = Serial.read()-'0';
    if(message == 1)
    {
      delay(100);
      int a = 0;
      int nb_mesure = 100;
      //Serial.println(myLidarLite.distance());
      for(int i=0;i<nb_mesure;i++){
        a += myLidarLite.distance();
      }
      Serial.println(a/nb_mesure);
    }
    else if(message == 2)
    {
      
      angle = tourner(angle);
      Serial.println(angle);
    }
  }
}

float tourner(float angle)
{
  digitalWrite(INH, LOW);
  delay(10);
  digitalWrite(INH, HIGH);
  angle = angle + 7.5;
  return angle;
}

int get_distance(){
  return myLidarLite.distance();
}




