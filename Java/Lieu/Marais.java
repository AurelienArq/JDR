public class Marais extends Lieu {

    public Marais() {
        super("Marais", 2); // Difficulté facile
    }

    @Override
    public void interagir(Personnage perso) {
        System.out.println("Vous décidez d'explorer le marais.");
        System.out.println("");

        int temps = 1;
        int tempsSejour = new Random().nextInt(5) + 1;

        while (temps <= tempsSejour) {
            temps += evenement("Marais", perso);
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
            case "Crocodile":
                System.out.println("Un crocodile vous attaque.");
                temps2 = combat(perso, new Crocodile(), temps2);
                break;
            case "Gobelin":
                System.out.println("Un gobelin vous attaque.");
                temps2 = combat(perso, new Gobelin(), temps2);
                break;
            case "Repos":
                System.out.println("Vous trouvez un endroit pour vous reposer.");
                System.out.println("Voulez-vous vous y arrêter pour vous reposer ? || OUI || || NON ||");
                String choix = new Scanner(System.in).nextLine();
                if (choix.equalsIgnoreCase("OUI")) {
                    System.out.println("Vous vous reposez et regagnez des PV.");
                    perso.changement(10, 0);
                } else {
                    System.out.println("Vous continuez votre route.");
                }
                break;
        }
        System.out.println("");
        return temps2;
    }
}