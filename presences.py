    #Gère les présences des élèves du daara.
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
    for i in range(len(eleves)):
        eleve = eleves[i]
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
# Tableau des élèves (exemple avec 3 élèves)
eleves = [
    {"nom": "Aïssatou Diop", "niveau": 1},
    {"nom": "Moussa Ndiaye", "niveau": 2},
    {"nom": "Fatou Sow", "niveau": 3}
]
# Tableau des présences (vide au départ)
presences = []
# Appel de la fonction
gerer_presences()