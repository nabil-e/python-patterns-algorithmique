# 💻 Pattern 4 : Binary Search — Squelettes, Code & Astuces

## 1. Squelette Générique (Boilerplate)

```python
def binary_search_boundary_skeleton(low: int, high: int) -> int:
    def is_valid(mid: int) -> bool:
        # Retourne True si mid satisfait la condition monotone
        return ...

    while low < high:
        mid: int = low + (high - low) // 2
        if is_valid(mid):
            high = mid      # mid est valide, on cherche encore plus à gauche
        else:
            low = mid + 1   # mid est trop petit, on l'exclut
    return low
```

---

## 2. Démos Exécutables (`main.py` — Section 1)

Code typé en anglais avec commentaires en français, prêt à être copié-collé et exécuté localement :

```python
import bisect

# --- 1. DÉMOS DU PATTERN (Exécutables) ---

def search_insert(nums: list[int], target: int) -> int:
    """LeetCode 35 : Trouve l'index de target ou sa position d'insertion."""
    left: int = 0
    right: int = len(nums) - 1

    while left <= right:
        mid: int = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # left pointe toujours vers la position d'insertion exacte
    return left


def first_bad_version(n: int, bad_version_start: int) -> int:
    """LeetCode 278 : Recherche de frontière monotone (première version défectueuse)."""
    def is_bad_version(version: int) -> bool:
        return version >= bad_version_start

    low: int = 1
    high: int = n

    while low < high:
        mid: int = low + (high - low) // 2
        if is_bad_version(mid):
            high = mid      # Peut être la première, on garde mid
        else:
            low = mid + 1   # Forcément après mid

    return low


def my_sqrt(x: int) -> int:
    """LeetCode 69 : Racine carrée entière par recherche sur l'espace des réponses."""
    if x < 2:
        return x

    left: int = 1
    right: int = x // 2

    while left <= right:
        mid: int = left + (right - left) // 2
        square: int = mid * mid
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1

    # right s'arrête sur le plus grand entier dont le carré est <= x
    return right


if __name__ == "__main__":
    print("35. Search Insert :", search_insert([1, 3, 5, 6], 2))  # 1
    print("278. First Bad Version :", first_bad_version(5, 4))  # 4
    print("69. Sqrt(8) :", my_sqrt(8))  # 2
    print("Astuce bisect :", bisect.bisect_left([1, 3, 5, 6], 2))  # 1
```

---

## 3. Bac à Sable Exercices (`main.py` — Section 2)

```python
# --- 2. BAC À SABLE EXERCICES (À compléter) ---

def is_perfect_square(num: int) -> bool:
    """LeetCode 367 : Valid Perfect Square."""
    # TODO : Appliquer Binary Search entre 1 et num // 2 (si num >= 2)
    pass


if __name__ == "__main__":
    # Décommente pour tester ton code :
    # assert is_perfect_square(16) is True
    # assert is_perfect_square(14) is False
    pass
```

---

## 4. Trucs et Astuces Python
- **Module standard `bisect` :**
  - `bisect.bisect_left(nums, target)` renvoie le premier index où insérer `target` en gardant le tri (équivalent exact de LeetCode 35).
  - `bisect.bisect_right(nums, target)` renvoie l'index juste après la dernière occurrence de `target`.
- **Calcul de `mid` sans dépassement :** Écris `mid = left + (right - left) // 2` par réflexe d'entretien (même si Python gère les entiers de taille arbitraire).

---

## 5. Pièges à éviter
- **Boucle infinie avec `while left < high` :** Si tu écris `low = mid` (sans `+ 1`), quand `high == low + 1`, `mid` vaut `low` et l'intervalle ne rétrécit jamais. Avec `low = mid`, il faut calculer `mid = low + (high - low + 1) // 2`.
- **Mauvaise condition d'arrêt (`<=` vs `<`) :**
  - Recherche exacte d'un élément pouvant être absent : `while left <= right:` avec `left = mid + 1` et `right = mid - 1`.
  - Recherche d'une frontière garantie d'exister : `while low < high:` avec `high = mid` et `low = mid + 1`.
