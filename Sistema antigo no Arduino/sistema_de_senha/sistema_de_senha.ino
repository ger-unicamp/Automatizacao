#include <Wire.h>
#include "rgb_lcd.h"

#define TAM_VEC_SENHAS 2
#define ENCONTROU 1
#define NAO_ENCONTROU 0
#define MAX_CONTADOR 3
#define TEMPO 120 * 1000

rgb_lcd lcd;

int colorR = 228; //228,192,85
int colorG = 192;
int colorB = 85;

String senha_leo = "123456";
String senha_marcelo = "199419";

String senhas[TAM_VEC_SENHAS];

int contador_erros = 0;

void setup() 
{

    Serial.begin(9600);
    // set up the LCD's number of columns and rows:
    lcd.begin(16, 2);
    
    lcd.setRGB(colorR, colorG, colorB);
    
    delay(1000);

    senhas[0] = senha_leo;
    senhas[1] = senha_marcelo;
}

int testa_senha(String senha) { //varre o vetor de senhas checando se ela esta certa - Mudar par aaplicar criptografia
  int encontrou = 0, i;

  for(i = 0; i < TAM_VEC_SENHAS && !encontrou; i++) {
    if(senhas[i] == senha) {
      encontrou = 1;
    }
  }

  return encontrou;
}

void loop() 
{
  String string = "";
  char letra;
  int tempo_inicial;
  
  int tempo = TEMPO * (contador_erros/3 + 1);

  //tone(5, 440);
  
  if(contador_erros >= MAX_CONTADOR) { //se a pessoa errou determinadas vezes, bloqueia
    lcd.clear();
    lcd.print("Travamento de");
    lcd.setCursor(0,1);
    lcd.print("tempo ativado");
    delay(2000);

    lcd.clear();
    lcd.print("Tempo restante:");
    tempo_inicial = millis();
    
    while(millis() - tempo_inicial < tempo) {
      lcd.setCursor(0,0);
      lcd.print("Tempo restante:");
      lcd.setCursor(0,1);
      lcd.print((tempo - millis() + tempo_inicial)/1000);
      lcd.print("   ");
    }
    contador_erros = 0;
    
  }

  lcd.setCursor(0,0);
  lcd.print("Digite a senha");
  lcd.setRGB(228, 192, 85);//228,192,85
 // when characters arrive over the serial port...
  if (Serial.available()) 
  {
    // wait a bit for the entire message to arrive
    delay(100);
    // clear the screen
    lcd.clear();
    // read all the available characters
    while (Serial.available() > 0) 
    {
      letra = Serial.read();
     // display each character to the LCD
     lcd.write(letra);

     string += letra;
     
    }
    lcd.setCursor(0,1);



    
    if(testa_senha(string)) {      //se a pessoa acertou a senha
      colorR = 0;
      colorG = 0;
      colorB = 255;
      lcd.print("Senha correta!");
      contador_erros = 0;
      lcd.setRGB(colorR, colorG, colorB);
      delay(2000);
      lcd.clear();
     }
    else { //se a pessoa errou a senha
      colorR = 255;
      colorG = 0;
      colorB = 0; 
      lcd.print("Senha incorreta!"); 
      contador_erros++;     
      lcd.setRGB(colorR, colorG, colorB);
      delay(2000);
      lcd.clear();
    }
    
    

     
  }
}
