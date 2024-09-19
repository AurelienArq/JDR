# Créé par Elève, le 30/09/2022 en Python 3.7
from random import randint

#//////////////////////////////////////////////////////////////////////////////#
##/////////////////Fonctions de génération du perso et ennemi/////////////////##
#//////////////////////////////////////////////////////////////////////////////#

class Personnage :
    def __init__ (self,nom,pv,inventaire,degats=1,protection=0,arme1="none",arme2="none",casque="chapeau de paille",plastron="chemise",jambières="pantalon",bottes="Souliers en cuir",argent=0):
        self.name=nom
        self.pv=pv
        self.inventaire=inventaire
        self.degats=degats
        self.protection=protection
        self.arme1=arme1
        self.arme2=arme2
        self.casque=casque
        self.plastron=plastron
        self.jambière=jambières
        self.bottes=bottes
        self.gold=argent

    def affiche_global(self):
        print("||",self.name,"||",self.pv,"PV ||  inventaire :",self.inventaire,"|| arme1 :",self.arme1,"|| arme2 :", self.arme2,"|| gold :",self.gold,"||")

    def affiche_stats(self):
        print("||",self.name,"||",self.pv,"PV || dégats :",self.degats,"|| portection :",self.protection,"||")

    def affiche_inventaire(self):
        print("|| inventaire :",self.inventaire,"||")

    def affiche_equipement(self):
        print("|| arme1 :",self.arme1,"|| arme2 :", self.arme2,"|| casque :",self.casque,"|| plastron :",self.plastron,"|| jambières ")

class Ennemi :
    def __init__(self,type,pv,degats):
        self.type=type
        self.pv=pv
        self.degats=degats


#//////////////////////////////////////////////////////////////////////////////#
##///////////////////////Fonctions génération des armes///////////////////////##
#//////////////////////////////////////////////////////////////////////////////#


class Arme:
    def __init__(self,name,niv,degats,protection):
        self.name=name
        self.lv=niv
        self.degats=degats*niv
        self.protection=protection*niv

class Potion:
    def __init__(self,name,soin):
        self.name=name
        self.soin=soin

class Armure:
    def __init__(self,name,niv,protection):
        self.name=name
        self.lv=niv
        self.protection=protection*niv



#//////////////////////////////////////////////////////////////////////////////#
##////////////////////////////Fonctions d'affichage////////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#

def separation():
    for i in range (0,5):
        print("")




#//////////////////////////////////////////////////////////////////////////////#
##/////////////////////////////Fonctions de lieux/////////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#

def Foret():
    print("Vous décidez d'allez explorer la forêt et vous vous engoufrez entre les arbres.")
    print("")



def Donjon():
    print("En quête de trésors et de combats vous choisissez d'explorer le donjon. Vous n'êtes qu'à l'entrée, que vous sentez déjà")
    print("une odeur d'or et de trésors mélée à celle des monstres qui parcours le donjon. Prenez garde !")
    print("")


def Marais():
    print("Vous entrez dans le marais")
    print("")


def Auberge():
    print("Fatigué, vous optez pour un passage à l'Auberge. À peine à l'interieur, vous vous approchez du feu pour vous reposer.")
    print("")


def Montagne():
    print("Vous vous dirigez vers le pied de la montagne et vous en commencez l'ascension")
    print("")


def Ville():
    print("Vous vous avancez en direction de l'Entrée principale de la ville et hélez les gardes pour qu'ils vous ouvrent.")
    print(" Alors que les portes s'ouvrent vous entrez dans la ville")
    print("")





#//////////////////////////////////////////////////////////////////////////////#
##//////////////////////////////Fonctions de jeu//////////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#

def action(Items,Lieu):
    EndroitA=Lieu[randint(0,len(Lieu)-1)]
    EndroitB=EndroitA
    while EndroitB==EndroitA:
        EndroitB=Lieu[randint(0,len(Lieu)-1)]
    move=0
    while move==0:
        print("Vous marchez le long de la route lorsque vous appercevez à gauche un(e)",EndroitA,"et à droite un(e)",EndroitB,". Où souhaitez vous allez ?",end="  ")
        deplacement=input("")
        if deplacement=="Gauche" or deplacement=="gauche" or deplacement=="g" or deplacement==EndroitA:
            move=1
            return EndroitA
        elif deplacement=="Droite" or deplacement=="droite" or deplacement=="d" or deplacement==EndroitB:
            move=1
            return EndroitB


def exploration(deplacement):
    if deplacement=="Foret":
        Foret()
    elif deplacement=="Donjon":
        Donjon()
    elif deplacement=="Auberge":
        Auberge()
    elif deplacement=="Ville":
        Ville()
    elif deplacement=="Marais":
        Marais()
    elif deplacement=="Montagen":
        Montagne()



def combat(self,ennemi,Items):
    nb_action=1
    fin_combat=""
    if fin_combat=="":
        while nb_action>0:
            print("Vous avez",Perso.pv,"PV")
            action=input("Que veux tu faire : ||boire une potion||  ||attaquer||  ||fuir||")

            if action=="boire une potion" :
                if Perso.inventaire!=[]:
                    for i in Perso.inventaire:   #utilisation de potion si le joueur en possède
                        if i=="Potion lv1":
                            Perso.pv=Perso.pv+10
                            nb_action=0
                        elif i=="Potion lv2":
                            Perso.pv=Perso.pv+25
                            nb_action=0
                        elif i=="Potion lv3":
                            Perso.pv=Perso.pv+50
                            nb_action=0

            elif action=="attaquer" :
                ennemi.pv=ennemi.pv-Perso.degats
                nb_action=0

            elif action=="fuir" :
                chance_de_fuite=randint(1,50)
                if chance_de_fuite%7==0:
                    print("Vous avez réussi à fuir")
                    nb_action=0
                else :
                    print("Vous n'avez pas réussi à fuir")
                    nb_action=0

        if ennemi.pv>0:
            Perso.pv=Perso.pv-ennemi.degats
        else :
            fin_combat="Victoire"

        if Perso.pv!=0 :
            combat(ennemi)
            loot=1

        else :
            fin_combat="Mort"



#//////////////////////////////////////////////////////////////////////////////#
##/////////////////////////////Préparation du jeu/////////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#

#création des armes
Epée_une_main=Arme("Epée une main",1,10,0)
Epée_deux_mains=Arme("Epée deux mains",1,20,0)
Arc=Arme("Arc",1,30,0)
Bouclier=Arme("Bouclier",1,0,15)

#création des potions
Potion_lv1=Potion("Potion lv1",10)
Potion_lv2=Potion("Potion lv2",25)
Potion_lv3=Potion("Potion lv3",50)

#création des armures
Casque=Armure("Casque",1,5)
Plastron=Armure("Plastron",1,20)
Jambières=Armure("Jambières",1,10)
Bottes=Armure("Bottes",1,5)

Items=[[Epée_une_main,Epée_deux_mains,Arc,Bouclier],[Potion_lv1,Potion_lv2,Potion_lv3],]
Lieu=["Forêt","Donjon","Forêt","Ville","Marais","Forêt","Marais","Auberge","Forêt","Forêt","Marais","Montagne"]
Perso=Personnage(input("Quel est le pseudo de ton personnage ?"),100,[])
Goblin=Ennemi("Goblin",10,2)
Troll=Ennemi("Troll",50,10)
Dragon=Ennemi("Dragon",200,50)





#//////////////////////////////////////////////////////////////////////////////#
##////////////////////////////////////////////////////////////////////////////##
##//////////////////////////////Lancement du jeu//////////////////////////////##
##////////////////////////////////////////////////////////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#
Perso.affiche_global()
print("")
print("Vous commencez l'aventure !!")
print("")

#while jeu!="Arrêter":
deplacement=action(Items,Lieu)
exploration(deplacement)

