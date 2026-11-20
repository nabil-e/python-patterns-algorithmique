# 💻 Pattern 14 : Dynamic Programming — Squelettes, Code & Astuces

## 1. Squelettes Génériques (Boilerplates)

### Squelette A : Top-Down (Mémoïsation avec `functools.cache`)
```python
from functools import cache


def dp_top_down_skeleton(n: int) -> int:
    @cache
    def dfs(state: int) -> int:
        # 1. Cas de base
        if state <= 1:
            return state

        # 2. Relation de récurrence (explorer les transitions)
        return dfs(state - 1) + dfs(state - 2)

    return dfs(n)
```

### Squelette B : Bottom-Up 1D (Tabulation)
```python
def dp_bottom_up_skeleton(n: int) -> int:
    if n <= 1:
        return n

    # 1. Initialisation du tableau DP
    dp: list[int] = [0] * (n + 1)
    dp[0], dp[1] = 1, 1

    # 2. Remplissage itératif
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```

---

## 2. Templates Python Exécutables (Prêts à lancer)

```python
from functools import cache


# --- DÉMO 1 : Climbing Stairs — DP 1D optimisée O(1) espace (LeetCode 70) ---
def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1


# --- DÉMO 2 : Coin Change — DP 1D Minimisation (LeetCode 322) ---
def coin_change(coins: list[int], amount: int) -> int:
    # Initialiser avec une valeur impossible (amount + 1)
    dp: list[int] = [amount + 1] * (amount + 1)
    dp[0] = 0

    for curr_amount in range(1, amount + 1):
        for coin in coins:
            if curr_amount - coin >= 0:
                dp[curr_amount] = min(dp[curr_amount], 1 + dp[curr_amount - coin])

    return dp[amount] if dp[amount] <= amount else -1


# --- DÉMO 3 : Unique Paths — DP Grille 2D (LeetCode 62) ---
def unique_paths(m: int, n: int) -> int:
    # Grille m x n initialisée à 1 (1 seule façon d'atteindre la 1re ligne/colonne)
    dp: list[list[int]] = [[1] * n for _ in range(m)]

    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

    return dp[m - 1][n - 1]


# --- BAC À SABLE EXERCICES (À compléter dans main.py) ---
def rob(nums: list[int]) -> int:
    """LeetCode 198 : House Robber (DP 1D : voler ou passer la maison i)."""
    pass


if __name__ == "__main__":
    print("Démo 1 (Climb Stairs n=5) :", climb_stairs(5))  # 8
    print("Démo 2 (Coin Change) :", coin_change([1, 2, 5], 11))  # 3
    print("Démo 3 (Unique Paths 3x7) :", unique_paths(3, 7))  # 28
```
