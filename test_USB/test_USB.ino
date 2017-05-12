int compteur = 0;

void setup(){
  Serial.begin(9600);
}

 
void loop(){
  Serial.print("Message numero ");
  Serial.println(compteur);
  Serial.println("Bonjour, la Framboise, ici l'Arduino!");
  compteur++;
  delay(3000);
}
