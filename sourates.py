def enregistrer_sourates(eleve):
    print("\n--- ENREGISTRER UNE SOURATE APPRISE ---")
    print("Élève actuel :", eleve["nom"])
    print("Nombre actuel de sourates :", eleve["sourates"])
    
    # 1. On demande le nom de la sourate mémorisée
    nom_sourate = input("Entrez le nom de la sourate mémorisée : ")
    if nom_sourate == "":
         print("Nom de sourate invalide.")
         return
    if eleve["sourates"] >= 114:
     print("Toutes les sourates sont déjà enregistrées.")
     return
    
    # 2. Ta logique : on prend la valeur actuelle et on fait + 1
    eleve["sourates"] = eleve["sourates"] + 1
    
    print("Bravo ! La sourate", nom_sourate, "a été ajoutée.")
    print("Nouveau total de sourates :", eleve["sourates"], "\n")