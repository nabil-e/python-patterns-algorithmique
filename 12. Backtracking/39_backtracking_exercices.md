# 🏋️ Pattern 12 : Backtracking — Plan d'Entraînement

Coche les cases `[x]` au fur et à mesure de ta progression. Les indices sont masqués pour te permettre de réfléchir sans spoiler.

---

## Série 1 : Les Fondamentaux (Subsets, Permutations & Combinaisons)

- [ ] **78. Subsets** (Medium) — [LeetCode](https://leetcode.com/problems/subsets/)
  <details><summary>💡 Indice d'approche</summary>Ajoute `path.copy()` à chaque entrée dans la fonction récursive et avance avec `start = i + 1`.</details>
  > Notes : 

- [ ] **46. Permutations** (Medium) — [LeetCode](https://leetcode.com/problems/permutations/)
  <details><summary>💡 Indice d'approche</summary>Parcours tous les index de `0` à `n - 1` à chaque appel en maintenant un tableau booléen `used` (ou en testant `if num not in path`).</details>
  > Notes : 

- [ ] **77. Combinations** (Medium) — [LeetCode](https://leetcode.com/problems/combinations/)
  <details><summary>💡 Indice d'approche</summary>Identique à `Subsets`, mais n'ajoute `path.copy()` que lorsque `len(path) == k` (et coupe la boucle dès qu'il ne reste plus assez d'éléments pour atteindre `k`).</details>
  > Notes : 

- [ ] **39. Combination Sum** (Medium) — [LeetCode](https://leetcode.com/problems/combination-sum/)
  <details><summary>💡 Indice d'approche</summary>Comme chaque élément peut être réutilisé plusieurs fois, passe `i` (et non `i + 1`) lors de l'appel récursif.</details>
  > Notes : 

- [ ] **22. Generate Parentheses** (Medium) — [LeetCode](https://leetcode.com/problems/generate-parentheses/)
  <details><summary>💡 Indice d'approche</summary>Maintiens deux compteurs `open_count` et `close_count` : ajoute `'('` si `open_count < n`, et `')'` uniquement si `close_count < open_count`.</details>
  > Notes : 

---

## Série 2 : Élagage des Doublons & Grille 2D

- [ ] **79. Word Search** (Medium) — [LeetCode](https://leetcode.com/problems/word-search/)
  <details><summary>💡 Indice d'approche</summary>Lance un DFS backtracking depuis chaque case correspondant à `word[0]`, marque la case visitée avec `"#"` et restaure-la après l'exploration des 4 directions.</details>
  > Notes : 

- [ ] **90. Subsets II** (Medium) — [LeetCode](https://leetcode.com/problems/subsets-ii/)
  <details><summary>💡 Indice d'approche</summary>Trie `nums` au préalable, puis dans la boucle `for i in range(start, len(nums)):`, saute les doublons avec `if i > start and nums[i] == nums[i - 1]: continue`.</details>
  > Notes : 

- [ ] **40. Combination Sum II** (Medium) — [LeetCode](https://leetcode.com/problems/combination-sum-ii/)
  <details><summary>💡 Indice d'approche</summary>Combine le tri + saut de doublons (`i > start and candidates[i] == candidates[i - 1]`) avec l'avancement `i + 1` (chaque élément n'est utilisé qu'une fois).</details>
  > Notes : 

- [ ] **17. Letter Combinations of a Phone Number** (Medium) — [LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
  <details><summary>💡 Indice d'approche</summary>Utilise un dictionnaire `digit -> lettres` et avance l'index dans la chaîne `digits` à chaque niveau de récursion.</details>
  > Notes : 

- [ ] **131. Palindrome Partitioning** (Medium) — [LeetCode](https://leetcode.com/problems/palindrome-partitioning/)
  <details><summary>💡 Indice d'approche</summary>À chaque position `start`, teste toutes les sous-chaînes `s[start:end+1]` : si la tranche est un palindrome, ajoute-la à `path` et explore `end + 1`.</details>
  > Notes :
