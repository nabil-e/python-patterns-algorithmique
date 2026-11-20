# 💻 Pattern 8 : Sorting Intervals — Squelettes, Code & Astuces

## 1. Squelette Générique (Boilerplate)

```python
def merge_intervals_skeleton(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    # Trier par heure de début
    intervals.sort(key=lambda x: x[0])
    merged: list[list[int]] = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start <= last_end:  # Chevauchement
            merged[-1][1] = max(last_end, end)
        else:  # Disjoint
            merged.append([start, end])

    return merged
```

---

## 2. Démos Exécutables & Bac à Sable (`main.py`)

```python
# --- 1. DÉMOS DU PATTERN (Exécutables) ---

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """LeetCode 56 : Fusionne tous les intervalles qui se chevauchent."""
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged: list[list[int]] = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def interval_intersection(
    first_list: list[list[int]], second_list: list[list[int]]
) -> list[list[int]]:
    """LeetCode 986 : Intersection de deux listes d'intervalles disjoints et triés."""
    i, j = 0, 0
    result: list[list[int]] = []

    while i < len(first_list) and j < len(second_list):
        start_max = max(first_list[i][0], second_list[j][0])
        end_min = min(first_list[i][1], second_list[j][1])

        if start_max <= end_min:
            result.append([start_max, end_min])

        # Avancer le pointeur de l'intervalle qui se termine le plus tôt
        if first_list[i][1] < second_list[j][1]:
            i += 1
        else:
            j += 1

    return result


def find_min_arrow_shots(points: list[list[int]]) -> int:
    """LeetCode 452 : Nombre minimal de flèches pour éclater tous les ballons."""
    if not points:
        return 0
    # Tri par borne de fin croissante (choix glouton optimal)
    points.sort(key=lambda x: x[1])
    arrows = 1
    current_end = points[0][1]

    for start, end in points[1:]:
        if start > current_end:
            arrows += 1
            current_end = end

    return arrows


# --- 2. BAC À SABLE EXERCICES (À compléter) ---

def find_poisoned_duration(time_series: list[int], duration: int) -> int:
    """LeetCode 495 : Teemo Attacking. À compléter !"""
    pass


if __name__ == "__main__":
    print("Merge :", merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(
        "Intersection :",
        interval_intersection([[0, 2], [5, 10]], [[1, 5], [8, 12]]),
    )
    print("Arrows :", find_min_arrow_shots([[10, 16], [2, 8], [1, 6], [7, 12]]))
    # assert find_poisoned_duration([1, 4], 2) == 4
```

---

## 3. Trucs et Astuces Python
- **Tri par fin (`key=lambda x: x[1]`) vs début (`key=lambda x: x[0]`) :**
  - Pour **fusionner** des intervalles (`Merge`), trie par **début** (`x[0]`).
  - Pour **compter le max d'intervalles sans chevauchement** ou tirer un minimum de flèches (`Arrows`), trie par **fin** (`x[1]`).
- **Formule universelle d'intersection :** Deux intervalles `[a, b]` et `[c, d]` se croisent si et seulement si `max(a, c) <= min(b, d)`.

---

## 4. Pièges à éviter
- **Oublier `max(last_end, end)` lors de la fusion :** Si `[1, 10]` est suivi de `[2, 5]`, la borne de fin reste `10`, pas `5` !
- **Modifier la liste pendant l'itération :** Construis toujours une nouvelle liste `merged` plutôt que de faire `.pop()` dans `intervals` en cours de boucle (coût $O(n)$ par suppression).
