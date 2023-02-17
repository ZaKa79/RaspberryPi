import sqlite3
import datetime
import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read sensor data using pin 14
instance = dht11.DHT11(pin = 14)

while True:

    result = instance.read() # data from sensor
    dt = datetime.datetime.now() #time ande date

    if result.is_valid(): #from sencor
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)
        
    else: #from sensor
        print("Error: %d" % result.error_code)

# Create a database/table
    try:
        conn = sqlite3.connect('dht11.db') #connect to Database
        c = conn.cursor() #make a cursor
        c.execute("CREATE TABLE IF NOT EXISTS readings (id integer PRIMARY KEY AUTOINCREMENT, datetime timestamp, temperature float, humidity float)") #creates the database 

        query = "INSERT INTO readings (DateTime,Temperature,Humidity) VALUES (?,?,?)" #setup for injection
        values = (dt,result.temperature, result.humidity) # the values
        c.execute (query, values)

        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        c.rollback()
        print(f'data not inserted! {e}')
    
    except KeyboardInterrupt:
        print("Program stopped.")

    time.sleep(10)



    

    