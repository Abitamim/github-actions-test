int i = 0;

void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    while (i < 10){
    digitalWrite(LED_BUILTIN, HIGH);
    delay(200);
    digitalWrite(LED_BUILTIN, LOW);
    delay(200);
    i++;
    }
}