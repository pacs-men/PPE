# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 09:37:05 2017

@author: Emeric Coudeville
"""
from Tkinter import *
import tkFileDialog
import pickle

class application:
    
    def ouvrir_fichier(self):
        fichier = tkFileDialog.askopenfilename(title = "ouvrir le fichier", filetypes = [("fichiers de scan d'environnement", "*.sce")])
        with open(fichier, "rb") as f:
            mon_pickler = pickle.Unpickler(f)
            self.ls_point = mon_pickler.load()
        
        self.taille_auto()
        self.tracer_points()
        
    def aller_gauche(self):
        
        self.taille[0] = self.taille[0]-self.pourcent
        self.taille[1] = self.taille[1]-self.pourcent
        self.tracer_points()
        
    def aller_droite(self):
        
        self.taille[0] = self.taille[0]+self.pourcent
        self.taille[1] = self.taille[1]+self.pourcent
        self.tracer_points()
        
    def aller_haut(self):
        
        self.taille[2] = self.taille[2]-self.pourcent
        self.taille[3] = self.taille[3]-self.pourcent
        self.tracer_points()
        
    def aller_bas(self):
        
        self.taille[2] = self.taille[2]+self.pourcent
        self.taille[3] = self.taille[3]+self.pourcent
        self.tracer_points()
        
    def zoom_out(self):
        
        self.taille[1]+=self.pourcent
        self.taille[3]+=self.pourcent
        self.taille[0]-=self.pourcent
        self.taille[2]-=self.pourcent
        
        self.calcul_pourcent()
        self.tracer_points()
        
    def zoom_in(self):
        
        self.taille[1]-=self.pourcent
        self.taille[3]-=self.pourcent
        self.taille[0]+=self.pourcent
        self.taille[2]+=self.pourcent
        
        self.calcul_pourcent()
        self.tracer_points()
        
    def aller_gauchek(self, event):
        
        self.taille[0] = self.taille[0]-self.pourcent
        self.taille[1] = self.taille[1]-self.pourcent
        self.tracer_points()
        
    def aller_droitek(self, event):
        
        self.taille[0] = self.taille[0]+self.pourcent
        self.taille[1] = self.taille[1]+self.pourcent
        self.tracer_points()
        
    def aller_hautk(self, event):
        
        self.taille[2] = self.taille[2]-self.pourcent
        self.taille[3] = self.taille[3]-self.pourcent
        self.tracer_points()
        
    def aller_bask(self, event):
        
        self.taille[2] = self.taille[2]+self.pourcent
        self.taille[3] = self.taille[3]+self.pourcent
        self.tracer_points()
        
    def zoom_outk(self, event):
        
        self.taille[1]+=self.pourcent
        self.taille[3]+=self.pourcent
        self.taille[0]-=self.pourcent
        self.taille[2]-=self.pourcent
        self.calcul_pourcent()
        self.tracer_points()
        
    def zoom_ink(self, event):
        
        self.taille[1]-=self.pourcent
        self.taille[3]-=self.pourcent
        self.taille[0]+=self.pourcent
        self.taille[2]+=self.pourcent
        self.calcul_pourcent()
        self.tracer_points()
        
    def click(self, event):
        print event.x, event.y
        if len(self.list_click)<2:
            self.list_click.append([(event.x/self.largeur)*(self.taille[1]-self.taille[0])-self.taille[0], (event.y/self.hauteur)*(self.taille[3]-self.taille[2])-self.taille[2]])
            print(((event.x/self.largeur)*(self.taille[1]-self.taille[0])-self.taille[0]), (event.y/self.hauteur)*(self.taille[3]-self.taille[2])-self.taille[2])
        
        
    
    
    def __init__(self, fen):
        
        self.largeur = 500
        self.hauteur = 500
        
        self.couleur_bg = "Black"
        self.couleur_point = "Blue"
        
        self.taille_point = 2
        
        self.taille = [0, 1, 0, 1]
        self.pourcent = 0.1
        self.ls_point = []
        
        self.list_click = []
        self.text_msg = "rien"
        
        # frame canvas
        self.frame_canvas = Frame(fen, borderwidth = 2, relief = GROOVE)
        self.frame_canvas.pack(side = LEFT)
        
        self.frame_direction = Frame(fen, borderwidth = 2, relief = GROOVE)
        self.frame_direction.pack(side = TOP)
        
        self.frame_fichier = Frame(fen, borderwidth = 2, relief = GROOVE)
        self.frame_fichier.pack()
        
        self.frame_message = Frame(fen, borderwidth = 2, relief = GROOVE)
        self.frame_message.pack()
        
        self.frame_zoom = Frame(fen, borderwidth = 2, relief = GROOVE)
        self.frame_zoom.pack(side = BOTTOM)
        
        self.msg = Label(self.frame_message, text = self.text_msg,  borderwidth = 2, relief = GROOVE)
        self.msg.pack()
        
        self.fen = fen
        fen.title("Visualisation des points")
        
        self.canvas = Canvas(self.frame_canvas, width = self.largeur, height = self.hauteur, bg= self.couleur_bg, bd = -1)
        self.canvas.pack()
        
        self.gauche = Button(self.frame_direction, text = "gauche", command = self.aller_gauche)
        self.gauche.pack(side = LEFT)
        
        self.droite = Button(self.frame_direction, text = "droite", command = self.aller_droite)
        self.droite.pack(side = RIGHT)
        
        self.haut = Button(self.frame_direction, text = "haut  ", command = self.aller_haut)
        self.haut.pack(side = TOP)
        
        self.bas = Button(self.frame_direction, text = "bas   ", command = self.aller_bas)
        self.bas.pack(side = BOTTOM)
        
        self.z_out = Button(self.frame_zoom, text = "zoom out", command = self.zoom_out)
        self.z_out.pack()
        
        self.z_in = Button(self.frame_zoom, text = "zoom in  ", command = self.zoom_in)
        self.z_in.pack()
        
        self.ouvrir = Button(fenetre, text = "ouvrir un fichier", command = self.ouvrir_fichier)    
        self.ouvrir.pack()
        
        # touche clavier
        fen.bind("<z>", self.aller_hautk)
        fen.bind("<s>", self.aller_bask)
        fen.bind("<q>", self.aller_gauchek)
        fen.bind("<d>", self.aller_droitek)
        fen.bind("<o>", self.zoom_outk)
        fen.bind("<i>", self.zoom_ink)
        
        
        # souris
        self.canvas.bind("<Button-1>", self.click)
        
        
    def calcul_pourcent(self):
        self.pourcent = 0.1*(self.taille[1]-self.taille[0])
        
    def aff_point(self, x, y):
        self.canvas.create_rectangle(x-self.taille_point, y-self.taille_point, x+self.taille_point, y+self.taille_point, fill = self.couleur_point, width = 0)
  
      
    def tracer_points(self):
        self.canvas.delete(ALL)
        
        taillel = self.taille[1]-self.taille[0]
        tailleh = self.taille[3]-self.taille[2]
        
        for point in self.ls_point:
            x = point[0]
            y = point[1]
            
            x = x-self.taille[0]
            y = y-self.taille[2]
            
            x = int((x/taillel)*self.largeur)
            y = int((y/tailleh)*self.hauteur)
            
            self.aff_point(x, y)
    
    def taille_auto(self):
        
        minp = self.ls_point[0][0]
        maxp = self.ls_point[0][0]
        for point in self.ls_point:
            for x in point:
                if x < minp:
                    minp = x
                    
                elif x > maxp:
                    maxp = x
                
        self.taille = [minp, maxp, minp, maxp]
        self.calcul_pourcent()
        self.taille = [self.taille[0]-self.pourcent, self.taille[1]+self.pourcent, self.taille[2]-self.pourcent, self.taille[3]+self.pourcent]
        
    

    
fenetre = Tk()
mg = application(fenetre)
    
fenetre.mainloop()