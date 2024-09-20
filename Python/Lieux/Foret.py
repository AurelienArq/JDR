from random import randint
from ..Evenement import evenement
from ..Quete import test_sejour_lieux
from ..main import Event

def Foret():
    print("Vous décidez d'allez explorer la forêt et vous vous engoufrez entre les arbres.")
    print("")
    test_sejour_lieux("Foret")
    temps_séjour=randint(1,5)
    temps=1
    while temps<=temps_séjour:
        temps2=int(evenement(Event.Forêt))
        temps=temps+temps2+1
    if temps>50:
        return "Fin"
    else :
        return 0
