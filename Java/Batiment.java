public class Batiment {
    protected String nom;

    public Batiment(String nom) {
        this.nom = nom;
    }

    public String getNom() {
        return nom;
    }

    // Méthode d'interaction par défaut
    public void interaction() {
        System.out.println("Vous êtes dans " + nom + ". Que voulez-vous faire ?");
    }
}
