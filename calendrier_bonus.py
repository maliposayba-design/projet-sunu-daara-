# Liste qui va contenir les examens
calendrier = []

# Fonction pour ajouter un examen
def ajouter_examen():
    matiere = input("Nom de l'examen : ").strip()
 
    if matiere == "":
      print("Nom invalide.")
      return
    date = input("Date (JJ/MM/AAAA) : ").strip()
    heure = input("Heure (HH:MM) : ").strip()

    examen = {
        "matiere": matiere,
        "date": date,
        "heure": heure
    }

    calendrier.append(examen)
    print("Examen ajouté avec succès !\n")

# Fonction pour afficher tous les examens
def afficher_examens():
    if len(calendrier) == 0:
        print("Aucun examen enregistré.\n")
    else:
        print("\n===== CALENDRIER DES EXAMENS =====")
        for i, examen in enumerate(calendrier, start=1):
            print(f"{i}. {examen['matiere']}")
            print(f"   Date : {examen['date']}")
            print(f"   Heure : {examen['heure']}")
            print("--------------------------")

# Fonction pour rechercher un examen par date
def rechercher_par_date():
    date = input("Entrez la date recherchée : ")

    trouve = False
    for examen in calendrier:
        if examen["date"] == date:
            print(f"\nExamen : {examen['matiere']}")
            print(f"Heure : {examen['heure']}")
            trouve = True

    if not trouve:
        print("Aucun examen trouvé à cette date.")
