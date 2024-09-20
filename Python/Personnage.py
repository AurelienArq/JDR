class Personnage :
    def __init__ (self,nom,pv,inventaire,pv_max=100,niv=1,exp=0,degats=2,protection=0,arme1="none",arme2="none",casque="chapeau de paille",plastron="chemise",jambières="pantalon",bottes="Souliers en cuir",argent=0,arme1_degats=0,arme1_protection=0,arme2_degats=0,arme2_protection=0,casque_protection=0,plastron_protection=0,jambières_protection=0,bottes_protection=0,kill_Chevres=0,kill_Crocodiles=0,kill_Bandits=0,kill_Gobelins=0,kill_Trolls=0,kill_Dragons=0,kill_Nains=0,Etat="Debut",degats_base=2,gold_total=0):
        self.name=nom
        self.Etat=Etat
        self.pv=pv
        self.pv_max=pv_max
        self.inventaire=inventaire
        self.degats=degats
        self.degats_base=degats_base
        self.protection=protection
        self.gold=argent
        self.gold_total=gold_total
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
        self.kill_Nain=kill_Nains
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
        print("Nains :",self.kill_Nain,end=" || ")
        print("Dragons :",self.kill_Dragon," || ")

    def affiche_inventaire(self):
        print("|| inventaire :",self.inventaire,"||")

    def affiche_equipement(self):
       print("|| arme1 :",self.arme1,"|| arme2 :", self.arme2,"|| casque :",self.casque,"|| plastron :",self.plastron,"|| jambières :",self.jambières,"|| bottes :",self.bottes,"||")

    def affiche_armes(self):
        print("|| arme1 :",self.arme1,self.arme1_degats,"de dégats et",self.arme1_protection,"de protection || arme2 :", self.arme2,self.arme2_degats,"de dégats et",self.arme2_protection,"de protection ||")

    def affiche_armures(self):
        print("|| Casque :",self.casque,self.casque_protection,"de protection || Plastron :", self.plastron,self.plastron_protection,"de protection || Jambières :", self.jambières,self.jambières_protection,"de protection || Bottes :", self.bottes,self.bottes_protection,"de protection ||")

