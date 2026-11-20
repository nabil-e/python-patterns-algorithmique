# 🪟 Pattern 5 : Sliding Window — Plan d'Entraînement

Coche les cases `[x]` au fur et à mesure de ta progression. Les indices sont masqués pour te permettre de réfléchir sans spoiler.

---

## Série 1 : Fenêtre de Taille Fixe

- [ ] **643. Maximum Average Subarray I** (Easy) — [LeetCode](https://leetcode.com/problems/maximum-average-subarray-i/)
  <details><summary>💡 Indice d'approche</summary>Fenêtre glissante de taille fixe `k` : calcule la somme des `k` premiers éléments, puis fais glisser en ajoutant l'élément entrant et en retirant l'élément sortant.</details>
  > Notes : 

- [ ] **1876. Substrings of Size Three with Distinct Characters** (Easy) — [LeetCode](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/)
  <details><summary>💡 Indice d'approche</summary>Fenêtre fixe de taille `3` : vérifie à chaque pas si la taille du `set` de la sous-chaîne vaut `3` (ou compare les 3 caractères directement).</details>
  > Notes : 

- [ ] **2379. Minimum Recolors to Get K Consecutive Black Blocks** (Easy) — [LeetCode](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/)
  <details><summary>💡 Indice d'approche</summary>Fenêtre fixe de taille `k` : compte les blocs blancs `'W'` dans la fenêtre initiale et minimise ce compteur au fil du glissement.</details>
  > Notes : 

- [ ] **219. Contains Duplicate II** (Easy) — [LeetCode](https://leetcode.com/problems/contains-duplicate-ii/)
  <details><summary>💡 Indice d'approche</summary>Fenêtre fixe de taille maximale `k` maintenue avec un `set` (Hashing) : supprime `nums[right - k]` dès que la fenêtre dépasse la taille `k`.</details>
  > Notes : 

- [ ] **2269. Find the K-Beauty of a Number** (Easy) — [LeetCode](https://leetcode.com/problems/find-the-k-beauty-of-a-number/)
  <details><summary>💡 Indice d'approche</summary>Convertis l'entier en chaîne `str(num)` et fais glisser une fenêtre de taille `k` en vérifiant que le diviseur extrait n'est pas nul (`!= 0`).</details>
  > Notes : 

- [ ] **1984. Minimum Difference Between Highest and Lowest of K Scores** (Easy) — [LeetCode](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/)
  <details><summary>💡 Indice d'approche</summary>Trie d'abord le tableau pour rapprocher les scores voisins, puis fais glisser une fenêtre de taille `k` en calculant `nums[right] - nums[left]`.</details>
  > Notes : 

---

## Série 2 : Entraînement Répétitif — Fenêtre Fixe & Variable

- [ ] **1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold** (Medium) — [LeetCode](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)
  <details><summary>💡 Indice d'approche</summary>Fenêtre fixe de taille `k` : compare la somme courante à `threshold * k` pour éviter les divisions flottantes.</details>
  > Notes : 

- [ ] **1456. Maximum Number of Vowels in a Substring of Given Length** (Medium) — [LeetCode](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)
  <details><summary>💡 Indice d'approche</summary>Fenêtre fixe de taille `k` : incrémente le compteur si le caractère entrant est dans `{"a", "e", "i", "o", "u"}` et décrémente si le caractère sortant en est une.</details>
  > Notes : 

- [ ] **3. Longest Substring Without Repeating Characters** (Medium) — [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
  <details><summary>💡 Indice d'approche</summary>Fenêtre variable + Hashing (`set` ou `dict` des derniers index) : tant que `s[right]` est déjà dans la fenêtre, avance `left`.</details>
  > Notes : 

- [ ] **1004. Max Consecutive Ones III** (Medium) — [LeetCode](https://leetcode.com/problems/max-consecutive-ones-iii/)
  <details><summary>💡 Indice d'approche</summary>Fenêtre variable : compte le nombre de `0` dans la fenêtre ; tant que ce compteur dépasse `k`, avance `left`.</details>
  > Notes : 

- [ ] **209. Minimum Size Subarray Sum** (Medium) — [LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/)
  <details><summary>💡 Indice d'approche</summary>Fenêtre variable minimale : tant que `current_sum >= target`, mets à jour `min_len` et rétrécis par la gauche (`left += 1`).</details>
  > Notes : 

- [ ] **424. Longest Repeating Character Replacement** (Medium) — [LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/)
  <details><summary>💡 Indice d'approche</summary>Fenêtre variable + `dict` de fréquences : la fenêtre reste valide tant que `(right - left + 1) - max_freq <= k`.</details>
  > Notes : 

---

## Note Hors-Pattern (Exercice de ta liste initiale)

- [ ] **14. Longest Common Prefix** (Easy) — [LeetCode](https://leetcode.com/problems/longest-common-prefix/)
  <details><summary>💡 Indice d'approche</summary>Hors Sliding Window (String Scanning) : compare caractère par caractère le premier et le dernier mot après un tri alphabétique (`strs.sort()`), ou effectue un balayage vertical sur `strs`.</details>
  > Notes :
