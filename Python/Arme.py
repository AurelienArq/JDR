from main import *

class Arme:
    def __init__(self,name,degats,protection,emplacement,niv=1):
        self.name=name
        self.lv=niv
        self.degats=degats*niv
        self.protection=protection*niv
        self.type="Arme"
        self.emplacement=emplacement

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
