def compter(liste):
    """Compte le nombre d'éléments dans une liste (comme len)"""
    compteur = 0
    for element in liste:
        compteur = compteur + 1
    return compteur

def afficher_classement(eleves):
    """Affiche le classement des élèves"""
    if compter(eleves) == 0:
        print("Aucun élève à classer.")
        return
    eleves_a_trier = []
    for eleve in eleves:
        eleves_a_trier.append(eleve)
    for i in range(compter(eleves_a_trier)):
        for j in range(compter(eleves_a_trier) - 1):
            # Compter les sourates de chaque élève
            nb1 = eleves_a_trier[j]["sourates"]
            nb2 = eleves_a_trier[j + 1]["sourates"]
            if nb1 < nb2:
                temp = eleves_a_trier[j]
                eleves_a_trier[j] = eleves_a_trier[j + 1]
                eleves_a_trier[j + 1] = temp
            elif nb1 == nb2:
                if eleves_a_trier[j]["nom"] > eleves_a_trier[j + 1]["nom"]:
                    temp = eleves_a_trier[j]
                    eleves_a_trier[j] = eleves_a_trier[j + 1]
                    eleves_a_trier[j + 1] = temp
    print("\n CLASSEMENT DES ÉLÈVES")
    for i in range(compter(eleves_a_trier)):
        eleve = eleves_a_trier[i]
        nb = eleve["sourates"]
        print(str(i + 1) + ". " + eleve["nom"] + " - " + str(nb) + " sourates")