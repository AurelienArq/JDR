import java.util.ArrayList;
import java.util.List;

public class Personnage {
    private String nom;
    private int vie;
    private List<Consommable> inventaire;
    private int force;
    private int defense;
    private int magie;
    private int agilite;
    private int dexterite;
    private int endurance;
    private int niveau;
    private int experience;
    private int or;
    private int argent;
    private int pointsDeVieMax;
    private int pointsDeMagieMax;
    private int forceSpeciale;
    private int defenseSpeciale;
    private int agiliteSpeciale;
    private int dexteriteSpeciale;
    private int enduranceSpeciale;

    // Constructeur
    public Personnage(String nom, int vie, List<Consommable> inventaire) {
        this.nom = nom;
        this.vie = vie;
        this.inventaire = inventaire;
        this.force = 10; // Valeur par défaut
        this.defense = 10; // Valeur par défaut
        this.magie = 10; // Valeur par défaut
        this.agilite = 10; // Valeur par défaut
        this.dexterite = 10; // Valeur par défaut
        this.endurance = 10; // Valeur par défaut
        this.niveau = 1; // Valeur par défaut
        this.experience = 0; // Valeur par défaut
        this.or = 0; // Valeur par défaut
        this.argent = 0; // Valeur par défaut
        this.pointsDeVieMax = 100; // Valeur par défaut
        this.pointsDeMagieMax = 50; // Valeur par défaut
        this.forceSpeciale = 0; // Valeur par défaut
        this.defenseSpeciale = 0; // Valeur par défaut
        this.agiliteSpeciale = 0; // Valeur par défaut
        this.dexteriteSpeciale = 0; // Valeur par défaut
        this.enduranceSpeciale = 0; // Valeur par défaut
    }

    // Méthodes getter et setter
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public int getVie() {
        return vie;
    }

    public void setVie(int vie) {
        this.vie = vie;
    }

    public List<Consommable> getInventaire() {
        return inventaire;
    }

    public void setInventaire(List<Consommable> inventaire) {
        this.inventaire = inventaire;
    }

    public int getForce() {
        return force;
    }

    public void setForce(int force) {
        this.force = force;
    }

    public int getDefense() {
        return defense;
    }

    public void setDefense(int defense) {
        this.defense = defense;
    }

    public int getMagie() {
        return magie;
    }

    public void setMagie(int magie) {
        this.magie = magie;
    }

    public int getAgilite() {
        return agilite;
    }

    public void setAgilite(int agilite) {
        this.agilite = agilite;
    }

    public int getDexterite() {
        return dexterite;
    }

    public void setDexterite(int dexterite) {
        this.dexterite = dexterite;
    }

    public int getEndurance() {
        return endurance;
    }

    public void setEndurance(int endurance) {
        this.endurance = endurance;
    }

    public int getNiveau() {
        return niveau;
    }

    public void setNiveau(int niveau) {
        this.niveau = niveau;
    }

    public int getExperience() {
        return experience;
    }

    public void setExperience(int experience) {
        this.experience = experience;
    }

    public int getOr() {
        return or;
    }

    public void setOr(int or) {
        this.or = or;
    }

    public int getArgent() {
        return argent;
    }

    public void setArgent(int argent) {
        this.argent = argent;
    }

    public int getPointsDeVieMax() {
        return pointsDeVieMax;
    }

    public void setPointsDeVieMax(int pointsDeVieMax) {
        this.pointsDeVieMax = pointsDeVieMax;
    }

    public int getPointsDeMagieMax() {
        return pointsDeMagieMax;
    }

    public void setPointsDeMagieMax(int pointsDeMagieMax) {
        this.pointsDeMagieMax = pointsDeMagieMax;
    }

    public int getForceSpeciale() {
        return forceSpeciale;
    }

    public void setForceSpeciale(int forceSpeciale) {
        this.forceSpeciale = forceSpeciale;
    }

    public int getDefenseSpeciale() {
        return defenseSpeciale;
    }

    public void setDefenseSpeciale(int defenseSpeciale) {
        this.defenseSpeciale = defenseSpeciale;
    }

    public int getAgiliteSpeciale() {
        return agiliteSpeciale;
    }

    public void setAgiliteSpeciale(int agiliteSpeciale) {
        this.agiliteSpeciale = agiliteSpeciale;
    }

    public int getDexteriteSpeciale() {
        return dexteriteSpeciale;
    }

    public void setDexteriteSpeciale(int dexteriteSpeciale) {
        this.dexteriteSpeciale = dexteriteSpeciale;
    }

    public int getEnduranceSpeciale() {
        return enduranceSpeciale;
    }

    public void setEnduranceSpeciale(int enduranceSpeciale) {
        this.enduranceSpeciale = enduranceSpeciale;
    }

    // Méthode pour attaquer un ennemi
    public void attaquer(Ennemi ennemi) {
        int degats = this.force - ennemi.getDefense();
        if (degats > 0) {
            ennemi.recevoirDegats(degats);
            System.out.println(nom + " attaque " + ennemi.getNom() + " et lui inflige " + degats + " dégâts.");
        } else {
            System.out.println(nom + " attaque " + ennemi.getNom() + " mais ne lui inflige aucun dégât.");
        }
    }

    // Méthode pour recevoir des dégâts
    public void recevoirDegats(int degats) {
        this.vie -= degats;
        if (this.vie < 0) this.vie = 0;
        System.out.println(nom + " reçoit " + degats + " dégâts. Vie restante : " + vie);
    }

    // Méthode pour gagner de l'expérience
    public void gagnerExperience(int points) {
        this.experience += points;
        System.out.println(nom + " gagne " + points + " points d'expérience.");
        verifierNiveau();
    }

    // Méthode pour vérifier et augmenter le niveau
    private void verifierNiveau() {
        int experienceNiveauSuivant = niveau * 100; // Exemple : 100 points par niveau
        if (experience >= experienceNiveauSuivant) {
            niveau++;
            experience -= experienceNiveauSuivant;
            System.out.println(nom + " passe au niveau " + niveau + " !");
            // Augmenter les attributs du personnage, par exemple :
            force += 5;
            defense += 5;
            pointsDeVieMax += 10;
            pointsDeMagieMax += 5;
            vie = pointsDeVieMax; // Remettre les points de vie au maximum
        }
    }

    // Méthode pour utiliser un consommable
    public void utiliserConsommable(Consommable consommable) {
        if (inventaire.contains(consommable)) {
            this.vie += consommable.getSoin(); // Exemple d'utilisation
            if (this.vie > pointsDeVieMax) this.vie = pointsDeVieMax;
            inventaire.remove(consommable);
            System.out.println(nom + " utilise " + consommable.getNom() + " et récupère " + consommable.getSoin() + " points de vie.");
        } else {
            System.out.println("Consommable non trouvé dans l'inventaire.");
        }
    }

    // Méthode pour afficher l'inventaire
    public void afficherInventaire() {
        if (inventaire.isEmpty()) {
            System.out.println(nom + " n'a pas d'objets dans son inventaire.");
        } else {
            System.out.println("Inventaire de " + nom + " :");
            for (Consommable consommable : inventaire) {
                System.out.println("- " + consommable.getNom());
            }
        }
    }

    // Méthode pour se défendre
    public void seDefendre(Ennemi ennemi) {
        int degatsBloques = this.defense - ennemi.getAttaque();
        if (degatsBloques > 0) {
            System.out.println(nom + " se défend contre l'attaque de " + ennemi.getNom() + " et bloque " + degatsBloques + " dégâts.");
        } else {
            System.out.println(nom + " ne parvient pas à se défendre contre l'attaque de " + ennemi.getNom() + ".");
            recevoirDegats(ennemi.getAttaque());
        }
    }

    // Méthode pour afficher les statistiques du personnage
    public void afficherStatistiques() {
        System.out.println("Nom : " + nom);
        System.out.println("Niveau : " + niveau);
        System.out.println("Vie : " + vie + "/" + pointsDeVieMax);
        System.out.println("Force : " + force);
        System.out.println("Défense : " + defense);
        System.out.println("Magie : " + magie);
        System.out.println("Agilité : " + agilite);
        System.out.println("Dextérité : " + dexterite);
        System.out.println("Endurance : " + endurance);
        System.out.println("Expérience : " + experience);
        System.out.println("Or : " + or);
        System.out.println("Argent : " + argent);
    }
}
