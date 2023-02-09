from gpiozero import PWMLED

led = PWMLED(15)  # Pins 15 connected with LED

while True:
    inp = input("Type 'on', 'off' or a number 1-10 to control the brightess: ").lower()

    if inp == 'on':
        led.on()
    elif inp == 'off':
        led.off()
    else:
        try:
            val = int(inp)
        except ValueError:
            print('Invalid input.')
        else:
            if 1 <= val <= 10:
                led.value = val / 10.0
            else:
                print('Input must be between 1 and 10')

       