# 🕸️ Pattern 13 : Graphs (Graphes, DFS, BFS & Tri Topologique)

## 1. Principe et Mécanique
Un **graphe** est un ensemble de sommets (*nodes / vertices*) reliés par des arêtes (*edges*). Contrairement aux arbres, un graphe peut contenir des **cycles** et ne possède pas de racine unique. Il est donc obligatoire de maintenir un ensemble **`visited`** pour ne pas tourner en rond indéfiniment.

### Les 3 représentations courantes sur LeetCode
1. **Grille 2D (`grid[r][c]`)** : Chaque case `(r, c)` est un nœud connecté à ses 4 voisins `(r±1, c)` et `(r, c±1)`.
2. **Liste d'arêtes (`edges = [[0, 1], [1, 2]]`)** : À convertir immédiatement en **liste d'adjacence** (`defaultdict(list)`).
3. **Liste d'adjacence (`adj[u] = [v1, v2]`)** : Structure optimale donnant les voisins d'un nœud en $O(1)$.

### DFS vs BFS sur un Graphe
```text
DFS (Stack / Récursif) : Explore une branche jusqu'au bout avant de revenir.
-> Idéal pour : Compter les îles (composantes connexes), détecter un cycle.

BFS (Queue / collections.deque) : Explore par cercles concentriques (distance 1, 2, 3...).
-> Idéal pour : Plus court chemin dans un graphe non pondéré, propagation (oranges pourries).
```

---

## 2. Mots-clés et Déclencheurs dans les énoncés
Repère ces indices pour identifier immédiatement ce pattern :
- **"Number of islands" / "Connected components"** (grille de `0` et `1`, régions isolées)
- **"Shortest path in a binary matrix / grid"** (plus court chemin sans poids sur les arêtes -> **BFS**)
- **"Prerequisites" / "Course Schedule" / "Dependencies"** (ordre de tâches avec dépendances -> **Tri Topologique / Kahn**)
- **"Clone Graph" / "Network Delay" / "Bipartite"**
- **"Rotting Oranges" / "Flood Fill"** (propagation simultanée depuis plusieurs sources -> **Multi-source BFS**)

---

## 3. Quand l'utiliser & Complexités

| Algorithme | Cas d'usage typique | Temps | Espace |
| :--- | :--- | :--- | :--- |
| **DFS (Grille ou Liste)** | Composantes connexes, accessibilité, flood fill | $O(V + E)$ | $O(V)$ |
| **BFS (`deque`)** | Plus court chemin (non pondéré), distance minimale | $O(V + E)$ | $O(V)$ |
| **Tri Topologique (Kahn)** | Ordonnancement de tâches, détection de cycle dirigé | $O(V + E)$ | $O(V + E)$ |

*(Où $V$ est le nombre de sommets et $E$ le nombre d'arêtes ; sur une grille $M \times N$, $V = M \cdot N$).*

---

## ⚠️ Cas limites à vérifier
- **Graphe non connexe (plusieurs composantes isolées) :** Ne jamais lancer un seul DFS/BFS depuis le nœud `0` en supposant que tout est relié : toujours boucler sur **tous** les nœuds `for node in range(n):` (ou toutes les cases `(r, c)` de la grille).
- **Graphe dirigé vs non dirigé :** Pour une liste d'arêtes non dirigées (`[u, v]`), penser à ajouter les deux sens (`adj[u].append(v)` **et** `adj[v].append(u)`).
- **Marquer `visited` AVANT d'ajouter à la file BFS :** En BFS, ajoute le voisin dans `visited` au moment où tu le pousses dans la `deque` (`queue.append(neighbor)`), pas au moment où tu le défiles (`popleft`), sinon le même nœud sera ajouté des dizaines de fois !

## 🚫 Quand éviter ce pattern
- **Graphe avec arêtes pondérées (coûts différents) :** BFS classique ne trouve pas le plus court chemin si les arêtes ont des poids différents (ex: temps de trajet variables). Utiliser l'algorithme de **Dijkstra** (`heapq`).
- **Structure garantie sans cycle avec une seule racine :** C'est un arbre (**Pattern 11 : Trees**), inutile d'allouer un ensemble `visited`.
