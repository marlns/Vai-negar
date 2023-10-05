from tkinter import *
import random
from sys import maxsize
import pygame


def aleatorio():
    n = random.randint(0,maxsize)
    if n%2==0:
        janela2()
    else: 
        janela3()
    

def janela2( ):
    pode = Tk()
    pode.title("Já Pode AO MOSSAR")
    pode.geometry("650x800")
    pode.configure(background = "gray")
           
    logo = PhotoImage(master = pode,file = "pode.png")
    figura2 = Label(master = pode, image = logo, bg = "gray")
    figura2.grid(row = 0, column = 0, padx = 0)

    textoinicio = Label(pode, text = "Obrigado você não negou um prato de comida.\n Agora posso AO MOSSAR em paiz.", font = ("Comic Sans MS", 15), bd = 0, bg = "gray")
    textoinicio.grid(column = 0 , row = 1, padx = 30 , pady = 1 )


    pygame.init()
    pygame.mixer.music.load("deu.mp3")
    pygame.mixer.music.play(0)
    pygame.mixer_music.set_volume(0.1)
    pygame.event.wait()


    pode.mainloop()


def janela3( ):
    negou = Tk()
    negou.title("Vai Negar?")
    negou.geometry("650x800")
    negou.configure(background = "gray")

    logo = PhotoImage(master = negou, file = "negou.png")
    figura3 = Label(master = negou, image = logo, bg = "gray")
    figura3.grid(row = 0, column = 0, padx = 0)

    textoinicio = Label(negou, text = "Não acredito que você vai me negar um prato de comida?", font = ("Comic Sans MS", 15), bd = 0, bg = "gray")
    textoinicio.grid(column = 0 , row = 1, padx = 30 , pady = 1 )


    pygame.init()
    pygame.mixer.music.load("negou.mp3")
    pygame.mixer.music.play(0)
    pygame.mixer_music.set_volume(0.1)
    pygame.event.wait()

    negou.mainloop()
   

janela1 = Tk()
janela1.title("Vai Negar?")
janela1.geometry("650x800")
janela1.configure(background = "gray")

logo = PhotoImage(file = "menu.png")
figura1 = Label(image = logo, bg = "gray")
figura1.grid(row = 0, column = 0, padx = 50)

textoinicio = Label(janela1, text = "Vai me negar um prato de comida?.", font = ("Comic Sans MS", 15), bd = 0, bg = "gray")
textoinicio.grid(column = 0 , row = 1, padx = 30 , pady = 1 )

botao = Button(janela1, text = "Vai negar?", font = ("Impact",15) , command = aleatorio)
botao.grid(column = 0, row = 20, padx = 50, pady = 50)
botao.configure(background = "white")

pygame.init()
pygame.mixer.music.load("menu.mp3")
pygame.mixer.music.play(0)
pygame.mixer_music.set_volume(0.1)
pygame.event.wait()


janela1.mainloop()    





