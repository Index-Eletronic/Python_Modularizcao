from pyfirmata import Arduino
from tkinter import *

#Especifique a Porta do Arduino

PORTA = "COM4"

arduino = Arduino(PORTA)
led = arduino.get_pin('d:13:o')
# d= Digital
#Pinno 13
#o = OUTPUT

def acender():
    led.write(1)

def apagar():
    led.write(2)

janela = Tk()
janela.title("Acender e Apagar LED com botão")
janela.geometry("350x60")
frame = Frame(master=janela)
frame.pack()
btacende = Button(master=frame, text="Acender", commaand=acender)
btacende.grid(row=0, column=0)
btapaga = Button(master=frame, text="Acender", commaand=apagar)
btapaga.grid(row=0, column=1)

janela.mainloop()
