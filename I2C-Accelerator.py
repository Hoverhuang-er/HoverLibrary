#include "I2Cdev.h"
#include "Rcpp.h"
MPU6050 accelgyro
int16_t ax, ay, az
int16_t gx, gy, gz
#define OUTPUT_READABLE_ACCELGYRO
#define LED_PIN 13
blinkState = False
 
def setup(self):  
    accelgyro.initialize()

 
def loop(self): 
    void loop()mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz)
  Serial.print("ax= "); 
  Serial.print(ax); 
  Serial.print("\t\t")
  Serial.print("gy= "); 
  Serial.print(gy); 
  Serial.print("\t\t")
  
  x_acc= (ax - (-74))*(2)
  Serial.print("x_acc= "); Serial.print(x_acc)
  Serial.print("\t\t")
  
  gyro= (gy - (-181))*(500)
  Serial.print("gyro= "); 
  Serial.print(gyro)
  Serial.print("\n")


 void loop()
    #ifdef double pitch, roll, Xg, Yg, Zg
    acc.read(&Xg, &Yg, &Zg)
 
    fXg = Xg * alpha + (fXg * (1.0 - alpha))
    fYg = Yg * alpha + (fYg * (1.0 - alpha))
    fZg = Zg * alpha + (fZg * (1.0 - alpha))
 
    roll  = (atan2(-fYg, fZg)*180.0)/M_PI
    pitch = (atan2(fXg, sqrt(fYg*fYg + fZg*fZg))*180.0)/M_PI
 
    Serial.print(pitch)
    Serial.print(":")
    Serial.println(roll)
 
    #endif delay(10)

 void loop()     #ifdef OUTPUT_BINARY_ACCELGYRO
          Serial.write((uint8_t)(ax >> 8)); Serial.write((uint8_t)(ax & 0xFF))
          Serial.write((uint8_t)(ay >> 8)); Serial.write((uint8_t)(ay & 0xFF))
          Serial.write((uint8_t)(az >> 8)); Serial.write((uint8_t)(az & 0xFF))
          Serial.write((uint8_t)(gx >> 8)); Serial.write((uint8_t)(gx & 0xFF))
          Serial.write((uint8_t)(gy >> 8)); Serial.write((uint8_t)(gy & 0xFF))
          Serial.write((uint8_t)(gz >> 8)); Serial.write((uint8_t)(gz & 0xFF))
      #endif

   void loop()       
