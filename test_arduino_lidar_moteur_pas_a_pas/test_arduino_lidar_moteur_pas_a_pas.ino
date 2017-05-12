// Moteur Pas a pas
const int CW_CCW = 6;
const int INH = 5;

//Lidar
#include <Wire.h>
#include <LIDARLite.h>

//serial
String message = "";

LIDARLite myLidarLite;


void setup()
{
  //moteur pas a pas
  pinMode(INH, OUTPUT);
   
  // capteur lidar
  myLidarLite.begin(0, true); // Set configuration to default and I2C to 400 kHz
  myLidarLite.configure(0); // Change this number to try out alternate configurations
  
  // communication serial
  Serial.begin(9600);
}
  

void loop()
{
  if (Serial.available())
  {
    message = Serial.read()-'0';
    if (message == "lidar_commande")
    {
       for(int i=0; i>=360; i+=7.5)
       {
          Serial.println("angle:");
          Serial.println((String)i);
          Serial.println("distance:");
          Serial.println(get_distance());
       }     
    }
    
  }
    
  

}

void tourner_p_a_p()
{
  digitalWrite(INH, HIGH);
  delay(10);
  digitalWrite(INH, LOW);
}
int get_distance()
{
  return myLidarLite.distance();
}
  
