public class Arme {
    private String nom;
    private int degats;
    private int defense;
    private int poids;
    private int identifiant;

    // Constructeur
    public Arme(String nom, int degats, int defense, int poids) {
        this.nom = nom;
        this.degats = degats;
        this.defense = defense;
        this.poids = poids;
        this.identifiant = -1; // Valeur par défaut si non fourni
    }

    // Constructeur avec identifiant
    public Arme(String nom, int degats, int defense, int poids, int identifiant) {
        this.nom = nom;
        this.degats = degats;
        this.defense = defense;
        this.poids = poids;
        this.identifiant = identifiant;
    }

    // Getters et Setters
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public int getDegats() {
        return degats;
    }

    public void setDegats(int degats) {
        this.degats = degats;
    }

    public int getDefense() {
        return defense;
    }

    public void setDefense(int defense) {
        this.defense = defense;
    }

    public int getPoids() {
        return poids;
    }

    public void setPoids(int poids) {
        this.poids = poids;
    }

    public int getIdentifiant() {
        return identifiant;
    }

    public void setIdentifiant(int identifiant) {
        this.identifiant = identifiant;
    }

    // Méthode pour afficher les détails de l'arme
    public void afficherDetails() {
        System.out.println("Nom : " + nom);
        System.out.println("Dégâts : " + degats);
        System.out.println("Défense : " + defense);
        System.out.println("Poids : " + poids);
        if (identifiant != -1) {
            System.out.println("Identifiant : " + identifiant);
        }
    }
}
