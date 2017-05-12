const int CW_CCW = 6;
const int INH = 2;

//conecte to clock (port 5 de l'arduino)
// Ground carte connecté au ground arduino
// Ground carte et 24V carte coneecté a des piles

void setup() {
  // put your setup code here, to run once:
  pinMode(CW_CCW, OUTPUT);
  pinMode(INH, OUTPUT);
  digitalWrite(INH, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
 /* 
  for(int i=0; i<48; i++)
  {
    digitalWrite(INH, HIGH);
    delay(200);
    digitalWrite(INH, LOW);
    delay(10);
  }
  digitalWrite(CW_CCW, LOW);
 
  for(int i=0; i<48; i++)
  {
    digitalWrite(INH, HIGH);
    delay(200);
    digitalWrite(INH, LOW);
    delay(10);
  }
  digitalWrite(CW_CCW, HIGH);
  
   digitalWrite(INH, HIGH);
   delay(200);
   digitalWrite(INH, LOW);
   delay(200);*/
   tourner();
   delay(10 );

}

void tourner(){
  digitalWrite(INH, LOW);
  delay(20);
  digitalWrite(INH, HIGH);
  }

