# 20. Greedy (Algorithmes Gloutons) — Code, Astuces et Pièges

## 1. Templates Python (Prêts à exécuter)

### Template A : Tri Glouton + Deux Pointeurs (Appariement optimal)
Idéal lorsque l'on doit associer des ressources limitées à des demandes (`Assign Cookies`).

```python
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
```

### Template B : Tri par Ratio / Valeur Décroissante (Sac à dos fractionnaire)
Idéal pour maximiser une capacité fixe en prenant les éléments les plus rentables en premier (`Maximum Units on a Truck`).

```python
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
```

### Template C : Profit Cumulé sur Variations Positives
Idéal pour capter tous les gains locaux successifs (`Best Time to Buy and Sell Stock II`).

```python
def profit_maximum_illimite(prix: list[int]) -> int:
    profit = 0
    for i in range(1, len(prix)):
        if prix[i] > prix[i - 1]:
            profit += prix[i] - prix[i - 1]
    return profit


if __name__ == "__main__":
    cours = [7, 1, 5, 3, 6, 4]
    print("Profit total :", profit_maximum_illimite(cours))  # Attendu : 7 (4 + 3)
```

## 2. Trucs et Astuces (Bibliothèque Standard)
* **Trier sur mesure avec `key=lambda` :** En glouton, 80 % du travail consiste à trouver le bon critère de tri. Utilise `items.sort(key=lambda x: x[1])` pour trier en place sans allouer de mémoire supplémentaire.
* **Vérifier les bords avec des sentinelles :** Pour des problèmes de placement linéaire (comme `Can Place Flowers`), traiter les bords `i == 0` et `i == len(arr) - 1` proprement avec `(i == 0 or arr[i - 1] == 0)` évite de dupliquer le code.
* **Vote de Boyer-Moore (`169. Majority Element`) :** Pour trouver un élément présent plus de $n/2$ fois en $O(1)$ d'espace, maintiens un `candidat` et un `compteur` (+1 si égal, -1 sinon, changement de candidat si compteur à 0).

## 3. Pièges à Éviter
* **Appliquer le glouton sans vérifier la propriété de choix optimal :** Teste toujours un petit contre-exemple mental avant de coder. Si un choix local peut bloquer la seule solution globale valide, passe à la Programmation Dynamique ou au Backtracking.
* **Oublier de trier avant de boucler :** Beaucoup d'énoncés donnent les tableaux dans le désordre. Assure-toi que le tri ne casse pas une contrainte d'ordre chronologique imposée par l'énoncé (ex: dans `Lemonade Change`, les clients arrivent dans un ordre fixe, il ne faut surtout **pas** trier !).
