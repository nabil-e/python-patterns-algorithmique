# PATTERN 11 / 11 : Trees (Arbres Binaires & BST)
> **Explorer une structure hiérarchique en profondeur (DFS) ou par niveau (BFS)**

**Principe clé :** Un arbre binaire est une structure récursive composée de nœuds (`val`, `left`, `right`). Le **DFS** (récursif ou pile) explore chaque branche jusqu'aux feuilles avant de remonter ; le **BFS** (file `collections.deque`) visite l'arbre étage par étage. Dans un **BST** (Binary Search Tree), le parcours *In-order* (`Gauche -> Nœud -> Droite`) produit les valeurs triées.  
**Complexité cible :** Temps : $O(n)$ | Espace : $O(h)$ (DFS) ou $O(w)$ (BFS)

---

## 1. INDICES DANS L'ÉNONCÉ & MOTS-CLÉS

| Ce que l'énoncé demande | Mots-clés (Anglais) | Approche à adopter |
| :--- | :--- | :--- |
| Hauteur maximale, diamètre, symétrie ou chemin racine-feuille | `max depth`, `diameter`, `path sum`, `invert` | **DFS Récursif** (remonter l'info des sous-arbres) |
| Parcours niveau par niveau, vue de droite ou distance minimale | `level order`, `right side view`, `min depth` | **BFS Itératif** avec `collections.deque` |
| Valider un BST, chercher une valeur ou le K-ième plus petit | `validate BST`, `kth smallest`, `lowest common ancestor` | **Propriété BST** (`In-order` ou bornes `min`/`max`) |

---

## 2. VARIANTES & ASTUCES DE DÉCISION

* **DFS (Diviser pour régner) :** Traitez le cas de base `if not root: return ...`, appelez récursivement sur `root.left` et `root.right`, puis combinez les deux résultats.
* **BFS par niveau :** Figez la taille de l'étage courant avec `for _ in range(len(queue)):` et utilisez `queue.popleft()` (en $O(1)$).
* **Piège du BST :** Ne comparez pas uniquement `root.left.val < root.val < root.right.val` ; passez les bornes `(low, high)` à chaque appel récursif pour valider tout le sous-arbre.

---

## 3. SQUELETTE DE CODE (PYTHON)

```python
from collections import deque

def levelOrderBFS(root):
    if not root:
        return []
    res, queue = [], deque([root])
    while queue:
        niveau = []
        for _ in range(len(queue)):
            node = queue.popleft()
            niveau.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(niveau)
    return res
```
