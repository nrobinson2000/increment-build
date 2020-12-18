#include "Particle.h"

#define STR(x) #x

SYSTEM_MODE(MANUAL);
SYSTEM_THREAD(ENABLED);

void setup() {
  Serial.begin(115200);
  Serial.print(STR(RELEASE_STRING));
}

void loop() {

}