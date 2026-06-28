from eleves import ajouter_eleve
from eleves import afficher_eleves
import eleves

from sourates import enregistrer_sourates
from progression import evaluer_progression
from classement import afficher_classement
from presences import gerer_presences
from certificat_bonus import generer_certificat

from affichage import vider_ecran
from affichage import menu
continuer = True

while continuer:

    choix = menu()

    if choix == "1":
         ajouter_eleve()
         input("\nAppuyez sur Entree pour continuer...")
         vider_ecran()
    elif choix == "2":
        afficher_eleves()
        id_eleve = int(input("ID élève : "))

        trouve = False

        for eleve in eleves.eleves:

         if eleve["id"] == id_eleve:
             trouve = True
             enregistrer_sourates(eleve)
         if trouve == False:
           print("Élève introuvable.")
        input("\nAppuyez sur Entree pour continuer...")
        vider_ecran()

    elif choix == "3":
        afficher_eleves()
        id_eleve = int(input("ID élève : "))

        for eleve in eleves.eleves:

            if eleve["id"] == id_eleve:
                  trouve = True
                  niveau = evaluer_progression(eleve)
                  print( "Niveau :", niveau)
            if trouve == False:
             print("Élève introuvable.")
        input("\nAppuyez sur Entree pour continuer...")
        vider_ecran()
    elif choix == "4":
        afficher_classement(eleves.eleves)
        input("\nAppuyez sur Entree pour continuer...")
        vider_ecran()
    elif choix == "5":
        gerer_presences(eleves.eleves)
        input("\nAppuyez sur Entree pour continuer...")
        vider_ecran()
    elif choix == "6":

        afficher_eleves()
        input("\nAppuyez sur Entree pour continuer...")
        vider_ecran()
    elif choix == "7":
        afficher_eleves()
        id_eleve = int(
            input(
                "ID élève : "
            )
        )

        for eleve in eleves.eleves:

            if eleve["id"] == id_eleve:
                 trouve = True
                 niveau = (evaluer_progression( eleve))
                 if niveau == 5:
                    generer_certificat(eleve)
                 else:
                    print("Niveau requis non atteint.")
            if trouve == False:
             print("Élève introuvable.")
        input("\nAppuyez sur Entree pour continuer...")
        vider_ecran()
    elif choix == "8":
        print("Au revoir !")
        continuer = False
        input("\nAppuyez sur Entree pour continuer...")
        vider_ecran()
    else:
        print( "Choix invalide.")