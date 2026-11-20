# Pattern 12 : Graphs, Backtracking & DP — Plan d'Entraînement

Issu de la fiche **BFS, DFS & Programmation Dynamique**. Les exos purement **arbres** (111, 637, 102, 199, 112, 572) sont dans `11. Trees`.

---

## 1. DFS / Backtracking sur grille

- [ ] **200. Number of Islands** (Medium) — [Lien LeetCode](https://leetcode.com/problems/number-of-islands/)
  - *Technique :* À chaque `'1'`, DFS (ou BFS) pour marquer toute la terre connectée.
  > Notes :

- [ ] **79. Word Search** (Medium) — [Lien LeetCode](https://leetcode.com/problems/word-search/)
  - *Technique :* DFS 4 directions + restauration de la case (backtracking) en cas d'échec.
  > Notes :

---

## 2. Programmation Dynamique

- [ ] **70. Climbing Stairs** (Easy) — [Lien LeetCode](https://leetcode.com/problems/climbing-stairs/)
  - *Technique :* `dp[i] = dp[i-1] + dp[i-2]` (pas de 1 ou 2).
  > Notes :

- [ ] **121. Best Time to Buy and Sell Stock** (Easy) — [Lien LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
  - *Technique :* Maintenir le prix d'achat minimal vu jusqu'ici ; maximiser `prix - min_achat`.
  > Notes :

- [ ] **322. Coin Change** (Medium) — [Lien LeetCode](https://leetcode.com/problems/coin-change/)
  - *Technique :* `dp[m] = min(dp[m], 1 + dp[m - c])` pour chaque pièce `c`.
  > Notes :

- [ ] **62. Unique Paths** (Medium) — [Lien LeetCode](https://leetcode.com/problems/unique-paths/)
  - *Technique :* `dp[r][c] = dp[r-1][c] + dp[r][c-1]` (uniquement haut / gauche).
  > Notes :
