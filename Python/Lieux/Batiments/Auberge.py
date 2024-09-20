from ...Util import *
from ...main import Perso
from ...Quete import *





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
            separation(2)
            print("▬"*100)
            separation(2)
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
                    print("Vous avez atteint l'utilisation max de cette fonctionnalité pour ce passage à l'Auberge")
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


