# Créé par Elève, le 30/09/2022 en Python 3.7
from random import randint

#//////////////////////////////////////////////////////////////////////////////#
##/////////////////Fonctions de génération du perso et ennemi/////////////////##
#//////////////////////////////////////////////////////////////////////////////#

class Personnage :
    def __init__ (self,nom,pv,inventaire,degats=5,protection=0,arme1="none",arme2="none",casque="chapeau de paille",plastron="chemise",jambières="pantalon",bottes="Souliers en cuir",argent=0):
        self.name=nom
        self.pv=pv
        self.inventaire=inventaire
        self.degats=degats
        self.protection=protection
        self.arme1=arme1
        self.arme2=arme2
        self.casque=casque
        self.plastron=plastron
        self.jambières=jambières
        self.bottes=bottes
        self.gold=argent

    def affiche_all(self):
        print("||",self.name,"||",self.pv,"PV || gold :",self.gold,"|| inventaire :",self.inventaire,"|| arme1 :",self.arme1,"|| arme2 :", self.arme2,"|| casque :",self.casque,"|| plastron :",self.plastron,"|| jambières :",self.jambières,"|| bottes :",self.bottes,"||")

    def affiche_global(self):
        print("||",self.name,"||",self.pv,"PV || inventaire :",self.inventaire,"|| arme1 :",self.arme1,"|| arme2 :", self.arme2,"|| gold :",self.gold,"||")

    def affiche_stats(self):
        print("||",self.name,"||",self.pv,"PV || dégats :",self.degats,"|| portection :",self.protection,"||")

    def affiche_inventaire(self):
        print("|| inventaire :",self.inventaire,"||")

    def affiche_equipement(self):
        print("|| arme1 :",self.arme1,"|| arme2 :", self.arme2,"|| casque :",self.casque,"|| plastron :",self.plastron,"|| jambières :",self.jambières,"|| bottes :",self.bottes,"||")

def Changement(pv,gold):
    if Perso.pv+pv>100:
        Perso.pv=100
    else :
        Perso.pv=Perso.pv+pv
    Perso.gold=Perso.gold-gold

class Ennemi :
    def __init__(self,type,pv,degats):
        self.type=type
        self.pv=pv
        self.degats=degats

class Evenement :
    def __init__(self):
        self.Forêt=["Coffre","Gobelin","Bandit","Repos","Rien"]
        self.Marais=["Coffre","Gobelin","Crocodile","Troll","Repos","Rien"]


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

def separation(n=5):
    for i in range (0,n):
        print("")

def Help():
    print("Pour afficher l'inventaire taper I")
    print("Pour afficher vos stats tapez S")
    print("Pour tout afficher tapez A")
    print("Pour quitter un batiment ou la ville tapez QUITTER")

def CREDITS():
    print("Merci d'avoir joué")
    print("Jeu programmé par Aurélien Arqué")
    print("Inspiré par Théophile, Romain, Tristan")

#//////////////////////////////////////////////////////////////////////////////#
##///////////////////////////Fonctions de batiments///////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#
def Auberge():
    print("Fatigué, vous optez pour un passage à l'Auberge. À peine à l'interieur, vous vous approchez du feu pour vous reposer.")
    print("")
    séjour_auberge="True"
    while séjour_auberge=="True":
        print("L'aubergiste s'approche et vous propose : ||BOIRE UN VERRE : restaure 5 PV, coût= 5 Gold||  ||RESTER PRES DU FEU : restaure 10 PV, coût= 0 Gold||  ||LOUER UNE CHAMBRE : restaure 20 PV, coût= 20 Gold||  ||LOUER UNE CHAMBRE VIP : restaure tout les PV, coût= 50 Gold||  ||QUITTER l'Auberge.")
        choix="False"
        while choix=="False":
            decision=input("")
            separation(5)
            if decision=="BOIRE UN VERRE":
                if Perso.gold>=5 :
                    Changement(5,5)
                    print("Vous commandez un verre de Grenadine.")
                    print("")
                    print("***Gain de 5 PV***")
                else :
                    print("Gold insuffisantes")
                print("")
                choix="True"

            if decision=="RESTER PRES DU FEU":
                Changement(10,0)
                print("Vous refusez gentiment et allez vous assoupir près du feu.")
                print("")
                print("***Gain de 10 PV***")
                print("")
                choix="True"

            if decision=="LOUER UNE CHAMBRE":
                if Perso.gold>=20 :
                    Changement(20,20)
                    print("Vous réservez une chambre.")
                    print("")
                    print("***Gain de 20 PV***")
                else :
                    print("Gold insuffisantes")
                print("")
                choix="True"

            if decision=="LOUER UNE CHAMBRE VIP":
                if Perso.gold>50 :
                    Changement(100,50)
                    print("Vous réservez la meilleure suite.")
                    print("")
                    print("***Restauration totale des PV***")
                else :
                    print("Gold insuffisantes")
                print("")
                choix="True"

            if decision=="QUITTER":
                choix="True"
                séjour_auberge="False"

            if decision=="HELP":
                Help()
            if decision=="A":
                Perso.affiche_all()
            if decision=="I":
                Perso.affiche_inventaire()
            if decision=="S":
                Perso.affiche_stats()


##////////////////////////////////////////////////////////////////////////////##

def Forge():
    print("Attiré par le bruit assourdissant du marteau sur l'enclume, vous vous diriger vers la Forge.")
    print("")
    séjour_forge="True"
    while séjour_forge=="True":
        print("Vous voyant approcher, le forgeron s'arrête et vous interpelle.")
        choix="False"
        while choix=="False":
            print("Il vous prospose plusieurs services : ||AMELIORER votre équipement||  ||QUITTER la forge||")
            action=input("")
            separation(5)
            if action=="AMELIORER":
                print("Il vous propose d'améliorer pour 20 gold: ||EPEE DEUX MAINS||  ||EPEE UNE MAIN||  ||ARC||  ||BOUCLIER||  ||CASQUE||  ||PLASTRON||  ||JAMBIERES||  ||BOTTES||  ||RETOUR||")
                decision="False"
                while decision=="False":
                    amelioration=input("")
                    separation(5)
                    if Perso.gold>=20:
                        if amelioration=="EPEE UNE MAIN":
                            if Perso.arme1=="Epée une main":
                                print("***Epée une main améliorée")
                                Epée_une_main.lv=Epée_une_main.lv+1
                                Epée_une_main=Arme(Epée_une_main.name,Epée_une_main.lv,Epée_une_main.degats,Epée_une_main.protection)
                            else :
                                print("Vous ne possedez pas de",amelioration)
                            decision=="True"

                        if amelioration=="EPEE DEUX MAINS":
                            if Perso.arme1=="Epée deux mains":
                                print("***Epée deux mains améliorée")
                                Epée_deux_mains.lv=Epée_deux_mains.lv+1
                                Epée_deux_mains=Arme(Epée_deux_mains.name,Epée_deux_mains.lv,Epée_deux_mains.degats,Epée_deux_mains.protection)
                            else :
                                print("Vous ne possedez pas de",amelioration)
                            decision=="True"

                        if amelioration=="ARC":
                            if Perso.arme1=="ARC":
                                print("***Arc amélioré")
                                Arc.lv=Arc.lv+1
                                Arc=Arme(Arc.name,Arc.lv,Arc.degats,Arc.protection)
                            else :
                                print("Vous ne possedez pas de",amelioration)
                            decision=="True"

                        if amelioration=="BOUCLIER":
                            if Perso.arme1=="BOUCLIER":
                                print("***Bouclier amélioré")
                                Bouclier.lv=Bouclier.lv+1
                                Bouclier=Arme(Bouclier.name,Bouclier.lv,Bouclier.degats,Bouclier.protection)
                            else :
                                print("Vous ne possedez pas de",amelioration)
                            decision=="True"

                        if amelioration=="CASQUE":
                            if Perso.arme1=="CASQUE":
                                print("***Casque amélioré")
                                Casque.lv=Casque.lv+1
                                Casque=Armure(Casque.name,Casque.lv,Casque.degats,Casque.protection)
                            else :
                                print("Vous ne possedez pas de",amelioration)
                            decision=="True"

                        if amelioration=="PLASTRON":
                            if Perso.arme1=="PLASTRON":
                                print("***Plastron amélioré")
                                Plastron.lv=Plastron.lv+1
                                Plastron=Armure(Plastron.name,Plastron.lv,Plastron.degats,Plastron.protection)
                            else :
                                print("Vous ne possedez pas de",amelioration)
                            decision=="True"

                        if amelioration=="JAMBIERES":
                            if Perso.arme1=="JAMBIERES":
                                print("***Jambières amélioré")
                                Jambières.lv=Jambières.lv+1
                                Jambières=Armure(Jambières.name,Jambières.lv,Jambières.degats,Jambières.protection)
                            else :
                                print("Vous ne possedez pas de",amelioration)
                            decision=="True"

                        if amelioration=="BOTTES":
                            if Perso.arme1=="BOTTES":
                                print("***Bottes amélioré")
                                Bottes.lv=Bottes.lv+1
                                Bottes=Armure(Bottes.name,Bottes.lv,Bottes.degats,Bottes.protection)
                            else :
                                print("Vous ne possedez pas de",amelioration)
                            decision=="True"

                        if amelioration=="RETOUR":
                            decision="True"

                        if amelioration=="HELP":
                            Help()
                        if amelioration=="A":
                            Perso.affiche_all()
                        if amelioration=="I":
                            Perso.affiche_inventaire()
                        if amelioration=="S":
                            Perso.affiche_stats()

                        print("")
                    else :
                        print("Vous n'avez pas assez de Gold")
                        print("")
                        decision="True"

            if action=="QUITTER":
                choix="TRUE"
                séjour_forge="False"

            if action=="HELP":
                Help()
            if action=="A":
                Perso.affiche_all()
            if action=="I":
                Perso.affiche_inventaire()
            if action=="S":
                Perso.affiche_stats()


##////////////////////////////////////////////////////////////////////////////##


def Boutique():
    print("L'attractivité de la vitrine de la Boutique vous pousse à l'intérieur.")
    print("")
    séjour_boutique="True"
    while séjour_boutique=="True":
        print("Le propriétaire s'avance dans votre direction et vous montre sa marchandise :  ||POTION LV1 : 10 Gold, restaure 10 PV||  ||POTION LV2 : 20 Gold restaure 20 PV||  ||POTION LV3 : 30 Gold, restaure 50 PV||  ||QUITTER||")
        choix="False"
        decision=input("")
        separation(5)
        if decision=="POTION LV1":
            if Perso.gold>=0 :
                inventaire=Perso.inventaire
                inventaire.append("Potion lv1")
                Perso.inventaire=inventaire
                print(Perso.inventaire)
                Changement(0,00)
                print("")
                print("***Potion lv1 achetée***")
            else :
                print("Vous n'avez pas assez de Gold")

        if decision=="POTION LV2":
            if Perso.gold>=20 :
                inventaire=Perso.inventaire
                inventaire.append("Potion lv2")
                Perso.inventaire=inventaire
                Changement(0,20)
                print("")
                print("***Potion lv2 achetée***")
            else :
                print("Vous n'avez pas assez de Gold")
        if decision=="POTION LV3":
            if Perso.gold>=30 :
                inventaire=Perso.inventaire
                inventaire.append("Potion lv3")
                Perso.inventaire=inventaire
                Changement(0,10)
                print("")
                print("***Potion lv3 achetée***")
            else :
                print("Vous n'avez pas assez de Gold")

        if decision=="QUITTER":
            séjour_boutique="False"

        if decision=="HELP":
            Help()
        if decision=="A":
            Perso.affiche_all()
        if decision=="I":
            Perso.affiche_inventaire()
        if decision=="S":
            Perso.affiche_stats()
        separation(5)



##////////////////////////////////////////////////////////////////////////////##

def Terrain_entrainement():
    print("Regorgeant d'énergie, vous choisissez d'aller vous entrainer.")
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


def Montagne():
    print("Vous vous dirigez vers le pied de la montagne et vous en commencez l'ascension")
    print("")


def Ville():
    print("Vous vous avancez en direction de l'Entrée principale de la ville et hélez les gardes pour qu'ils vous ouvrent.")
    print("Alors que les portes s'ouvrent vous entrez dans la ville")
    print("")
    séjour_ville="True"
    while séjour_ville=="True":
        separation(3)
        print("Vous avez le choix entre plusieurs boutique : ||FORGE||   ||BOUTIQUE||   ||AUBERGE||  ||TERRAIN D'ENTRAINEMENT||")
        print("Voulez vous entrez dans l'une de ces boutiques ou QUITTER la ville ?")
        choix="False"
        while choix=="False":
            action=(input(""))
            separation(5)
            if action=="FORGE":
                choix="True"
                Forge()
            if action=="BOUTIQUE":
                choix="True"
                Boutique()
            if action=="AUBERGE":
                choix="True"
                Auberge()
            if action=="TERRAIN D'ENTRAINEMENT":
                choix="True"
                Terrain_entrainement()
            if action=="QUITTER":
                choix="True"
                séjour_ville="False"

            if action=="HELP":
                Help()
            if action=="A":
                Perso.affiche_all()
            if action=="I":
                Perso.affiche_inventaire()
            if action=="S":
                Perso.affiche_stats()


#//////////////////////////////////////////////////////////////////////////////#
##/////////////////////////////Fonction évenement/////////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#

def evenement(event):
    action=event[randint(0,len(event)-1)]
    if action=="Coffre":
        print("Vous avez trouvé un coffre.")
    if action=="Gobelin":
        print("Un Gobelin vous attaque.")
        combat(Perso,Gobelin)
    if action=="Bandit":
        print("Un Guillaume sauvage apparait !")
        combat(Perso,Bandit)
    if action=="Crocodile":
        print("Un crocodile vous a choisi pour son dîner.")
        combat(Perso,Crocodile)
    if action=="Repos":
        print("Fatigué, vous décidier d'installerle campement.")
        print("***Gain de 10 PV***")
        Changement(10,0)
    if action=="Rien":
        print("Vous avancez sur la route en observant le paysage.")
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
    print("Vous marchez le long de la route lorsque vous appercevez à gauche un(e)",EndroitA,"et à droite un(e)",EndroitB,". Où souhaitez vous allez ?",end="  ")

    while move==0:
        deplacement=input("")
        if deplacement=="Gauche" or deplacement=="gauche" or deplacement=="g" or deplacement==EndroitA:
            move=1
            return EndroitA
        if deplacement=="Droite" or deplacement=="droite" or deplacement=="d" or deplacement==EndroitB:
            move=1
            return EndroitB
        if deplacement=="STOP" :
            return "Arrêter"
            move=1
        if deplacement=="HELP":
            Help()
        if deplacement=="A":
            Perso.affiche_all()
        if deplacement=="I":
            Perso.affiche_inventaire()
        if deplacement=="S":
            Perso.affiche_stats()


def exploration(deplacement):
    if deplacement=="FORET":
        Foret()
    elif deplacement=="DONJON":
        Donjon()
    elif deplacement=="AUBERGE":
        Auberge()
    elif deplacement=="VILLE":
        Ville()
    elif deplacement=="MARAIS":
        Marais()
    elif deplacement=="MONTAGNE":
        Montagne()



def combat(Perso,ennemi):
    nb_action=1
    fin_combat=""
    if fin_combat=="":
        while nb_action>0:
            print("Vous avez",Perso.pv,"PV")
            action=input("Que veux tu faire : ||BOIRE UNE POTION||  ||ATTAQUER||  ||FUIR||")

            if action=="BOIRE UNE POTION" :
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

            elif action=="ATTAQUER" :
                ennemi.pv=ennemi.pv-Perso.degats
                nb_action=0

            elif action=="FUIR" :
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
Lieu=["FORET","DONJON","FORET","VILLE","MARAIS","FORET","MARAIS","AUBERGE","FORET","FORET","MARAIS","MONTAGNE"]
Perso=Personnage(input("Quel est le pseudo de ton personnage ?"),100,[])
Bandit=Ennemi("Bandit Guillaume",5,2)
Crocodile=Ennemi("Crocodile",5,4)
Gobelin=Ennemi("Gobelin",10,2)
Troll=Ennemi("Troll",50,10)
Dragon=Ennemi("Dragon",200,50)
Event=Evenement()





#//////////////////////////////////////////////////////////////////////////////#
##////////////////////////////////////////////////////////////////////////////##
##//////////////////////////////Lancement du jeu//////////////////////////////##
##////////////////////////////////////////////////////////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#
Perso.affiche_global()
compris="False"
while compris=="False":
    print("Tout au long de la partie vous serz amené à faire des choix. Pour choisir, réécrivez les propositions en MAJUSCULES.")
    Help()
    as_tu_compris=input("As-tu compris ?  ||OUI||  ||NON||")
    if as_tu_compris=="OUI":
        compris="True"
print("Si besoin au cours de la partie, vous pouvez taper HELP pour réaccéder aux commandes spéciales")
separation(3)
print("Vous commencez l'aventure !!")
print("")
jeu=""
while jeu!="Arrêter":
    deplacement=action(Items,Lieu)
    jeu=deplacement
    exploration(deplacement)
CREDITS()


