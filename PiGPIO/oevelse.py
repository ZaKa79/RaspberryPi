import pigpio # (1)
from time import sleep

GPIO_PIN = 21
pi = pigpio.pi() # (2)
pi.set_mode(GPIO_PIN, pigpio.OUTPUT) # (3)

while True:
    pi.write(GPIO_PIN, 1) # 1 = High = On # (4)
    sleep(1) # 1 second
    pi.write(GPIO_PIN, 0) # 0 = Low = Off # (5)
    sleep(1) # 1 second