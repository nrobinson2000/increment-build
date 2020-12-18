#include "Particle.h"

#define STR_EXPAND(x) #x
#define STR(x) STR_EXPAND(x)

SYSTEM_MODE(MANUAL);
SYSTEM_THREAD(ENABLED);

void setup() {
  Serial.begin(115200);
  delay(3000);

  #ifdef RELEASE_STRING
  Serial.printlnf("Build version: %s", STR(RELEASE_STRING));
  #endif
}

void loop() {

}