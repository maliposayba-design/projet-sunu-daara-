def menu():

    print("\n=============================")
    print(" Gestion du Daara")
    print("=============================")

    print("1. Ajouter un élève")
    print("2. Enregistrer les sourates")
    print("3. Évaluer la progression")
    print("4. Afficher le classement")
    print("5. Gérer les présences")
    print("6. Afficher les élèves")
    print("7. Générer certificat")
    print("8. Quitter")

    return input("Votre choix : ")
def vider_ecran():
    import os
    os.system("cls" if os.name == "nt" else "clear")    
