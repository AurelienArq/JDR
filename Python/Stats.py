from Python.Gestion_Exp_et_Lv import montée_lv_mob
from Python.main import Perso, Bandit, Gobelin, Troll, Nain, Dragon, Chevre, Crocodile


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
    if ennemi.type=="Troll":
        Perso.kill_Nain=Perso.kill_Nain+1
        if Perso.kill_Nain%5==0:
            montée_lv_mob(Nain)
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

def stats_fin():
    print("")
    print("")
    print("//////////////////////////////////STATS À LA FIN DE VOTRE PARTIE//////////////////////////////////")
    print("")
    print("PSEUDO :",Perso.name)
    print("----------------------------------------------------------")
    print("LV :",Perso.lv)
    exp_total=((Perso.lv*150*(Perso.lv-1))/2)+Perso.exp
    print("EXP TOTAL:", exp_total)
    print("EXP RESTANTS:",Perso.exp)
    print("----------------------------------------------------------")
    print("PV max :",Perso.pv_max)
    print("PV restant en fin de partie :",Perso.pv)
    print("----------------------------------------------------------")
    print("DEGATS TOTAUX :",Perso.degats)
    print("DEGATS DE BASE :",Perso.degats_base)
    print("DEGATS TOTAL DES ARMES :",Perso.arme1_degats+Perso.arme2_degats)
    print("----------------------------------------------------------")
    print("ARME1 :",Perso.arme1," "*(14-len(Perso.arme1)),"| DEGATS :",Perso.arme1_degats," "*(4-len(str(Perso.arme1_degats))),"| PROTECTION :",Perso.arme1_protection)
    print("ARME2 :",Perso.arme2," "*(14-len(Perso.arme2)),"| DEGATS :",Perso.arme2_degats," "*(4-len(str(Perso.arme2_degats))),"| PROTECTION :",Perso.arme2_protection)
    print("----------------------------------------------------------")
    print("PROTECTION TOTALE :",Perso.protection)
    print("CASQUE :",Perso.casque," "*(17-len(Perso.casque)),"| PROTECTION :",Perso.casque_protection)
    print("PLASTRON :",Perso.plastron," "*(15-len(Perso.plastron)),"| PROTECTION :",Perso.plastron_protection)
    print("JAMBIÈRES :",Perso.jambières," "*(14-len(Perso.jambières)),"| PROTECTION :",Perso.jambières_protection)
    print("BOTTES :",Perso.bottes," "*(17-len(Perso.bottes)),"| PROTECTION :",Perso.bottes_protection)
    print("----------------------------------------------------------")
    print("TOTAL DES GOLDS :",Perso.gold_total)
    print("GOLDS POSSÉDÉES À LA FIN :",Perso.gold)
    print("----------------------------------------------------------")
    print("INVENTAIRE :")
    print(Perso.inventaire)
    print("----------------------------------------------------------")
    print("KILLS :")
    print("")
    print("CHEVRE(S)    :",Perso.kill_Chevre)
    print("CROCODILE(S) :",Perso.kill_Crocodile)
    print("BANDIT(S)    :",Perso.kill_Bandit)
    print("GOBELIN(S)   :",Perso.kill_Gobelin)
    print("TROLL(S)     :",Perso.kill_Troll)
    print("NAIN(S)      :",Perso.kill_Troll)
    print("DRAGON(S)    :",Perso.kill_Dragon)
    print("----------------------------------------------------------")
    print("STATS ENNEMIS :")
    print("")
    print("CHEVRE(S)    :    ","LV",Chevre.lv," "*(7-len(str(Chevre.lv))),"DEGATS ",Chevre.degats)
    print("CROCODILE(S) :    ","LV",Crocodile.lv," "*(7-len(str(Crocodile.lv))),"DEGATS ",Crocodile.degats)
    print("BANDIT(S)    :    ","LV",Bandit.lv," "*(7-len(str(Bandit.lv))),"DEGATS ",Bandit.degats)
    print("GOBELIN(S)   :    ","LV",Gobelin.lv," "*(7-len(str(Gobelin.lv))),"DEGATS ",Gobelin.degats)
    print("TROLL(S)     :    ","LV",Troll.lv," "*(7-len(str(Troll.lv))),"DEGATS ",Troll.degats)
    print("NAIN(S)      :    ","LV",Nain.lv," "*(7-len(str(Nain.lv))),"DEGATS ",Nain.degats)
    print("DRAGON(S)    :    ","LV",Dragon.lv," "*(7-len(str(Dragon.lv))),"DEGATS ",Dragon.degats)
    print("")
    print("/////////////////////////////////////////////////////////////////////////////////////////////////")
    print("")
    print("")