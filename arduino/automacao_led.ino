char cmd;                     //Define a variável dos comandos seriais
int led = 10;

void setup() {
  Serial.begin(9600);         //Inicia o Monitor Serial
  pinMode(led, OUTPUT);         //Define o pino como saída
  digitalWrite(led, LOW);
}

void loop() {
  cmd = Serial.read();        //Realiza a leitura do serial
  if (cmd == 'L') {           //Se o comando for "l", liga o led
    digitalWrite(led, HIGH); 
  }

  else if (cmd == 'D') {      //Se o comando for "d", desliga o led
    digitalWrite(led, LOW);
  }
}