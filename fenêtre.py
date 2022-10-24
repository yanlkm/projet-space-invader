from tkinter import *
from score import *

class Fenetre(Frame):
    def __init__(self, mater= None):
        Frame.__init__(self)
        self.pack()
        self.setup_ui()
        self.affichage_listebox()
        
    
    def setup_ui(self):
        self.titre = Label(self, text = "Space Invaders", font=('Fixedsys',24))
        self.titre.pack()
        self.texte = Entry(self, width =30, font ="Arial 14")
        self.texte.pack(padx =8, pady =8)
        self.listebox = Listbox(self, width =100)
        self.listebox.pack(padx = 10, pady = 10)
        self.boutton_ajouter =Button(self, text='Ajouter un joueur', command = self.ajouter_joueur)
        self.boutton_ajouter.pack()
        self.boutton_effacer =Button(self, text='Effacer un joueur')
        self.boutton_effacer.pack()
        self.boutton_jouer =Button(self, text='Commencer une partie')
        self.boutton_jouer.pack()


    def ajouter_joueur(self):
        self.resultat = Resultat()
        self.nom_du_joueur = self.texte.get()
        self.score = Score(self.nom_du_joueur, 0, 0)
        self.resultat.ajout(self.score)
        self.resultat.toFile(DATA)
        self.resultat.fromFile(DATA)
        
        


    def affichage_listebox(self):
        self.resultat = Resultat()
        self.listebox.insert(END, self.resultat.fromFile(DATA))
        self.listebox.pack()

    


        

        



win = Fenetre()
win.mainloop()

