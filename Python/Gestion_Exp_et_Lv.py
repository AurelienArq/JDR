from Python.main import Perso


def montée_lv_mob(ennemi):
    ennemi.lv=int(ennemi.lv+1)
    ennemi.pv=int(ennemi.pv_base*ennemi.lv)
    ennemi.pv_a_restituer=ennemi.pv
    ennemi.degats=int(ennemi.degats_base*ennemi.lv)
    ennemi.exp=int(ennemi.exp_base*ennemi.lv)
    print("Attention",ennemi.type,"est maintenant niv",ennemi.lv," et ses dégats ont augmenté à",ennemi.degats,"mais l'exp gagnée a doublée")

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