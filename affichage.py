from calendrier_bonus import afficher_examens
from calendrier_bonus import ajouter_examen
from calendrier_bonus import rechercher_par_date
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
    print("8. gestion des examens")
    print("9. Quitter")
    return input("Votre choix : ")

# Menu principal exam
def menu_exam():
    continuer = True

    while continuer:
     print("\n===== GESTION DES EXAMENS D'UN DAARA =====")
     print("1. Ajouter un examen")
     print("2. Afficher les examens")
     print("3. Rechercher par date")
     print("4. revenir au menu princpal")

     choix = input("Votre choix : ")

     if choix == "1":
         ajouter_examen()
         input("\nAppuyez sur Entree pour continuer...")
         vider_ecran()
     elif choix == "2":
         afficher_examens()
         input("\nAppuyez sur Entree pour continuer...")
         vider_ecran()
     elif choix == "3":
         rechercher_par_date()
         input("\nAppuyez sur Entree pour continuer...")
         vider_ecran()
     elif choix == "4":
         continuer = False
         vider_ecran()
     else:
         print("Choix invalide.")
         input("\nAppuyez sur Entree pour continuer...")
         vider_ecran()
def vider_ecran():
    import os
    os.system("cls" if os.name == "nt" else "clear")    
