import pyfirmata
import Stepper


PORTA = "COM4"

arduino = pyfirmata.Arduino(PORTA)
led = arduino.get_pin('d:13:o')
'''
ms1 = arduino.get_pin('d:9:o') # A1
ms2 = arduino.get_pin('d:10:o') # A2
ms3 = arduino.get_pin('d:11:o') # B1
ms4 = arduino.get_pin('d:12:o') # b2
'''
'''
while True:
    led.write(1)
    arduino.pass_time(0.5)
    led.write(0)
    arduino.pass_time(0.50)
'''
while True:
    estado = int(input("Digite 1 para ligar LED ou 0 para desligar: "))
    if estado == 0 or estado == 1:
        led.write(estado)
    else:
        print("Digite apenas valores 0 ou 1")