# Créé par Elève, le 19/10/2022 en Python 3.7
def sauvegarde():
    clé_sauvegarde=[Perso.name,Perso.pv,Perso.inventaire,Perso.pv_max,Perso.lv,Perso.exp,Perso.degats,Perso.protection,Perso.arme1,Perso.arme2,Perso.casque,Perso.plastron,Perso.jambières,Perso.bottes,Perso.gold,Perso.arme1_degats,Perso.arme1_protection,Perso.arme2_degats,Perso.arme2_protection,Perso.casque_protection,Perso.plastron_protection,Perso.jambières_protection,Perso.bottes_protection,Perso_kill_Chevre,Perso.kill_Crocodile,Perso.kill_Bandit,Perso.kill_Gobelin,Perso.kill_Troll,Perso.kill_Dragon,Perso.Etat,Perso.degats_base,Perso.gold_total]

nom_fichier=str(input("Donne un nom à ta sauvegarde"))+".txt"
fichier = open (nom_fichier,"w")
for i in clé_sauvegarde:
    fichier.write(i)
fichier.close()

fichier=open(nom_fichier,"r")
clé = []
line = fichier.readline()
while line != '' :
    clé.append(line)
    line = fichier.readline()
fichier.close()