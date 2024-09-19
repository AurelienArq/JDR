public class Boutique extends Batiment {
    public Boutique() {
        super("Boutique");
    }

    @Override
    public void interaction() {
        System.out.println("Bienvenue à la Boutique. Voulez-vous acheter des objets ?");
        // Code pour acheter des objets
    }
}
