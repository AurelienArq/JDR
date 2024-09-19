from main import *

class Armure:
    def __init__(self,name,protection,niv=1):
        self.name=name
        self.lv=niv
        self.protection=protection*niv
        self.type="Armure"


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
