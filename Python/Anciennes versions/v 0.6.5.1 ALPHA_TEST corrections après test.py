# Créé par arqau, le 06/10/2022 en Python 3.7
# Créé par Elève, le 30/09/2022 en Python 3.7
from random import randint

#//////////////////////////////////////////////////////////////////////////////#
##//////////////Fonctions de génération du perso, PNJ et ennemis//////////////##
#//////////////////////////////////////////////////////////////////////////////#

class Personnage :
    def __init__ (self,nom,pv,inventaire,pv_max=100,niv=1,exp=0,degats=2,protection=0,arme1="none",arme2="none",casque="chapeau de paille",plastron="chemise",jambières="pantalon",bottes="Souliers en cuir",argent=0,arme1_degats=0,arme1_protection=0,arme2_degats=0,arme2_protection=0,casque_protection=0,plastron_protection=0,jambières_protection=0,bottes_protection=0,kill_Chevres=0,kill_Crocodiles=0,kill_Bandits=0,kill_Gobelins=0,kill_Trolls=0,kill_Dragons=0,Etat="Debut"):
        self.name=nom
        self.Etat=Etat
        self.pv=pv+10000
        self.pv_max=pv_max+10000
        self.inventaire=inventaire
        self.degats=degats+10000
        self.degats_base=degats+1000
        self.protection=protection
        self.gold=argent+500
        self.lv=niv
        self.exp=exp
        self.lieux_vsitiés=[]

        self.arme1=arme1
        self.arme2=arme2
        self.arme1_degats=arme1_degats
        self.arme1_protection=arme1_protection
        self.arme2_degats=arme2_degats
        self.arme2_protection=arme2_protection

        self.casque=casque
        self.plastron=plastron
        self.jambières=jambières
        self.bottes=bottes
        self.casque_protection=casque_protection
        self.plastron_protection=plastron_protection
        self.jambières_protection=jambières_protection
        self.bottes_protection=bottes_protection

        self.kill_Chevre=kill_Chevres
        self.kill_Crocodile=kill_Crocodiles
        self.kill_Bandit=kill_Bandits
        self.kill_Gobelin=kill_Gobelins
        self.kill_Troll=kill_Trolls
        self.kill_Dragon=kill_Dragons #mettre +15 pour tester la fin du jeu

    def affiche_all(self):
        print("||",self.name,"||",self.pv,"PV || Lv :",self.lv,"|| Exp :",self.exp,"|| gold :",self.gold,"|| inventaire :",self.inventaire,"|| arme1 :",self.arme1,"|| arme2 :", self.arme2,"|| casque :",self.casque,"|| plastron :",self.plastron,"|| jambières :",self.jambières,"|| bottes :",self.bottes,"||")

    def affiche_global(self):
        print("||",self.name,"||",self.pv,"PV || inventaire :",self.inventaire,"|| arme1 :",self.arme1,"|| arme2 :", self.arme2,"|| gold :",self.gold,"||")

    def affiche_stats(self):
        print("||",self.name,"||",self.pv,"PV || Lv :",self.lv,"|| dégats :",self.degats,"|| protection :",self.protection,"||")

    def affiche_kills(self):
        print("//KILLS//")
        print("Chèvres :",self.kill_Chevre,end=" || ")
        print("Crocodiles :",self.kill_Crocodile,end=" || ")
        print("Bandits :",self.kill_Bandit,end=" || ")
        print("Gobelins :",self.kill_Gobelin,end=" || ")
        print("Trolls :",self.kill_Troll,end=" || ")
        print("Dragons :",self.kill_Dragon," || ")

    def affiche_inventaire(self):
        print("|| inventaire :",self.inventaire,"||")

    def affiche_equipement(self):
       print("|| arme1 :",self.arme1,"|| arme2 :", self.arme2,"|| casque :",self.casque,"|| plastron :",self.plastron,"|| jambières :",self.jambières,"|| bottes :",self.bottes,"||")

    def affiche_armes(self):
        print("|| arme1 :",self.arme1,self.arme1_degats,"de dégats et",self.arme1_protection,"de protection || arme2 :", self.arme2,self.arme2_degats,"de dégats et",self.arme2_protection,"de protection ||")

    def affiche_armures(self):
        print("|| Casque :",self.casque,self.casque_protection,"de protection || Plastron :", self.plastron,self.plastron_protection,"de protection || Jambières :", self.jambières,self.jambières_protection,"de protection || Bottes :", self.bottes,self.bottes_protection,"de protection ||")

class Ennemi :
    def __init__(self,type,pv,degats,loot,exp,gold_min=0,gold_max=0,niv=1):
        self.type=type
        self.pv=pv
        self.pv_base=pv
        self.pv_a_restituer=self.pv
        self.degats=degats
        self.degats_base=degats
        self.lv=niv
        self.loot=loot
        self.gold_lachées=randint(gold_min,gold_max)
        self.exp=exp
        self.exp_base=exp

def montée_lv_mob(ennemi):
    ennemi.lv=ennemi.lv+1
    ennemi.pv=ennemi.pv_base*ennemi.lv
    ennemi.pv_a_restituer=ennmi.pv
    ennemi.degats=ennemi.degats_base*ennemi.lv
    ennemi.exp=ennemi.exp_base*ennemi.lv
    print("Attention",ennemi.type,"est maintenant niv",ennemi.lv," et ses dégats ont augmenté à",ennemi.degats,"mais l'exp gagnée a doublée")

class PNJ:
    def __init__(self,name,dialogue,quete):
        self.name=name
        self.dialogue=dialogue
        self.quete=quete

#//////////////////////////////////////////////////////////////////////////////#
##////////////////////////Fonctions gestion expérience////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#


def montée_lv_Perso():
    print("Félicitation, vous venez de monter de niveau. Vous êtes maintenant lv",Perso.lv)
    print("Vous pouvez augmenter l'une des deux stats suivantes : ||PV (augmentation de 5 pv)||  ||DEGATS (augmentation permanente de vos dégats de base de 1||")
    reponse="False"
    while reponse=="False":
        choix=input("")
        if choix=="PV":
            Perso.pv_max=Perso.pv_max+5
            Perso.pv=Perso.pv_max
            print("***PV max augmenté à",Perso.pv_max,"PV et restauration totale des PV***")
            reponse="True"
        if choix=="DEGATS":
            Perso.degats_base=Perso.degats_base+1
            Perso.degats=Perso.degats+1
            print("*** Dégats de base augmenté à",Perso.degats_base,"***")
            reponse="True"
    print("")

def test_exp_Perso():
    if Perso.exp>=(Perso.lv*150):
        Perso.exp=Perso.exp-(Perso.lv*150)
        Perso.lv=Perso.lv+1
        montée_lv_Perso()

def augmentation_exp(exp):
    Perso.exp=Perso.exp+exp
    test_exp_Perso()

#//////////////////////////////////////////////////////////////////////////////#
##///////////////////////Fonctions génération des armes///////////////////////##
#//////////////////////////////////////////////////////////////////////////////#


class Arme:
    def __init__(self,name,niv,degats,protection,emplacement):
        self.name=name
        self.lv=niv
        self.degats=degats*niv
        self.protection=protection*niv
        self.type="Arme"
        self.emplacement=emplacement

class Consommable:
    def __init__(self,name,soin):
        self.name=name
        self.soin=soin
        self.type="Consommable"

class Armure:
    def __init__(self,name,niv,protection):
        self.name=name
        self.lv=niv
        self.protection=protection*niv
        self.type="Armure"

def amelioration_arme(arme):
    if Perso.arme1==arme.name:
        print("***",arme.name,"amélioré(e) ***")
        arme.__init__(arme.name,(arme.lv)+1,(arme.degats)/arme.lv,(arme.protection)/arme.lv,arme.emplacement)
        Perso.degats=Perso.degats-Perso.arme1_degats+arme.degats
        Perso.protection=Perso.protection-Perso.arme1_protection+arme.protection
        Perso.arme1_degats=arme.degats
        Perso.arme1_protection=arme.protection
    else :
        print("Vous ne possedez pas de",arme.name)

def amelioration_armure(armure):
    if Perso.arme1==armure.name:
        print("***",armure.name,"amélioré ***")
        Perso.protection=Perso.protection-armure.protection
        armure.__init__(armure.name,armure.lv+1,(armure.degats)/armure.lv,(armure.protection)/armure.lv)
        if armure.name=="Casque":
            Perso.casque_protection=armure.protection
        if armure.name=="Plastron":
            Perso.plastron_protection=armure.protection
        if armure.name=="Jambières":
            Perso.jambières_protection=armure.protection
        if armure.name=="Bottes":
            Perso.bottes_protection=armure.protection
        Perso.protection=Perso.protection+armure.protection
    else :
        print("Vous ne possedez pas de",amelioration)


#//////////////////////////////////////////////////////////////////////////////#
##//////////////////Fonctions changement inventaire et stats//////////////////##
#//////////////////////////////////////////////////////////////////////////////#


def Changement(pv,gold):
    if Perso.pv+pv>Perso.pv_max:
        Perso.pv=Perso.pv_max
    else :
        Perso.pv=Perso.pv+pv
    Perso.gold=Perso.gold-gold

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
            print("Vous avez déjà une arme d'équipé :",Perso.arme1)
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
                print("Vous avez déjà une arme d'équipé :",Perso.arme2)
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
            print("Vous avez des armes d'équipées : arme1:",Perso.arme1,"  arme2 :",Perso.arme2)
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
        print("Vous avez déjà une armure d'équipée :",emplacement)
        print("Vous laissez donc",armure.name)
    Perso.affiche_armures

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
    if ennemi.loot!=[]:
        equip_laché=ennemi.loot[randint(0,len(ennemi.loot)-1)]
        if equip_laché=="Rien":
            print("Vous ne trouvez rien d'interessant sur son cadavre.")
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


def stats_kill(ennemi):
    if ennemi.type=="Bandit Guillaume":
        Perso.kill_Bandit=Perso.kill_Bandit+1
        if Perso.kill_Bandit%5==0:
            montée_lv_mob(Bandit)
    if ennemi.type=="Gobelin":
        Perso.kill_Gobelin=Perso.kill_Gobelin+1
        if Perso.kill_Gobelin%5==0:
            montée_lv_mob(Gobelin)
    if ennemi.type=="Troll":
        Perso.kill_Troll=Perso.kill_Troll+1
        if Perso.kill_Troll%5==0:
            montée_lv_mob(Troll)
    if ennemi.type=="Dragon":
        Perso.kill_Dragon=Perso.kill_Dragon+1
        if Perso.kill_Dragon%10==0:
            montée_lv_mob(Dragon)
    if ennemi.type=="Chèvre":
        Perso.kill_Chevre=Perso.kill_Chevre+1
    if ennemi.type=="Crocodile":
        Perso.kill_Crocodile=Perso.kill_Crocodile+1

    if Perso.kill_Dragon>=15:
        print("***Carte vers l'antre de Balarion trouvée***")
        return "True"
    else :
        return "False"


def test_sejour_lieux(lieu):
    if Perso.lieux_vsitiés!=[]:
        deja_visité="False"
        for i in Perso.lieux_vsitiés:
            if i==lieu:
                deja_visité="True"
        if deja_visité=="False":
            ajout_compteur_lieux(lieu)
    else :
        ajout_compteur_lieux(lieu)

def ajout_compteur_lieux(lieu):
    lieux_visité=Perso.lieux_vsitiés
    lieux_visité.append(lieu)
    Perso.lieux_vsitiés=lieux_visité

#//////////////////////////////////////////////////////////////////////////////#
##////////////////////////Class + Fonctions des quêtes////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#


class QUETE:
    def __init__(self,cible,nb_cible,type,exp,recompense=[],lv=1):
        if type=="Tuer":
            self.cible=cible
            self.nb_cible_base=nb_cible
            self.nb_cible=nb_cible*lv
            self.name=type,self.nb_cible,self.cible
        if type=="Visiter":
            self.lieux=cible
            self.name=type,self.lieux
        self.exp_base=exp
        self.exp=exp*lv
        self.recompense=recompense
        self.lv=lv
        self.type=type

def montée_lv_quête(quete):
    quete.__init__(quete.cible,quete.nb_cible_base,quete.type,quete.exp_base,quete.recompense,quete.lv+1)

def quete_achevée(quete):
    print("Felicitation vous avez achevé la quête",quete.name)
    Perso.exp=Perso.exp+quete.exp
    print("***Gain de",quete.exp,"exp***")
    montée_lv_quête(quete)

def test_quetes(quete):
    if quete.type=="Tuer":
        if quete.cible=="Bandits":
            if Perso.kill_Bandit>=quete.nb_cible:
                quete_achevée(quete)
        if quete.cible=="Gobelins":
            if Perso.kill_Gobelin>=quete.nb_cible:
                quete_achevée(quete)
        if quete.cible=="Trolls":
            if Perso.kill_Troll>=quete.nb_cible:
                quete_achevée(quete)
    if quete.type=="Visiter":
        compte=0
        for i in Perso.lieux_vsitiés:
            for j in quete.lieux:
                if i==j:
                    compte=compte+1
        if compte==len(quete.lieux):
            quete_achevée(quete)
#//////////////////////////////////////////////////////////////////////////////#
##////////////////////////Fonctions gestion evenements////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#

class Evenement :
    def __init__(self):
        self.Forêt=["Coffre","Bandit","Gobelin","Gobelin","Bandit","Gobelin","Bandit","Repos","Bandit","Bandit","Gobelin","Gobelin","Bandit","Gobelin","Bandit","Repos","Bandit","Bandit","Gobelin","Gobelin","Bandit","Gobelin","Bandit","Repos","Bandit"]
        self.Marais=["Coffre","Crocodile","Gobelin","Crocodile","Gobelin","Gobelin","Crocodile","Gobelin","Repos","Crocodile","Gobelin","Crocodile","Gobelin","Gobelin","Crocodile","Gobelin","Repos"]
        self.Donjon=["Bandit","Troll","Coffre","Troll","Troll","Bandit","Bandit","Bandit"]
        self.Montagne=["Dragon","Chèvre","Troll","Troll","Troll","Coffre","Repos","Troll","Bandit","Bandit","Coffre2"]

        self.coffre=[Epée_une_main,Epée_une_main,Dague,Epée_deux_mains,Potion_lv1,Potion_lv2,Potion_lv3,Bouclier]

def restauration_ennemi():
    Bandit.pv=Bandit.pv_a_restituer
    Chevre.pv=Chevre.pv_a_restituer
    Crocodile.pv=Crocodile.pv_a_restituer
    Gobelin.pv=Gobelin.pv_a_restituer
    Troll.pv=Troll.pv_a_restituer
    Dragon.pv=Dragon.pv_a_restituer

def dé():
    return randint(1,20)

def coffre():
    butin=Event.coffre[randint(0,len(Event.coffre)-1)]
    butin_gold=randint(5,20)
    print("En ouvrant le coffre vous trouvez",butin_gold,"Gold")
    print("***Gain de",butin_gold,"Gold***")
    Perso.gold=Perso.gold+butin_gold
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
    print("Pour afficher le nombre de kills tapez K")
    print("Pour quitter un batiment ou la ville tapez QUITTER")


def CREDITS():
    print("Merci d'avoir joué")
    print("Jeu programmé par Aurélien Arqué")
    print("Avec les conseils de Théophile, Romain, Tristan, Guillaume, Alexandre, Thomas, Antoine, M.Koroloff")
    print("Et le soutien de la Classe de Terminale 5")

#//////////////////////////////////////////////////////////////////////////////#
##///////////////////////////Fonctions de batiments///////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#
def Auberge(utilisation):
    print("Fatigué, vous optez pour un passage à l'Auberge. À peine à l'interieur, vous vous approchez du feu pour vous reposer.")
    print("")
    test_sejour_lieux("Auberge")
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
                if utilisation>0:
                    Changement(10,0)
                    print("Vous refusez gentiment et allez vous assoupir près du feu.")
                    print("")
                    print("***Gain de 10 PV***")
                    utilisation=utilisation-1
                else :
                    print("Vous avez atteint l'utilisation max de cette fonctionnalité pour se passage à l'Auberge")
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
            if decision=="K":
                Perso.affiche_kills()
            return utilisation


##////////////////////////////////////////////////////////////////////////////##

def Forge():
    print("Attiré par le bruit assourdissant du marteau sur l'enclume, vous vous diriger vers la Forge.")
    print("")
    test_sejour_lieux("Forge")
    séjour_forge="True"
    while séjour_forge=="True":
        print("Vous voyant approcher, le forgeron s'arrête et vous interpelle.")
        choix="False"
        while choix=="False":
            print("Il vous prospose plusieurs services : ||AMELIORER votre équipement||  ||QUITTER la forge||")
            action=input("")
            separation(5)
            if action=="AMELIORER":
                choix="True"
                print("Il vous propose d'améliorer pour 20 gold X le niveau de votre arme/armure: ||DAGUE||  ||EPEE UNE MAIN||  ||BOUCLIER||  ||CASQUE||  ||PLASTRON||  ||JAMBIERES||  ||BOTTES|| et pour 40 gold X le niveau de votre arme/armure :  ||EPEE DEUX MAINS||   ||ARC||  ||RETOUR||")
                decision="False"
                while decision=="False":
                    amelioration=input("")
                    separation(5)
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

                    if amelioration=="ARC":
                        if Perso.gold>=(40*Arc.lv):
                            Perso.gold=Perso.gold-(40*Arc.lv)
                            print("***Dépense de",40*Arc.lv,"Gold***")
                            amelioration_arme(Arc)
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


##////////////////////////////////////////////////////////////////////////////##


def Boutique():
    print("L'attractivité de la vitrine de la Boutique vous pousse à l'intérieur.")
    print("")
    test_sejour_lieux("Boutique")
    séjour_boutique="True"
    while séjour_boutique=="True":
        print("Le propriétaire s'avance dans votre direction et vous montre sa marchandise :  ||POTION LV1 : 10 Gold, restaure 10 PV||  ||POTION LV2 : 20 Gold restaure 20 PV||  ||POTION LV3 : 30 Gold, restaure 50 PV||  ||QUITTER||")
        choix="False"
        decision=input("")
        separation(5)
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
        separation(5)



##////////////////////////////////////////////////////////////////////////////##

def Terrain_entrainement():
    print("Regorgeant d'énergie, vous choisissez d'aller vous entrainer.")
    test_sejour_lieux("Terrain d'entrainement")
    print("Une fois sur place, le capitaine de la garde vous invite à vous entrainer.")
    reponse="False"
    while reponse=="False":
        print("Il vous propose deux séances : ||GRATUIT (gain de 20 exp)||  ||PAYANTE (gain de 50 exp pour 20 Gold)||")
        choix=input("")
        if choix=="PAYANT":
            if Perso.gold>=20:
                augmentation_exp(50)
                Changement(0,20)
                print("***Gain de 50 exp***")
                reponse="True"
            else :
                print("Vous n'avez pas assez de Gold pour participer à cette séance.")
                print("Voulez vous participer à l'autre séance ?")
                choix2=input("")
                if choix2=="OUI":
                    choix="GRATUIT"

        if choix=="GRATUIT":
            augmentation_exp(20)
            print("***Gain de 20 exp***")
            reponse="True"

#//////////////////////////////////////////////////////////////////////////////#
##/////////////////////////////Fonctions de lieux/////////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#

def Foret():
    print("Vous décidez d'allez explorer la forêt et vous vous engoufrez entre les arbres.")
    print("")
    test_sejour_lieux("Foret")
    temps_séjour=randint(1,5)
    temps=1
    while temps<=temps_séjour:
        temps2=int(evenement(Event.Forêt))
        temps=temps+temps2+1
    if temps>50:
        return "Fin"
    else :
        return 0


def Donjon():
    print("En quête de trésors et de combats vous choisissez d'explorer le donjon. Vous n'êtes qu'à l'entrée, que vous sentez déjà")
    print("une odeur d'or et de trésors mélée à celle des monstres qui parcours le donjon. Prenez garde !")
    print("")
    test_sejour_lieux("Donjon")
    temps_séjour=randint(1,5)
    temps=1
    while temps<=temps_séjour:
        temps2=int(evenement(Event.Donjon))
        temps=temps+temps2+1
    if temps>50:
        return "Fin"
    else :
        return 0


def Marais():
    print("Vous entrez dans le marais")
    print("")
    test_sejour_lieux("Marais")
    temps_séjour=randint(1,5)
    temps=1
    while temps<=temps_séjour:
        temps2=evenement(Event.Marais)
        temps=temps+temps2+1
    if temps>50:
        return "Fin"
    else :
        return 0


def Montagne():
    print("Vous vous dirigez vers le pied de la montagne et vous en commencez l'ascension")
    print("")
    test_sejour_lieux("Montagne")
    temps_séjour=randint(1,5)
    temps=1
    while temps<=temps_séjour:
        temps2=int(evenement(Event.Montagne))
        temps=temps+temps2+1
    if temps>50:
        return "Fin"
    else :
        return 0


def Ville():
    utilisation_terrain_entrainement=1
    print("Vous vous avancez en direction de l'Entrée principale de la ville et hélez les gardes pour qu'ils vous ouvrent.")
    print("Alors que les portes s'ouvrent vous entrez dans la ville")
    print("")
    test_sejour_lieux("Ville")
    séjour_ville="True"
    utilisation=1
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
                utilisation=Auberge(utilisation)
            if action=="TERRAIN D'ENTRAINEMENT":
                choix="True"
                if utilisation_terrain_entrainement==1:
                    Terrain_entrainement()
                else :
                    print("Toutes les séances programmées pour la semaine sont finies. Revenez une autre fois.")
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
            if action=="K":
                Perso.affiche_kills()


#//////////////////////////////////////////////////////////////////////////////#
##/////////////////////////////Fonction évenement/////////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#

def evenement(event,temps2=0):
    action=event[randint(0,len(event)-1)]
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
        print("Un Guillaume sauvage apparait !")
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


def combat(Perso,ennemi,temps2):
    nb_action=1
    fin_combat=""
    while fin_combat=="":
        nb_action=1
        while nb_action>0:
            print("Vous avez",Perso.pv,"PV")
            print(ennemi.type,"a",ennemi.pv,"PV")
            print("Que veux tu faire : ||UTILISER UN CONSOMABLE||  ||ATTAQUER||  ||FUIR||")
            action=input("")
            print("")
            if action=="UTILISER UN CONSOMABLE" :
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
                            for i in Perso.inventaire:   #utilisation de potion si le joueur en possède
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
                                print("Vous ne possedez pas ce consomable")
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
    restauration_ennemi()
    return temps2



#//////////////////////////////////////////////////////////////////////////////#
##/////////////////////////////Fonctions histoire/////////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#

def Histoire_intro():
    print("Vous êtes un jeune soldat, et aujourd'hui, après plusieurs années d'entrainement, vous allez être nommé chevalier par le Roi Auréus 1er en personne.",end=" ")
    print("La ville entière est en effervescence, les commercants installent leur stands et les enfants slalomment entre les ouvriers qui installent l'estrade de la cérémonie.",end=" ")
    print("Les boulangers et cuisiniers royaux dressent la table du banquet.")
    print("Alors que vous contemplez cette fourmilière en ébullition depuis la fenêtre de votre chambre, une main ferme sur votre épaule vous rappelle à la réalité. Vous vous retournez et apercevez votre plus fidèle compagnon, Conrad.",end=" ")
    print("Ce dernier vous tend une miche de pain :'Prend ça",Perso.name,", j'entend ton ventre gronder à des kilomètres.'",end=" ")
    print("Votre estomac criait effectivement famine et vous le remerciez en avalant la miche de pain.",end=" ")
    print("Soudain, vous entendez un rugissement au loin. Conrad se retourne : 'Si tu as si faim que ça va donc voir en cuisine s'il ne reste pas quelques ...'. Vous ne lui laissez",end=" ")
    print("pas le temps de finir que vous êtes déjà dehors. Le cri provenait de la place et alors que vous vous y dirigez vous vous rappelez que vous avez laissé votre équipement à l'Armurerie.")
    print("Voulez vous allez le chercher ?  ||OUI||   ||NON||",end="")
    reponse="False"
    while reponse=="False":
        choix=input("")
        if choix=="OUI":
            reponse="True"
            print("")
            print("Vous vous hâtez d'aller le récupérer. Mais une fois devans, vous la trouvez entièrement rasée et vous ne trouvez aucune trace des équipements. Furieux vous faites demi-tour vers la place.",end=" ")
        if choix=="NON":
            reponse="True"
            print("")
            print("Vous prenez conscience de l'urgence de la situation et préférez y aller directement.",end=" ")
    print("Une fois arrivé sur place, vous apperecevez les gardes qui tirent en direction d'une forme gigantesque dans le ciel. À mesure que vos yeux s'habituent à la lumière aveuglante du Soleil, vous réalisez que cette forme est celle d'un dragon et pas n'importe lequel : Balarion, le Seigneur des Dragons.",end=" ")
    print("En observant ses griffes, vous comprenez immédiatement la situation : il a kidnappé le Roi. À peine avez vous eu le temps de le réaliser que Balarion s'envole déjà vers la Montagne pour rejoindre son antre. ")
    print("Quelques heures seulement après, à la suite d'une réunion du Conseil, son représentant s'approche de l'assistance encore sous le choc :'Afin de maintenir la stabilité du royaume, le Prince Leon assumera les fonctions. Quant à notre bien-aimé Souverain, nous avons décidé d'envoyer les nouveaux chevaliers",end=" ")
    print("à sa recherche. Ils devront parcourir le Royaume, traverser Forêts et Marais, et affronter tout les obstacles qui s'opposerons à eux en trouvant de l'équipement sur leur route, faute d'Armurerie. Gloire et richesses s'offfreront à celui qui ramènera notre Souverain !!'",end=" ")
    print("À peine le Conseil eut-il fini leur annonce, que vous vous empressez de partir à l'Aventure...")

def combat_final():
    print("Vous arrivez à l'entrée de la grotte du Seigneur des Dragons. Vous avancez à pas feutrés et vous trouvez l'imposant dragon en pleine digestion.",end=" ")
    if Perso.arme1=="Arc":
        print("Vous repérez un immense stalactite au-dessus de sa tête. Vous bandez donc votre Arc, tirez sur le pic qui vient s'empaler dans le crâne du Dragon.",end=" ")
    if Perso.arme1=="Epée une main" or Perso.arme1=="Epée deux mains":
        print("Vous prenez votre courage à deux mains, vous vous glissez entre ses pattes et lui plantez votre Épée dans le coeur puis lui ouvrez le ventre pour accélérer sa mort.",end=" ")
    if Perso.arme1=="Dague":
        print("Vous vous approcher silencieusement vers son oeil et, muni de votre dague, l'y la lui planter jusqu'au cerveau.",end=" ")
    print("Surpris dans son sommeil, Balarion n'a que le temps d'expirer avant de s'étendre à jamais.")
    print("***Gain d'une tête de Balarion***")
    inventaire=Perso.inventaire
    inventaire.append("Tête de Balarion")
    Perso.inventaire=inventaire
    print("En avancant vers le fond de la caverne, vous aprecevez deux chemins. Lequel voulez-vous prendre ? ||GAUCHE|| ou ||DROITE||")
    reponse="False"
    while reponse=="False":
        choix=input("")
        if choix=="GAUCHE":
            print("Vous prenez le chemin de gauche et vous tomber sur un tas d'osement d'humain, de bétail, de gobelin et de troll. Vous faites donc demi-tou et prenez l'autre chemin.",end=" ")
            reponse="True"
        if choix=="DROITE":
            print("Vous prenez le chemin de droite et vous tomber sur un tas d'osement d'humain, de bétail, de gobelin et de troll. Vous faites donc demi-tou et prenez l'autre chemin.",end=" ")
            reponse="True"
    print("Vous trouver alors, après plusieurs mois d'aventure, le Roi Auréus 1er, affaiblit par tout ce temps de captivité. Vous lui donnez un peu de viande de dragon et vous entamez le voyage retour. Avec l'expérience accumulé au fil du voyage, vous ne faites qu'une bouchée",end=" ")
    print("des créatures qui vous attaquent sur le retour. Une fois arrivé aux portes de la Capitale, les gardes vous ouvrent et vous entrez sous les acclamations de la foule qui scande votre nom :","'",Perso.name,"!",Perso.name,"!",Perso.name,"!'",end="")
    print("Quelques mois après, le roi, de nouveau en plein santé, vous accueille lors d'une grande cérémonie où il vous nomme héros national et générale des armées du Royaume. Cela marque le début de prochaines aventures ...")
    print("")
    print("Félicitiation pour avoir terminé le jeu. Vous avez réussi à sauver le Roi et à éliminer Balarion mais que ce serait-il passé si vous aviez fait d'autre choix ?")
    print("Voulez vous voir les CREDITS ?")
    reponse_inutilse=input("")
    print("Peu importe votre réponse vous allez les avoir")


#//////////////////////////////////////////////////////////////////////////////#
##/////////////////////////////Préparation du jeu/////////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#

#création des armes
Epée_une_main=Arme("Epée une main",1,5,0,1)
Epée_deux_mains=Arme("Epée deux mains",1,10,0,3)
Arc=Arme("Arc",1,10,0,3)
Bouclier=Arme("Bouclier",1,0,5,2)
Dague=Arme("Dague",1,2,0,1)

#création des consommables
Potion_lv1=Consommable("Potion lv1",10)
Potion_lv2=Consommable("Potion lv2",25)
Potion_lv3=Consommable("Potion lv3",50)
Viande=Consommable("Viande",15)

#création des armures
Casque=Armure("Casque",1,2)
Plastron=Armure("Plastron",1,4)
Jambières=Armure("Jambières",1,2)
Bottes=Armure("Bottes",1,1)

#création des quêtes
Quête_Bandit=QUETE("Bandits",5,"Tuer",20)
Quête_Gobelin=QUETE("Gobelins",3,"Tuer",30)
Quête_Troll=QUETE("Trolls",2,"Tuer",40)
Quête_visite_ville=QUETE(["Forge","Terrain d'entrainement","Boutique","Auberge"],0,"Visiter",40)


Items=[[Epée_une_main,Epée_deux_mains,Arc,Bouclier,Dague],[Potion_lv1,Potion_lv2,Potion_lv3]]
Lieu=["FORET (difficulté Debutant)","DONJON (difficulté Moyenne)","FORET (difficulté Debutant)","VILLE","MARAIS (difficulté Facile)","FORET (difficulté Debutant)","MARAIS (difficulté Facile)","AUBERGE","FORET (difficulté Debutant)","FORET (difficulté Debutant)","MARAIS (difficulté Facile)","MONTAGNE (difficulté Maximale)"]
Perso=Personnage(input("Quel est le pseudo de ton personnage ?"),100,[])

Chevre=Ennemi("Chèvre",10,2,[Viande,"Rien","Rien","Rien","Rien"],5)
Gobelin=Ennemi("Gobelin",15,2,["Rien","Rien","Rien","Rien","Rien","Rien","Rien","Rien","Rien","Rien","Rien","Rien",Epée_une_main,Epée_une_main,Dague,Dague,Dague,Dague,Dague,Dague,Dague,Dague,Casque],30,1,3)
Bandit=Ennemi("Bandit Guillaume",10,2,["Rien","Rien","Rien","Rien","Rien","Rien","Rien","Rien","Rien","Rien","Rien","Rien","Rien","Rien","Rien","Rien",Arc,Arc,Arc,Arc,Potion_lv1,Potion_lv1,Potion_lv1,Potion_lv1,Potion_lv2,Epée_une_main,Epée_une_main,Epée_une_main,Epée_une_main,Bottes,Jambières],15,1,3)
Crocodile=Ennemi("Crocodile",10,4,["Rien",Viande,Viande,Viande],20)
Troll=Ennemi("Troll",70,10,[Epée_deux_mains,Epée_deux_mains,Epée_deux_mains,Epée_une_main,Plastron,Casque,"Rien","Rien","Rien","Rien"],50,5,15)
Dragon=Ennemi("Dragon",200,50,[Epée_une_main,Epée_deux_mains,Bouclier,Plastron],500,50,200)
Event=Evenement()





#//////////////////////////////////////////////////////////////////////////////#
##////////////////////////////////////////////////////////////////////////////##
##//////////////////////////////Lancement du jeu//////////////////////////////##
##////////////////////////////////////////////////////////////////////////////##
#//////////////////////////////////////////////////////////////////////////////#
Perso.affiche_global()
print("")
compris="False"
while compris=="False":
    print("Tout au long de la partie vous serz amené à faire des choix. Pour choisir, réécrivez les propositions en MAJUSCULES.")
    print("Pour choisir les lieux tapez GAUCHE ou G et DROITE ou D")
    Help()
    as_tu_compris=input("As-tu compris ?  ||OUI||  ||NON||")
    if as_tu_compris=="OUI":
        compris="True"
        print("")
print("---Si besoin au cours de la partie, vous pouvez taper HELP pour réaccéder aux commandes spéciales---")
separation(2)
Histoire_intro()
print("Êtes-vous prêt ?  ||OUI||   ||NON||",end="")
reponse="False"
while reponse=="False":
    choix=input("")
    if choix=="OUI":
        reponse="True"
print("VOUS COMMENCEZ L'AVENTURE !!")
print("")
jeu=""
while Perso.Etat!="Mort" and Perso.Etat!="Arrêt":
    deplacement=action(Items,Lieu)
    jeu=deplacement
    if deplacement!="PASSE": ## if pour les tests à supprimer à la fin
        if deplacement!="Arrêter":
            jeu=exploration(deplacement)

CREDITS()



