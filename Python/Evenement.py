from random import randint

from Python.Combat import combat
from Python.Gestion_Inventaire import gain_inventaire_arme, gain_inventaire_consommable, gain_inventaire_armure
from Python.Util import Changement
from Python.main import Perso, Epée_une_main, Dague, Epée_deux_mains, Potion_lv1, Potion_lv2, Potion_lv3, Bouclier, \
    Gobelin, Bandit, Crocodile, Chevre, Dragon, Troll, Nain, Event


class Evenement :
    def __init__(self):
        self.Forêt=["Coffre","Bandit","Gobelin","Gobelin","Bandit","Gobelin","Bandit","Repos","Bandit","Bandit","Gobelin","Gobelin","Bandit","Gobelin","Bandit","Repos","Bandit","Bandit","Gobelin","Gobelin","Bandit","Gobelin","Bandit","Repos","Bandit"]
        self.Marais=["Coffre","Crocodile","Gobelin","Crocodile","Gobelin","Gobelin","Crocodile","Gobelin","Repos","Crocodile","Gobelin","Crocodile","Gobelin","Gobelin","Crocodile","Gobelin","Repos"]
        self.Donjon=["Bandit","Troll","Coffre","Troll","Troll","Bandit","Bandit","Bandit"]
        self.Montagne=["Dragon","Chèvre","Troll","Troll","Nain","Coffre","Repos","Nain","Bandit","Bandit","Coffre2","Nain","Troll"]

        self.coffre=[Epée_une_main,Epée_une_main,Dague,Epée_deux_mains,Potion_lv1,Potion_lv2,Potion_lv3,Bouclier]

def evenement(event,temps2=0):
    action=event[randint(0,len(event)-1)]
    print(" ")
    print("▬"*100)
    print(" ")
    if action=="Coffre":
        print("Vous avez trouvé un coffre.")
        coffre()
    if action=="Coffre2":
        print("Vous avez trouvé deux coffres.")
        print("Vous vous approchez du premier")
        coffre()
        print("Vous allez maintenant vers le deuxième")
        coffre()

    if action=="Gobelin":
        print("Un Gobelin vous attaque.")
        temps2=combat(Perso,Gobelin,temps2)
    if action=="Bandit":
        print("Vous tombez dans une embuscade tendu pas un bandit !")
        temps2=combat(Perso,Bandit,temps2)
    if action=="Crocodile":
        print("Un crocodile vous a choisi pour son prochain dîner.")
        temps2=combat(Perso,Crocodile,temps2)
    if action=="Chèvre":
        print("Une chèvre vous a pris pour cible.")
        temps2=combat(Perso,Chevre,temps2)
    if action=="Dragon":
        print("Vous avez reveillé un dragon.")
        temps2=combat(Perso,Dragon,temps2)
    if action=="Troll":
        print("Un troll vous a pris pour cible.")
        temps2=combat(Perso,Troll,temps2)
    if action=="Nain":
        print("Vous tombez sur le nain Guillaume entrain de miner.")
        temps2=combat(Perso,Nain,temps2)

    if action=="Repos":
        print("Vous avancez sur la route en observant le paysage. Vous tombez sur un magnifique emplacement. Voulez-vous vous y arrêter pour vous reposer ?  ||OUI||   ||NON||")
        reponse="False"
        while reponse=="False":
            choix=input("")
            if choix=="OUI":
                print("Fatigué, vous décidez d'installer le campement.")
                print("***Gain de 10 PV***")
                Changement(10,0)
                reponse="True"
            if choix=="NON":
                print("Vous regorgez d'énergie et décidez de continuer votre route.")
                reponse="True"
    print("")
    return temps2

def coffre():
    butin=Event.coffre[randint(0,len(Event.coffre)-1)]
    butin_gold=randint(5,20)
    print("En ouvrant le coffre vous trouvez",butin_gold,"Gold")
    print("***Gain de",butin_gold,"Gold***")
    Perso.gold=Perso.gold+butin_gold
    Perso.gold_total=Perso.gold_total+butin_gold
    print("Vous trouvez également",butin.name)
    print("Voulez-vous le récupérer ? ||OUI||   ||NON||")
    reponse="False"
    while reponse=="False":
        choix=input("")
        if choix=="OUI":
            if butin.type=="Arme":
                gain_inventaire_arme(butin)
            if butin.type=="Consommable":
                gain_inventaire_consommable(butin)
            if butin.type=="Armure":
                gain_inventaire_armure(butin)
            reponse="True"
        else :
            print("Vous laissez",butin.name)
            reponse="True"
    print("")
