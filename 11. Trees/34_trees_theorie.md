# 🌳 Pattern 11 : Trees (Arbres Binaires & BST)

## 1. Principe et Mécanique
Un **arbre binaire** (`TreeNode`) est une structure hiérarchique acyclique où chaque nœud possède une valeur (`val`) et au plus deux enfants : gauche (`left`) et droit (`right`). Parce qu'un arbre est naturellement récursif (chaque enfant est la racine d'un sous-arbre), la quasi-totalité des problèmes se résout avec **2 stratégies d'exploration** :

### A. DFS — Depth-First Search (Parcours en Profondeur)
On plonge le plus loin possible dans une branche avant de revenir en arrière (via la pile d'appels récursifs ou une `Stack` explicite).
Il existe **3 ordres de visite** :
- **Pre-order (`Racine -> Gauche -> Droite`) :** Idéal pour copier un arbre ou propager une information du haut vers le bas (ex: somme d'un chemin).
- **In-order (`Gauche -> Racine -> Droite`) :** Sur un **BST** (Binary Search Tree), ce parcours visite les valeurs dans l'**ordre croissant strict**.
- **Post-order (`Gauche -> Droite -> Racine`) :** Idéal pour remonter des résultats des feuilles vers la racine (ex: hauteur maximale, diamètre, suppression).

```text
        4
       / \
      2   6        Pre-order  : 4, 2, 1, 3, 6
     / \           In-order   : 1, 2, 3, 4, 6  (Trié car BST !)
    1   3          Post-order : 1, 3, 2, 6, 4

```

### B. BFS — Breadth-First Search (Parcours en Largeur / Niveau par Niveau)
On explore l'arbre étage par étage de haut en bas en utilisant une file FIFO (`collections.deque`). À chaque tour de boucle `while queue:`, on fige la taille du niveau actuel avec `nb_noeuds = len(queue)`.

```text
Niveau 0 :      [4]         -> queue = [4]
Niveau 1 :   [2]   [6]      -> queue = [2, 6]
Niveau 2 : [1] [3]          -> queue = [1, 3]
```

### C. Propriété du BST (Binary Search Tree)
Pour chaque nœud d'un BST :
- **Tous** les nœuds du sous-arbre gauche ont une valeur `< node.val`.
- **Tous** les nœuds du sous-arbre droit ont une valeur `> node.val`.
Cela permet une recherche en **$O(h)$** (soit $O(\log n)$ si l'arbre est équilibré).

---

## 2. Mots-clés et Déclencheurs dans les énoncés
Repère ces indices pour choisir immédiatement la bonne approche :
- **"Binary Tree"** / **"TreeNode"** / **"root"** -> Arbre classique (DFS ou BFS).
- **"Binary Search Tree" (BST)** -> Exploiter l'ordre (`left < root < right`) ou un parcours **In-order** trié.
- **"Maximum depth"** / **"Height"** / **"Diameter"** / **"Path sum"** -> **DFS** (récursif).
- **"Level order"** / **"Each level"** / **"Minimum depth"** / **"Right side view"** / **"Zigzag"** -> **BFS** avec `collections.deque`.
- **"Invert"** / **"Symmetric"** / **"Same tree"** / **"Subtree"** -> **DFS** comparant gauche et droite.

---

## 3. Quand l'utiliser & Complexités

| Approche | Cas d'usage typique | Temps | Espace |
| :--- | :--- | :--- | :--- |
| **DFS (Récursif)** | Profondeur max, validation BST, chemins, inversion | $O(n)$ | $O(h)$ (pile d'appels, $O(n)$ pire cas) |
| **BFS (`deque`)** | Parcours par niveau, profondeur min, vue de droite | $O(n)$ | $O(w)$ (largeur max, jusqu'à $n/2$) |
| **Recherche BST** | Trouver/insérer une valeur dans un BST | $O(h)$ | $O(1)$ en itératif |
---

## ⚠️ Cas limites à vérifier
- **Arbre vide (`root is None`) :** Cas de base obligatoire en première ligne de toute fonction récursive DFS ou avant d'initialiser une file BFS `deque([root])`.
- **Arbre dégénéré (peigne / liste chaînée) :** Un arbre déséquilibré de $10^5$ nœuds peut atteindre la limite de récursion Python (`RecursionError`, fixée par défaut à 1000 appels). Dans ce cas, privilégier un parcours itératif avec une `stack` ou `deque`.
- **Validation d'un BST (`Validate Binary Search Tree`) :** Vérifier uniquement `node.left.val < node.val < node.right.val` est **faux** : il faut transmettre les bornes globales `(min_val, max_val)` héritées des ancêtres.

## 🚫 Quand éviter ce pattern
- **Structure contenant des cycles (Graphe général) :** Un arbre est acyclique par définition, donc on n'a pas besoin de `visited`. Dès qu'un nœud peut avoir plusieurs parents ou former une boucle, basculer sur le pattern **Graphs (DFS/BFS + `visited` set)**.
