import pyfirmata

PORTA = "COM3"

arduino = pyfirmata.Arduino(PORTA)
led = arduino.get_pin('d:13:o')


while True:
    led.write(1)
    arduino.pass_time(0.5)
    led.write(0)
    arduino.pass_time(0.50)
