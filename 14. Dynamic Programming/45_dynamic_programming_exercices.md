# 🏋️ Pattern 14 : Dynamic Programming — Plan d'Entraînement

Coche les cases `[x]` au fur et à mesure de ta progression. Les indices sont masqués pour te permettre de réfléchir sans spoiler.

---

## Série 1 : DP 1D — Fondamentaux & Optimisations

- [ ] **70. Climbing Stairs** (Easy) — [LeetCode](https://leetcode.com/problems/climbing-stairs/)
  <details><summary>💡 Indice d'approche</summary>Le nombre de façons d'arriver à la marche `i` est la somme des façons d'arriver à `i-1` et à `i-2` (suite de Fibonacci optimisable avec 2 variables).</details>
  > Notes : 

- [ ] **746. Min Cost Climbing Stairs** (Easy) — [LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/)
  <details><summary>💡 Indice d'approche</summary>Pour atteindre chaque marche `i`, choisis le minimum entre venir de `i-1` et venir de `i-2`, puis ajoute `cost[i]`.</details>
  > Notes : 

- [ ] **121. Best Time to Buy and Sell Stock** (Easy) — [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
  <details><summary>💡 Indice d'approche</summary>DP à 1 état (ou glouton) : maintiens le prix minimum rencontré jusqu'à présent (`min_price`) et maximise `price - min_price` à chaque jour.</details>
  > Notes : 

- [ ] **198. House Robber** (Medium) — [LeetCode](https://leetcode.com/problems/house-robber/)
  <details><summary>💡 Indice d'approche</summary>À chaque maison `i`, deux choix : la voler (`nums[i] + dp[i-2]`) ou l'ignorer (`dp[i-1]`). Prends le maximum des deux.</details>
  > Notes : 

- [ ] **213. House Robber II** (Medium) — [LeetCode](https://leetcode.com/problems/house-robber-ii/)
  <details><summary>💡 Indice d'approche</summary>Les maisons forment un cercle : réutilise exactement ta fonction House Robber sur `nums[:-1]` et sur `nums[1:]`, puis retourne le maximum des deux.</details>
  > Notes : 

---

## Série 2 : DP 1D Avancé & DP 2D (Grilles & Sous-séquences)

- [ ] **322. Coin Change** (Medium) — [LeetCode](https://leetcode.com/problems/coin-change/)
  <details><summary>💡 Indice d'approche</summary>DP Bottom-Up sur le montant de `1` à `amount` : pour chaque pièce `c`, `dp[i] = min(dp[i], 1 + dp[i - c])`. Retourne `-1` si `dp[amount]` reste infini.</details>
  > Notes : 

- [ ] **300. Longest Increasing Subsequence** (Medium) — [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/)
  <details><summary>💡 Indice d'approche</summary>Initialise `dp = [1] * len(nums)`. Pour chaque `i`, regarde tous les `j < i` : si `nums[j] < nums[i]`, alors `dp[i] = max(dp[i], 1 + dp[j])`.</details>
  > Notes : 

- [ ] **139. Word Break** (Medium) — [LeetCode](https://leetcode.com/problems/word-break/)
  <details><summary>💡 Indice d'approche</summary>`dp[i]` vaut `True` si le préfixe `s[:i]` est segmentable : vérifie s'il existe un `j < i` tel que `dp[j]` est `True` et `s[j:i]` est dans `wordDict` (converti en `set`).</details>
  > Notes : 

- [ ] **62. Unique Paths** (Medium) — [LeetCode](https://leetcode.com/problems/unique-paths/)
  <details><summary>💡 Indice d'approche</summary>DP Grille 2D : chaque case `(r, c)` n'est accessible que depuis le haut `(r-1, c)` ou la gauche `(r, c-1)`, donc `dp[r][c] = dp[r-1][c] + dp[r][c-1]`.</details>
  > Notes : 

- [ ] **1143. Longest Common Subsequence** (Medium) — [LeetCode](https://leetcode.com/problems/longest-common-subsequence/)
  <details><summary>💡 Indice d'approche</summary>DP 2D sur les deux chaînes : si `text1[i] == text2[j]`, `dp[i][j] = 1 + dp[i+1][j+1]`, sinon `max(dp[i+1][j], dp[i][j+1])`.</details>
  > Notes : 
