/******************************************************************************************
 * L'Arduino attend la requête du Rasperry Pi.  Lorsqu'il reçoit cette requête, il envoie en
 * retour le signal mesuré à la pin A0.
 ******************************************************************************************/
#define LED1 2
#define LED2 3
#define LED3 4


int message = 0;


void setup()
{ 
  Serial.begin(9600);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
}

void loop()
{
  if (Serial.available())  {
    message = Serial.read()-'0';  // on soustrait le caractère 0, qui vaut 48 en ASCII

    
      switch (message) {
    case 1:
      digitalWrite(LED1, HIGH);
      Serial.println("allumer led 1");
      break;
    case 2:
      digitalWrite(LED2, HIGH);
      Serial.println("allumer led 2");
      break;
    case 3:
      digitalWrite(LED3, HIGH);
      Serial.println("allumer led 3");
      break;
    case 4:
      digitalWrite(LED1, LOW);
      Serial.println("eteindre led 1");
      break;
    case 5:
      digitalWrite(LED2, LOW);
      Serial.println("eteindre led 2");
      break;
    case 6:
      digitalWrite(LED3, LOW);
      Serial.println("eteindre led 3");
      break;
      
    }
  }
}
