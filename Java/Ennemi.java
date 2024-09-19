import java.util.List;

public class Ennemi {
    private String nom;
    private int pointsDeVie;
    private int niveau;
    private List<Object> objets;
    private int attaque;
    private int defense;
    private int vitesse;
    private int experience;

    // Constructeur
    public Ennemi(String nom, int pointsDeVie, int niveau, List<Object> objets, int attaque, int defense, int vitesse, int experience) {
        this.nom = nom;
        this.pointsDeVie = pointsDeVie;
        this.niveau = niveau;
        this.objets = objets;
        this.attaque = attaque;
        this.defense = defense;
        this.vitesse = vitesse;
        this.experience = experience;
    }

    // Constructeur avec valeurs par défaut
    public Ennemi(String nom, int pointsDeVie, int niveau, List<Object> objets, int attaque) {
        this(nom, pointsDeVie, niveau, objets, attaque, 0, 0, 0);
    }

    // Getters et Setters
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public int getPointsDeVie() {
        return pointsDeVie;
    }

    public void setPointsDeVie(int pointsDeVie) {
        this.pointsDeVie = pointsDeVie;
    }

    public int getNiveau() {
        return niveau;
    }

    public void setNiveau(int niveau) {
        this.niveau = niveau;
    }

    public List<Object> getObjets() {
        return objets;
    }

    public void setObjets(List<Object> objets) {
        this.objets = objets;
    }

    public int getAttaque() {
        return attaque;
    }

    public void setAttaque(int attaque) {
        this.attaque = attaque;
    }

    public int getDefense() {
        return defense;
    }

    public void setDefense(int defense) {
        this.defense = defense;
    }

    public int getVitesse() {
        return vitesse;
    }

    public void setVitesse(int vitesse) {
        this.vitesse = vitesse;
    }

    public int getExperience() {
        return experience;
    }

    public void setExperience(int experience) {
        this.experience = experience;
    }

    // Méthode pour afficher les détails de l'ennemi
    public void afficherDetails() {
        System.out.println("Nom : " + nom);
        System.out.println("Points de Vie : " + pointsDeVie);
        System.out.println("Niveau : " + niveau);
        System.out.println("Objets : " + objets);
        System.out.println("Attaque : " + attaque);
        System.out.println("Défense : " + defense);
        System.out.println("Vitesse : " + vitesse);
        System.out.println("Experience : " + experience);
    }
}
