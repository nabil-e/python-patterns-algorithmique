# 11. TREES (ARBRES BINAIRES & BST)
*Exploration récursive par sous-arbres (DFS) ou parcours niveau par niveau (BFS)*

---

## 1. IDÉE CENTRALE & COMPLEXITÉ

Un arbre binaire est une structure récursive où chaque nœud (`TreeNode`) possède une valeur `val` et deux enfants (`left` et `right`). La majorité des problèmes se résolvent en décomposant la question sur les sous-arbres gauche et droit (DFS), ou en explorant étage par étage avec une file (BFS).

* **Complexité temporelle :** $O(n)$ — chaque nœud est visité exactement une fois.
* **Complexité spatiale :**
  * **DFS (Récursif) :** $O(h)$ où $h$ est la hauteur de l'arbre ($O(\log n)$ si équilibré, $O(n)$ au pire cas si filiforme).
  * **BFS (File `deque`) :** $O(w)$ où $w$ est la largeur maximale de l'arbre ($O(n/2) = O(n)$ au niveau des feuilles).

---

## 2. INDICES DANS L'ÉNONCÉ

| Indice dans l'énoncé | Mots-clés (Anglais) | Approche à privilégier |
| :--- | :--- | :--- |
| Hauteur, profondeur, diamètre ou équilibrage d'un arbre | `max depth`, `height`, `diameter`, `balanced tree` | **DFS Post-Order** (remonter les hauteurs) |
| Parcours niveau par niveau, vue de droite ou moyenne par étage | `level order`, `right side view`, `zigzag`, `average of levels` | **BFS avec `deque`** (boucle `for _ in range(len(q))`) |
| Chemin de la racine vers une feuille, somme cible ou ancêtre commun | `root-to-leaf`, `path sum`, `lowest common ancestor (LCA)` | **DFS Pre-Order** (descendre l'état) |
| Arbre binaire de recherche : validation, k-ième plus petit élément | `Binary Search Tree (BST)`, `validate BST`, `kth smallest` | **DFS In-Order** (`Left -> Root -> Right` = trié) |
| Comparer deux arbres ou vérifier une symétrie miroir | `same tree`, `symmetric`, `subtree`, `invert binary tree` | **DFS simultané** sur `(node1, node2)` |

---

## 3. VARIANTES & PIÈGES COURANTS

### Les 3 ordres du DFS (Parcours en profondeur)
* **Pre-Order (`Root -> Left -> Right`) :** On traite le nœud **avant** de descendre (ex. : copier un arbre, transmettre une somme ou des bornes `(min_val, max_val)`).
* **In-Order (`Left -> Root -> Right`) :** Sur un **BST**, visite les valeurs dans l'**ordre croissant strict**.
* **Post-Order (`Left -> Right -> Root`) :** On récupère d'abord les résultats des enfants pour calculer celui du parent (ex. : hauteur, diamètre, suppression).

### Les 3 pièges classiques à éviter
1. **Oublier le cas de base `if not root:` :** C'est la première ligne de presque toute fonction récursive sur un arbre. Définissez clairement ce qu'elle renvoie (`0` pour une hauteur, `True` pour une validation, `None` pour un nœud).
2. **Confondre nœuds et arêtes :** La hauteur/profondeur en nombre de **nœuds** renvoie `0` si `not root` (et `1 + max(...)`), tandis qu'en nombre d'**arêtes** elle renvoie `-1`.
3. **Valider un BST uniquement avec ses enfants directs :** Vérifier `node.left.val < node.val < node.right.val` est **faux** (tout le sous-arbre gauche doit être strictement inférieur à `node.val`). Il faut transmettre un intervalle `(low, high)` en descendant.

---

## 4. SQUELETTES DE CODE EN PYTHON

### Variante A : DFS Récursif (Hauteur & Diamètre — Post-Order)
```python
from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def max_depth_and_diameter(root: Optional[TreeNode]) -> int:
    diameter = 0

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal diameter
        if not node:
            return 0  # Cas de base : hauteur d'un arbre vide
        
        left_h = dfs(node.left)
        right_h = dfs(node.right)
        
        # Mise à jour globale (Post-Order)
        diameter = max(diameter, left_h + right_h)
        
        # Remonter la hauteur au parent
        return 1 + max(left_h, right_h)

    dfs(root)
    return diameter
```

### Variante B : BFS Niveau par Niveau (`collections.deque`)
```python
from collections import deque
from typing import Optional, List

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
        
    res: List[List[int]] = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)  # Figer la taille de l'étage actuel
        current_level: List[int] = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        res.append(current_level)
        
    return res
```
