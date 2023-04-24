from gpiozero import LED, MotionSensor
import time

# PIR pin nummer
pir = MotionSensor(23)

# LED pins
led_red = LED(15)
led_green = LED(21)

print("Security System is On.")

try:
    while True:
        if pir.value:
            led_red.on()
            led_green.off()
            print("Motion Detected")
            time.sleep(1)
        else:
            led_red.off()
            led_green.on()
            print("All Clear")
            time.sleep(1) 
            
except KeyboardInterrupt:
    print("Security System is Turned off.\nHave a Nice Day\n\n...and good luck!")
    
