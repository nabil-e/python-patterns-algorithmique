# 💻 Pattern 7 : Greedy (Glouton) — Squelettes, Code & Astuces

## 1. Squelette Générique (Boilerplate)

```python
def greedy_skeleton(items: list[tuple[int, int]]) -> int:
    # 1. Trier selon le critère glouton optimal
    items.sort(key=lambda x: x[1])
    current_state: int = 0
    result: int = 0

    for item in items:
        if item[0] >= current_state:  # 2. Vérifier si le choix local est valide
            current_state = item[1]   # 3. Appliquer le choix immédiatement
            result += 1

    return result
```

---

## 2. Démos Exécutables (`main.py` — Section 1)

Code typé en anglais avec commentaires en français, prêt à être copié-collé et exécuté localement :

```python
# --- 1. DÉMOS DU PATTERN (Exécutables) ---

def find_content_children(g: list[int], s: list[int]) -> int:
    """LeetCode 455 : Appariement glouton (satisfaire le plus d'enfants possible)."""
    g.sort()
    s.sort()
    child_idx: int = 0
    cookie_idx: int = 0

    while child_idx < len(g) and cookie_idx < len(s):
        # On donne le plus petit biscuit suffisant à l'enfant le moins gourmand
        if s[cookie_idx] >= g[child_idx]:
            child_idx += 1
        cookie_idx += 1

    return child_idx


def max_profit_ii(prices: list[int]) -> int:
    """LeetCode 122 : Cumuler toutes les hausses consécutives (transactions illimitées)."""
    total_profit: int = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            total_profit += prices[i] - prices[i - 1]

    return total_profit


def majority_element(nums: list[int]) -> int:
    """LeetCode 169 : Algorithme de vote de Boyer-Moore en O(n) temps et O(1) espace."""
    candidate: int = 0
    count: int = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate


if __name__ == "__main__":
    print("455. Assign Cookies :", find_content_children([1, 2, 3], [1, 1]))  # 1
    print("122. Best Time Stock II :", max_profit_ii([7, 1, 5, 3, 6, 4]))  # 7
    print("169. Majority Element :", majority_element([2, 2, 1, 1, 1, 2, 2]))  # 2
```

---

## 3. Bac à Sable Exercices (`main.py` — Section 2)

```python
# --- 2. BAC À SABLE EXERCICES (À compléter) ---

def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    """LeetCode 605 : Can Place Flowers."""
    # TODO : Parcourir le parterre et planter dès que gauche, centre et droite sont à 0
    pass


if __name__ == "__main__":
    # Décommente pour tester ton code :
    # assert can_place_flowers([1, 0, 0, 0, 1], 1) is True
    # assert can_place_flowers([1, 0, 0, 0, 1], 2) is False
    pass
```

---

## 4. Trucs et Astuces Python
- **Tri sur clé personnalisée :** `items.sort(key=lambda x: -x[1])` permet de trier par ordre décroissant sur le second élément d'un tuple (indispensable pour LeetCode 1710 *Maximum Units on a Truck*).
- **Somme génératrice concise :** LeetCode 122 s'écrit en une ligne idiomatique :
  ```python
  sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))
  ```
- **Sentinelles aux extrémités :** Pour LeetCode 605 (*Can Place Flowers*), ajouter `[0] + flowerbed + [0]` élimine les vérifications d'index `i == 0` et `i == len(flowerbed) - 1`.

---

## 5. Pièges à éviter
- **Appliquer un algorithme glouton sans vérifier la propriété de choix optimal :** Sur un problème de rendu de monnaie avec des pièces arbitraires (`[1, 3, 4]` pour rendre `6`), prendre la plus grosse pièce (`4 + 1 + 1 = 3 pièces`) échoue face à `3 + 3 = 2 pièces`. Dans ce cas, il faut de la **Programmation Dynamique (DP)**.
- **Modifier une liste pendant qu'on itère dessus :** Si tu modifies le tableau en place (comme dans `can_place_flowers`), mets bien à jour `flowerbed[i] = 1` immédiatement afin que l'itération suivante `i + 1` voie la fleur fraîchement plantée.
