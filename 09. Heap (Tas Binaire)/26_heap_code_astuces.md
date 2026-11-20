# 💻 Pattern 9 : Heap (Tas Binaire) — Squelettes, Code & Astuces

## 1. Squelettes Génériques (Boilerplates)

### Squelette A : Top K éléments (Min-Heap de taille K)
```python
import heapq


def heap_top_k_skeleton(nums: list[int], k: int) -> int:
    min_heap: list[int] = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # Éjecte le plus petit
    return min_heap[0]  # Le K-ième plus grand élément
```

### Squelette B : Simulation dynamique (Max-Heap via négation)
```python
import heapq


def max_heap_skeleton(nums: list[int]) -> int:
    max_heap: list[int] = [-x for x in nums]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        first = -heapq.heappop(max_heap)
        second = -heapq.heappop(max_heap)
        if first != second:
            heapq.heappush(max_heap, -(first - second))

    return -max_heap[0] if max_heap else 0
```

---

## 2. Démos Exécutables & Bac à Sable (`main.py`)

```python
from collections import Counter
import heapq


# --- 1. DÉMOS DU PATTERN (Exécutables) ---

def find_kth_largest(nums: list[int], k: int) -> int:
    """LeetCode 215 : K-ième plus grand élément en O(n log k)."""
    min_heap: list[int] = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]


def last_stone_weight(stones: list[int]) -> int:
    """LeetCode 1046 : Simulation avec Max-Heap par négation."""
    max_heap = [-s for s in stones]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        heavy1 = -heapq.heappop(max_heap)
        heavy2 = -heapq.heappop(max_heap)
        if heavy1 != heavy2:
            heapq.heappush(max_heap, -(heavy1 - heavy2))

    return -max_heap[0] if max_heap else 0


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """LeetCode 347 : Mix Hashing (Counter) + Heap."""
    counts = Counter(nums)
    min_heap: list[tuple[int, int]] = []

    for num, freq in counts.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for freq, num in min_heap]


# --- 2. BAC À SABLE EXERCICES (À compléter) ---

def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    """LeetCode 973 : K Closest Points to Origin. À compléter !"""
    pass


if __name__ == "__main__":
    print("2nd largest :", find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5
    print("Last stone :", last_stone_weight([2, 7, 4, 1, 8, 1]))  # 1
    print("Top 2 frequent :", top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # [2, 1]
    # assert k_closest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
```

---

## 3. Trucs et Astuces Python
- **`heapq.heapify(liste)` est en $O(n)$ :** Toujours préférer `heapify` sur une liste existante plutôt que d'insérer $n$ éléments un par un avec `heappush` (qui coûte $O(n \log n)$).
- **Tuples dans un tas `(priorite, donnee)` :** Python compare élément par élément de gauche à droite. Mets toujours la clé de tri en premier dans le tuple.
- **`heapq.heappushpop(heap, item)` :** Plus rapide que d'appeler `heappush` puis `heappop` séparément.

---

## 4. Pièges à éviter
- **Oublier que `heapq` est UNIQUEMENT un Min-Heap :** Il n'existe pas de `max_heap` natif dans la bibliothèque standard. Utilise `-val` à l'entrée et `-heapq.heappop()` à la sortie.
- **Trier le tableau `heap` à la main :** `heap[0]` est garanti d'être le minimum, mais `heap[1]` n'est pas forcément le 2e minimum (c'est un arbre binaire aplati, pas une liste triée).
- **Collision de tuples non comparables :** Si deux éléments ont la même priorité `(freq, objet)` et que `objet` ne supporte pas `<`, Python lève un `TypeError`. Ajoute un index de départage : `(freq, index, objet)`.
