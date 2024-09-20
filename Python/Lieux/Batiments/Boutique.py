from Python.Quete import test_sejour_lieux
from Python.Util import separation, Changement, Help
from Python.main import Perso


def Boutique():
    print("L'attractivité de la vitrine de la Boutique vous pousse à l'intérieur.")
    print("")
    test_sejour_lieux("Boutique")
    séjour_boutique="True"
    while séjour_boutique=="True":
        print("Le propriétaire s'avance dans votre direction et vous montre sa marchandise :  ||POTION LV1 : 10 Gold, restaure 10 PV||  ||POTION LV2 : 20 Gold restaure 20 PV||  ||POTION LV3 : 30 Gold, restaure 50 PV||  ||QUITTER||")
        choix="False"
        decision=input("")
        separation(2)
        print("▬"*100)
        separation(2)
        if decision=="POTION LV1":
            if Perso.gold>=10 : ##pour les tests remettre Perso.gold>=0
                inventaire=Perso.inventaire
                inventaire.append("Potion lv1")
                Perso.inventaire=inventaire
                print(Perso.inventaire)
                Changement(0,00) ##pour les test remettre à 10 gold
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
        if decision=="K":
                Perso.affiche_kills()
        separation(2)
        print("▬"*100)
        separation(2)
