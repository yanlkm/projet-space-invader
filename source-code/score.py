import json
import os
CURDIR = os.path.dirname(__file__)
DATA = os.path.join(CURDIR, "data", "score.json")

class Score(object):
    def __init__(self, nom_joueur, nb_points,temps):
        self.nom_joueur=nom_joueur
        self.nb_points=nb_points
        self.temps=temps

    def getTemps(self):
        return self.temps

    def getNomJoueur(self):
        return self.nom_joueur

    def getNbPoints(self):
        return self.nb_points

    def toFile(self, fich):
        f = open(fich,"w")
        l=self
        json.dump(l.__dict__,f)
        f.close()

    @classmethod
    def fromFile(cls, fich):
        f = open(fich,"r")
        d = json.load(f)
        lnew=Score(d["nom_joueur"],d["nb_points"], d["temps"])
        f.close()
        return lnew


    def __str__(self):
        return "Joueur " + self.nom_joueur + " nbPoints "+ str(self.nb_points) + " temps: " + str(self.temps)+"\n"


class Resultat(object):
    def __init__(self):
        self.lesScores=[]

    def ajout(self, score):
        self.lesScores.append(score)

    def getLesScores(self):
        return self.lesScores

    def __str__(self):
        chaine=str(self.lesScores[0])
        for e in self.lesScores[1:]:
            chaine=chaine+ "," + str(e)+"\n"
        return chaine

    @classmethod
    def fromFile(cls,fich):
        f = open(fich,"r")
        #chargement
        tmp = json.load(f)

        liste = []
        for d in tmp:
            #créer un score
            l=Score(d["nom_joueur"],d["nb_points"], d["temps"])
            #l'ajouter dans la liste
            liste.append(l)
        res=Resultat()
        res.lesScores=liste
        f.close()
        return res

    def toFile(self,fich):
        f = open(fich,"w")
        tmp = []
        for l in self.lesScores:
        #créer un dictionnaire
            d = {}
            d["nom_joueur"] = l.nom_joueur
            d["nb_points"] = l.nb_points
            d["temps"] = l.temps
            tmp.append(d)
        json.dump(tmp,f)
        f.close()

import playsound