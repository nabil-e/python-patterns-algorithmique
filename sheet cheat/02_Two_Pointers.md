# 02. Two Pointers (Deux Pointeurs)

## 💡 Idée Centrale
Utiliser deux indices (ou plus) qui se déplacent dans une structure linéaire (tableau, chaîne) selon des règles précises afin d'éviter les doubles boucles imbriquées et de modifier les données sur place sans mémoire supplémentaire.

* **Complexité temporelle :** $O(n)$ (ou $O(n \log n)$ si un tri préalable est nécessaire).
* **Complexité spatiale :** $O(1)$ (modification *in-place*).

---

## 🔍 Indices dans l'énoncé & Mots-clés

| Ce que demande l'énoncé | Mots-clés en anglais | Variante à choisir |
| :--- | :--- | :--- |
| Trouver une paire ou un triplet atteignant une cible dans un tableau **trié**. | *sorted array*, *pair sum*, *3Sum*, *closest sum* | **Pointeurs opposés** (`left`, `right`) |
| Vérifier une symétrie ou inverser une chaîne/un tableau. | *palindrome*, *reverse*, *valid palindrome* | **Pointeurs opposés** (`left`, `right`) |
| Supprimer des doublons ou déplacer des éléments sans créer un nouveau tableau. | *in-place*, *remove duplicates*, *move zeroes*, *O(1) extra space* | **Lent & Rapide** (`slow`, `fast`) |
| Fusionner deux tableaux dont l'un a de l'espace libre à la fin. | *merge sorted array*, *without extra space* | **Parcours depuis la fin** |

---

## 🛠️ Variantes & Quand partir de la fin

1. **Opposés (`left = 0`, `right = n - 1`) :** Ils avancent l'un vers l'autre. Si la somme est trop petite, on fait `left += 1` ; si elle est trop grande, `right -= 1`.
2. **Même sens (`slow`, `fast`) :** `fast` explore le tableau, `slow` marque la position où écrire les éléments valides.
3. **3 Pointeurs :** Une boucle fixe un élément (`i`), et deux pointeurs (`left`, `right`) cherchent dans le reste du tableau (ex: *3Sum*), ou partitionnement en 3 zones (*Dutch National Flag*).
4. **Partir de la fin (`i = n - 1`) :** Indispensable pour **fusionner sur place** sans écraser les données non lues à gauche, ou quand le calcul dépend des éléments situés à droite.

---

## 💻 Squelette de Code (Python)

```python
# Variante 1 : Pointeurs opposés (tableau trié)
def two_pointers_opposite(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1   # Besoin d'une plus grande valeur
        else:
            right -= 1  # Besoin d'une plus petite valeur
    return []

# Variante 2 : Lent et Rapide (modification sur place)
def two_pointers_same_direction(arr):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != 0:  # Condition de conservation
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1
    return slow
```
