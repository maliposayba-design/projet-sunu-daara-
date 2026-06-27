from datetime import date
# Importe l'outil date pour récupérer la date d'aujourd'hui


def calcul_duree(eleve):

    # Récupère la date actuelle
    aujourdhui = date.today()

    # Sépare la date d'inscription
    # Ex : "17/06/2025"
    # devient :
    # jour = 17
    # mois = 6
    # annee = 2025
    jour, mois, annee = map(
        int,
        eleve["date_inscription"].split("/")
    )
      #split() → découpe
      # map() → convertit
      #jour, mois, annee = → stocke
      # Calcul de la durée en mois
    duree = (
        (aujourdhui.year - annee) * 12
        + (aujourdhui.month - mois)
    )

    return duree

def evaluer_progression(eleve, duree):

    if eleve["sourates"] >0 and eleve["sourates"]<=1 and duree<=3:
        niveau = 1

    elif eleve["sourates"] >1 and eleve["sourates"]<=3 and duree>3 and duree<=6:
        niveau = 2

    elif eleve["sourates"]>3 and eleve["sourates"]<=30 and duree>6 and duree<=12:
        niveau = 3
 
    elif eleve["sourates"] >30 and eleve["sourates"]<114 and duree>12 and duree<=24:
        niveau = 4

    elif eleve["sourates"]==114 and duree>24 and duree<=36:
        niveau = 5
    
    else:
        print("progression anormale")
    return niveau