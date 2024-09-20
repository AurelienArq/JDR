from ...Util import *
from ...main import *
from ...Quete import *
from ...main import Perso


def Forge():
    print("Attiré par le bruit assourdissant du marteau sur l'enclume, vous vous dirigez vers la Forge.")
    print("")
    test_sejour_lieux("Forge")
    séjour_forge="True"
    while séjour_forge=="True":
        print("Vous voyant approcher, le forgeron s'arrête et vous interpelle.")
        choix="False"
        while choix=="False":
            print("Il vous propose plusieurs services : ||AMELIORER votre équipement||  ||QUITTER la forge||")
            action=input("")
            separation(2)
            print("▬"*100)
            separation(2)
            if action=="AMELIORER":
                choix="True"
                print("Il vous propose d'améliorer pour 20 golds X le niveau de votre arme/armure: ||DAGUE||  ||EPEE UNE MAIN||  ||MARTEAU||  ||BOUCLIER||  ||CASQUE||  ||PLASTRON||  ||JAMBIERES||  ||BOTTES|| et pour 40 golds X le niveau de votre arme/armure :  ||EPEE DEUX MAINS||  ||HACHE||  ||ARC||  ||RETOUR||")
                decision="False"
                while decision=="False":
                    amelioration=input("")
                    separation(2)
                    print("▬"*100)
                    separation(2)
                    if amelioration=="EPEE UNE MAIN":
                        if Perso.gold>=(20*Epée_une_main.lv):
                            Perso.gold=Perso.gold-(20*Epée_une_main.lv)
                            print("***Dépense de",20*Epée_une_main.lv,"Gold***")
                            amelioration_arme(Epée_une_main)
                            decision="True"
                        else :
                            decision="Pas assez de gold"

                    if amelioration=="EPEE DEUX MAINS":
                        if Perso.gold>=(40*Epée_deux_mains.lv):
                            Perso.gold=Perso.gold-(40*Epée_deux_mains.lv)
                            print("***Dépense de",40*Epée_deux_mains.lv,"Gold***")
                            amelioration_arme(Epée_deux_mains)
                            decision="True"
                        else :
                            decision="Pas assez de gold"

                    if amelioration=="HACHE":
                        if Perso.gold>=(40*Hache.lv):
                            Perso.gold=Perso.gold-(40*Hache.lv)
                            print("***Dépense de",40*Hache.lv,"Gold***")
                            amelioration_arme(Hache)
                            decision="True"
                        else :
                            decision="Pas assez de gold"

                    if amelioration=="ARC":
                        if Perso.gold>=(40*Arc.lv):
                            Perso.gold=Perso.gold-(40*Arc.lv)
                            print("***Dépense de",40*Arc.lv,"Gold***")
                            amelioration_arme(Arc)
                            decision="True"
                        else :
                            decision="Pas assez de gold"

                    if amelioration=="MARTEAU":
                        if Perso.gold>=(20*Marteau.lv):
                            Perso.gold=Perso.gold-(20*Marteau.lv)
                            print("***Dépense de",20*Marteau.lv,"Gold***")
                            amelioration_arme(Marteau)
                            decision="True"
                        else :
                            decision="Pas assez de gold"

                    if amelioration=="BOUCLIER":
                        if Perso.gold>=(20*Bouclier.lv):
                            Perso.gold=Perso.gold-(20*Bouclier.lv)
                            print("***Dépense de",20*Bouclier.lv,"Gold***")
                            amelioration_arme(Bouclier)
                            decision="True"
                        else :
                            decision="Pas assez de gold"

                    if amelioration=="DAGUE":
                        if Perso.gold>=(20*Dague.lv):
                            Perso.gold=Perso.gold-(20*Dague.lv)
                            print("***Dépense de",20*Dague.lv,"Gold***")
                            amelioration_arme(Dague)
                            decision="True"
                        else :
                            decision="Pas assez de gold"

                    if amelioration=="CASQUE":
                        if Perso.gold>=(20*Casque.lv):
                            Perso.gold=Perso.gold-(20*Casque.lv)
                            print("***Dépense de",20*Casque.lv,"Gold***")
                            amelioration_armure(Casque)
                            decision="True"
                        else :
                            decision="Pas assez de gold"

                    if amelioration=="PLASTRON":
                        if Perso.gold>=(20*Plastron.lv):
                            Perso.gold=Perso.gold-(20*Plastron.lv)
                            print("***Dépense de",20*Plastron.lv,"Gold***")
                            amelioration_armure(Plastron)
                            decision="True"
                        else :
                            decision="Pas assez de gold"

                    if amelioration=="JAMBIERES":
                        if Perso.gold>=(20*Jambières.lv):
                            Perso.gold=Perso.gold-(20*Jambières.lv)
                            print("***Dépense de",20*Jambières.lv,"Gold***")
                            amelioration_armure(Jambières)
                            decision="True"
                        else :
                            decision="Pas assez de gold"

                    if amelioration=="BOTTES":
                        if Perso.gold>=(20*Bottes.lv):
                            Perso.gold=Perso.gold-(20*Bottes.lv)
                            print("***Dépense de",20*Bottes.lv,"Gold***")
                            amelioration_armure(Bottes)
                            decision="True"
                        else :
                            decision="Pas assez de gold"

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
                    if amelioration=="K":
                        Perso.affiche_kills()

                    print("")
                    if decision=="Pas assez de gold":
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
            if action=="K":
                Perso.affiche_kills()
