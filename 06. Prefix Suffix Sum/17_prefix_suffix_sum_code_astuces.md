# 💻 Pattern 6 : Prefix / Suffix Sum — Squelettes, Code & Astuces

## 1. Squelettes Génériques (Boilerplates)

### Squelette A : Tableau de sommes préfixes (`prefix` de taille `n + 1`)
```python
def prefix_sum_skeleton(nums: list[int]) -> list[int]:
    n: int = len(nums)
    prefix: list[int] = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    # Somme de l'index left à right inclus en O(1) :
    # range_sum = prefix[right + 1] - prefix[left]
    return prefix
```

### Squelette B : Prefix Sum + Hashing (Sous-tableaux de somme K)
```python
from collections import defaultdict

def prefix_sum_hashing_skeleton(nums: list[int], k: int) -> int:
    prefix_counts: dict[int, int] = defaultdict(int)
    prefix_counts[0] = 1  # Cas où le sous-tableau démarre à l'index 0
    current_sum: int = 0
    total_subarrays: int = 0

    for num in nums:
        current_sum += num
        total_subarrays += prefix_counts[current_sum - k]
        prefix_counts[current_sum] += 1

    return total_subarrays
```

---

## 2. Démos Exécutables (`main.py` — Section 1)

Code typé en anglais avec commentaires en français, prêt à être copié-collé et exécuté localement :

```python
from collections import defaultdict
from itertools import accumulate

# --- 1. DÉMOS DU PATTERN (Exécutables) ---

class NumArray:
    """LeetCode 303 : Requêtes de sommes sur plages en O(1) après précalcul O(n)."""

    def __init__(self, nums: list[int]) -> None:
        # accumulate(..., initial=0) construit directement [0, n0, n0+n1, ...]
        self.prefix: list[int] = list(accumulate(nums, initial=0))

    def sum_range(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


def product_except_self(nums: list[int]) -> list[int]:
    """LeetCode 238 : Produit de tous les éléments sauf nums[i] en O(1) espace extra."""
    n: int = len(nums)
    result: list[int] = [1] * n

    # Passe 1 : Produits des préfixes (tout ce qui est à gauche de i)
    left_product: int = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    # Passe 2 : Multiplication par les produits des suffixes (tout ce qui est à droite)
    right_product: int = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result


def subarray_sum_k(nums: list[int], k: int) -> int:
    """LeetCode 560 : Nombre de sous-tableaux contigus dont la somme vaut k."""
    prefix_counts: dict[int, int] = defaultdict(int)
    prefix_counts[0] = 1
    current_sum: int = 0
    count: int = 0

    for num in nums:
        current_sum += num
        # Si (current_sum - k) a déjà été vu, la tranche intermédiaire somme à k
        count += prefix_counts[current_sum - k]
        prefix_counts[current_sum] += 1

    return count


if __name__ == "__main__":
    na = NumArray([-2, 0, 3, -5, 2, -1])
    print("303. Sum Range (0, 2) :", na.sum_range(0, 2))  # 1
    print("238. Product Except Self :", product_except_self([1, 2, 3, 4]))  # [24, 12, 8, 6]
    print("560. Subarray Sum K :", subarray_sum_k([1, -1, 0], 0))  # 3
```

---

## 3. Bac à Sable Exercices (`main.py` — Section 2)

```python
# --- 2. BAC À SABLE EXERCICES (À compléter) ---

def largest_altitude(gain: list[int]) -> int:
    """LeetCode 1732 : Find the Highest Altitude."""
    # TODO : Calculer la somme cumulée en partant de 0 et garder le maximum
    pass


if __name__ == "__main__":
    # Décommente pour tester ton code :
    # assert largest_altitude([-5, 1, 5, 0, -7]) == 1
    pass
```

---

## 4. Trucs et Astuces Python
- **`itertools.accumulate(nums, initial=0)` :** Génère en une seule ligne optimisée en C le tableau `prefix` de taille `n + 1` commençant par `0`.
- **La sentinelle `prefix[0] = 0` :** Prévoir une case supplémentaire à l'index `0` évite d'écrire un `if left == 0:` spécial lors du calcul `prefix[right + 1] - prefix[left]`.

---

## 5. Pièges à éviter
- **Oublier `prefix_counts[0] = 1` dans LeetCode 560 :** Sans cette initialisation, tout sous-tableau valide qui commence dès l'index `0` (où `current_sum == k`, donc `current_sum - k == 0`) ne sera jamais comptabilisé.
- **Mettre à jour `prefix_counts[current_sum]` avant de lire `prefix_counts[current_sum - k]` :** Si `k == 0`, tu compterais le sous-tableau vide de longueur 0 ! Toujours lire le dictionnaire **avant** d'y ajouter la somme courante.
