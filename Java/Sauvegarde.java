import java.io.*;
import java.util.List;
import java.util.ArrayList;

public class Sauvegarde {

    // Méthode pour sauvegarder les données dans un fichier texte
    public static void sauvegarderJeu(String nomFichier, Personnage perso, List<Ennemi> ennemis, List<Arme> armes, List<Armure> armures, List<Consommable> consommables) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(nomFichier))) {
            // Sauvegarde du personnage
            writer.write("Personnage\n");
            writer.write(perso.getNom() + "," + perso.getPv() + "," + perso.getForce() + "," + perso.getDefense() + "," + perso.getVitesse() + "\n");

            // Sauvegarde des ennemis
            writer.write("Ennemis\n");
            for (Ennemi ennemi : ennemis) {
                writer.write(ennemi.getNom() + "," + ennemi.getPv() + "," + ennemi.getForce() + "," + ennemi.getDefense() + "\n");
            }

            // Sauvegarde des armes
            writer.write("Armes\n");
            for (Arme arme : armes) {
                writer.write(arme.getNom() + "," + arme.getDegats() + "," + arme.getPortee() + "\n");
            }

            // Sauvegarde des armures
            writer.write("Armures\n");
            for (Armure armure : armures) {
                writer.write(armure.getNom() + "," + armure.getDefense() + "\n");
            }

            // Sauvegarde des consommables
            writer.write("Consommables\n");
            for (Consommable conso : consommables) {
                writer.write(conso.getNom() + "," + conso.getSoin() + "\n");
            }

            System.out.println("Sauvegarde réussie dans " + nomFichier);
        } catch (IOException e) {
            System.out.println("Erreur lors de la sauvegarde : " + e.getMessage());
        }
    }

    // Méthode pour charger les données depuis un fichier texte
    public static void chargerJeu(String nomFichier, Personnage perso, List<Ennemi> ennemis, List<Arme> armes, List<Armure> armures, List<Consommable> consommables) {
        try (BufferedReader reader = new BufferedReader(new FileReader(nomFichier))) {
            String ligne;
            String section = "";

            while ((ligne = reader.readLine()) != null) {
                if (ligne.equals("Personnage")) {
                    section = "Personnage";
                } else if (ligne.equals("Ennemis")) {
                    section = "Ennemis";
                } else if (ligne.equals("Armes")) {
                    section = "Armes";
                } else if (ligne.equals("Armures")) {
                    section = "Armures";
                } else if (ligne.equals("Consommables")) {
                    section = "Consommables";
                } else {
                    String[] data = ligne.split(",");
                    switch (section) {
                        case "Personnage":
                            perso.setNom(data[0]);
                            perso.setPv(Integer.parseInt(data[1]));
                            perso.setForce(Integer.parseInt(data[2]));
                            perso.setDefense(Integer.parseInt(data[3]));
                            perso.setVitesse(Integer.parseInt(data[4]));
                            break;
                        case "Ennemis":
                            Ennemi ennemi = new Ennemi(data[0], Integer.parseInt(data[1]), Integer.parseInt(data[2]), Integer.parseInt(data[3]));
                            ennemis.add(ennemi);
                            break;
                        case "Armes":
                            Arme arme = new Arme(data[0], Integer.parseInt(data[1]), Integer.parseInt(data[2]));
                            armes.add(arme);
                            break;
                        case "Armures":
                            Armure armure = new Armure(data[0], Integer.parseInt(data[1]));
                            armures.add(armure);
                            break;
                        case "Consommables":
                            Consommable consommable = new Consommable(data[0], Integer.parseInt(data[1]));
                            consommables.add(consommable);
                            break;
                    }
                }
            }
            System.out.println("Chargement réussi depuis " + nomFichier);
        } catch (IOException e) {
            System.out.println("Erreur lors du chargement : " + e.getMessage());
        }
    }
}
