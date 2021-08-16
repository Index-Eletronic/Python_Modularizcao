from pyfirmata import Arduino, SERVO
from tkinter import *
from time import sleep

PORTA = 'COM4' # Porta de comunicação do Arduino.
board = Arduino(PORTA)
#Configuração pinos 8 9 10 Arduino para as portas do driver TB6560
pin = 10
'''
clkp = arduino.get_pin('p:8:o') # clk+ - PWM
clkn = arduino.get_pin('p:9:o') # clk- - PWM
cwp = arduino.get_pin('d:10:o') # cw+
npassos = 6400 # Numero de pasos por revolução.
mspeed = 60 # velocidade do motor em rpm'''

board.digital[pin].mode = SERVO

def rotateServo(pin, angulo):
    board.digital[pin].write(angulo)
    sleep(0.015)

def horario():
    while True:
        for i in range(0,180):
            rotateServo(pin, i)

def anti():
    while True:
        for i in range(180,1,-1):
         rotateServo(pin, i)

def stop():
   while horario() is True:
    break


janela = Tk()
janela.title("CONTROLE DE COMANDO DO MOTOR")
janela.geometry("350x60")
frame = Frame(master=janela)
frame.pack()
btacende = Button(master=frame, text="HORARIO", command=horario)
btacende.grid(row=0, column=0)

btapaga = Button(master=frame, text="ANTI-HORARIO", command=anti)
btapaga.grid(row=0, column=1)

btstop = Button(master=frame, text="STOP", command=stop)
btstop.grid(row=0, column=2)

janela.mainloop()


