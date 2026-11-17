# 💻 Pattern 11 : Trees — Squelettes, Code & Astuces

## 1. Squelettes Génériques (Boilerplates)

### Squelette A : DFS Récursif (Post-order / Remontée d'info)
```python
def squelette_dfs(root):
    # 1. Cas de base (nœud vide)
    if not root:
        return ...  # 0, True, None, etc.

    # 2. Appels récursifs sur les sous-arbres gauche et droit
    gauche = squelette_dfs(root.left)
    droite = squelette_dfs(root.right)

    # 3. Combiner les résultats au niveau du nœud courant
    return ...
```

### Squelette B : BFS Niveau par Niveau (`collections.deque`)
```python
from collections import deque

def squelette_bfs(root):
    if not root:
        return []

    queue = deque([root])
    resultat = []

    while queue:
        taille_niveau = len(queue)
        niveau_courant = []

        for _ in range(taille_niveau):
            node = queue.popleft()
            niveau_courant.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        resultat.append(niveau_courant)

    return resultat
```

---

## 2. Templates Python Exécutables (Prêts à lancer)

Ce fichier inclut un constructeur d'arbre à partir d'une liste LeetCode (`construire_arbre`) pour tester tes fonctions directement dans `main.py`.

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


# --- Utilitaire de test local (format LeetCode [3, 9, 20, None, None, 15, 7]) ---
def construire_arbre(valeurs: list[Optional[int]]) -> Optional[TreeNode]:
    if not valeurs or valeurs[0] is None:
        return None
    root = TreeNode(valeurs[0])
    queue = deque([root])
    i = 1
    while queue and i < len(valeurs):
        curr = queue.popleft()
        if i < len(valeurs) and valeurs[i] is not None:
            curr.left = TreeNode(valeurs[i])
            queue.append(curr.left)
        i += 1
        if i < len(valeurs) and valeurs[i] is not None:
            curr.right = TreeNode(valeurs[i])
            queue.append(curr.right)
        i += 1
    return root


# --- Template 1 : Profondeur maximale par DFS (LeetCode 104) ---
def profondeur_max(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(profondeur_max(root.left), profondeur_max(root.right))


# --- Template 2 : Parcours par niveau par BFS (LeetCode 102) ---
def parcours_par_niveau(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []
    queue = deque([root])
    niveaux = []
    while queue:
        niveau = []
        for _ in range(len(queue)):
            node = queue.popleft()
            niveau.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        niveaux.append(niveau)
    return niveaux


# --- Template 3 : Valider un BST avec bornes min/max (LeetCode 98) ---
def est_bst_valide(
    root: Optional[TreeNode],
    borne_min: float = float("-inf"),
    borne_max: float = float("inf"),
) -> bool:
    if not root:
        return True
    if not (borne_min < root.val < borne_max):
        return False
    return est_bst_valide(root.left, borne_min, root.val) and est_bst_valide(
        root.right, root.val, borne_max
    )


if __name__ == "__main__":
    # Arbre : [3, 9, 20, None, None, 15, 7]
    arbre = construire_arbre([3, 9, 20, None, None, 15, 7])
    print("Profondeur max :", profondeur_max(arbre))         # 3
    print("Niveaux BFS    :", parcours_par_niveau(arbre))    # [[3], [9, 20], [15, 7]]

    # Test BST valide
    bst = construire_arbre([5, 3, 7, 2, 4, 6, 8])
    print("Est un BST ?   :", est_bst_valide(bst))           # True
```

---

## 3. Trucs et Astuces Python
- **Toujours utiliser `collections.deque` en BFS :** `queue.popleft()` s'exécute en **$O(1)$**, alors que `liste.pop(0)` sur une liste Python standard décale tous les éléments en **$O(n)$**.
- **`float("-inf")` et `float("inf")` :** Indispensables pour initialiser les bornes lors de la validation d'un BST (`LeetCode 98`) ou la recherche d'un maximum dans un arbre pouvant contenir des valeurs négatives.
- **Échange d'enfants en une ligne :** Pour inverser un arbre binaire (`LeetCode 226`), le tuple unpacking rend le code limpide :
  ```python
  root.left, root.right = inverser_arbre(root.right), inverser_arbre(root.left)
  ```

---

## 4. Pièges à éviter
- **Vérifier uniquement `node.left.val < node.val < node.right.val` pour un BST :** C'est un piège classique ! Un nœud tout en bas à droite du sous-arbre gauche peut être plus grand que la racine globale. Il faut toujours transmettre les bornes `(borne_min, borne_max)` tout au long de la descente.
- **Oublier `if not root:` en tout début de fonction :** C'est le cas de base universel des arbres. Sans lui, la récursion échoue immédiatement sur les feuilles (`None`).
- **Utiliser une variable mutable par défaut :** Ne jamais écrire `def dfs(node, chemin=[]):` en Python, car la liste `chemin` est partagée entre tous les appels. Passe `None` ou utilise une fonction interne (`helper`).
