from Python.Util import ecrit
from Python.main import Perso


def Histoire_intro():
    ecrit("Vous êtes un jeune soldat, et aujourd'hui, après plusieurs années d'entrainement, vous allez être nommé chevalier par le Roi Auréus 1er en personne.")
    ecrit("La ville entière est en effervescence, les commerçants installent leurs stands et les enfants slaloment entre les ouvriers qui installent l'estrade de la cérémonie.")
    ecrit("Les boulangers et cuisiniers royaux dressent la table pour le banquet.")
    ecrit("Alors que vous contemplez cette fourmilière en ébullition depuis la fenêtre de votre chambre, une main ferme sur votre épaule vous rappelle à la réalité. Vous vous retournez et apercevez votre plus fidèle compagnon, Conrad.")
    TEXT=("Ce dernier vous tend une miche de pain :'Prend ça ",Perso.name,", j'entends ton ventre gronder à des kilomètres.'",)
    ecrit(TEXT)
    ecrit("Votre estomac criait effectivement famine, vous le remerciez en avalant la miche de pain.",)
    ecrit("Soudain, vous entendez un rugissement au loin. Conrad se retourne : 'Si tu as si faim que ça va donc voir en cuisine s'il ne reste pas quelques ...'. Vous ne lui laissez ")
    ecrit("pas le temps de finir que vous êtes déjà dehors. Le cri provenait de la place et alors que vous vous y dirigez vous vous rappelez que vous avez laissé votre équipement à l'Armurerie.")
    print("Voulez vous allez le chercher ?  ||OUI||   ||NON||",end="")
    reponse="False"
    while reponse=="False":
        choix=input("")
        if choix=="OUI":
            reponse="True"
            print("")
            ecrit("Vous vous hâtez d'aller le récupérer. Mais une fois devant, vous la trouvez entièrement rasée et vous ne trouvez aucune trace des équipements. Furieux vous faites demi-tour vers la place.")
        if choix=="NON":
            reponse="True"
            print("")
            ecrit("Vous prenez conscience de l'urgence de la situation et préférez y aller directement.")
    ecrit("Une fois arrivé sur place, vous apercevez les gardes qui tirent en direction d'une forme gigantesque dans le ciel. À mesure que vos yeux s'habituent à la lumière aveuglante du Soleil, vous réalisez que cette forme est celle d'un dragon et pas n'importe lequel : Balarion, le Seigneur des Dragons.")
    ecrit("En observant ses griffes, vous comprenez immédiatement la situation : il a kidnappé le Roi. À peine avez vous eu le temps de le réaliser que Balarion s'envole déjà vers la Montagne pour rejoindre son antre. ")
    ecrit("Quelques heures seulement après, à la suite d'une réunion du Conseil, son représentant, Romain, s'approche de l'assistance encore sous le choc :'Afin de maintenir la stabilité du royaume, le Prince Leon assumera les fonctions. Quant à notre bien-aimé Souverain, nous avons décidé d'envoyer les nouveaux chevaliers")
    ecrit("à sa recherche. Ils devront parcourir le Royaume, traverser Forêts et Marais, et affronter tous les obstacles qui s'opposerons à eux en trouvant de l'équipement sur leur route, faute d'Armurerie. Gloire et richesse s'offfreront à celui qui ramènera notre Souverain !!'")
    ecrit("À peine le Conseil eut-il fini son annonce, que vous vous empressez de partir à l'Aventure...")

def combat_final():
    print("Vous arrivez à l'entrée de la grotte du Seigneur des Dragons. Vous avancez à pas feutrés et vous trouvez l'imposant dragon en pleine digestion.",end=" ")
    if Perso.arme1=="Arc":
        print("Vous repérez un immense stalactite au-dessus de sa tête. Vous bandez donc votre Arc, tirez sur le pic qui vient s'empaler dans le crâne du Dragon.",end=" ")
    if Perso.arme1=="Epée une main" or Perso.arme1=="Epée deux mains":
        print("Vous prenez votre courage à deux mains, vous vous glissez entre ses pattes et lui plantez votre Épée dans le coeur puis lui ouvrez le ventre pour accélérer sa mort.",end=" ")
    if Perso.arme1=="Dague":
        print("Vous vous approchez silencieusement vers son oeil et, muni de votre dague, l'y la lui plantez jusqu'au cerveau.",end=" ")
    print("Surpris dans son sommeil, Balarion n'a que le temps d'expirer avant de s'étendre à jamais.")
    print("***Gain d'une tête de Balarion***")
    inventaire=Perso.inventaire
    inventaire.append("Tête de Balarion")
    Perso.inventaire=inventaire
    print("En avançant vers le fond de la caverne, vous apercevez deux chemins. Lequel voulez-vous prendre ? ||GAUCHE|| ou ||DROITE||")
    reponse="False"
    while reponse=="False":
        choix=input("")
        if choix=="GAUCHE":
            print("Vous prenez le chemin de gauche et vous tomber sur un tas d'ossements d'humain, de bétail, de gobelin et de troll. Vous faites donc demi-tour et prenez l'autre chemin.",end=" ")
            reponse="True"
        if choix=="DROITE":
            print("Vous prenez le chemin de droite et vous tomber sur un tas d'osement d'humain, de bétail, de gobelin et de troll. Vous faites donc demi-tour et prenez l'autre chemin.",end=" ")
            reponse="True"
    print("Vous trouvez alors, après plusieurs mois d'aventure, le Roi Auréus 1er, affaiblit par tout ce temps de captivité. Vous lui donnez un peu de viande de dragon et vous entamez le voyage retour. Avec l'expérience accumulée au fil du voyage, vous ne faites qu'une bouchée",end=" ")
    print("des créatures qui vous attaquent sur le retour. Une fois arrivé aux portes de la Capitale, les gardes vous ouvrent et vous entrez sous les acclamations de la foule qui scande votre nom :","'",Perso.name,"!",Perso.name,"!",Perso.name,"!'",end="")
    print("Quelques mois après, le roi, de nouveau en plein santé, vous accueille lors d'une grande cérémonie où il vous nomme héros national et général des armées du Royaume. Cela marque le début de prochaines aventures ...")
    print("")
    print("Félicitiation pour avoir terminé le jeu. Vous avez réussi à sauver le Roi et à éliminer Balarion mais que ce serait-il passé si vous aviez fait d'autres choix ?")
    print("Voulez vous voir les CREDITS ?")
    reponse_inutilse=input("")
    print("Peu importe votre réponse vous allez les avoir")
