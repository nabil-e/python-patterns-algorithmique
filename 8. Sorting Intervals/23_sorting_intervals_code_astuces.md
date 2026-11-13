# Sorting Intervals — Code Exécutable, Astuces et Pièges

## 1. Templates Python Prêts à Lancer

### Template A : Fusionner des intervalles qui se chevauchent
```python
def fusionner_intervalles(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    
    # Tri par heure de début croissante
    intervals.sort(key=lambda x: x[0])
    fusionnes = [intervals[0]]
    
    for debut, fin in intervals[1:]:
        dernier_fin = fusionnes[-1][1]
        if debut <= dernier_fin:
            # Chevauchement : on étend la fin du dernier intervalle
            fusionnes[-1][1] = max(dernier_fin, fin)
        else:
            fusionnes.append([debut, fin])
            
    return fusionnes

if __name__ == "__main__":
    entree = [[1, 3], [8, 10], [2, 6], [15, 18]]
    print("Intervalles fusionnés :", fusionner_intervalles(entree))
    # Sortie attendue : [[1, 6], [8, 10], [15, 18]]
```

### Template B : Intersection de deux listes d'intervalles (Two Pointers)
```python
def intersection_intervalles(firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
    i, j = 0, 0
    resultat = []
    
    while i < len(firstList) and j < len(secondList):
        debut = max(firstList[i][0], secondList[j][0])
        fin = min(firstList[i][1], secondList[j][1])
        
        if debut <= fin:
            resultat.append([debut, fin])
            
        # On avance le pointeur de l'intervalle qui se termine le premier
        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1
            
    return resultat

if __name__ == "__main__":
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    print("Intersections :", intersection_intervalles(A, B))
    # Sortie attendue : [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
```

### Template C : Minimum de flèches pour éclater des ballons (Tri par fin)
```python
def min_fleches(points: list[list[int]]) -> int:
    if not points:
        return 0
        
    # Tri glouton par extrémité droite croissante
    points.sort(key=lambda x: x[1])
    fleches = 1
    pos_fleche = points[0][1]
    
    for debut, fin in points[1:]:
        if debut > pos_fleche:
            fleches += 1
            pos_fleche = fin
            
    return fleches

if __name__ == "__main__":
    ballons = [[10, 16], [2, 8], [1, 6], [7, 12]]
    print("Minimum de flèches :", min_fleches(ballons))
    # Sortie attendue : 2
```

---

## 2. Trucs et Astuces Python
* **Tri par défaut sur les listes de paires :** En Python, `intervals.sort()` trie naturellement par le premier élément `x[0]`, puis départage en cas d'égalité par `x[1]`. Pas besoin de `lambda` si tu tries par début croissant.
* **Tri par fin explicite :** Pour trier par la fin, utilise `intervals.sort(key=lambda x: x[1])` qui est lisible et rapide en C.
* **Insérer un intervalle en $O(n)$ :** Si la liste est déjà triée (comme dans l'exercice **57**), découpe le problème en 3 boucles `while` séquentielles : tout ce qui finit avant `newInterval[0]`, tout ce qui chevauche `newInterval`, puis tout le reste.

---

## 3. Pièges à Éviter
* **Oublier `max()` lors de la fusion :** Si `[1, 10]` est suivi de `[2, 5]`, la nouvelle fin n'est pas `5`, mais `max(10, 5) = 10`.
* **Inégalité stricte vs large (`<` vs `<=`) :** Vérifie toujours dans l'énoncé si `[1, 4]` et `[4, 5]` sont considérés comme se chevauchant (`<=`) ou disjoints (`<`). Dans la majorité des problèmes LeetCode (dont **56**, **57**, **452**, **986**), un point de contact compte comme un chevauchement (`<=`).
* **Trier par début pour les problèmes de comptage maximal :** Pour compter le maximum de réunions possibles ou le minimum de flèches (**452**), trier par heure de début échoue sur un long intervalle `[1, 100]` qui bloque tout. Trie toujours par heure de **fin**.
