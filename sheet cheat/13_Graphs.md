# 13. Graphs (Parcours DFS, BFS & Tri Topologique)

## 💡 Idée Centrale
Modéliser des relations entre entités (nœuds et arêtes) ou explorer une grille 2D en maintenant un ensemble **`visited`** pour éviter de tourner en rond dans les cycles. On choisit **DFS** pour explorer en profondeur et compter les composantes, **BFS** pour le plus court chemin non pondéré, et le **Tri Topologique** pour ordonner des dépendances.

* **Complexité Temporelle :** O(V + E) (V sommets, E arêtes) ou \(O(R \times C)\) sur une grille
* **Complexité Spatiale :** O(V) ou \(O(R \times C)\) (ensemble `visited`, file `deque` ou pile de récursion)

---

## 🔍 Indices dans l'énoncé & Mots-clés

| Ce que dit l'énoncé | Mots-clés anglais fréquents |
| :--- | :--- |
| Compter des zones connectées ou explorer une matrice 2D d'eau/terre. | *number of islands*, *connected components*, *grid*, *flood fill* |
| Trouver le plus court chemin ou le temps minimal de propagation (non pondéré). | *shortest path*, *minimum steps*, *rotting oranges*, *word ladder* |
| Ordonner des tâches avec prérequis ou détecter un cycle dans un graphe orienté. | *course schedule*, *prerequisites*, *dependencies*, *topological sort* |
| Cloner ou parcourir un réseau de nœuds arbitraires avec cycles. | *clone graph*, *valid tree*, *bipartite*, *adjacency list* |

---

## 🧩 Variantes Principales

### 1. DFS sur Grille 2D (Composantes connexes / Îles)
Parcourir la grille ; dès qu'on trouve une case cible (`"1"`), incrémenter le compteur et lancer un DFS qui « coule » (transforme en `"0"`) ou marque toutes les cases voisines reliées.

### 2. BFS avec `collections.deque` (Plus court chemin / Multi-sources)
* **Simple source :** Insérer le départ dans `deque`, traiter niveau par niveau avec `for _ in range(len(queue)):` pour compter les étapes.
* **Multi-sources :** Insérer **toutes** les sources initiales dans la `deque` au temps t = 0 (ex: toutes les oranges pourries) pour simuler une propagation simultanée.

### 3. Tri Topologique — Algorithme de Kahn (Dépendances)
Construire la liste d'adjacence et un tableau `in_degree` (nombre de prérequis par nœud). Mettre tous les nœuds ayant `in_degree == 0` dans une `deque`, puis décrémenter les voisins au fur et à mesure. Si le nombre de nœuds traités < N, il y a un cycle.

---

## ⚠️ Pièges à éviter
* **Utiliser `list.pop(0)` au lieu de `deque.popleft()` :** Retirer le premier élément d'une liste Python prend O(n), ce qui fait passer un BFS de O(V+E) à O(V²) (*Time Limit Exceeded*). Toujours importer `from collections import deque`.
* **Marquer `visited` trop tard dans un BFS :** Ajoutez toujours le voisin dans `visited` **au moment où vous l'ajoutez dans la `deque`** (et non quand vous le sortez), sinon le même nœud sera ajouté des dizaines de fois par ses voisins.
* **Graphe non connexe :** Ne supposez jamais que tous les nœuds sont accessibles depuis le nœud `0`. Bouclez toujours sur l'ensemble des sommets `for i in range(n):`.

---

## 💻 Squelettes de Code (Python)

### Variante A : BFS Plus Court Chemin / Multi-Sources sur Grille 2D
```python
from collections import deque

def bfs_grid(grid: list[list[int]], sources: list[tuple[int, int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue: deque[tuple[int, int]] = deque(sources)
    visited: set[tuple[int, int]] = set(sources)
    steps = 0

    while queue:
        # Traiter tout le niveau courant (1 unité de temps / distance)
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 1:
                    visited.add((nr, nc))  # Marquer dès l'insertion !
                    queue.append((nr, nc))
        if queue:
            steps += 1

    return steps
```

### Variante B : Tri Topologique — Algorithme de Kahn (Détection de cycle)
```python
from collections import deque

def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph: list[list[int]] = [[] for _ in range(num_courses)]
    in_degree: list[int] = [0] * num_courses

    for course, pre in prerequisites:
        graph[pre].append(course)
        in_degree[course] += 1

    # Démarrer avec tous les cours sans prérequis
    queue: deque[int] = deque([i for i in range(num_courses) if in_degree[i] == 0])
    visited_count = 0

    while queue:
        curr = queue.popleft()
        visited_count += 1
        for neighbor in graph[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return visited_count == num_courses
```

### Variante C : bfs shortest path
```python
from collections import deque, defaultdict
from typing import List, Dict, Set

def bfs_shortest_path(n: int, edges: List[List[int]], start: int, target: int) -> int:
    # 1. Construire la liste d'adjacence
    graph: Dict[int, List[int]] = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # Retirer si graphe orienté

    # 2. Initialiser la file et le set visited
    queue = deque([(start, 0)])  # (noeud_actuel, distance)
    visited: Set[int] = {start}

    while queue:
        node, dist = queue.popleft()
        if node == target:
            return dist

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)  # Marquer AVANT d'enfiler
                queue.append((neighbor, dist + 1))

    return -1  # Cible inaccessible
```