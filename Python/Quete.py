from Python.main import Perso


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
    print("Félicitation vous avez achevé la quête",quete.name)
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
