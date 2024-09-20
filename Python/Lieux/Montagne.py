from random import randint
from ..Evenement import evenement
from ..Quete import test_sejour_lieux
from ..main import Event

def Montagne():
    print("Vous vous dirigez vers le pied de la montagne et vous commencez l'ascension")
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
