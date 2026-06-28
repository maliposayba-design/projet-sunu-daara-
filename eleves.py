# ============================================
#   Gestion du Daara - Partie : Ajout d'élèves
#   (Version avec listes et dictionnaires)
# ============================================

from datetime import date

# Liste qui stocke tous les élèves en mémoire
eleves = []

def ajouter_eleve():
    """Permet d'ajouter un nouvel élève au daara."""
    print("\n--- Ajouter un élève ---")

    # Saisie du nom
    nom = input("Nom de l'élève : ").strip()
    if nom == "":
        print("Erreur : le nom ne peut pas être vide.")
        return

    # Contrôle : le nom ne doit pas contenir de chiffres
    if any(c.isdigit() for c in nom):
        print("Erreur : le nom ne doit pas contenir de chiffres.")
        return

    # Saisie de l'âge
    age_saisi = input("Âge de l'élève : ")
    if not age_saisi.isdigit():
        print("Erreur : veuillez entrer un nombre pour l'âge.")
        return

    age = int(age_saisi)
    if age <= 0:
        print("Erreur : l'âge doit être un nombre positif.")
        return

    # Saisie manuelle de la date d'inscription
    date_inscription = input("Date d'inscription (ex: 28/06/2026) : ").strip()
    if date_inscription == "":
        print("Erreur : la date ne peut pas être vide.")
        return
    
    # Création du dictionnaire représentant l'élève
    eleve = {
        "id": len(eleves) + 1,
        "nom": nom,
        "age": age,
        "date_inscription": date_inscription,
        "sourates": 0
    }

    # Ajout à la liste
    eleves.append(eleve)

    print("Élève '" + nom + "' ajouté avec succès (inscrit le " + date_inscription + ").")


def afficher_eleves():
    """Affiche tous les élèves enregistrés."""
    print("\n--- Liste des élèves ---")
    if not eleves:
        print("Aucun élève enregistré pour l'instant.")
        return

    for eleve in eleves:
        print("[" + str(eleve['id']) + "] " + eleve['nom'] + " | Âge : " + str(eleve['age']) + " ans | Inscrit le : " + eleve['date_inscription'])


