#include "max6675.h" // max6675.h file is part of the library that you should download from Robojax.com



int Temp_1_SO = 2;// SO = Serial Out
int Temp_1_CS = 3;// CS = chip select CS pin
int Temp_1_SCK = 4;// SCK = Serial Clock pin

int Temp_2_SO = 5;// SO = Serial Out
int Temp_2_CS = 6;// CS = chip select CS pin
int Temp_2_SCK = 7;// SCK = Serial Clock pin

int Temp_3_SO = 8;
int Temp_3_CS = 9;
int Temp_3_SCK = 10;

int Temp_4_SO = 11;
int Temp_4_CS = 12;
int Temp_4_SCK = 13;

char c;
MAX6675 Temp_3(Temp_3_SCK, Temp_3_CS, Temp_3_SO);// create instance object of MAX6675
MAX6675 Temp_1(Temp_1_SCK, Temp_1_CS, Temp_1_SO);
MAX6675 Temp_2(Temp_2_SCK, Temp_2_CS, Temp_2_SO);
MAX6675 Temp_4(Temp_4_SCK, Temp_4_CS, Temp_4_SO);

void setup() {       
  Serial.begin(9600);// initialize serial monitor with 9600 baud
}

void loop() {
  // testing loop to interact with the serial monitor 
  if(Serial.available()){
    c = Serial.read();
  }
  if(c == '1'){
    Serial.print("TEST");
  }
  // basic readout that print the current temp
  // Robojax.com MAX6675 Temperature reading on Serial monitor
   Serial.print(Temp_1.readCelsius());
   Serial.print(",");

   Serial.print(Temp_2.readCelsius());
   Serial.print(",");
   
   Serial.print(Temp_3.readCelsius());
   Serial.print(",");
   
   Serial.println(Temp_4.readCelsius());
   
   delay(500);
}

