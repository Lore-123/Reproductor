#Hernandez Hernandez Lorenzo 41s
#1 REPRODUCTOR
from tkinter import *
import pygame, sys
from pygame.locals import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

pygame.init()
def openFileSong():
    cancion = filedialog.askopenfilename()  
    print(cancion)
    pygame.mixer.music.load(cancion)
        
    
def playSong():
    pygame.mixer.music.play()

def stopSong():
    pygame.mixer.music.stop()

def resumeSong():
    pygame.mixer.music.unpause()
    
def pauseSong():
    pygame.mixer.music.pause()
    
def volumenUp():
    levelup=pygame.mixer.music.get_volume() +0.1
    print(levelup)
    pygame.mixer.music.set_volume(levelup)

def volumenDown():
    leveldown=pygame.mixer.music.get_volume() -0.1
    print(leveldown)
    pygame.mixer.music.set_volume(leveldown)

raiz = Tk()
raiz.title("Reproductor MP3 - GUI")
#raiz.iconbitmap("disk-jockey.ico")
raiz.geometry("900x500")
raiz.resizable(0,0)

#Crear frame
framePrincipal = Frame(raiz, bg="#FF6699")
framePrincipal.pack(fill="both", expand=1)

#TITULO DEL REPRODUCTOR
tituloReproductor = Label(framePrincipal, text="Reproductor lore", font=("Arial", 20, "bold"), bg="#FF6699", fg="#fbfbfb")
tituloReproductor.place(relx=0.20,rely=0.4)

#botton open song
botonOpenSong = Button(framePrincipal, text="Open Song", bg="#00CCFF", fg="#000000", font=("Roboto", 10, "bold"), width=12, height=2, command=openFileSong)
botonOpenSong.place(relx=0.01, rely=0.5)

#Play song
botonPlaySong = Button(framePrincipal, text="Play song", bg="#993399", fg="#000000", font=("Roboto", 10, "bold"), width=12, height=2, command=playSong) #e2504c rojo, #42ab49 verde, #ffc400 amarillo, #55009 morado, #0000FF
botonPlaySong.place(relx= 0.15, rely=0.5)

#Stop song 
botonStopSong = Button(framePrincipal, text="Stop song", bg="#FF9966", fg="#000000", font=("Roboto", 10, "bold"), width=12, height=2, command=stopSong)
botonStopSong.place(relx= 0.3, rely=0.5)

#Resume
botonResumeSong = Button(framePrincipal, text="ResumeSong", bg="#993399", fg="#000000", font=("Roboto", 10, "bold"), width=12, height=2, command=resumeSong)
botonResumeSong.place(relx= 0.45, rely=0.5)

#Pause
botonPause = Button(framePrincipal, text="Pause", bg="#00CCFF", fg="#000000", font=("Roboto", 10, "bold"), width=12, height=2, command=pauseSong)
botonPause.place(relx= 0.60, rely=0.5)

#Volumenmas
botonVolumenUp = Button(framePrincipal, text="Volumen +", bg="#66CC88", fg="#000000", font=("Roboto", 10, "bold"), width=12, height=2, command=volumenUp)
botonVolumenUp.place(relx= 0.15, rely=0.8)

#Volumenmenos
botonVolumenDown = Button(framePrincipal, text="Volumen -", bg="#66CC88", fg="#000000", font=("Roboto", 10, "bold"), width=12, height=2, command=volumenDown)
botonVolumenDown.place(relx= 0.45, rely=0.8)

raiz.mainloop()