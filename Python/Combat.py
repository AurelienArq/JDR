from random import randint

from Python.Gestion_Exp_et_Lv import augmentation_exp
from Python.Gestion_Inventaire import utilisation, gain_inventaire_consommable, gain_inventaire_arme, \
    gain_inventaire_armure
from Python.Histoire import combat_final
from Python.Stats import stats_kill
from Python.Util import dé, Help
from Python.main import Potion_lv1, Viande, Potion_lv2, Potion_lv3, Perso, Bandit, Chevre, Crocodile, Gobelin, Troll, \
    Dragon, Nain


def combat(Perso,ennemi,temps2):
    nb_action=1
    fin_combat=""
    while fin_combat=="":
        nb_action=1
        while nb_action>0:
            print("Vous avez",Perso.pv,"PV")
            print(ennemi.type,"a",ennemi.pv,"PV")
            print("Que veux tu faire : ||UTILISER UN CONSOMMABLE||  ||ATTAQUER||  ||FUIR||")
            action=input("")
            print("")
            if action=="UTILISER UN CONSOMMABLE" :
                if Perso.inventaire!=[]:
                    print("Lequel veut-tu utiliser : ||VIANDE||  ||POTION LV1||  ||POTION LV2||  ||POTION LV3||")
                    reponse="False"
                    while reponse=="False":
                        choix=input("")
                        if choix=="VIANDE" or choix=="POTION LV1" or choix=="POTION LV2" or choix=="POTION LV3" :
                            if choix=="VIANDE":
                                choix="Viande"

                            if choix=="POTION LV1":
                                choix="Potion lv1"

                            if choix=="POTION LV2":
                                choix="Potion lv2"

                            if choix=="POTION LV3":
                                choix="Potion lv3"

                            reponse="True"
                            use="NO"
                            for i in Perso.inventaire:
                                print(i)   #utilisation de potion si le joueur en possède
                                if i==choix:
                                    use="OK"
                            if use=="OK":
                                if choix=="Viande":
                                    utilisation(Viande)
                                if choix=="Potion lv1":
                                    utilisation(Potion_lv1)
                                if choix=="Potion lv2":
                                    utilisation(Potion_lv2)
                                if choix=="Potion lv3":
                                    utilisation(Potion_lv3)
                            else :
                                print("Vous ne possedez pas ce consommable.")
                    nb_action=0
                else :
                    print("Vous n'avez pas de consommables.")

            if action=="ATTAQUER" :
                if dé()>3:
                    print("Vous attaquez",ennemi.type,end="")
                    perte_pv(Perso,ennemi)
                    nb_action=0
                else :
                    print("Vous l'avez manqué.")
                    nb_action=0

            if action=="FUIR" :
                print(ennemi.type)
                if ennemi.type=="Nain Guillaume":
                    print("'Nous les nains, nous sommes des sprinteurs, redoutables sur de courtes distances.' Vous ne pouvez pas fuir")
                else :
                    chance_de_fuite=randint(1,2)
                    if chance_de_fuite==1:
                        print("Vous avez réussi à fuir")
                        fin_combat="Fuite"
                        nb_action=0
                    else :
                        print("Vous n'avez pas réussi à fuir")
                        nb_action=0
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

        print("")
        if ennemi.pv>0:
            if dé()>6:
                print(ennemi.type,"vous attaque.",end="")
                perte_pv(ennemi,Perso,Perso.protection)
            else :
                print(ennemi.type,"vous a manqué.")
        else :
            fin_combat="Victoire"

        if Perso.pv<=0 :
            fin_combat="Mort"
            Perso.pv=20
        print(" ")
        print("▬"*100)
        print(" ")
    if fin_combat=="Fuite":
        print("Vous avez réussi à fuir.")

    if fin_combat=="Victoire":
        print("Vous avez vaincu le",ennemi.type)
        loot(ennemi)
        boss_final=stats_kill(ennemi)
        print("Tuer",ennemi.type,"vous a rapporté",ennemi.exp,"exp",end="  ")
        print("***Gain de",ennemi.exp,"exp***")
        augmentation_exp(ennemi.exp)
        if boss_final=="True":
            print("Ca y est, vous avez enfin trouvé une carte menant à Balarion. Vous quittez donc cette endroit et commencez le voyage vers son antre.")
            inventaire=Perso.inventaire
            inventaire.append("Carte vers l'antre de Balarion")
            Perso.inventaire=inventaire
            Perso.Etat="Arrêt"
            temps2=100
            print("")
            combat_final()


    if fin_combat=="Mort":
        print("|**|**|**| VOUS ÊTES MORT |**|**|**|")
        Perso.Etat="Mort"
        temps2=100
        print("")

    print("")
    print(" ")
    print("▬"*100)
    print(" ")
    restauration_ennemi()
    return temps2

def perte_pv(attaquant,defenseur,protection=0):
    degats=attaquant.degats-protection
    if degats<0:
        degats=0
    defenseur.pv=defenseur.pv-degats
    print("***Fait perdre",degats,"PV***")

def loot(ennemi):
    if ennemi.gold_lachées>0:
        print("En fouillant le",ennemi.type,"vous trouvez",ennemi.gold_lachées,"Gold.")
        print("***Gain de",ennemi.gold_lachées,"Gold***")
        Perso.gold=Perso.gold+ennemi.gold_lachées
        Perso.gold_total=Perso.gold_total+ennemi.gold_lachées
    if ennemi.loot!=[]:
        equip_laché=ennemi.loot[randint(0,len(ennemi.loot)-1)]
        if equip_laché=="Rien":
            print("Vous ne trouvez rien d'intéressant sur son cadavre.")
        else :
            print("En fouillant son cadavre vous trouvez :  ||",equip_laché.name,"||")
            print("Voulez vous le récupérer ?  ||OUI||   ||NON||")
            reponse="False"
            while reponse=="False":
                choix=input("")
                if choix=="OUI":
                    if equip_laché.type=="Consommable":
                        gain_inventaire_consommable(equip_laché)
                    if equip_laché.type=="Arme":
                        gain_inventaire_arme(equip_laché)
                    if equip_laché.type=="Armure":
                        gain_inventaire_armure(equip_laché)
                    reponse="True"
                elif choix=="NON":
                    print("Vous laissez",equip_laché.name)
                    reponse="True"
    print("||Inventaire :",Perso.inventaire,"|| Gold :",Perso.gold,"||")

def restauration_ennemi():
    Bandit.pv=Bandit.pv_a_restituer
    Chevre.pv=Chevre.pv_a_restituer
    Crocodile.pv=Crocodile.pv_a_restituer
    Gobelin.pv=Gobelin.pv_a_restituer
    Troll.pv=Troll.pv_a_restituer
    Dragon.pv=Dragon.pv_a_restituer
    Nain.pv=Nain.pv_a_restituer
