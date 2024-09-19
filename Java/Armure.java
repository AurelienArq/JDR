public class Armure {
    private String nom;
    private int protection;
    private int identifiant;

    // Constructeur
    public Armure(String nom, int protection) {
        this.nom = nom;
        this.protection = protection;
        this.identifiant = -1; // Valeur par défaut si non fourni
    }

    // Constructeur avec identifiant
    public Armure(String nom, int protection, int identifiant) {
        this.nom = nom;
        this.protection = protection;
        this.identifiant = identifiant;
    }

    // Getters et Setters
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public int getProtection() {
        return protection;
    }

    public void setProtection(int protection) {
        this.protection = protection;
    }

    public int getIdentifiant() {
        return identifiant;
    }

    public void setIdentifiant(int identifiant) {
        this.identifiant = identifiant;
    }

    // Méthode pour afficher les détails de l'armure
    public void afficherDetails() {
        System.out.println("Nom : " + nom);
        System.out.println("Protection : " + protection);
        if (identifiant != -1) {
            System.out.println("Identifiant : " + identifiant);
        }
    }
}
