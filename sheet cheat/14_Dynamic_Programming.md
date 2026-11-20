# 14. Dynamic Programming (Programmation Dynamique)

## 💡 Idée Centrale & Complexité
La **Programmation Dynamique (DP)** résout des problèmes complexes en les décomposant en **sous-problèmes qui se chevauchent** (*overlapping subproblems*) et possèdent une **sous-structure optimale**. On stocke le résultat de chaque sous-problème pour ne jamais le recalculer deux fois.
* **Top-Down (Mémoïsation) :** Récursion naturelle + cache (`@cache`). On part du problème global vers les cas de base.
* **Bottom-Up (Tabulation) :** Boucles itératives remplissant un tableau `dp`. On part des cas de base vers la solution finale.
* **Complexité temporelle :** $\text{Nombre d'états} \times \text{Coût de transition par état}$ (souvent $O(n)$ ou $O(n \cdot m)$).
* **Complexité spatiale :** $O(n)$ ou $O(n \cdot m)$, souvent réductible à **$O(1)$** en Bottom-Up si l'état `i` ne dépend que de `i-1` et `i-2`.

---

## 🔍 Indices dans l'énoncé & Mots-clés
| Ce que demande l'énoncé | Mots-clés en anglais (LeetCode) | Approche à adopter |
| :--- | :--- | :--- |
| Compter le **nombre total** de façons d'atteindre un objectif | *number of ways, how many distinct ways, count combinations* | DP comptage (`dp[i] += dp[i - step]`) |
| Trouver le **minimum ou maximum** (coût, score, longueur) | *minimum cost, maximum profit, longest subsequence, min coins* | DP optimisation (`min()` / `max()` sur les choix) |
| Décisions séquentielles où un choix affecte les choix futurs | *house robber, jump game, best time to buy and sell stock* | DP 1D avec suivi d'états (`prev1, prev2`) |
| Comparer ou aligner **deux séquences** (chaînes ou tableaux) | *longest common subsequence, edit distance, distinct subsequences* | DP 2D (`dp[i][j]`) |
| Remplir une capacité / atteindre une somme cible | *knapsack, partition equal subset sum, coin change, target sum* | DP Sac à dos (0/1 ou illimité) |

---

## ⚠️ Variantes & Pièges Courants
1. **Le piège des arguments non hachables avec `@cache` :** `@functools.cache` utilise un dictionnaire en interne. Les paramètres de la fonction récursive doivent être **immuables (hachables)** : passez des `int`, `str` ou `tuple`, **jamais** une `list` ou un `set` (sinon `TypeError: unhashable type: 'list'`).
2. **Oublier les cas de base :** En Top-Down, définissez toujours les conditions d'arrêt en tout début de fonction (`if i < 0: return ...`) avant les transitions.
3. **Optimisation d'espace $O(1)$ :** En Bottom-Up, si `dp[i]` ne lit que `dp[i-1]` et `dp[i-2]`, remplacez le tableau `dp` par deux variables (`prev2, prev1 = ...`). Pour un DP 2D, on peut souvent réduire à un tableau 1D.

---

## 💻 Squelette de Code (Python)

```python
from functools import cache
from typing import List

# --- APPROCHE 1 : Top-Down (Mémoïsation) ---
def rob_top_down(nums: List[int]) -> int:
    @cache
    def dp(i: int) -> int:
        # 1. Cas de base
        if i < 0:
            return 0
        # 2. Relation de récurrence : prendre i ou ignorer i
        return max(dp(i - 1), nums[i] + dp(i - 2))

    return dp(len(nums) - 1)

# --- APPROCHE 2 : Bottom-Up Optimisée O(1) en espace ---
def rob_bottom_up(nums: List[int]) -> int:
    prev2, prev1 = 0, 0  # Représente dp[i-2] et dp[i-1]
    for num in nums:
        curr = max(prev1, num + prev2)
        prev2, prev1 = prev1, curr
    return prev1
```
