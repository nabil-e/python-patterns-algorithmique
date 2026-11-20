# ⛰️ Pattern 9 : Heap (Tas Binaire) — Plan d'Entraînement

Coche les cases `[x]` au fur et à mesure de ta progression. Les indices sont masqués pour te permettre de réfléchir sans spoiler.

---

## Série 1 : Simulation & Top K (Tes Exercices Prioritaires)

- [ ] **1046. Last Stone Weight** (Easy) — [LeetCode](https://leetcode.com/problems/last-stone-weight/)
  <details><summary>💡 Indice d'approche</summary>Simule un Max-Heap en inversant le signe des pierres (`-x`), extrais les deux plus lourdes et réinsère la différence si non nulle.</details>
  > Notes : 

- [ ] **2558. Take Gifts From the Richest Pile** (Easy) — [LeetCode](https://leetcode.com/problems/take-gifts-from-the-richest-pile/)
  <details><summary>💡 Indice d'approche</summary>Max-Heap via négation : répète `k` fois l'extraction du maximum et réinsère `-math.isqrt(val)`.</details>
  > Notes : 

- [ ] **506. Relative Ranks** (Easy) — [LeetCode](https://leetcode.com/problems/relative-ranks/)
  <details><summary>💡 Indice d'approche</summary>Insère `(-score, index)` dans un tas (ou trie les index par score décroissant) pour attribuer les médailles aux bonnes positions.</details>
  > Notes : 

- [ ] **703. Kth Largest Element in a Stream** (Easy) — [LeetCode](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
  <details><summary>💡 Indice d'approche</summary>Maintiens un Min-Heap de taille fixe `k` : le sommet `heap[0]` représente toujours le K-ième plus grand élément du flux.</details>
  > Notes : 

- [ ] **215. Kth Largest Element in an Array** (Medium) — [LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/)
  <details><summary>💡 Indice d'approche</summary>Min-Heap de taille `k` en $O(n \log k)$ : pousse chaque élément et fais `heappop` dès que `len(heap) > k`.</details>
  > Notes : 

- [ ] **973. K Closest Points to Origin** (Medium) — [LeetCode](https://leetcode.com/problems/k-closest-points-to-origin/)
  <details><summary>💡 Indice d'approche</summary>Max-Heap de taille `k` sur la distance au carré `-(x*x + y*y)` (inutile de calculer la racine carrée).</details>
  > Notes : 

- [ ] **347. Top K Frequent Elements** (Medium) — [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)
  <details><summary>💡 Indice d'approche</summary>Hashing (`Counter`) + Min-Heap de taille `k` sur les paires `(freq, num)`.</details>
  > Notes : 

---

## Série 2 : Entraînement Répétitif & Compléments

- [ ] **2099. Find Subsequence of Length K With the Largest Sum** (Easy) — [LeetCode](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/)
  <details><summary>💡 Indice d'approche</summary>Min-Heap de taille `k` avec `(valeur, index)` pour retenir les `k` plus grands, puis trie ces `k` éléments selon leur `index` d'origine.</details>
  > Notes : 

- [ ] **2335. Minimum Amount of Time to Fill Cups** (Easy) — [LeetCode](https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/)
  <details><summary>💡 Indice d'approche</summary>Max-Heap via négation : à chaque seconde, décrémente les deux types de boissons ayant le plus grand volume restant.</details>
  > Notes : 

- [ ] **451. Sort Characters By Frequency** (Medium) — [LeetCode](https://leetcode.com/problems/sort-characters-by-frequency/)
  <details><summary>💡 Indice d'approche</summary>Compte les fréquences avec `Counter`, puis utilise un Max-Heap `(-freq, char)` pour reconstruire la chaîne.</details>
  > Notes : 

- [ ] **373. Find K Pairs with Smallest Sums** (Medium) — [LeetCode](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)
  <details><summary>💡 Indice d'approche</summary>Initialise un Min-Heap avec `(nums1[i] + nums2[0], i, 0)` pour `i < min(k, len(nums1))`, puis avance l'index de `nums2` à chaque extraction.</details>
  > Notes : 

- [ ] **692. Top K Frequent Words** (Medium) — [LeetCode](https://leetcode.com/problems/top-k-frequent-words/)
  <details><summary>💡 Indice d'approche</summary>`Counter` + tas avec clé `(-freq, mot)` afin de départager les égalités de fréquence par ordre alphabétique croissant.</details>
  > Notes :
