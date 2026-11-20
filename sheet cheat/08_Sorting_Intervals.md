# 08. Sorting Intervals (Tri d'Intervalles)
> **Pattern 08 / 14** • **Temps :** `O(n log n)` • **Espace :** `O(n)`

---

## 1. Idée Centrale
Face à des intervalles `[start, end]` désordonnés, le premier réflexe est de **trier par heure de début** (`key=lambda x: x[0]`). Une fois triés, deux intervalles consécutifs `A` et `B` se chevauchent si et seulement si `B[0] <= A[1]`.

---

## 2. Indices dans l'énoncé

| Indice dans l'énoncé | Mots-clés (Anglais) | Approche recommandée |
| :--- | :--- | :--- |
| Fusionner tous les créneaux qui se superposent | `merge intervals`, `overlapping intervals`, `combine ranges` | Tri par `start` + extension de `end = max(end, curr[1])` |
| Insérer un nouvel intervalle dans une liste déjà triée et fusionner | `insert interval`, `non-overlapping sorted intervals` | 3 phases : avant, chevauchement (min/max), après |
| Retirer le minimum d'intervalles pour supprimer tout chevauchement | `non-overlapping intervals`, `minimum removals`, `erase overlap` | Tri par `end` croissant (approche gloutonne) |
| Compter le nombre minimum de salles de réunion simultanées | `meeting rooms`, `minimum platforms`, `concurrent events` | Tri par `start` + Min-Heap des heures de fin |

---

## 3. Variantes & Pièges Courants

### Variantes principales
* **Fusion standard (Tri par début) :** Trier par `start`, comparer `curr[0] <= merged[-1][1]` et mettre à jour la fin avec `max(merged[-1][1], curr[1])`.
* **Sélection maximale / Suppressions minimales (Tri par fin) :** Trier par `end` croissant pour libérer la ressource le plus tôt possible et garder un maximum d'intervalles.
* **Chevauchement simultané maximal (Sweep Line / Heap) :** Séparer les débuts et fins (ou utiliser un Min-Heap sur `end`) pour compter les conflits actifs.

### Pièges à éviter
* **Écraser `end` sans `max()` :** Si l'intervalle `[1, 10]` est suivi de `[2, 5]`, la fin fusionnée est `max(10, 5) = 10`, et non `5`.
* **Inégalités strictes vs larges (`<` vs `<=`) :** Vérifiez dans l'énoncé si deux créneaux qui se touchent (ex. `[1, 4]` et `[4, 5]`) sont considérés comme un chevauchement ou non.
* **Trier par `start` pour supprimer des conflits :** Pour maximiser les intervalles compatibles (ou minimiser les suppressions), il faut trier par **heure de fin** (`x[1]`), pas par heure de début.

---

## 4. Squelettes de Code (Python)

### Variante 1 : Merge Intervals (Tri par début + Fusion)
```python
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start <= last_end:     # Chevauchement détecté
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged
```

### Variante 2 : Non-overlapping Intervals (Tri par fin pour min suppressions)
```python
def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])  # Garder ceux qui finissent le plus tôt
    removals = 0
    prev_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start < prev_end:      # Conflit : on supprime l'intervalle courant
            removals += 1
        else:
            prev_end = end        # Pas de conflit : on met à jour la fin
    return removals
```
