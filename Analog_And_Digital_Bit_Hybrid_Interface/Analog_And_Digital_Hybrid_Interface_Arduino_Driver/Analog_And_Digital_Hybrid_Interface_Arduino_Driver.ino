
// write ram state variable
char strWriteRamState;

// bit 0 value
double dblBit0 = 0;

// bit 1 value
double dblBit1 = 0;

// bit 2 value
double dblBit2 = 0;

// bit 0 analog state
double dblBit0State = 0;

// bit 1 analog state
double dblBit1State = 0;

// bit 2 analog state
double dblBit2State = 0;

// function for setting state of ram
void SetState(char strBitState) {
  // sets bit 0 to 0
  if(strBitState == 'a') {
    analogWrite(3, LOW);
  }
  // sets bit 0 to 1
  if(strBitState == 'b') {
    analogWrite(3, HIGH);
  }
  // sets bit 1 to 0
  if(strBitState == 'c') {
    analogWrite(5, LOW);
  }
  // sets bit 1 to 1
  if(strBitState == 'd') {
    analogWrite(5, HIGH);
  }
  // sets bit 2 to 0
  if(strBitState == 'e') {
    analogWrite(6, LOW);
  }
  // sets bit 2 to 1
  if(strBitState == 'f') {
    analogWrite(6, HIGH);
  }
  // states for bit 0 in analog mode
  if(strBitState == 'g') {
    // input for bit 0 state
    dblBit0State = Serial.read();
    // Writes bit 0 state to ram    
    analogWrite(3, dblBit0State);
  }
  // states for bit 1 in analog mode
  if(strBitState == 'h') {
    // input for bit 1 state
    dblBit0State = Serial.read();
    // Writes bit 1 state to ram
    analogWrite(5, dblBit0State);
  }
  // states for bit 2 in analog mode
  if(strBitState == 'i') {
    // input for  bit 2 state
    dblBit0State = Serial.read();
    // Writes bit 2 state to ram
    analogWrite(6, dblBit0State);
  }

}
void setup() {
  // put your setup code here, to run once:
  // starts serial connection at 57600 baud
  Serial.begin(57600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    // input for Analog_And_Digital_Bit_Hybrid_Interface for user
    strWriteRamState = Serial.read();
    // function needed
    SetState(strWriteRamState);
    // read dblBit0
    dblBit0 = analogRead(A0);
    // sends data from dblBit0 back to user
    Serial.print((double) dblBit0, "/n");
    // read dblBit1
    dblBit1 = analogRead(A1);
    // sends data from dblBit1 back to user
    Serial.print((double) dblBit1, "/n");
    // read dblBit2
    dblBit2 = analogRead(A2);
    // sends data from dblBit2 back to user
    Serial.print((double) dblBit2, "/n");
  }
}
