from Python.main import Perso


def utilisation(Item):
    print("Vous avez utilisé une",Item.name)
    print("***Gain de",Item.soin,"PV***")
    Perso.pv=Perso.pv+Item.soin
    if Perso.pv>Perso.pv_max:
        Perso.pv=Perso.pv_max
    perte_inventaire(Item)

def perte_inventaire(item_perdu):
    inventaire=Perso.inventaire
    perte="False"
    i=0
    while perte=="False":
        if inventaire[i]==item_perdu.name:
            Perso.inventaire=inventaire[:i]+inventaire[i+1 :]
            perte="True"
        i=i+1

def gain_inventaire_consommable(loot):
    inventaire=Perso.inventaire
    inventaire.append(loot.name)
    Perso.inventaire=inventaire
    print("***",loot.name,"récupéré(e) **")

def gain_inventaire_arme(arme):
    if arme.emplacement==1:
        if Perso.arme1=="none":
            print("***",arme.name,"équipée ***")
            Perso.arme1=arme.name
            Perso.degats=Perso.degats+arme.degats
            Perso.protection=Perso.protection+arme.protection
            Perso.arme1_degats=arme.degats
            Perso.arme1_protection=arme.protection
        else :
            print("Vous avez déjà une arme équipée :",Perso.arme1)
            print("Voulez vous la remplacer ?  ||OUI (cela entrainera la perte définitive de l'arme équipée)||   ||NON (cela entrainera la perte définitive de l'arme lootée)||")
            reponse="False"
            while reponse=="False":
                choix=input("")
                if choix=="OUI":
                    Perso.degats=Perso.degats-Perso.arme1_degats+arme.degats
                    Perso.protection=Perso.protection-Perso.arme1_protection+arme.protection
                    Perso.arme1_degats=arme.degats
                    Perso.arme1_protection=arme.protection
                    Perso.arme1=arme.name
                    print("***",arme.name,"équipée ***")
                    reponse="True"
                elif choix=="NON":
                    print("Vous avez abandonné,",arme.name)
                    reponse="True"
    if arme.emplacement==2:
        if Perso.arme2=="none":
            print("***",arme.name,"équipée ***")
            Perso.arme2=arme.name
            Perso.degats=Perso.degats+arme.degats
            Perso.protection=Perso.protection+arme.protection
            Perso.arme2_degats=arme.degats
            Perso.arme2_protection=arme.protection
        else :
            if Perso.arme1=="Epée deux mains" or Perso.arme1=="Arc":
                print("Vous avez une arme à deux emplacements :",Perso.arme1)
                arme_double="True"
            else :
                print("Vous avez déjà une arme équipée :",Perso.arme2)
                arme_double="False"
            print("Voulez vous la remplacer ?  ||OUI (cela entrainera la perte définitive de l'arme équipée)||   ||NON (cela entrainera la perte définitive de l'arme lootée)||")
            reponse="False"
            while reponse=="False":
                choix=input("")
                if choix=="OUI":
                    if arme_double=="True":
                        Perso.degats=Perso.degats-Perso.arme1_degats+arme.degats
                        Perso.protection=Perso.protection-Perso.arme1_protection+arme.protection
                        Perso.arme1="none"
                        Perso.arme1_degats=0
                        Perso.arme1_protection=0
                    else :
                        Perso.degats=Perso.degats-Perso.arme2_degats+arme.degats
                        Perso.protection=Perso.protection-Perso.arme2_protection+arme.protection
                    Perso.arme2_degats=arme.degats
                    Perso.arme2_protection=arme.protection
                    Perso.arme2=arme.name
                    print("***",arme.name,"équipée ***")
                    reponse="True"
                elif choix=="NON":
                    print("Vous avez abandonné,",arme.name)
                    reponse="True"
    if arme.emplacement==3:
        if Perso.arme1=="none" and Perso.arme2=="none":
            print("***",arme.name,"équipée ***")
            Perso.arme1=arme.name
            Perso.degats=Perso.degats+arme.degats
            Perso.protection=Perso.protection+arme.protection
            Perso.arme1_degats=arme.degats
            Perso.arme1_protection=arme.protection
        else :
            print("Vous avez des armes équipées : arme1:",Perso.arme1,"  arme2 :",Perso.arme2)
            print("Cette arme est une arme à deux mains, si vous l'équipez vous perdrez toutes les armes équipées")
            print("Voulez vous la remplacer ?  ||OUI (cela entrainera la perte définitive des armes équipées)||   ||NON (cela entrainera la perte définitive de l'arme lootée)||")
            reponse="False"
            while reponse=="False":
                choix=input("")
                if choix=="OUI":
                    if Perso.arme1!="none":
                        Perso.degats=Perso.degats-Perso.arme1_degats
                        Perso.protection=Perso.protection-Perso.arme1_protection
                    if Perso.arme2!="none":
                        Perso.degats=Perso.degats-Perso.arme2_degats
                        Perso.protection=Perso.protection-Perso.arme2_protection
                    Perso.degats=Perso.degats+arme.degats
                    Perso.protection=Perso.protection+arme.protection
                    Perso.arme1_degats=arme.degats
                    Perso.arme1_protection=arme.protection
                    Perso.arme2_degats=0
                    Perso.arme2_protection=0
                    Perso.arme1=arme.name
                    Perso.arme2="none"
                    print("***",arme.name,"équipée ***")
                    reponse="True"
                elif choix=="NON":
                    print("Vous avez abandonné,",arme.name)
                    reponse="True"

    Perso.affiche_armes()

def gain_inventaire_armure(armure):
    if armure.name=="Casque":
        emplacement=Perso.casque
    if armure.name=="Plastron":
        emplacement=Perso.plastron
    if armure.name=="Jambières":
        emplacement=Perso.jambières
    if armure.name=="Bottes":
        emplacement=Perso.bottes

    if armure.name=="Casque" or armure.name=="Plastron" or armure.name=="Jambières" or armure.name=="Bottes":
        print("***",armure.name,"équipée ***")
        if armure.name=="Casque":
            Perso.casque=armure.name
            Perso.casque_protection=armure.protection
        if armure.name=="Plastron":
            Perso.plastron=armure.name
            Perso.plastron_protection=armure.protection
        if armure.name=="Jambières":
            Perso.jambières=armure.name
            Perso.jambières_protection=armure.protection
        if armure.name=="Bottes":
            Perso.bottes=armure.name
            Perso.bottes_protection=armure.protection
        Perso.protection=Perso.protection+armure.protection
    else :
        print("Vous avez déjà une armure équipée :",emplacement)
        print("Vous laissez donc",armure.name)
    Perso.affiche_armures

def amelioration_arme(arme):
    if Perso.arme1==arme.name:
        print("***",arme.name,"amélioré(e) ***")
        arme.__init__(arme.name,int(arme.degats)/arme.lv,int(arme.protection)/arme.lv,arme.emplacement,(arme.lv)+1)
        Perso.degats=int(Perso.degats-Perso.arme1_degats+arme.degats)
        Perso.protection=int(Perso.protection-Perso.arme1_protection+arme.protection)
        Perso.arme1_degats=int(arme.degats)
        Perso.arme1_protection=int(arme.protection)
    else :
        print("Vous ne possedez pas de",arme.name)

def amelioration_armure(armure):
    if Perso.casque==armure.name or Perso.plastron==armure.name or Perso.jambières==armure.name or Perso.bottes==armure.name:
        print("***",armure.name,"amélioré ***")
        Perso.protection=Perso.protection-armure.protection
        armure.__init__(armure.name,(armure.protection)/armure.lv,armure.lv+1)
        if armure.name=="Casque":
            Perso.casque_protection=int(armure.protection)
        if armure.name=="Plastron":
            Perso.plastron_protection=int(armure.protection)
        if armure.name=="Jambières":
            Perso.jambières_protection=int(armure.protection)
        if armure.name=="Bottes":
            Perso.bottes_protection=int(armure.protection)
        Perso.protection=int(Perso.protection+armure.protection)
    else :
        print("Vous ne possedez pas de",armure.name)
