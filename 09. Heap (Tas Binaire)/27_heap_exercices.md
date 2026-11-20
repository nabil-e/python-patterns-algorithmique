# Heap (Tas Binaire) : Plan d'Entraînement

---

## 1. Tes Exercices Prioritaires (Liste Officielle)

### Niveau 1 : Mécanique de base (Simulation Max-Heap et Min-Heap)
* [ ] **1046. Last Stone Weight**
  * *Objectif :* Transformer la liste en Max-Heap (`-s`), extraire les deux plus grandes valeurs tant que `len(heap) > 1`, et réinsérer la différence si elles ne sont pas égales.
  * *Lien :* https://leetcode.com/problems/last-stone-weight/
* [ ] **2558. Take Gifts From the Richest Pile**
  * *Objectif :* Simuler un Max-Heap, extraire le maximum `k` fois et réinsérer `int(math.isqrt(val))` (ou `int(val ** 0.5)`).
  * *Lien :* https://leetcode.com/problems/take-gifts-from-the-richest-pile/
* [ ] **506. Relative Ranks**
  * *Pattern secondaire :* Sorting / Hashing.
  * *Objectif :* Utiliser un Max-Heap stockant des tuples `(-score, index)` pour attribuer les médailles et les rangs directement aux bons indices du tableau résultat.
  * *Lien :* https://leetcode.com/problems/relative-ranks/

### Niveau 2 : Top K et Flux de données
* [ ] **703. Kth Largest Element in a Stream**
  * *Objectif :* Maintenir un Min-Heap de taille `k` dans le `__init__` et dans la méthode `add(val)`. Retourner `self.heap[0]`.
  * *Lien :* https://leetcode.com/problems/kth-largest-element-in-a-stream/
* [ ] **215. Kth Largest Element in an Array**
  * *Objectif :* Appliquer exactement le Modèle B (Min-Heap de taille `k`) sur un tableau statique en `O(n log k)`.
  * *Lien :* https://leetcode.com/problems/kth-largest-element-in-an-array/
* [ ] **973. K Closest Points to Origin**
  * *Objectif :* Utiliser un Max-Heap de taille `k` stockant `(-(x*x + y*y), x, y)` pour garder les `k` points les plus proches de `(0, 0)` sans calcul de racine carrée.
  * *Lien :* https://leetcode.com/problems/k-closest-points-to-origin/
* [ ] **347. Top K Frequent Elements**
  * *Pattern secondaire :* Hashing (`Counter`).
  * *Objectif :* Compter les fréquences avec `Counter`, puis filtrer les `k` meilleurs via un Min-Heap de taille `k` (Modèle C).
  * *Lien :* https://leetcode.com/problems/top-k-frequent-elements/

---

## 2. Entraînement Complémentaire Répétitif

* [ ] **1337. The K Weakest Rows in a Matrix** *(Easy — Tuple `(force, index)` dans un Heap)*
* [ ] **692. Top K Frequent Words** *(Medium — Mixte Hashing + Heap avec ordre lexicographique)*
* [ ] **378. Kth Smallest Element in a Sorted Matrix** *(Medium — Min-Heap multi-listes)*

---

## 3. Compléments Top K (fiche Intervals / Top K / Sliding Window)

* [ ] **2099. Find Subsequence of Length K With the Largest Sum** *(Easy)* — Garder les K plus grandes valeurs **en préservant l'ordre d'apparition** (conserver l'indice avant sélection). [LeetCode](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/)
* [ ] **2335. Minimum Amount of Time to Fill Cups** *(Easy)* — Max-Heap : à chaque seconde, piocher les 2 catégories au plus grand besoin restant. [LeetCode](https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/)
* [ ] **451. Sort Characters By Frequency** *(Medium)* — `Counter` + Heap / tri par fréquence pour reconstruire la chaîne. *(Secondaire : Hashing)*. [LeetCode](https://leetcode.com/problems/sort-characters-by-frequency/)
* [ ] **373. Find K Pairs with Smallest Sums** *(Medium)* — Min-Heap pour explorer les plus petites sommes de paires sans tout générer. [LeetCode](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)
