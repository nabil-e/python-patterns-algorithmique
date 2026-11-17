def distribuer_biscuits(enfants: list[int], biscuits: list[int]) -> int:
    enfants.sort()
    biscuits.sort()

    i = 0  # Pointeur sur les enfants
    j = 0  # Pointeur sur les biscuits

    while i < len(enfants) and j < len(biscuits):
        if biscuits[j] >= enfants[i]:
            i += 1  # L'enfant est satisfait
        j += 1  # On passe au biscuit suivant dans tous les cas

    return i


if __name__ == "__main__":
    enfants = [1, 2, 3]
    biscuits = [1, 1]
    print("Enfants satisfaits :", distribuer_biscuits(enfants, biscuits))  # Attendu : 1

def max_unites_camion(boites: list[list[int]], taille_camion: int) -> int:
    # Trier par nombre d'unités par boîte (index 1) en ordre décroissant
    boites.sort(key=lambda x: x[1], reverse=True)

    unites_totales = 0
    for nb_boites, unites_par_boite in boites:
        boites_prises = min(taille_camion, nb_boites)
        unites_totales += boites_prises * unites_par_boite
        taille_camion -= boites_prises

        if taille_camion == 0:
            break

    return unites_totales


if __name__ == "__main__":
    boites = [[1, 3], [2, 2], [3, 1]]
    capacite = 4
    print("Unités max :", max_unites_camion(boites, capacite))  # Attendu : 8

def profit_maximum_illimite(prix: list[int]) -> int:
    profit = 0
    for i in range(1, len(prix)):
        if prix[i] > prix[i - 1]:
            profit += prix[i] - prix[i - 1]
    return profit


if __name__ == "__main__":
    cours = [7, 1, 5, 3, 6, 4]
    print("Profit total :", profit_maximum_illimite(cours))  # Attendu : 7 (4 + 3)
