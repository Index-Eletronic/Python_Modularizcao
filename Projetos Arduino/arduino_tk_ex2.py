from pyfirmata import Arduino, PWM
from tkinter import *

PORTA = 'COM3'

arduino = Arduino(PORTA)
arduino.digital[10].mode = PWM

def controle (intensidade):
    arduino.digital[10].write(int(intensidade)/100)
    if intensidade == 100:
         print(intensidade, '\n')

janela = Tk()
janela.title("Controle de intensidade do LED")
janela.geometry("400x50")

frame = Frame(master=janela)
frame.pack()

slider = Scale(master=frame, length=300, from_=0, to=100, orient=HORIZONTAL, command=controle)
slider.grid(row=0, column=0)

janela.mainloop()

