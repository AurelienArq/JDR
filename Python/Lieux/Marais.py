from random import randint
from ..Evenement import evenement
from ..Quete import test_sejour_lieux
from ..main import Event

def Marais():
    print("Vous entrez dans le marais")
    print("")
    test_sejour_lieux("Marais")
    temps_séjour=randint(1,5)
    temps=1
    while temps<=temps_séjour:
        temps2=evenement(Event.Marais)
        temps=temps+temps2+1
    if temps>50:
        return "Fin"
    else :
        return 0

