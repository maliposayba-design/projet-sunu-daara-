from progression import evaluer_progression
def generer_certificat(eleve):
    niveau = evaluer_progression(eleve)
    if niveau == 5:

        print("\n========================")
        print("CERTIFICAT DE FIN D'ÉTUDES DU DAARA")
        print("========================")

        print("Nom :", eleve["nom"])
        print("Niveau :", niveau)

        print("\nFélicitations pour être arrivé/e à la fin de vos études!")
    else:
        print(
            "Certificat indisponible : "
            "niveau final non atteint."
        )