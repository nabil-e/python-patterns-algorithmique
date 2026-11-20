# 🧩 Squelettes Génériques des 14 Patterns (Boilerplates)

Utilise ces structures abstraites typées dans ton fichier `main.py` comme point de départ pour résoudre un exercice sans partir d'une feuille blanche.

---

## 1. Hashing

### Recherche de complément / Mémoire de passage
```python
def hashing_lookup_skeleton(elements: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}  # ou set() si seule la présence compte
    for index, value in enumerate(elements):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index
    return []
```

### Comptage de fréquences
```python
from collections import Counter


def hashing_frequency_skeleton(elements: list[int]) -> int:
    counts = Counter(elements)
    for item, freq in counts.items():
        if freq == 1:  # Condition sur la fréquence
            return item
    return -1
```

---

## 2. Two Pointers

### Pointeurs convergents (extrémités vers centre)
```python
def two_pointers_converging_skeleton(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    while left < right:  # ou <= selon si le centre doit être traité
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

### Pointeurs lent et rapide (modification en place)
```python
def two_pointers_slow_fast_skeleton(nums: list[int]) -> int:
    slow = 0  # Position d'écriture valide
    for fast in range(len(nums)):  # Pointeur d'exploration
        if nums[fast] != 0:  # Condition pour conserver nums[fast]
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

---

## 3. Stack

### Validation d'imbrication / Élimination adjacente
```python
def stack_skeleton(sequence: str) -> bool:
    stack: list[str] = []
    pairs: dict[str, str] = {")": "(", "]": "[", "}": "{"}

    for char in sequence:
        if char not in pairs:  # Ouverture ou ajout
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0
```

---

## 4. Binary Search

### Recherche de frontière monotone (première occurrence valide)
```python
def binary_search_skeleton(low: int, high: int) -> int:
    def is_valid(mid: int) -> bool:
        # Retourne True si mid satisfait le critère recherché
        return True

    while low < high:
        mid = low + (high - low) // 2
        if is_valid(mid):
            high = mid  # On garde mid et on cherche plus à gauche
        else:
            low = mid + 1  # mid est trop petit, on l'exclut
    return low
```

---

## 5. Sliding Window

### Fenêtre de taille fixe `k`
```python
def sliding_window_fixed_skeleton(nums: list[int], k: int) -> int:
    window_sum = 0
    best = float("-inf")

    for right in range(len(nums)):
        # 1. Entrée de nums[right] dans la fenêtre
        window_sum += nums[right]

        # 2. Une fois la taille k atteinte
        if right >= k - 1:
            best = max(best, window_sum)
            # 3. Retrait de l'élément sortant à gauche
            window_sum -= nums[right - k + 1]

    return int(best)
```

### Fenêtre de taille variable (dynamique)
```python
from collections import defaultdict


def sliding_window_variable_skeleton(s: str) -> int:
    window_counts: dict[str, int] = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(s)):
        # 1. Entrée de s[right]
        window_counts[s[right]] += 1

        # 2. Tant que la fenêtre est invalide, rétrécir par la gauche
        while window_counts[s[right]] > 1:
            window_counts[s[left]] -= 1
            if window_counts[s[left]] == 0:
                del window_counts[s[left]]
            left += 1

        # 3. Mise à jour de la meilleure fenêtre valide
        max_len = max(max_len, right - left + 1)

    return max_len
```

---

## 6. Prefix / Suffix Sum

### Somme de plage en $O(1)$
```python
def prefix_sum_skeleton(nums: list[int]) -> list[int]:
    n = len(nums)
    prefix: list[int] = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    # Somme de l'index left à right inclus :
    # range_sum = prefix[right + 1] - prefix[left]
    return prefix
```

### Prefix Sum + Hashing (Sous-tableaux de somme `k`)
```python
from collections import defaultdict


def prefix_sum_hashing_skeleton(nums: list[int], k: int) -> int:
    prefix_counts: dict[int, int] = defaultdict(int)
    prefix_counts[0] = 1
    current_sum = 0
    total_subarrays = 0

    for num in nums:
        current_sum += num
        total_subarrays += prefix_counts[current_sum - k]
        prefix_counts[current_sum] += 1

    return total_subarrays
```

---

## 7. Greedy

### Choix local optimal après tri
```python
def greedy_skeleton(elements: list[int]) -> int:
    elements.sort()  # Tri selon le critère glouton
    count = 0

    for item in elements:
        if item > 0:  # Vérifier si le choix local est possible
            count += 1
    return count
```

---

## 8. Sorting Intervals

### Fusion d'intervalles qui se chevauchent
```python
def sorting_intervals_skeleton(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])  # Tri par début d'intervalle
    merged: list[list[int]] = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start <= last_end:  # Chevauchement
            merged[-1][1] = max(last_end, end)
        else:  # Disjoint
            merged.append([start, end])

    return merged
```

---

## 9. Heap

### Top K éléments (Min-Heap de taille `k`)
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

---

## 10. Linked Lists

### Inversion sur place (In-place Reversal)
```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def linked_list_reverse_skeleton(head: Optional[ListNode]) -> Optional[ListNode]:
    prev: Optional[ListNode] = None
    curr = head
    while curr:
        nxt = curr.next      # 1. Sauvegarder la suite
        curr.next = prev     # 2. Inverser le pointeur
        prev = curr          # 3. Avancer prev
        curr = nxt           # 4. Avancer curr
    return prev
```

---

## 11. Trees

### DFS Récursif & BFS par Niveau (`deque`)
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


def tree_dfs_skeleton(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    left_res = tree_dfs_skeleton(root.left)
    right_res = tree_dfs_skeleton(root.right)
    return 1 + max(left_res, right_res)


def tree_bfs_skeleton(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []
    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level_size = len(queue)
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

## 12. Backtracking

### Exploration combinatoire (Choisir -> Explorer -> Annuler)
```python
def backtracking_skeleton(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []

    def backtrack(start_index: int) -> None:
        # 1. Condition d'enregistrement d'une solution valide
        result.append(path.copy())

        # 2. Exploration des choix possibles
        for i in range(start_index, len(nums)):
            path.append(nums[i])      # Choisir
            backtrack(i + 1)          # Explorer
            path.pop()                # Annuler (Backtrack)

    backtrack(0)
    return result
```

---

## 13. Graphs

### BFS sur Graphe / Grille 2D avec `visited`
```python
from collections import deque


def graph_bfs_skeleton(graph: dict[int, list[int]], start: int) -> set[int]:
    visited: set[int] = {start}
    queue: deque[int] = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited
```

---

## 14. Dynamic Programming

### Tabulation 1D (Bottom-Up)
```python
def dp_1d_skeleton(n: int) -> int:
    if n <= 1:
        return n
    dp: list[int] = [0] * (n + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```
