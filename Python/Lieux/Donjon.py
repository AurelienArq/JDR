from random import randint
from ..Evenement import evenement
from ..Quete import test_sejour_lieux
from ..main import Event


def Donjon():
    print("En quête de trésors et de combats vous choisissez d'explorer le donjon. Vous n'êtes qu'à l'entrée, que vous sentez déjà",end=" ")
    print("une odeur d'or et de trésors mélée à celle des monstres qui parcourent le donjon. Prenez garde !")
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

