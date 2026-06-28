from datetime import date
# Gère les présences des élèves du daara.
def gerer_presences(eleves):
    # Vérifie s'il y a des élèves
    if len(eleves) == 0:
        print("Aucun élève inscrit.")
        return
    # Date du jour
    date_jour = date.today().strftime("%d/%m/%Y")
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
        while statut_presence not in ["P","p","A","a"]:
           statut_presence = input("Entrer P ou A : ")
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
# Tableau des présences 
presences = []