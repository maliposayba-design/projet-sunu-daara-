# Ajouter des élèves
def ajouter_eleves():
    print("=== AJOUT DES ÉLÈVES ===")
    print("Laissez le nom vide et appuyez sur Entrée pour terminer.\n")
    
    while True:
        nom = input("Nom de l'élève : ")
        if nom == "":
            break
        age = input("Âge de l'élève : ")
        date_inscription = input("Date d'inscription (JJ/MM/AAAA) : ")
        
        eleve = {
            "id": len(eleves) + 1,
            "nom": nom,
            "age": age,
            "date_inscription": date_inscription
        }
        eleves.append(eleve)
        print(f" {nom} ajouté !\n")
    
    if len(eleves) == 0:
        print("Aucun élève ajouté.")
    else:
        print(f"\n{len(eleves)} élève(s) ajouté(s).\n")
# Gère les présences des élèves du daara.
def gerer_presences():
    # Vérifie s'il y a des élèves
    if len(eleves) == 0:
        print("Aucun élève inscrit.")
        return
    # Date du jour
    date_jour = "26/06/2026"
    print(f"\n=== PRÉSENCES DU {date_jour} ===")
    print("P = Présent, A = Absent\n")
    # Compteurs
    presents = 0
    absents = 0
    # Boucle for : parcourt chaque élève
    for eleve in eleves:
        print(f"[{eleve['id']}] {eleve['nom']} | Âge : {eleve['age']} ans | Inscrit le : {eleve['date_inscription']}")
        # Demande la présence
        statut_presence = input(f"{eleve['nom']} [P/A] : ")
        # Affiche le statut de présence
        if statut_presence == "P" or statut_presence == "p":
            presents = presents + 1
            print("Présent")
        else:
            absents = absents + 1
            print("Absent")
        # Enregistre la présence dans le tableau
        presence = {
            "date": date_jour,
            "eleve": eleve["nom"],
            "present": (statut_presence == "P" or statut_presence == "p")
        }
        presences.append(presence)
    # Affiche le statut de présence
    print(f"\n=== STATUT DE PRÉSENCE ===")
    print(f"Présents : {presents}")
    print(f"Absents  : {absents}")
    print(f"Total    : {presents + absents}")
# Tableau des élèves 
eleves = []
# Tableau des présences 
presences = []
# Gérer l'ajout des élèves
ajouter_eleves()
# Gérer les présences
gerer_presences()