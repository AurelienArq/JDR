import java.util.Random;

public class Evenement {
    private String description;
    private int probabilite;

    // Constructeur
    public Evenement(String description, int probabilite) {
        this.description = description;
        this.probabilite = probabilite;
    }

    // Getters et Setters
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public int getProbabilite() {
        return probabilite;
    }

    public void setProbabilite(int probabilite) {
        this.probabilite = probabilite;
    }

    // Méthode pour générer un événement aléatoire basé sur la probabilité
    public boolean declencherEvenement() {
        Random rand = new Random();
        int tirage = rand.nextInt(100);  // Génère un nombre aléatoire entre 0 et 99
        return tirage < probabilite;
    }

    // Affichage des détails de l'événement
    public void afficherEvenement() {
        System.out.println("Description de l'événement : " + description);
        System.out.println("Probabilité de déclenchement : " + probabilite + "%");
    }
}
