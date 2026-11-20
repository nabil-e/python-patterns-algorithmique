# 🏋️ Pattern 06 : Prefix / Suffix Sum — Plan d'Entraînement

Coche les cases `[x]` au fur et à mesure de ta progression et note tes observations clés.

---

## Série 1 : Tes Exercices Prioritaires (Sommes cumulées)
*Objectif : Maîtriser la construction du tableau de préfixes et la requête en O(1).*

- [ ] **1480. Running Sum of 1d Array** (Easy) — [Lien LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/)
  <details><summary>💡 Indice d'approche</summary>Accumule la somme au fur et à mesure (`itertools.accumulate(nums)` ou boucle simple en place).</details>
  > Notes : 

- [ ] **1732. Find the Highest Altitude** (Easy) — [Lien LeetCode](https://leetcode.com/problems/find-the-highest-altitude/)
  <details><summary>💡 Indice d'approche</summary>Part d'une altitude initiale de 0, ajoute chaque variation `gain[i]` et garde le maximum atteint.</details>
  > Notes : 

- [ ] **303. Range Sum Query - Immutable** (Easy) — [Lien LeetCode](https://leetcode.com/problems/range-sum-query-immutable/)
  <details><summary>💡 Indice d'approche</summary>Précalcule un tableau `prefix` de taille `n + 1` avec `prefix = 0` pour répondre à `sumRange(left, right)` via `prefix[right + 1] - prefix[left]`.</details>
  > Notes : 

- [ ] **1413. Minimum Value to Get Positive Step by Step Sum** (Easy) — [Lien LeetCode](https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/)
  <details><summary>💡 Indice d'approche</summary>Calcule la somme cumulée minimale `min_prefix`. Pour ne jamais descendre sous 1, `startValue = max(1, 1 - min_prefix)`.</details>
  > Notes : 

- [ ] **2574. Left and Right Sum Differences** (Easy) — [Lien LeetCode](https://leetcode.com/problems/left-and-right-sum-differences/)
  <details><summary>💡 Indice d'approche</summary>Maintiens `left_sum = 0` et `right_sum = sum(nums)`. À chaque élément `x`, retire `x` de `right_sum`, calcule `abs(left_sum - right_sum)`, puis ajoute `x` à `left_sum`.</details>
  > Notes : 

---

## Série 2 : Préfixe/Suffixe & Combinaison avec Hashing
*Objectif : Résoudre les problèmes intermédiaires classiques sans boucle imbriquée.*

- [ ] **238. Product of Array Except Self** (Medium) — [Lien LeetCode](https://leetcode.com/problems/product-of-array-except-self/)
  <details><summary>💡 Indice d'approche</summary>Fais deux passes sans division : une passe gauche-droite pour stocker les produits préfixes dans `res`, puis une passe droite-gauche en multipliant par un accumulateur `suffix`.</details>
  > Notes : 

- [ ] **560. Subarray Sum Equals K** (Medium) — [Lien LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/)
  <details><summary>💡 Indice d'approche</summary>Combinaison <b>Prefix Sum + Hashing</b> : stocke la fréquence de chaque somme préfixe rencontrée (avec `{0: 1}` au départ) et ajoute `count[curr_sum - k]`.</details>
  > Notes : 

- [ ] **724. Find Pivot Index** (Easy) — [Lien LeetCode](https://leetcode.com/problems/find-pivot-index/)
  <details><summary>💡 Indice d'approche</summary>Calcule `total = sum(nums)`. À chaque index, `right_sum = total - left_sum - nums[i]`. Vérifie si `left_sum == right_sum`.</details>
  > Notes : 

- [ ] **525. Contiguous Array** (Medium) — [Lien LeetCode](https://leetcode.com/problems/contiguous-array/)
  <details><summary>💡 Indice d'approche</summary>Transforme mentalement chaque `0` en `-1` : le problème revient à trouver le plus long sous-tableau de somme nulle via <b>Prefix Sum + Hashing</b> (mémoriser le premier index de chaque somme).</details>
  > Notes : 
