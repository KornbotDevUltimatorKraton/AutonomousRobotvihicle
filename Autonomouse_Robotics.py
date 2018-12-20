import serial
from nanpy import(ArduinoApi,SerialManager)
import time
sensor1 = 0
sensor2 = 0
try:
   connection = SerialManager()
   motorunit = ArduinoApi(connection=connection) #Connection astrablished 

except:
    print("Motor unit control ")

#try:
 #  sensor_msg = serial.Serial("/dev/ttyUSB0",115200)
#except:
#   print("Sensor read message error please check the sensor unit")

   # Backward function for the robot to move back and detect obstable 
def Backward_active(sensor1,SpeedStart,SpeedEnd,timechange):
      if int(sensor1) >= 50:
             motorunit.analogWrite(6,0)
             motorunit.analogWrite(10,0)
             motorunit.analogWrite(4,0)
             motorunit.analogWrite(3,0)
             motorunit.analogWrite(9,SpeedEnd)
             motorunit.analogWrite(11,SpeedEnd)
             motorunit.analogWrite(2,SpeedEnd)
             motorunit.analogWrite(5,SpeedEnd)
      else:
             #Backward part
             motorunit.analogWrite(6,SpeedStart)     # Roughly 150    
             motorunit.analogWrite(10,SpeedStart)
             motorunit.analogWrite(4,SpeedStart)
             motorunit.analogWrite(3,SpeedStart)
             time.sleep(timechange) # time sleep speed change 0.05
             motorunit.analogWrite(6,SpeedEnd)           # Roughly 127
             motorunit.analogWrite(10,SpeedEnd)
             motorunit.analogWrite(4,SpeedEnd)
             motorunit.analogWrite(3,SpeedEnd)
             #Forward function  
             motorunit.analogWrite(9,0)
             motorunit.analogWrite(11,0)
             motorunit.analogWrite(2,0)
             motorunit.analogWrite(5,0)
    # Forward and detect the obstacle in front 
def Foward_active(sensor1,sensor2,SpeedStart,SpeedEnd,timechange): 
       if int(sensor2) >= 65:
             motorunit.analogWrite(6,SpeedEnd)
             motorunit.analogWrite(10,SpeedEnd)
             motorunit.analogWrite(4,SpeedEnd)
             motorunit.analogWrite(3,SpeedEnd)
             motorunit.analogWrite(9,SpeedEnd)
             motorunit.analogWrite(11,0)
             motorunit.analogWrite(2,0)
             motorunit.analogWrite(5,)
             if int(sensor1) >= 50:  
                  motorunit.analogWrite(6,0)
                  motorunit.analogWrite(10,0)
                  motorunit.analogWrite(4,0)
                  motorunit.analogWrite(3,0)
                  motorunit.analogWrite(9,SpeedEnd)
                  motorunit.analogWrite(11,SpeedEnd)
                  motorunit.analogWrite(2,SpeedEnd)
                  motorunit.analogWrite(5,SpeedEnd)
                  
       if int(sensor2) < 65: 
             #Backward part
            Backward_active(sensor1,SpeedStart,SpeedEnd,timechange)
while True:
         sensor1 = motorunit.analogRead(0)#Sensor 1 functioning for the Back se$
         sensor2 = motorunit.analogRead(1)#Sensor 2 functioning for the front u$

         print("Back sensor detection:")
         print(sensor1)
         print("Fron sensor distance :")
         print(sensor2)
         Foward_active(sensor1,sensor2,150,127,0.05) 
          

         