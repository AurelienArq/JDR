public abstract class Lieu {
    private String nom;
    private int difficulte;

    public Lieu(String nom, int difficulte) {
        this.nom = nom;
        this.difficulte = difficulte;
    }

    public String getNom() {
        return nom;
    }

    public int getDifficulte() {
        return difficulte;
    }

    public abstract void interagir(Personnage perso);
    protected void coffre() {
        // Implémenter la logique pour gérer le coffre
    }

    protected int combat(Personnage perso, Ennemi ennemi, int temps2) {
        // Implémenter la logique pour gérer le combat
        return temps2;
    }
}
