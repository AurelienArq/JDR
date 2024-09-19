public class Auberge extends Batiment {
    public Auberge() {
        super("Auberge");
    }

    @Override
    public void interaction() {
        System.out.println("Bienvenue à l'Auberge. Voulez-vous vous reposer ?");
        // Code pour restaurer les points de vie
    }
}
