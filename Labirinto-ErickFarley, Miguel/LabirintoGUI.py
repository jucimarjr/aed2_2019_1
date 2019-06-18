from tkinter import *
import random as rand
import LabirintoCode as LC
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Labirinto")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
  
        self.alturaLabel = Label(self.segundoContainer,text="Altura", font=self.fontePadrao)
        self.alturaLabel.pack(side=LEFT)
  
        self.alturaIn = Entry(self.segundoContainer)
        self.alturaIn["width"] = 10
        self.alturaIn["font"] = self.fontePadrao
        self.alturaIn.pack(side=LEFT)
  
        self.larguraLabel = Label(self.terceiroContainer, text="Largura", font=self.fontePadrao)
        self.larguraLabel.pack(side=LEFT)
  
        self.larguraIn = Entry(self.terceiroContainer)
        self.larguraIn["width"] = 10
        self.larguraIn["font"] = self.fontePadrao
        self.larguraIn.pack(side=LEFT)
  
        self.criarLab = Button(self.quartoContainer)
        self.criarLab["text"] = "criarLab"
        self.criarLab["font"] = ("Calibri", "8")
        self.criarLab["width"] = 12
        self.criarLab["command"] = (lambda : LC.clickButton(self.alturaIn.get(), self.larguraIn.get()))
        self.criarLab.pack()
  

        plt.rcParams['toolbar'] = 'None'
        plt.figure(0)
        plt.axes().invert_yaxis()
        plt.figure(1)
        plt.axes().invert_yaxis()

    #Método verificar largura

#=======================MAIN==========================
root = Tk()
Application(root)
root.mainloop()