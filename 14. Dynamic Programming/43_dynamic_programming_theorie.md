# 🧮 Pattern 14 : Dynamic Programming (Programmation Dynamique)

## 1. Principe et Mécanique
La **Programmation Dynamique (DP)** consiste à résoudre un problème complexe en le décomposant en **sous-problèmes qui se chevauchent**, et à **mémoriser** leurs résultats pour ne jamais recalculer deux fois la même chose. Contrairement au Greedy (qui fait un choix local définitif), la DP explore intelligemment toutes les décisions possibles en éliminant les calculs redondants.

On distingue **2 approches équivalentes** :

### A. Top-Down (Mémoïsation = Récursion + Cache)
On part du problème global `dp(n)` et on descend récursivement vers les cas de base, en stockant chaque résultat dans un dictionnaire `memo` (ou `@functools.cache`).

```text
Sans mémoïsation (fib(4)) :        Avec mémoïsation :
          fib(4)                         fib(4)
         /      \                       /      \
     fib(3)    fib(2) [recalculé!]  fib(3)    [memo[2]] -> O(1)
     /    \                         /    \
 fib(2)  fib(1)                 fib(2)  fib(1)
```

### B. Bottom-Up (Tabulation = Itératif avec tableau `dp`)
On part des cas de base (`dp[0]`, `dp[1]`) et on remplit un tableau 1D ou 2D étape par étape jusqu'à `dp[n]`, sans récursion.

```text
Index :    0     1     2     3     4     5
dp[]  :  [ 1 ] [ 1 ] [ 2 ] [ 3 ] [ 5 ] [ 8 ]
                       ^
                       +-- dp[i] = dp[i-1] + dp[i-2]
```

---

## 2. Les 4 Étapes pour construire une solution DP
1. **Définir l'état :** Que représente `dp[i]` (ou `dp[i][j]`) ? *(Ex: `dp[i]` = nombre de façons d'atteindre la marche `i`)*.
2. **Trouver la relation de récurrence :** Comment calculer `dp[i]` à partir des états précédents ? *(Ex: `dp[i] = dp[i-1] + dp[i-2]`)*.
3. **Identifier les cas de base :** Quelles sont les valeurs connues au départ ? *(Ex: `dp[0] = 1, dp[1] = 1`)*.
4. **Optimiser l'espace (optionnel) :** Si `dp[i]` ne dépend que de `dp[i-1]` et `dp[i-2]`, deux variables `prev1, prev2` suffisent en $O(1)$ espace.

---

## 3. Mots-clés et Déclencheurs dans les énoncés
- **"How many ways..."** / **"Number of distinct ways..."** (compter le nombre de chemins ou combinaisons)
- **"Minimum / Maximum cost / path / steps..."** (optimisation globale où un choix local glouton échoue)
- **"Longest increasing / common subsequence"** (sous-séquences optimales)
- **"Coin change"** / **"Knapsack"** / **"Partition equal subset"** (choix d'objets sous contrainte de capacité)
- **"Can you reach..."** avec choix multiples et chevauchements d'états

---

## 4. Complexités Comparées

| Approche | Temps | Espace | Avantage |
| :--- | :--- | :--- | :--- |
| **Récursion brute** | $O(2^n)$ | $O(n)$ | Trop lent (Time Limit Exceeded dès $n > 30$) |
| **Top-Down (Mémoïsation)** | $O(\text{États} \times \text{Transitions})$ | $O(\text{États})$ | Intuitif, ne calcule que les états utiles |
| **Bottom-Up (Tabulation)** | $O(\text{États} \times \text{Transitions})$ | $O(\text{États})$ ou $O(1)$ | Pas de limite de récursion, optimisable en mémoire |

---

## ⚠️ Cas limites à vérifier
- **Entrées minimales (`n == 0`, `n == 1`, tableau vide `[]`) :** Vérifier que l'initialisation `dp[1]` ne déclenche pas d'`IndexError` si `len(nums) == 1`.
- **État impossible à atteindre (ex: Coin Change) :** Initialiser le tableau avec `float("inf")` (ou `amount + 1`) et vérifier en sortie si `dp[amount] == float("inf")` pour retourner `-1`.
- **Mémoïsation avec arguments non hachables :** `@functools.cache` exige des arguments immuables (`int`, `str`, `tuple`). Ne jamais passer une `list` en paramètre d'une fonction décorée par `@cache`.

## 🚫 Quand éviter ce pattern
- **Un choix local optimal est toujours garanti (Greedy) :** Si prendre le meilleur choix immédiat ne bloque jamais l'avenir (ex: intervalles qui finissent le plus tôt, achat/revente d'actions illimité `#122`), **Greedy** résout le problème en $O(n)$ ou $O(n \log n)$ sans tableau DP.
- **L'énoncé demande de générer *toutes* les combinaisons elles-mêmes :** La DP excelle pour *compter* ou *optimiser* une valeur. S'il faut retourner la liste complète de tous les chemins ou sous-ensembles, utiliser **Backtracking**.
