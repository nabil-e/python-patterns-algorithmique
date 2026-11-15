# 06. Prefix / Suffix Sum (Sommes Préfixes et Suffixes)

## 💡 Idée Centrale
Pré-calculer les sommes cumulées depuis le début (préfixe) ou depuis la fin (suffixe) d'un tableau. Cela permet d'obtenir la somme de n'importe quel segment `[i, j]` en temps constant $O(1)$ via la formule `prefix[j + 1] - prefix[i]`, évitant ainsi des boucles imbriquées.

* **Complexité Temporelle :** $O(n)$ pour la construction, $O(1)$ par requête
* **Complexité Spatiale :** $O(n)$ (ou $O(1)$ si calculé à la volée dans une variable)

---

## 🔍 Indices dans l'énoncé & Mots-clés
| Ce que dit l'énoncé | Mots-clés anglais fréquents |
| :--- | :--- |
| Calculer la somme de plusieurs sous-tableaux définis par des plages d'indices. | *range sum query*, *sum between indices i and j*, *immutable array* |
| Trouver le nombre de sous-tableaux dont la somme vaut exactement $k$ (**avec nombres négatifs**). | *subarray sum equals k*, *number of subarrays*, *divisible by k* |
| Calculer une valeur à l'index $i$ en combinant tout ce qui est à gauche et à droite (sans division). | *product of array except self*, *left and right*, *pivot index*, *equilibrium* |

---

## 🧩 Variantes Principales

### 1. Tableau de Préfixes Classique (Range Queries)
On crée un tableau `prefix` de taille $n + 1$ commençant par `0` (pour éviter de gérer le cas limite `i == 0`).

### 2. Prefix Sum + Hash Map (Le Duo Redoutable)
Si la somme cumulée actuelle est `curr_sum` et qu'on cherche un sous-tableau de somme `k`, il suffit de vérifier combien de fois la somme `curr_sum - k` a déjà été vue auparavant dans notre dictionnaire.

### 3. Préfixe et Suffixe combinés (Gauche & Droite)
Utile pour calculer le produit de tous les éléments sauf `nums[i]` : on fait une passe de gauche à droite pour accumuler les préfixes, puis une passe de droite à gauche pour multiplier par les suffixes.

---

## ⚠️ Pièges à éviter
* **Oublier d'initialiser la Hash Map avec `{0: 1}` :** Si un sous-tableau commençant dès l'indice `0` a une somme égale à `k`, alors `curr_sum - k == 0`. Sans `{0: 1}`, ce sous-tableau ne sera pas comptabilisé.
* **Décalage d'indice (+1) :** Dans un tableau `prefix` de taille $n + 1$, `prefix[i]` représente la somme des $i$ premiers éléments (indices `0` à `i - 1`).

---

## 💻 Squelettes de Code (Python)

### Variante A : Prefix Sum + Hash Map (Sous-tableaux de somme K)
```python
def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    # {somme_prefixe: nombre_d_occurrences}
    prefix_counts = {0: 1}
    curr_sum = 0
    count = 0

    for num in nums:
        curr_sum += num
        # Si (curr_sum - k) a déjà été vu, le segment entre les deux vaut k
        diff = curr_sum - k
        if diff in prefix_counts:
            count += prefix_counts[diff]
            
        prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1

    return count
```

### Variante B : Préfixe & Suffixe sans mémoire extra (Produit sauf soi-même)
```python
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [1] * n

    # 1. Passe Préfixe (de gauche à droite)
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    # 2. Passe Suffixe (de droite à gauche)
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]

    return res
```
