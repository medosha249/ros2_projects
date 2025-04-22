String input;
int LED_PIN = 7;
void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    input = Serial.readStringUntil('\n');
    input.trim();
    if (input == "ON" | input == "1") {
      digitalWrite(LED_PIN, HIGH);
    } else if (input == "OFF" | input== "0") {
      digitalWrite(LED_PIN, LOW);
    }
  }
}
