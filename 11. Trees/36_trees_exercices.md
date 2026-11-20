# 🌳 Pattern 11 : Trees (Arbres Binaires & BST) — Plan d'Entraînement

Coche les cases `[x]` au fur et à mesure de ta progression. Les indices sont masqués pour te permettre de réfléchir sans spoiler.

---

## Série 1 : Parcours DFS Fondamentaux

- [ ] **104. Maximum Depth of Binary Tree** (Easy) — [LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
  <details><summary>💡 Indice d'approche</summary>DFS récursif : `1 + max(maxDepth(root.left), maxDepth(root.right))` avec `0` si `not root`.</details>
  > Notes : 

- [ ] **226. Invert Binary Tree** (Easy) — [LeetCode](https://leetcode.com/problems/invert-binary-tree/)
  <details><summary>💡 Indice d'approche</summary>DFS récursif : échange `root.left` et `root.right`, puis appelle récursivement sur les deux enfants.</details>
  > Notes : 

- [ ] **100. Same Tree** (Easy) — [LeetCode](https://leetcode.com/problems/same-tree/)
  <details><summary>💡 Indice d'approche</summary>DFS simultané sur `p` et `q` : vérifie les cas `None` et compare `p.val == q.val` ainsi que les sous-arbres gauche et droit.</details>
  > Notes : 

- [ ] **101. Symmetric Tree** (Easy) — [LeetCode](https://leetcode.com/problems/symmetric-tree/)
  <details><summary>💡 Indice d'approche</summary>Fonction auxiliaire `is_mirror(t1, t2)` comparant `t1.left` avec `t2.right` et `t1.right` avec `t2.left`.</details>
  > Notes : 

- [ ] **543. Diameter of Binary Tree** (Easy) — [LeetCode](https://leetcode.com/problems/diameter-of-binary-tree/)
  <details><summary>💡 Indice d'approche</summary>DFS bottom-up : la fonction renvoie la hauteur du sous-arbre tout en mettant à jour une variable maximale avec `left_height + right_height`.</details>
  > Notes : 

- [ ] **112. Path Sum** (Easy) — [LeetCode](https://leetcode.com/problems/path-sum/)
  <details><summary>💡 Indice d'approche</summary>DFS récursif en soustrayant `node.val` à `targetSum` ; vérifie l'égalité uniquement lorsque le nœud est une **feuille** (`not node.left and not node.right`).</details>
  > Notes : 

- [ ] **572. Subtree of Another Tree** (Easy) — [LeetCode](https://leetcode.com/problems/subtree-of-another-tree/)
  <details><summary>💡 Indice d'approche</summary>Parcours chaque nœud de `root` en DFS et teste l'identité exacte avec `subRoot` via la logique de `Same Tree`.</details>
  > Notes : 

---

## Série 2 : Parcours BFS (Par Niveau) & Propriétés des BST

- [ ] **111. Minimum Depth of Binary Tree** (Easy) — [LeetCode](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
  <details><summary>💡 Indice d'approche</summary>BFS avec `collections.deque` : la première feuille rencontrée donne immédiatement la profondeur minimale.</details>
  > Notes : 

- [ ] **637. Average of Levels in Binary Tree** (Easy) — [LeetCode](https://leetcode.com/problems/average-of-levels-in-binary-tree/)
  <details><summary>💡 Indice d'approche</summary>BFS par niveau : somme les valeurs de la boucle `for _ in range(len(queue)):` et divise par la taille du niveau.</details>
  > Notes : 

- [ ] **102. Binary Tree Level Order Traversal** (Medium) — [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/)
  <details><summary>💡 Indice d'approche</summary>Template classique BFS avec `deque` en accumulant les valeurs de chaque étage dans une sous-liste.</details>
  > Notes : 

- [ ] **199. Binary Tree Right Side View** (Medium) — [LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/)
  <details><summary>💡 Indice d'approche</summary>BFS par niveau : ajoute uniquement le dernier élément de chaque niveau (`i == level_size - 1`).</details>
  > Notes : 

- [ ] **700. Search in a Binary Search Tree** (Easy) — [LeetCode](https://leetcode.com/problems/search-in-a-binary-search-tree/)
  <details><summary>💡 Indice d'approche</summary>Exploite la propriété du BST : descends à gauche si `val < root.val`, sinon à droite, en $O(h)$.</details>
  > Notes : 

- [ ] **98. Validate Binary Search Tree** (Medium) — [LeetCode](https://leetcode.com/problems/validate-binary-search-tree/)
  <details><summary>💡 Indice d'approche</summary>DFS récursif en transmettant les bornes strictes `(min_val, max_val)` autorisées à chaque nœud.</details>
  > Notes : 

- [ ] **230. Kth Smallest Element in a BST** (Medium) — [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
  <details><summary>💡 Indice d'approche</summary>Un parcours **In-order** (Gauche -> Racine -> Droite) visite les éléments d'un BST dans l'ordre croissant exact.</details>
  > Notes : 

- [ ] **235. Lowest Common Ancestor of a Binary Search Tree** (Medium) — [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
  <details><summary>💡 Indice d'approche</summary>Tant que `p` et `q` sont tous deux plus petits ou tous deux plus grands que `curr`, descends du même côté ; le point de divergence est le LCA.</details>
  > Notes :
