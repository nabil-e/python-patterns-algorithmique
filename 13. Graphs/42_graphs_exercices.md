# 🕸️ Pattern 13 : Graphs — Plan d'Entraînement

Coche les cases `[x]` au fur et à mesure de ta progression. Les indices sont masqués pour te permettre de réfléchir sans spoiler.

---

## Série 1 : Grilles 2D & Composantes Connexes (DFS / BFS)

- [ ] **200. Number of Islands** (Medium) — [LeetCode](https://leetcode.com/problems/number-of-islands/)
  <details><summary>💡 Indice d'approche</summary>Parcours chaque cellule de la grille : dès que tu rencontres un `'1'`, incrémente le compteur et lance un DFS ou BFS pour marquer toute l'île comme visitée (`'0'`).</details>
  > Notes : 

- [ ] **695. Max Area of Island** (Medium) — [LeetCode](https://leetcode.com/problems/max-area-of-island/)
  <details><summary>💡 Indice d'approche</summary>Identique à Number of Islands, mais ta fonction DFS retourne la taille de la composante (`1 + dfs(haut) + dfs(bas) + dfs(gauche) + dfs(droite)`).</details>
  > Notes : 

- [ ] **733. Flood Fill** (Easy) — [LeetCode](https://leetcode.com/problems/flood-fill/)
  <details><summary>💡 Indice d'approche</summary>Sauvegarde la couleur de départ ; si elle est déjà égale à la nouvelle couleur, retourne immédiatement l'image (sinon boucle infinie), puis propage en DFS/BFS.</details>
  > Notes : 

- [ ] **994. Rotting Oranges** (Medium) — [LeetCode](https://leetcode.com/problems/rotting-oranges/)
  <details><summary>💡 Indice d'approche</summary>BFS multi-sources : ajoute initialement toutes les oranges pourries (`2`) dans `deque` avec un temps `0`, puis propage niveau par niveau en comptant les oranges fraîches restantes.</details>
  > Notes : 

- [ ] **130. Surrounded Regions** (Medium) — [LeetCode](https://leetcode.com/problems/surrounded-regions/)
  <details><summary>💡 Indice d'approche</summary>Inverse le problème : lance un DFS depuis tous les `'O'` situés sur les **4 bords** de la grille pour les protéger (`'#'`), puis transforme les `'O'` restants en `'X'`.</details>
  > Notes : 

---

## Série 2 : Listes d'Adjacence, Clonage & Tri Topologique

- [ ] **133. Clone Graph** (Medium) — [LeetCode](https://leetcode.com/problems/clone-graph/)
  <details><summary>💡 Indice d'approche</summary>Utilise un dictionnaire `old_to_new` (Hashing) couplé à un DFS ou BFS pour éviter de cloner plusieurs fois un même nœud en cas de cycle.</details>
  > Notes : 

- [ ] **207. Course Schedule** (Medium) — [LeetCode](https://leetcode.com/problems/course-schedule/)
  <details><summary>💡 Indice d'approche</summary>Détection de cycle dans un graphe orienté : utilise l'algorithme de Kahn (BFS avec tableau des degrés entrants `in_degree`) ou un DFS à 3 états (`0=non visité`, `1=en cours`, `2=visité`).</details>
  > Notes : 

- [ ] **210. Course Schedule II** (Medium) — [LeetCode](https://leetcode.com/problems/course-schedule-ii/)
  <details><summary>💡 Indice d'approche</summary>Même logique que Course Schedule avec l'algorithme de Kahn : ajoute chaque cours dépilé à une liste `order` et vérifie à la fin que `len(order) == numCourses`.</details>
  > Notes : 

- [ ] **417. Pacific Atlantic Water Flow** (Medium) — [LeetCode](https://leetcode.com/problems/pacific-atlantic-water-flow/)
  <details><summary>💡 Indice d'approche</summary>Remonte le courant depuis les deux océans (bords haut/gauche pour Pacifique, bas/droite pour Atlantique) vers les hauteurs `>=` et prends l'intersection des deux `set` de cellules visitées.</details>
  > Notes : 

- [ ] **1091. Shortest Path in Binary Matrix** (Medium) — [LeetCode](https://leetcode.com/problems/shortest-path-in-binary-matrix/)
  <details><summary>💡 Indice d'approche</summary>Plus court chemin dans un graphe non pondéré avec 8 directions autorisées : un BFS standard avec `deque` garantit la distance minimale dès la première arrivée en `(n-1, n-1)`.</details>
  > Notes : 
