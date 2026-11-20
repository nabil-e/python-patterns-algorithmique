# 🏋️ Pattern 11 : Trees (Arbres Binaires & BST) — Plan d'Entraînement

Coche les cases `[x]` au fur et à mesure de ta progression et note tes observations clés.

---

## Série 1 : DFS Fondamental (Récursif & Propriétés)
*Objectif : Maîtriser les appels récursifs sur les sous-arbres gauche et droit ainsi que le cas de base `if not root:`.*

- [ ] **104. Maximum Depth of Binary Tree** (Easy) — [Lien LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
  - *Technique :* DFS Post-order (`1 + max(left, right)`).
  > Notes : 

- [ ] **226. Invert Binary Tree** (Easy) — [Lien LeetCode](https://leetcode.com/problems/invert-binary-tree/)
  - *Technique :* DFS Pre-order ou Post-order (échange des pointeurs `left` et `right`).
  > Notes : 

- [ ] **100. Same Tree** (Easy) — [Lien LeetCode](https://leetcode.com/problems/same-tree/)
  - *Technique :* DFS simultané sur deux arbres (`p` et `q`).
  > Notes : 

- [ ] **101. Symmetric Tree** (Easy) — [Lien LeetCode](https://leetcode.com/problems/symmetric-tree/)
  - *Technique :* DFS miroir (`isMirror(t1.left, t2.right)` et `isMirror(t1.right, t2.left)`).
  > Notes : 

- [ ] **112. Path Sum** (Easy) — [Lien LeetCode](https://leetcode.com/problems/path-sum/)
  - *Technique :* DFS Top-down (soustraire `root.val` jusqu'aux feuilles `not root.left and not root.right`).
  > Notes : 

- [ ] **543. Diameter of Binary Tree** (Easy) — [Lien LeetCode](https://leetcode.com/problems/diameter-of-binary-tree/)
  - *Technique :* DFS Post-order avec mise à jour d'un maximum global (`left_h + right_h`).
  > Notes : 

---

## Série 2 : BFS par Niveau (`collections.deque`) & BST
*Objectif : Utiliser une file FIFO pour traiter l'arbre étage par étage et exploiter la propriété `gauche < racine < droite` des BST.*

- [ ] **102. Binary Tree Level Order Traversal** (Medium) — [Lien LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/)
  - *Technique :* BFS classique avec boucle `for _ in range(len(queue)):`.
  > Notes : 

- [ ] **199. Binary Tree Right Side View** (Medium) — [Lien LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/)
  - *Technique :* BFS par niveau (garder le dernier élément `i == taille_niveau - 1` de chaque étage).
  > Notes : 

- [ ] **700. Search in a Binary Search Tree** (Easy) — [Lien LeetCode](https://leetcode.com/problems/search-in-a-binary-search-tree/)
  - *Technique :* Recherche orientée en $O(h)$ dans un BST.
  > Notes : 

- [ ] **98. Validate Binary Search Tree** (Medium) — [Lien LeetCode](https://leetcode.com/problems/validate-binary-search-tree/)
  - *Technique :* DFS Top-down en transmettant les bornes `(min_val, max_val)` autorisées.
  > Notes : 

- [ ] **230. Kth Smallest Element in a BST** (Medium) — [Lien LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
  - *Technique :* DFS In-order (Gauche -> Racine -> Droite produit les éléments triés).
  > Notes : 

- [ ] **235. Lowest Common Ancestor of a Binary Search Tree** (Medium) — [Lien LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
  - *Technique :* Exploiter l'ordre BST pour trouver le point de divergence entre `p` et `q`.
  > Notes : 

---

## Série 3 : Compléments BFS / DFS (fiche BFS, DFS & DP)

- [ ] **111. Minimum Depth of Binary Tree** (Easy) — [Lien LeetCode](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
  - *Technique :* BFS — dès qu'une feuille apparaît, retourner la profondeur courante (plus court chemin).
  > Notes : 

- [ ] **637. Average of Levels in Binary Tree** (Easy) — [Lien LeetCode](https://leetcode.com/problems/average-of-levels-in-binary-tree/)
  - *Technique :* BFS — figer `len(queue)` pour isoler chaque niveau et calculer sa moyenne.
  > Notes : 

- [ ] **572. Subtree of Another Tree** (Easy) — [Lien LeetCode](https://leetcode.com/problems/subtree-of-another-tree/)
  - *Technique :* Double DFS — parcours de l'arbre principal + test d'identité structurelle de deux sous-arbres.
  > Notes : 
