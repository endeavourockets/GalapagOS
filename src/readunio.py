import serial
import random
import time

# Change these to the ground arduino specifics
ser = serial.Serial('PORT', baudrate=9600, timeout=1)
list_data = ["Sensor : Tempreture , Tempreture : 13.09 , Humidity : 2.12",
             "Sensor : GPS , Altitude : 234 , Longitude : 12"]
list_data.append(
    "Sensor : Motion , Velocity : 23 , acceleration : 12.3 , rotation : 38")
list_data.append("Sensor : Pressure, Pressure : 103110")
i = 0
while i < 10:
    i = i + 1
    Data = ser.readline().decode('ascii')
    # The data sent is assumed in the format " Sensor : Pressure , Pressure : 2 ; Sensor : Sensor2 , Data : 23"
    filein = open('aruino-database.txt', 'a')
    for d in Data.split(';'):
        filein.write(d + "/n")
    filein.close()
    time.sleep(1)
