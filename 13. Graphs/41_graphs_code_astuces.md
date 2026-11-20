# 💻 Pattern 13 : Graphs — Squelettes, Code & Astuces

## 1. Squelettes Génériques (Boilerplates)

### Squelette A : BFS sur Grille 2D (Plus court chemin / Propagation)
```python
from collections import deque


def bfs_grid_skeleton(grid: list[list[int]], start_r: int, start_c: int) -> int:
    rows, cols = len(grid), len(grid[0])
    queue: deque[tuple[int, int, int]] = deque([(start_r, start_c, 0)])
    visited: set[tuple[int, int]] = {(start_r, start_c)}
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        r, c, dist = queue.popleft()
        if ...:  # Condition d'arrivée atteinte
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and (nr, nc) not in visited
                and grid[nr][nc] == 1  # Condition de case praticable
            ):
                visited.add((nr, nc))  # Marquer AVANT d'enfiler
                queue.append((nr, nc, dist + 1))

    return -1
```

### Squelette B : Tri Topologique (Algorithme de Kahn — BFS)
```python
from collections import defaultdict, deque


def topological_sort_skeleton(num_nodes: int, edges: list[list[int]]) -> list[int]:
    adj: dict[int, list[int]] = defaultdict(list)
    in_degree: list[int] = [0] * num_nodes

    for dest, src in edges:
        adj[src].append(dest)
        in_degree[dest] += 1

    queue: deque[int] = deque([i for i in range(num_nodes) if in_degree[i] == 0])
    order: list[int] = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == num_nodes else []
```

---

## 2. Démos Exécutables (Prêtes à lancer dans `main.py`)

```python
from collections import defaultdict, deque


# --- Démo 1 : Nombre d'îles par DFS sur grille (LeetCode 200 - Number of Islands) ---
def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        # Couler l'île sur place pour éviter un set visited
        grid[r][c] = "0"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                dfs(r, c)

    return islands


# --- Démo 2 : Détection de cycle / Prérequis de cours (LeetCode 207 - Course Schedule) ---
def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    adj: dict[int, list[int]] = defaultdict(list)
    in_degree: list[int] = [0] * num_courses

    for course, prereq in prerequisites:
        adj[prereq].append(course)
        in_degree[course] += 1

    queue: deque[int] = deque([c for c in range(num_courses) if in_degree[c] == 0])
    completed = 0

    while queue:
        curr = queue.popleft()
        completed += 1
        for next_course in adj[curr]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    # Si tous les cours ont pu être suivis, il n'y a aucun cycle
    return completed == num_courses


if __name__ == "__main__":
    ocean_grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print("Nombre d'îles :", num_islands(ocean_grid))  # 3

    print("Cours possibles [[1, 0]] :", can_finish(2, [[1, 0]]))          # True
    print("Cours impossibles [[1, 0], [0, 1]] :", can_finish(2, [[1, 0], [0, 1]]))  # False
```

---

## 3. Bac à Sable Exercice (À compléter dans `main.py`)

```python
from collections import deque


# Exercice : LeetCode 994 - Rotting Oranges (Multi-source BFS)
# 0 = vide, 1 = orange fraîche, 2 = orange pourrie.
# Retourne le nombre minimal de minutes pour que toutes les oranges pourrissent (ou -1).
def oranges_rotting(grid: list[list[int]]) -> int:
    # TODO : Initialiser la deque avec TOUTES les oranges pourries (2) à t=0,
    # puis propager minute par minute.
    pass


if __name__ == "__main__":
    # Décommente pour tester ton implémentation :
    # assert oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    # assert oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    pass
```

---

## 4. Trucs et Astuces Python
- **Multi-source BFS :** Quand plusieurs points de départ propagent un état simultanément (ex: *Rotting Oranges*, *01 Matrix*), mets **toutes** les sources dans `queue` dès l'initialisation avant de lancer `while queue:`.
- **Tuple de directions :** Définir `DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]` rend le parcours des 4 voisins propre et sans duplication de code.
- **Modifier la grille sur place :** Si l'énoncé autorise de modifier `grid`, changer `"1"` en `"0"` (ou `1` en `2`) sert de marqueur `visited` gratuit en $O(1)$ mémoire.

## 5. Pièges à éviter
- **Marquer `visited` trop tard en BFS :** Si tu fais `visited.add((r, c))` après `popleft()` au lieu de le faire avant `append()`, des voisins communs seront ajoutés plusieurs fois dans la file, provoquant un *Time Limit Exceeded*.
- **Oublier la limite de récursion Python (`RecursionError`) :** Sur une grande grille ($300 \times 300 = 90\,000$ cases), un DFS récursif peut dépasser la pile d'appels par défaut (`1000`). Utiliser soit un BFS itératif (`deque`), soit `sys.setrecursionlimit(10**6)`.
