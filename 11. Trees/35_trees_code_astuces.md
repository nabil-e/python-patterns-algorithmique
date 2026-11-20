# 💻 Pattern 11 : Trees (Arbres Binaires & BST) — Squelettes, Code & Astuces

## 1. Squelettes Génériques (Boilerplates)

### Squelette A : DFS Récursif (Profondeur)
```python
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def dfs_tree_skeleton(root: Optional[TreeNode]) -> int:
    # 1. Cas de base
    if not root:
        return 0

    # 2. Appels récursifs sur les sous-arbres gauche et droit
    left_res = dfs_tree_skeleton(root.left)
    right_res = dfs_tree_skeleton(root.right)

    # 3. Combinaison des résultats pour le nœud courant
    return 1 + max(left_res, right_res)
```

### Squelette B : BFS Itératif par niveau (`deque`)
```python
from collections import deque
from typing import Optional


def bfs_tree_skeleton(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []

    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level_size = len(queue)  # Figer la taille du niveau actuel
        current_level: list[int] = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result
```

---

## 2. Démos Exécutables & Bac à Sable (`main.py`)

```python
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


# --- Utilitaire de test local (format tableau LeetCode) ---
def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue: deque[TreeNode] = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# --- 1. DÉMOS DU PATTERN (Exécutables) ---

def max_depth(root: Optional[TreeNode]) -> int:
    """LeetCode 104 : Profondeur maximale par DFS post-order."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def level_order(root: Optional[TreeNode]) -> list[list[int]]:
    """LeetCode 102 : Parcours par niveau (BFS)."""
    if not root:
        return []
    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level: list[int] = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


def is_valid_bst(
    root: Optional[TreeNode],
    min_val: float = float("-inf"),
    max_val: float = float("inf"),
) -> bool:
    """LeetCode 98 : Validation d'un BST via bornes min/max héritées."""
    if not root:
        return True
    if not (min_val < root.val < max_val):
        return False
    return is_valid_bst(root.left, min_val, root.val) and is_valid_bst(
        root.right, root.val, max_val
    )


# --- 2. BAC À SABLE EXERCICES (À compléter) ---

def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """LeetCode 226 : Invert Binary Tree. À compléter !"""
    pass


if __name__ == "__main__":
    tree = build_tree([3, 9, 20, None, None, 15, 7])
    print("Max depth :", max_depth(tree))  # 3
    print("Level order :", level_order(tree))  # [[3], [9, 20], [15, 7]]

    bst = build_tree([5, 1, 7, None, None, 6, 8])
    print("Valid BST :", is_valid_bst(bst))  # True
```

---

## 3. Trucs et Astuces Python
- **`collections.deque` obligatoire pour le BFS :** `queue.popleft()` s'exécute en $O(1)$, alors que `list.pop(0)` coûte $O(n)$ à chaque nœud (dégradant le BFS en $O(n^2)$).
- **Parcours In-order sur un BST :** Visiter `Gauche -> Racine -> Droite` sur un arbre binaire de recherche produit toujours les valeurs **triées par ordre croissant**.
- **`float("-inf")` et `float("inf")` :** Idéal pour initialiser les bornes de validation d'un BST sans se soucier de la taille des entiers.

---

## 4. Pièges à éviter
- **Valider un BST uniquement avec les enfants directs :** Vérifier `node.left.val < node.val < node.right.val` est **faux**. Tout le sous-arbre droit doit être supérieur à la racine (d'où la propagation des bornes `min_val` et `max_val`).
- **Oublier `if not root:` en tête de fonction récursive :** C'est le cas de base universel des arbres ; sans lui, `root.left` provoque immédiatement un `AttributeError`.
- **Ne pas figer `len(queue)` dans la boucle BFS :** La longueur de `queue` augmente pendant qu'on ajoute les enfants ; `for _ in range(len(queue)):` évalue `len(queue)` une seule fois au début du tour, ce qui isole proprement chaque niveau.
