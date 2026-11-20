# Graphs & DP — Code, Astuces et Pièges (amorce)

## 1. BFS grille / graphe

```python
from collections import deque

def bfs_plus_court(start, voisins):
    queue = deque([(start, 0)])  # (noeud, distance)
    vus = {start}
    while queue:
        noeud, dist = queue.popleft()
        if ...:  # cible atteinte
            return dist
        for nxt in voisins(noeud):
            if nxt not in vus:
                vus.add(nxt)
                queue.append((nxt, dist + 1))
    return -1
```

---

## 2. DFS îles / composantes (marquage in-place)

```python
def dfs_ile(grille, i, j):
    if i < 0 or j < 0 or i >= len(grille) or j >= len(grille[0]):
        return
    if grille[i][j] != "1":
        return
    grille[i][j] = "0"  # marquer visité
    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        dfs_ile(grille, i + di, j + dj)
```

---

## 3. DP Bottom-Up classique (Climbing Stairs)

```python
def climbing_stairs(n: int) -> int:
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1


if __name__ == "__main__":
    assert climbing_stairs(2) == 2
    assert climbing_stairs(3) == 3
    print("OK")
```

**Piège :** oublier les cas de base ; confondre Top-Down (cache) et Bottom-Up (ordre de remplissage).
