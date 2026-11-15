# 08. Sorting Intervals (Tri et Fusion d'Intervalles)

## 💡 Idée Centrale
Face à des plages horaires, des segments ou des intervalles `[début, fin]`, **trier les intervalles par heure de début** permet d'aligner chronologiquement tous les chevauchements potentiels. Il suffit ensuite d'une seule passe linéaire pour comparer chaque intervalle avec le précédent.

* **Complexité Temporelle :** $O(n \log n)$ (dominée par le tri initial)
* **Complexité Spatiale :** $O(n)$ (pour stocker la liste fusionnée) ou $O(1)$

---

## 🔍 Indices dans l'énoncé & Mots-clés
| Ce que dit l'énoncé | Mots-clés anglais fréquents |
| :--- | :--- |
| L'entrée est une liste de paires `[start, end]` représentant des plages ou segments. | *intervals*, *start and end times*, *ranges*, *meetings* |
| Fusionner les intervalles qui se superposent ou en insérer un nouveau. | *merge overlapping intervals*, *insert interval*, *non-overlapping* |
| Compter le nombre minimum de salles de réunion ou de ressources simultanées. | *meeting rooms*, *minimum platforms*, *concurrent events* |
| Trouver les créneaux libres entre plusieurs emplois du temps. | *employee free time*, *find gaps*, *covered intervals* |

---

## 🧩 Variantes Principales

### 1. Fusion d'intervalles (Merge Intervals)
* **Tri :** Par heure de début `x[0]`.
* **Condition de chevauchement :** `current[0] <= last_merged[1]`.
* **Action :** On étend la fin : `last_merged[1] = max(last_merged[1], current[1])`.

### 2. Supprimer le minimum d'intervalles pour éviter les conflits
* **Tri :** Par **heure de fin** `x[1]` ! (Plus une réunion finit tôt, plus elle laisse de place aux suivantes).
* **Condition de conflit :** `current[0] < prev_end`.

### 3. Compter les chevauchements simultanés (Sweep Line / Meeting Rooms II)
Séparer tous les `start` dans un tableau trié et tous les `end` dans un autre tableau trié, puis avancer avec deux pointeurs (`+1` à chaque début, `-1` à chaque fin).

---

## ⚠️ Pièges à éviter
* **Oublier le `max()` lors de la fusion :** Un intervalle `[1, 10]` suivi de `[2, 5]` doit devenir `[1, 10]` et non `[1, 5]`. Prenez toujours `max(last[1], curr[1])`.
* **Cas limites de contact (`[1, 4]` et `[4, 5]`) :** Vérifiez dans l'énoncé si deux intervalles qui se touchent à la limite comptent comme un chevauchement (`<=`) ou non (`<`).

---

## 💻 Squelettes de Code (Python)

### Variante A : Fusion d'intervalles (Tri par début)
```python
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    # 1. Trier par heure de début
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        # 2. Chevauchement : on fusionne en gardant la fin la plus tardive
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged
```

### Variante B : Minimiser les suppressions (Tri par fin)
```python
def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    # Trier par heure de FIN pour maximiser le nombre de réunions gardées
    intervals.sort(key=lambda x: x[1])
    prev_end = intervals[0][1]
    removed = 0

    for start, end in intervals[1:]:
        if start < prev_end:
            # Conflit : on supprime l'intervalle actuel (qui finit plus tard)
            removed += 1
        else:
            prev_end = end

    return removed
```
