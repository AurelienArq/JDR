public class Consommable {
    private String nom;
    private int valeur;

    // Constructeur
    public Consommable(String nom, int valeur) {
        this.nom = nom;
        this.valeur = valeur;
    }

    // Getters et Setters
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public int getValeur() {
        return valeur;
    }

    public void setValeur(int valeur) {
        this.valeur = valeur;
    }

    // Méthode pour afficher les détails du consommable
    public void afficherDetails() {
        System.out.println("Nom : " + nom);
        System.out.println("Valeur : " + valeur);
    }
}
