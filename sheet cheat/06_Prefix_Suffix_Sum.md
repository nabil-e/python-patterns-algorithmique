# 06. Prefix & Suffix Sum (Sommes Préfixes / Suffixes)
> **Pattern 06 / 14** • **Temps :** `O(n)` • **Espace :** `O(n)` ou `O(1)`

---

## 1. Idée Centrale
Pré-calculer la somme (ou le produit) cumulée depuis le début (**Prefix**) et/ou depuis la fin (**Suffix**). La somme d'un sous-tableau `[i..j]` s'obtient alors instantanément par soustraction : `prefix[j+1] - prefix[i]`, évitant de recalculer la même plage plusieurs fois.

---

## 2. Indices dans l'énoncé

| Indice dans l'énoncé | Mots-clés (Anglais) | Approche recommandée |
| :--- | :--- | :--- |
| Calculer la somme de plusieurs plages fixes sur un tableau immuable | `range sum query`, `immutable array`, `sum of subarray` | Prefix Sum 1D standard (`O(1)` par requête) |
| Compter les sous-tableaux de somme exactement égale à K (avec négatifs) | `subarray sum equals k`, `contiguous subarray`, `negative numbers` | Prefix Sum + Hash Map (`curr_sum - k`) |
| Calculer le produit (ou min/max) de tous les éléments sauf l'index actuel | `product of array except self`, `without division` | Double passe Prefix & Suffix sur place (`O(1)` espace) |
| Trouver un index pivot où la somme à gauche égale celle à droite | `pivot index`, `equilibrium point`, `left sum equals right` | Somme totale moins cumul courant (`total - left - x == left`) |

---

## 3. Variantes & Pièges Courants

### Variantes principales
* **Prefix Sum 1D / 2D :** Tableau de taille `n + 1` avec `prefix[0] = 0` pour simplifier le calcul de plage `prefix[r + 1] - prefix[l]`.
* **Prefix Sum + Hash Map :** Stocke la fréquence de chaque somme préfixe rencontrée. Indispensable dès que le tableau contient des **nombres négatifs ou des zéros** (où Sliding Window échoue).
* **Prefix & Suffix sur place :** Deux passes successives (gauche→droite puis droite→gauche) directement dans le tableau résultat pour réduire l'espace à `O(1)`.

### Pièges à éviter
* **Oublier l'état initial `{0: 1}` :** Dans Prefix Sum + Hash Map, ne pas initialiser `counts = {0: 1}` fait rater tous les sous-tableaux valides commençant à l'index `0`.
* **Décalage d'index (Off-by-one) :** Avec un tableau `prefix` de taille `n + 1`, la somme de `nums[l..r]` inclus est `prefix[r + 1] - prefix[l]`, et non `prefix[r] - prefix[l]`.
* **Utiliser Sliding Window avec des négatifs :** Si l'énoncé autorise des valeurs négatives pour une somme cible `k`, la fenêtre n'est plus monotone : basculez immédiatement sur Prefix Sum + Hash Map.

---

## 4. Squelettes de Code (Python)

### Variante 1 : Subarray Sum Equals K (Prefix Sum + Hash Map)
```python
def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    prefix_counts: dict[int, int] = {0: 1}  # Base : somme 0 vue 1 fois avant le début
    curr_sum = 0
    total_subarrays = 0

    for num in nums:
        curr_sum += num
        # Si (curr_sum - k) a déjà été vu, les sous-tableaux entre ces points valent k
        total_subarrays += prefix_counts.get(curr_sum - k, 0)
        prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1

    return total_subarrays
```

### Variante 2 : Product Except Self (Prefix & Suffix en espace O(1))
```python
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [1] * n

    prefix = 1
    for i in range(n):
        res[i] = prefix          # Produit de tout ce qui est à gauche de i
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix         # Multiplie par tout ce qui est à droite de i
        suffix *= nums[i]

    return res
```
