import java.util.List;

public class Quete {
    private String nom;
    private int niveauDifficulte;
    private String type;
    private int experienceRecompense;
    private List<String> lieux;

    // Constructeur
    public Quete(String nom, int niveauDifficulte, String type, int experienceRecompense, List<String> lieux) {
        this.nom = nom;
        this.niveauDifficulte = niveauDifficulte;
        this.type = type;
        this.experienceRecompense = experienceRecompense;
        this.lieux = lieux;
    }

    // Getters et Setters
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public int getNiveauDifficulte() {
        return niveauDifficulte;
    }

    public void setNiveauDifficulte(int niveauDifficulte) {
        this.niveauDifficulte = niveauDifficulte;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public int getExperienceRecompense() {
        return experienceRecompense;
    }

    public void setExperienceRecompense(int experienceRecompense) {
        this.experienceRecompense = experienceRecompense;
    }

    public List<String> getLieux() {
        return lieux;
    }

    public void setLieux(List<String> lieux) {
        this.lieux = lieux;
    }

    // Méthode pour afficher les détails de la quête
    public void afficherDetails() {
        System.out.println("Nom de la Quête : " + nom);
        System.out.println("Niveau de Difficulté : " + niveauDifficulte);
        System.out.println("Type de Quête : " + type);
        System.out.println("Expérience Récompensée : " + experienceRecompense);
        System.out.println("Lieux Associés : " + lieux);
    }
}
