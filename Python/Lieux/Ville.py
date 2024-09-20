from random import randint
from ..Evenement import evenement
from ..Quete import test_sejour_lieux
from ..main import Event

def Ville():
    utilisation_terrain_entrainement=1
    print("Vous vous avancez en direction de l'Entrée principale de la ville et hélez les gardes pour qu'ils vous ouvrent.")
    print("Alors que les portes s'ouvrent vous entrez dans la ville")
    print("")
    test_sejour_lieux("Ville")
    séjour_ville="True"
    utilisation=1
    while séjour_ville=="True":
        print(" ")
        print("▬"*100)
        print(" ")
        print("Vous avez le choix entre plusieurs boutique : ||FORGE||   ||BOUTIQUE||   ||AUBERGE||  ||TERRAIN D'ENTRAINEMENT||")
        print("Voulez vous entrez dans l'une de ces boutiques ou QUITTER la ville ?")
        choix="False"
        while choix=="False":
            action=(input(""))
            separation(2)
            print("▬"*100)
            separation(2)
            if action=="FORGE":
                choix="True"
                Forge()
            if action=="BOUTIQUE":
                choix="True"
                Boutique()
            if action=="AUBERGE":
                choix="True"
                utilisation=Auberge(utilisation)
            if action=="TERRAIN D'ENTRAINEMENT":
                choix="True"
                if utilisation_terrain_entrainement==1:
                    Terrain_entrainement()
                else :
                    print("Toutes les séances programmées pour la semaine sont finies. Revenez une autre fois.")
            if action=="QUITTER":
                choix="True"
                séjour_ville="False"

            if action=="HELP":
                Help()
            if action=="A":
                Perso.affiche_all()
            if action=="I":
                Perso.affiche_inventaire()
            if action=="S":
                Perso.affiche_stats()
            if action=="K":
                Perso.affiche_kills()
