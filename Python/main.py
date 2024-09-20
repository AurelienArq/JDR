# Créé par arqau, le 06/10/2022 en Python 3.7
# Modifié par arquea, le 19/09/2024 en Python 3.12
from timeit import default_timer as timer
from random import randint

from Python.Arme import Arme
from Python.Armure import Armure
from Python.Consommable import Consommable
from Python.Ennemi import Ennemi
from Python.Evenement import Evenement
from Python.Histoire import Histoire_intro
from Python.Jeu import action, exploration
from Python.Personnage import Personnage
from Python.Quete import QUETE
from Python.Sauvegarde import ouverture_sauvegarde, création_sauvegarde
from Python.Stats import stats_fin
from Python.Util import separation, Help, CREDITS

#//////////////////////////////////////////////////////////////////////////////#
##/////////////////////////////Préparation du jeu/////////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#

a=0
separation(40)
while a!=11:
    print("Chargement :","["+"|"*a+" "*(10-a)+"]")
    a=a+1
    debut=timer()
    while timer()<1+debut:
        b=0
    separation(40)

sauv = input("Avez-vous une sauvegarde ? ||OUI||  ||NON||")
if sauv == "OUI":
    nom_sauv = input("Quel est son nom") + ".txt"
    clé = ouverture_sauvegarde(nom_sauv)
    for i in range(0, len(clé)):
        if clé[i].isnumeric() == True:
            clé[i] = int(clé[i])
    print(clé)
    clé_Perso = [clé[i] for i in range(0, 33)]
    clé_Chevre = [clé[i] for i in range(33, 40)]
    clé_Crocodile = [clé[i] for i in range(40, 47)]
    clé_Bandit = [clé[i] for i in range(47, 54)]
    clé_Gobelin = [clé[i] for i in range(54, 61)]
    clé_Troll = [clé[i] for i in range(61, 68)]
    clé_Dragon = [clé[i] for i in range(68, 75)]
    clé_Nain = [clé[i] for i in range(75, 82)]
    clé_Arme_et_Armure = [clé[i] for i in range(82, len(clé))]
    print(clé_Chevre)
    print(clé_Crocodile)
    print(clé_Bandit)
    print(clé_Gobelin)
    print(clé_Troll)
    print(clé_Dragon)
    print(clé_Nain)
    print(clé_Arme_et_Armure)

# création des armes
if sauv == "OUI":
    Epée_une_main = Arme("Epée une main", 5, 0, 1, clé_Arme_et_Armure[0])
    Epée_deux_mains = Arme("Epée deux mains", 10, 0, 3, clé_Arme_et_Armure[1])
    Arc = Arme("Arc", 10, 0, 3, clé_Arme_et_Armure[2])
    Dague = Arme("Dague", 2, 0, 1, clé_Arme_et_Armure[3])
    Bouclier = Arme("Bouclier", 0, 5, 2, clé_Arme_et_Armure[4])
    Marteau = Arme("Marteau", 5, 0, 1, clé_Arme_et_Armure[5])
    Hache = Arme("Hache", 15, 0, 3, clé_Arme_et_Armure[6])

else:
    Epée_une_main = Arme("Epée une main", 5, 0, 1)
    Epée_deux_mains = Arme("Epée deux mains", 10, 0, 3)
    Arc = Arme("Arc", 10, 0, 3)
    Bouclier = Arme("Bouclier", 0, 5, 2)
    Dague = Arme("Dague", 2, 0, 1)
    Marteau = Arme("Marteau", 15, 0, 3, 1)
    Hache = Arme("Hache", 15, 0, 3, 1)

# création des consommables
Potion_lv1 = Consommable("Potion lv1", 10)
Potion_lv2 = Consommable("Potion lv2", 25)
Potion_lv3 = Consommable("Potion lv3", 50)
Viande = Consommable("Viande", 15)

# création des armures
if sauv == "OUI":
    Casque = Armure("Casque", 2, clé_Arme_et_Armure[5])
    Plastron = Armure("Plastron", 4, clé_Arme_et_Armure[6])
    Jambières = Armure("Jambières", 2, clé_Arme_et_Armure[7])
    Bottes = Armure("Bottes", 1, clé_Arme_et_Armure[8])
else:
    Casque = Armure("Casque", 2)
    Plastron = Armure("Plastron", 4)
    Jambières = Armure("Jambières", 2)
    Bottes = Armure("Bottes", 1)

# création des quêtes
Quête_Bandit = QUETE("Bandits", 5, "Tuer", 20)
Quête_Gobelin = QUETE("Gobelins", 3, "Tuer", 30)
Quête_Troll = QUETE("Trolls", 2, "Tuer", 40)
Quête_visite_ville = QUETE(["Forge", "Terrain d'entrainement", "Boutique", "Auberge"], 0, "Visiter", 40)

Items = [[Epée_une_main, Epée_deux_mains, Arc, Bouclier, Dague], [Potion_lv1, Potion_lv2, Potion_lv3]]
Lieu = ["FORET (difficulté Debutant)", "DONJON (difficulté Moyenne)", "FORET (difficulté Debutant)", "VILLE",
        "MARAIS (difficulté Facile)", "FORET (difficulté Debutant)", "MARAIS (difficulté Facile)", "AUBERGE",
        "FORET (difficulté Debutant)", "FORET (difficulté Debutant)", "MARAIS (difficulté Facile)",
        "MONTAGNE (difficulté Maximale)"]
if sauv == "OUI":
    inventaire = []
    for i in clé_Perso[2]:
        if i == "d":
            inventaire.append("Viande")
        if i == "1":
            inventaire.append("Potion lv1")
        if i == "2":
            inventaire.append("Potion lv2")
        if i == "3":
            inventaire.append("Potion lv3")
    Perso = Personnage(clé_Perso[0], clé_Perso[1], inventaire, clé_Perso[3], clé_Perso[4], clé_Perso[5],
                       clé_Perso[6], clé_Perso[7], clé_Perso[8], clé_Perso[9], clé_Perso[10], clé_Perso[11],
                       clé_Perso[12], clé_Perso[13], clé_Perso[14], clé_Perso[15], clé_Perso[16], clé_Perso[17],
                       clé_Perso[18], clé_Perso[19], clé_Perso[20], clé_Perso[21], clé_Perso[22], clé_Perso[23],
                       clé_Perso[24], clé_Perso[25], clé_Perso[26], clé_Perso[27], clé_Perso[28], clé_Perso[29],
                       clé_Perso[30], clé_Perso[31])

    Chevre = Ennemi(clé_Chevre[0], clé_Chevre[1], clé_Chevre[2], [Viande, "Rien", "Rien", "Rien", "Rien"],
                    clé_Chevre[3], clé_Chevre[4], clé_Chevre[5], clé_Chevre[6])
    Gobelin = Ennemi(clé_Gobelin[0], clé_Gobelin[1], clé_Gobelin[2],
                     ["Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien",
                      "Rien", Epée_une_main, Epée_une_main, Dague, Dague, Dague, Dague, Dague, Dague, Dague, Dague,
                      Casque], clé_Gobelin[3], clé_Gobelin[4], clé_Gobelin[5], clé_Gobelin[6])
    Bandit = Ennemi(clé_Bandit[0], clé_Bandit[1], clé_Bandit[2],
                    ["Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien",
                     "Rien", "Rien", "Rien", "Rien", Arc, Arc, Arc, Arc, Potion_lv1, Potion_lv1, Potion_lv1,
                     Potion_lv1, Potion_lv2, Epée_une_main, Epée_une_main, Epée_une_main, Epée_une_main, Bottes,
                     Jambières], clé_Bandit[3], clé_Bandit[4], clé_Bandit[5], clé_Bandit[6])
    Crocodile = Ennemi(clé_Crocodile[0], clé_Crocodile[1], clé_Crocodile[2], ["Rien", Viande, Viande, Viande],
                       clé_Crocodile[3], clé_Crocodile[4], clé_Crocodile[5], clé_Crocodile[6])
    Troll = Ennemi(clé_Troll[0], clé_Troll[1], clé_Troll[2],
                   [Epée_deux_mains, Epée_deux_mains, Epée_deux_mains, Epée_une_main, Plastron, Casque, "Rien",
                    "Rien", "Rien", "Rien"], clé_Troll[3], clé_Troll[4], clé_Troll[5], clé_Troll[6])
    Dragon = Ennemi(clé_Dragon[0], clé_Dragon[1], clé_Dragon[2],
                    [Epée_une_main, Epée_deux_mains, Bouclier, Plastron], clé_Dragon[3], clé_Dragon[4],
                    clé_Dragon[5], clé_Dragon[6])
    Nain = Ennemi(clé_Nain[0], clé_Nain[1], clé_Nain[2], [Marteau, Marteau, Hache, Hache], clé_Nain[3], clé_Nain[4],
                  clé_Nain[5], clé_Nain[6])

else:
    Perso = Personnage(input("Quel est le pseudo de ton personnage ?"), 100, [])
    Chevre = Ennemi("Chèvre", 10, 2, [Viande, "Rien", "Rien", "Rien", "Rien"], 5)
    Gobelin = Ennemi("Gobelin", 15, 2,
                     ["Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien",
                      "Rien", Epée_une_main, Epée_une_main, Dague, Dague, Dague, Dague, Dague, Dague, Dague, Dague,
                      Casque], 30, 1, 3)
    Bandit = Ennemi("Bandit", 10, 2,
                    ["Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien", "Rien",
                     "Rien", "Rien", "Rien", "Rien", Arc, Arc, Arc, Arc, Potion_lv1, Potion_lv1, Potion_lv1,
                     Potion_lv1, Potion_lv2, Epée_une_main, Epée_une_main, Epée_une_main, Epée_une_main, Bottes,
                     Jambières], 15, 1, 3)
    Crocodile = Ennemi("Crocodile", 10, 4, ["Rien", Viande, Viande, Viande], 20)
    Troll = Ennemi("Troll", 70, 10,
                   [Epée_deux_mains, Epée_deux_mains, Epée_deux_mains, Epée_une_main, Plastron, Casque, "Rien",
                    "Rien", "Rien", "Rien"], 50, 5, 15)
    Nain = Ennemi("Nain Guillaume", 80, 10, [Marteau, Marteau, Hache, Hache, ], 70, 10, 20)
    Dragon = Ennemi("Dragon", 200, 50, [Epée_une_main, Epée_deux_mains, Bouclier, Plastron], 500, 50, 200)
Event = Evenement()






#//////////////////////////////////////////////////////////////////////////////#
##////////////////////////////////////////////////////////////////////////////##
##//////////////////////////////Lancement du jeu//////////////////////////////##
##////////////////////////////////////////////////////////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#
Perso.affiche_global()
if sauv!="OUI":
    print("")
    compris="False"
    while compris=="False":
        print("Tout au long de la partie vous serez amené à faire des choix. Pour choisir, réécrivez les propositions qui sont en MAJUSCULES.")
        print("Pour choisir les lieux tapez GAUCHE ou G et DROITE ou D")
        Help()
        as_tu_compris=input("As-tu compris ?  ||OUI||  ||NON||")
        if as_tu_compris=="OUI":
            compris="True"
            print("")
    print("---Si besoin au cours de la partie, vous pouvez taper HELP pour accéder aux commandes spéciales---")
    print(" ")
    print("▬"*100)
    print(" ")
    Histoire_intro()
    print("Êtes-vous prêt ?  ||OUI||   ||NON||",end="")
    reponse="False"
    while reponse=="False":
        choix=input("")
        if choix=="OUI":
            reponse="True"
print("VOUS COMMENCEZ L'AVENTURE !!!")
print("")
jeu=""
while Perso.Etat!="Mort" and Perso.Etat!="Arrêt":
    deplacement=action(Items,Lieu)
    jeu=deplacement
    if deplacement!="PASSE": ## if pour les tests à supprimer à la fin
        if deplacement!="Arrêter":
            jeu=exploration(deplacement)

stats_fin()
CREDITS()
création_sauvegarde()




