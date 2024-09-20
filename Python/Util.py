from random import randint
from timeit import default_timer as timer
from Python.main import Perso


def dé():
    return randint(1,20)

def Changement(pv,gold):
    if Perso.pv+pv>Perso.pv_max:
        Perso.pv=Perso.pv_max
    else :
        Perso.pv=Perso.pv+pv
    Perso.gold=Perso.gold-gold

def separation(n=5):
    for i in range (0,n):
        print("")

def ecrit(texte):
    i=0
    while i!=len(texte):
        print(texte[i],end="")
        i=i+1
        debut=timer()
        while timer()<0.04+debut:
            b=0


def Help():
    print("Pour afficher l'inventaire taper I")
    print("Pour afficher vos stats tapez S")
    print("Pour tout afficher tapez A")
    print("Pour afficher le nombre de kills tapez K")
    print("Pour quitter un batiment ou la ville tapez QUITTER")
    print("Pour sauvegarder tapez SAUVEGARDER")


def CREDITS():
    print("Merci d'avoir joué")
    print("Jeu programmé par Aurélien Arqué")
    print("Graphismes réalisés par ... ... sous la direction de ...")
    if Perso.arme1=="none":
        print("Menssion spéssial à Romain pour sont investicemant dans la corection et pour ces nombreu conseilles.")
    else :
        print("Mention spéciale à Romain pour son investissement dans la correction et pour ses nombreux conseils.")
    print("Ainsi qu'à Theophile pour son aide avec la sauvegarde.")
    print("Avec les conseils de Théophile, Tristan, Morgan, Alexandre, Thomas, Antoine, M.Koroloff")
    print("Et le soutien de la Classe de Terminale 5")
