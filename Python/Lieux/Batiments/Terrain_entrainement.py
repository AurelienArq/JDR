from ...Quete import test_sejour_lieux
from ...main import *

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
