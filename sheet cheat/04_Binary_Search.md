# 04. Binary Search (Recherche Binaire)

> **Complexité visée :** Temps $O(\log n)$ (ou $O(n \log M)$ sur espace de réponse) | Espace $O(1)$

---

## 1. Idée Centrale
Éliminer la moitié de l'espace de recherche à chaque étape en exploitant une **propriété monotone** (tableau trié ou fonction de faisabilité qui passe de `False` à `True`). Dès que la complexité exigée est $O(\log n)$ ou que $N \ge 10^9$, la recherche binaire est incontournable.

---

## 2. Indices dans l'énoncé & Mots-clés (LeetCode)

| Indice dans l'énoncé | Mots-clés (Anglais) | Approche / Variante |
| :--- | :--- | :--- |
| Chercher une cible exacte ou sa position d'insertion dans un tableau trié | `sorted array`, `O(log n)`, `search insert` | **Classic Binary Search** |
| Trouver la première ou dernière occurrence (bornes gauche/droite) | `first/last position`, `lower/upper bound` | **Leftmost / Rightmost Bound** |
| Tableau trié ayant subi une rotation ou recherche d'un pic | `rotated sorted array`, `peak element`, `minimum` | **Modified Binary Search** |
| Minimiser le maximum ou maximiser le minimum d'une capacité/vitesse | `min max capacity`, `koko eating`, `split array` | **Binary Search on Answer** |

---

## 3. Variantes & Pièges Courants

### Variantes Clés
* **Recherche Exacte / Bornes (`left <= right`) :** Converge vers une cible ou le premier élément $\ge \text{target}$ (équivalent à `bisect_left`).
* **Binary Search on Answer :** On cherche directement la valeur de la réponse entre `min_ans` et `max_ans` en testant chaque candidat `mid` via une fonction booléenne `can_achieve(mid)` en $O(n)$.

### Pièges à Éviter
* **Boucle infinie :** Avec `while left < right:`, si vous faites `left = mid` (sans `+ 1`), lorsque `right == left + 1`, `mid` vaut `left` et la boucle ne s'arrête jamais. Utilisez `mid = left + (right - left) // 2` et avancez toujours d'au moins 1.
* **Mauvaise condition d'arrêt :** Soyez cohérent entre `while left <= right:` (intervalle fermé `[left, right]`) et `while left < right:` (intervalle semi-ouvert `[left, right)`).

---

## 4. Squelettes Python

### Variante A : Recherche Exacte & Borne Gauche (`bisect_left`)
```python
def binary_search_left(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    ans = len(nums)

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            ans = mid
            right = mid - 1  # Continue à chercher plus à gauche
        else:
            left = mid + 1

    return ans
```

### Variante B : Binary Search on Answer (Capacité minimale)
```python
def min_capacity(weights: list[int], days: int) -> int:
    def is_feasible(cap: int) -> bool:
        needed_days, current_load = 1, 0
        for w in weights:
            if current_load + w > cap:
                needed_days += 1
                current_load = 0
            current_load += w
        return needed_days <= days

    left, right = max(weights), sum(weights)
    ans = right
    while left <= right:
        mid = left + (right - left) // 2
        if is_feasible(mid):
            ans = mid
            right = mid - 1  # Tente une capacité plus petite
        else:
            left = mid + 1
    return ans
```
