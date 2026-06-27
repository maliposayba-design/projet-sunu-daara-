def generer_certificat(eleve):

    print("\n==============================")
    print(" CERTIFICAT DE FIN D'ÉTUDE")
    print("==============================")

    print("Nom :", eleve["nom"])
    print("Niveau atteint :", eleve["niveau"])

    if eleve["niveau"] == 5:
        print("Statut : Formation terminée")
    else:
        print("Statut : En cours")

    print("\nFélicitations !")