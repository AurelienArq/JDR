from random import randint

from Python.Lieux.Batiments.Auberge import Auberge
from Python.Lieux.Donjon import Donjon
from Python.Lieux.Foret import Foret
from Python.Lieux.Marais import Marais
from Python.Lieux.Montagne import Montagne
from Python.Lieux.Ville import Ville
from Python.Sauvegarde import création_sauvegarde
from Python.Util import Help
from Python.main import Perso


def action(Items,Lieu):
    EndroitA=Lieu[randint(0,len(Lieu)-1)]
    EndroitB=EndroitA
    while EndroitB==EndroitA:
        EndroitB=Lieu[randint(0,len(Lieu)-1)]
    move=0
    print(" ")
    print("▬"*100)
    print(" ")
    print("Vous marchez le long de la route lorsque vous apercevez à gauche un(e)",EndroitA,"et à droite un(e)",EndroitB,". Où souhaitez vous aller ?",end="  ")

    while move==0:
        deplacement=input("")
        if deplacement=="GAUCHE" or deplacement=="G" or deplacement==EndroitA:
            move=1
            return EndroitA
        if deplacement=="DROITE" or deplacement=="D" or deplacement==EndroitB:
            move=1
            return EndroitB
        if deplacement=="PASSE":  ##condition pour les tests à supprimer à la fin
            move=1
            return "PASSE"
        if deplacement=="STOP" :
            Perso.Etat="Arrêt"
            move=1
            return "Arrêter"
        if deplacement=="HELP":
            Help()
        if deplacement=="SAUVEGARDER":
            création_sauvegarde()
        if deplacement=="A":
            Perso.affiche_all()
        if deplacement=="I":
            Perso.affiche_inventaire()
        if deplacement=="S":
            Perso.affiche_stats()
        if deplacement=="K":
            Perso.affiche_kills()


def exploration(deplacement):
    if deplacement=="FORET (difficulté Debutant)":
        condition=Foret()
    elif deplacement=="DONJON (difficulté Moyenne)":
        Donjon()
    elif deplacement=="AUBERGE":
        Auberge(1)
    elif deplacement=="VILLE":
        Ville()
    elif deplacement=="MARAIS (difficulté Facile)":
        condition=Marais()
    elif deplacement=="MONTAGNE (difficulté Maximale)":
        Montagne()
