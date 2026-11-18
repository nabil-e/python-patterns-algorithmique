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

## Implémentation des parcours DFS et BFS en Python

Voici la structure de base d'un arbre binaire (`TreeNode`), les trois fonctions de parcours en profondeur (DFS), le parcours en largeur (BFS), ainsi qu'une fonction utilitaire pour générer un arbre à partir d'une liste niveau par niveau.

```python
from collections import deque

# 1. Définition d'un nœud de l'arbre
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 2. Les 3 parcours DFS (Depth-First Search)
def pre_order(root):
    if not root:
        return []
    return [root.val] + pre_order(root.left) + pre_order(root.right)

def in_order(root):
    if not root:
        return []
    return in_order(root.left) + [root.val] + in_order(root.right)

def post_order(root):
    if not root:
        return []
    return post_order(root.left) + post_order(root.right) + [root.val]

# 3. Le parcours BFS (Breadth-First Search / Niveau par niveau)
def level_order(root):
    if not root:
        return []
    queue = deque([root])
    result = []

    while queue:
        level = len(queue)
        current_level = []
        for _ in range(level):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)

    return result

# 4. Fonction utilitaire pour construire l'arbre depuis une liste (niveau par niveau)
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        current = queue.popleft()
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

# --- Test avec l'arbre du quiz ---
root = build_tree([10, 5, 15, 2, 7, None, 20])

print("Pre-order   :", pre_order(root))    # [10, 5, 2, 7, 15, 20]
print("In-order    :", in_order(root))     # [2, 5, 7, 10, 15, 20]
print("Post-order  :", post_order(root))   # [2, 7, 5, 20, 15, 10]
print("Level-order :", level_order(root))  # [[10], [5, 15], [2, 7, 20]]
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
    result = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


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
## Comment choisir entre DFS et BFS sur un arbre ?

### 1. La règle d'or : Que cherche l'énoncé ?
* **Cherche le « Plus court » ou le « Plus proche » (`minDepth`, chemin le plus rapide) $\rightarrow$ BFS :** Le BFS explore étage par étage. Dès qu'il touche la cible, il s'arrête. Le DFS perdrait du temps à plonger jusqu'au fond de branches inutiles.
* **Cherche le « Plus long » ou doit visiter *tout* l'arbre (`maxDepth`, somme totale, inverser) $\rightarrow$ DFS :** Comme pour `maxDepth`, il est impossible de connaître le maximum sans avoir inspecté toutes les branches jusqu'au bout. Le DFS est alors beaucoup plus court et propre à écrire (4 à 6 lignes).

### 2. Tableau de décision rapide

| Indice dans l'énoncé | Choix recommandé | Pourquoi ? |
| :--- | :--- | :--- |
| **"Niveau par niveau"**, **"par étage"**, **"vue de droite"** | **BFS** (avec `deque`) | L'algorithme est naturellement conçu pour grouper les nœuds par profondeur. |
| **"Profondeur minimale"**, **"feuille la plus proche"** | **BFS** (avec `deque`) | Permet un arrêt immédiat (*early exit*) dès que la première feuille est trouvée. |
| **"Profondeur maximale"**, **"diamètre"**, **"équilibré ?"** | **DFS** (Post-order) | On a besoin de remonter une information des feuilles vers la racine. |
| **"Chemin de la racine à une feuille"**, **"somme d'un chemin"** | **DFS** (Pre-order) | La pile d'appels récursifs mémorise automatiquement le chemin parcouru. |
| **"Arbre Binaire de Recherche (BST)"**, **"k-ième plus petit"** | **DFS** (In-order) | Visite automatiquement les éléments dans l'ordre croissant. |


---

## 4. Pièges à éviter
- **Vérifier uniquement `node.left.val < node.val < node.right.val` pour un BST :** C'est un piège classique ! Un nœud tout en bas à droite du sous-arbre gauche peut être plus grand que la racine globale. Il faut toujours transmettre les bornes `(borne_min, borne_max)` tout au long de la descente.
- **Oublier `if not root:` en tout début de fonction :** C'est le cas de base universel des arbres. Sans lui, la récursion échoue immédiatement sur les feuilles (`None`).
- **Utiliser une variable mutable par défaut :** Ne jamais écrire `def dfs(node, chemin=[]):` en Python, car la liste `chemin` est partagée entre tous les appels. Passe `None` ou utilise une fonction interne (`helper`).
