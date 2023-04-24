#https://www.engineersgarage.com/articles-raspberry-pi-python-software-pwm-led-fading/

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)

soft_pwm = GPIO.PWM(40, 1)
soft_pwm.start(50)
input("Press return to stop: ")
soft_pwm.stop()
GPIO.cleanup()