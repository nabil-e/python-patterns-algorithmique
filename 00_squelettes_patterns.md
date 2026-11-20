# 🧩 Squelettes Génériques des 11 Patterns (Boilerplates)

Utilise ces structures abstraites en **Python typé (noms en anglais, commentaires en français)** dans ton fichier `main.py` comme point de départ pour résoudre un exercice sans partir d'une feuille blanche.

---

## 1. Hashing

### Recherche de complément / Mémoire de passage
```python
def hashing_lookup_skeleton(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}  # ou set() si seule la présence compte
    for idx, val in enumerate(nums):
        complement = target - val  # Calcul du complément recherché
        if complement in seen:
            return [seen[complement], idx]  # Solution trouvée en O(1)
        seen[val] = idx  # Mémorisation de l'état courant
    return []
```

### Comptage de fréquences
```python
from collections import Counter


def hashing_frequency_skeleton(items: list[str]) -> str:
    counts = Counter(items)
    for item, freq in counts.items():
        if freq == 1:  # Condition sur la fréquence
            return item
    return ""
```

---

## 2. Two Pointers

### Pointeurs convergents (extrémités vers centre)
```python
def two_pointers_converging_skeleton(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    while left < right:  # ou <= selon si le centre doit être traité
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:  # Solution trouvée
            return [left, right]
        elif curr_sum < target:  # Besoin d'augmenter la valeur
            left += 1
        else:  # Besoin de diminuer la valeur
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
        if char not in pairs:  # Condition d'ouverture ou d'ajout
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:  # Pile vide ou incompatibilité
                return False
            stack.pop()

    return len(stack) == 0
```

---

## 4. Binary Search

### Recherche de frontière monotone (première occurrence valide)
```python
def binary_search_skeleton(low: int, high: int) -> int:
    def condition(mid: int) -> bool:
        # Retourne True si mid satisfait le critère recherché
        return mid * mid >= 10

    while low < high:
        mid = low + (high - low) // 2
        if condition(mid):
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
    max_result = float("-inf")

    for right in range(len(nums)):
        # 1. Ajouter nums[right] à l'état de la fenêtre
        window_sum += nums[right]

        # 2. Une fois la taille k atteinte
        if right >= k - 1:
            max_result = max(max_result, window_sum)
            # 3. Retirer l'élément sortant à gauche
            window_sum -= nums[right - k + 1]

    return int(max_result)
```

### Fenêtre de taille variable (dynamique)
```python
from collections import defaultdict


def sliding_window_variable_skeleton(s: str) -> int:
    counts: dict[str, int] = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(s)):
        # 1. Entrée de s[right] dans la fenêtre
        counts[s[right]] += 1

        # 2. Tant que la fenêtre est invalide, rétrécir par la gauche
        while counts[s[right]] > 1:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1

        # 3. Mise à jour de la meilleure fenêtre valide
        max_len = max(max_len, right - left + 1)

    return max_len
```

---

## 6. Prefix / Suffix Sum

### Somme de plage en O(1)
```python
def prefix_sum_skeleton(nums: list[int]) -> list[int]:
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    # Somme de l'index left à right inclus :
    # range_sum = prefix[right + 1] - prefix[left]
    return prefix
```

### Prefix Sum + Hashing (Sous-tableaux de somme K)
```python
from collections import defaultdict


def prefix_sum_hashing_skeleton(nums: list[int], k: int) -> int:
    prefix_counts: dict[int, int] = defaultdict(int)
    prefix_counts[0] = 1
    curr_sum = 0
    total_subarrays = 0

    for num in nums:
        curr_sum += num
        total_subarrays += prefix_counts[curr_sum - k]
        prefix_counts[curr_sum] += 1

    return total_subarrays
```

---

## 7. Greedy

### Choix local optimal après tri
```python
def greedy_skeleton(items: list[tuple[int, int]]) -> int:
    items.sort(key=lambda x: x[1])  # Tri selon le critère glouton
    curr_state = 0
    result = 0

    for start, end in items:
        if start >= curr_state:  # Vérifier si le choix local est possible
            curr_state = end
            result += 1
    return result
```

---

## 8. Sorting Intervals

### Fusion d'intervalles qui se chevauchent
```python
def intervals_merge_skeleton(intervals: list[list[int]]) -> list[list[int]]:
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

### Top K éléments (Min-Heap de taille K)
```python
import heapq


def heap_top_k_skeleton(nums: list[int], k: int) -> int:
    min_heap: list[int] = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # Éjecte le plus petit pour garder les K plus grands
    return min_heap[0]  # Le K-ième plus grand élément
```

### Simulation dynamique (Max-Heap via négation)
```python
import heapq


def max_heap_skeleton(nums: list[int]) -> int:
    max_heap = [-x for x in nums]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        first = -heapq.heappop(max_heap)
        second = -heapq.heappop(max_heap)
        if first != second:  # Condition de réinsertion
            heapq.heappush(max_heap, -(first - second))

    return -max_heap[0] if max_heap else 0
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


def reverse_linked_list_skeleton(head: Optional[ListNode]) -> Optional[ListNode]:
    prev: Optional[ListNode] = None
    curr = head
    while curr:
        nxt = curr.next      # 1. Sauvegarder la suite
        curr.next = prev     # 2. Inverser le pointeur
        prev = curr          # 3. Avancer prev
        curr = nxt           # 4. Avancer curr
    return prev              # Nouvelle tête de liste
```

### Fast & Slow Pointers
```python
from typing import Optional


def fast_slow_skeleton(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # Condition de rencontre (cycle)
            return slow
    return slow  # Milieu de la liste si pas de cycle
```

---

## 11. Trees

### Parcours DFS Récursif
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
    if not root:  # Cas de base obligatoire
        return 0

    left_res = dfs_tree_skeleton(root.left)
    right_res = dfs_tree_skeleton(root.right)

    # Combinaison des résultats (Post-order)
    return 1 + max(left_res, right_res)
```

### Parcours BFS par Niveau (Queue)
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
        curr_level: list[int] = []

        for _ in range(level_size):
            node = queue.popleft()
            curr_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(curr_level)

    return result
```
