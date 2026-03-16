int ledRojo = 8;
int ledVerde = 9;

String comando;

void setup(){

Serial.begin(9600);

pinMode(ledRojo,OUTPUT);
pinMode(ledVerde,OUTPUT);

}

void loop(){

if(Serial.available()){

comando = Serial.readStringUntil('\n');
comando.trim();

if(comando=="ROJO_ON"){
digitalWrite(ledRojo,HIGH);
}

if(comando=="ROJO_OFF"){
digitalWrite(ledRojo,LOW);
}

if(comando=="VERDE_ON"){
digitalWrite(ledVerde,HIGH);
}

if(comando=="VERDE_OFF"){
digitalWrite(ledVerde,LOW);
}

}

}
