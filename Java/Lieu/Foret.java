import java.util.List;
import java.util.Random;

public class Foret extends Lieu {

    public Foret() {
        super("Foret", 1); // Difficulté débutante
    }

    @Override
    public void interagir(Personnage perso) {
        System.out.println("Vous décidez d'aller explorer la forêt et vous vous enfoncez entre les arbres.");
        System.out.println("");

        int temps = 1;
        int tempsSejour = new Random().nextInt(5) + 1;

        while (temps <= tempsSejour) {
            temps += evenement("Foret", perso);
            temps++;
        }

        if (temps > 50) {
            System.out.println("Fin de l'exploration.");
        }
    }

    private int evenement(String type, Personnage perso) {
        List<String> evenements = Evenement.getEvenements(type);
        String action = evenements.get(new Random().nextInt(evenements.size()));
        int temps2 = 0;

        System.out.println(" ");
        System.out.println("▬".repeat(100));
        System.out.println(" ");
        switch (action) {
            case "Coffre":
                System.out.println("Vous avez trouvé un coffre.");
                coffre();
                break;
            case "Coffre2":
                System.out.println("Vous avez trouvé deux coffres.");
                coffre();
                System.out.println("Vous vous approchez du deuxième coffre.");
                coffre();
                break;
            case "Gobelin":
                System.out.println("Un Gobelin vous attaque.");
                temps2 = combat(perso, new Gobelin(), temps2);
                break;
            case "Bandit":
                System.out.println("Vous tombez dans une embuscade tendue par un bandit !");
                temps2 = combat(perso, new Bandit(), temps2);
                break;
            case "Crocodile":
                System.out.println("Un crocodile vous a choisi pour son prochain dîner.");
                temps2 = combat(perso, new Crocodile(), temps2);
                break;
            case "Chèvre":
                System.out.println("Une chèvre vous a pris pour cible.");
                temps2 = combat(perso, new Chevre(), temps2);
                break;
            case "Dragon":
                System.out.println("Vous avez réveillé un dragon.");
                temps2 = combat(perso, new Dragon(), temps2);
                break;
            case "Troll":
                System.out.println("Un troll vous a pris pour cible.");
                temps2 = combat(perso, new Troll(), temps2);
                break;
            case "Nain":
                System.out.println("Vous tombez sur le nain Guillaume en train de miner.");
                temps2 = combat(perso, new Nain(), temps2);
                break;
            case "Repos":
                System.out.println("Vous trouvez un magnifique emplacement pour vous reposer.");
                System.out.println("Voulez-vous vous y arrêter pour vous reposer ? || OUI || || NON ||");
                String choix = new Scanner(System.in).nextLine();
                if (choix.equalsIgnoreCase("OUI")) {
                    System.out.println("Fatigué, vous décidez d'installer le campement.");
                    System.out.println("***Gain de 10 PV***");
                    perso.changement(10, 0);
                } else {
                    System.out.println("Vous regorgez d'énergie et décidez de continuer votre route.");
                }
                break;
        }
        System.out.println("");
        return temps2;
    }