from Python.main import Perso, Chevre, Crocodile, Bandit, Gobelin, Troll, Dragon, Nain, Epée_deux_mains, Epée_une_main, \
    Arc, Dague, Bouclier, Marteau, Hache, Casque, Plastron, Jambières, Bottes


def création_sauvegarde():
    clé_sauvegarde=[Perso.name,Perso.pv,Perso.inventaire,Perso.pv_max,Perso.lv,Perso.exp,int(Perso.degats),int(Perso.protection),Perso.arme1,Perso.arme2,Perso.casque,Perso.plastron,Perso.jambières,Perso.bottes,Perso.gold,int(Perso.arme1_degats),int(Perso.arme1_protection),int(Perso.arme2_degats),int(Perso.arme2_protection),int(Perso.casque_protection),int(Perso.plastron_protection),int(Perso.jambières_protection),int(Perso.bottes_protection),Perso.kill_Chevre,Perso.kill_Crocodile,Perso.kill_Bandit,Perso.kill_Gobelin,Perso.kill_Troll,Perso.kill_Dragon,Perso.kill_Nain,"Vivant",Perso.degats_base,Perso.gold_total,Chevre.type,Chevre.pv,Chevre.degats,Chevre.exp,Chevre.gold_lachées,Chevre.gold_lachées,Chevre.lv,Crocodile.type,Crocodile.pv,Crocodile.degats,Crocodile.exp,Crocodile.gold_lachées,Crocodile.gold_lachées,Crocodile.lv,Bandit.type,Bandit.pv,Bandit.degats,Bandit.exp,Bandit.gold_lachées,Bandit.gold_lachées,Bandit.lv,Gobelin.type,Gobelin.pv,Gobelin.degats,Gobelin.exp,Gobelin.gold_lachées,Gobelin.gold_lachées,Gobelin.lv,Troll.type,Troll.pv,Troll.degats,Troll.exp,Troll.gold_lachées,Troll.gold_lachées,Troll.lv,Dragon.type,Dragon.pv,Dragon.degats,Dragon.exp,Dragon.gold_lachées,Dragon.gold_lachées,Dragon.lv,Nain.type,Nain.pv,Nain.degats,Nain.exp,Nain.gold_lachées,Nain.gold_lachées,Nain.lv,Epée_une_main.lv,Epée_deux_mains.lv,Arc.lv,Dague.lv,Bouclier.lv,Marteau.lv,Hache.lv,Casque.lv,Plastron.lv,Jambières.lv,Bottes.lv]

    nom_fichier=str(input("Donne un nom à ta sauvegarde"))+".txt"
    fichier = open (nom_fichier,"w")
    for i in clé_sauvegarde:
        fichier.write(str(i)+'\n')
    fichier.close()

def ouverture_sauvegarde(nom_fichier):
    print(nom_fichier)
    fichier = open(nom_fichier,"r")
    clé = []
    line = fichier.readline()
    while line != '' :
        clé.append(line[:len(line)-1])
        line = fichier.readline()
    fichier.close()
    return clé
