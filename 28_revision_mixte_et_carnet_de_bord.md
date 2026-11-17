# 🧩 Squelettes Génériques des 11 Patterns (Boilerplates)

Utilise ces structures abstraites dans ton fichier `main.py` comme point de départ pour résoudre un exercice sans partir d'une feuille blanche.

---

## 1. Hashing (`1. Hashing`)

### Recherche de complément / Mémoire de passage
```python
def squelette_hashing_lookup(elements):
    vus = {}  # ou set() si seule la présence compte
    for index, valeur in enumerate(elements):
        cible = ...  # Calcul du complément recherché
        if cible in vus:
            return ...  # Solution trouvée en O(1)
        vus[valeur] = index  # Mémorisation de l'état courant
    return ...
```

### Comptage de fréquences
```python
from collections import Counter

def squelette_hashing_frequences(elements):
    compteur = Counter(elements)
    for element, freq in compteur.items():
        if ...:  # Condition sur la fréquence
            return ...
    return ...
```

---

## 2. Two Pointers (`2. Two Pointers`)

### Pointeurs convergents (extrémités vers centre)
```python
def squelette_two_pointers_convergents(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        if ...:  # Solution trouvée
            return ...
        elif ...:  # Besoin d'augmenter la valeur
            left += 1
        else:  # Besoin de diminuer la valeur
            right -= 1
    return ...
```

### Pointeurs lent et rapide (modification en place)
```python
def squelette_two_pointers_slow_fast(nums):
    slow = 0  # Position d'écriture valide
    for fast in range(len(nums)):
        if ...:  # Condition pour conserver nums[fast]
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

---

## 3. Stack (`3. Stack`)

### Validation d'imbrication / Élimination adjacente
```python
def squelette_stack(sequence):
    stack = []
    correspondances = {")": "(", "]": "[", "}": "{"}

    for item in sequence:
        if ...:  # Condition d'ouverture ou d'ajout
            stack.append(item)
        else:
            if not stack or ...:  # Pile vide ou incompatibilité avec stack[-1]
                return False
            stack.pop()

    return len(stack) == 0
```

---

## 4. Binary Search (`4. Binary Search`)

### Recherche de frontière monotone (première occurrence valide)
```python
def squelette_binary_search(low, high):
    def condition(mid):
        return ...

    while low < high:
        mid = low + (high - low) // 2
        if condition(mid):
            high = mid  # On garde mid et on cherche plus à gauche
        else:
            low = mid + 1  # mid est trop petit, on l'exclut
    return low
```

---

## 5. Sliding Window (`5. Sliding Window`)

### Fenêtre de taille fixe `k`
```python
def squelette_sliding_window_fixe(nums, k):
    etat_fenetre = 0
    resultat = float("-inf")

    for right in range(len(nums)):
        etat_fenetre += nums[right]
        if right >= k - 1:
            resultat = max(resultat, etat_fenetre)
            etat_fenetre -= nums[right - k + 1]
    return resultat
```

### Fenêtre de taille variable (dynamique)
```python
from collections import defaultdict

def squelette_sliding_window_variable(s):
    etat = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(s)):
        etat[s[right]] += 1
        while ...:  # Tant que la fenêtre est invalide
            etat[s[left]] -= 1
            if etat[s[left]] == 0:
                del etat[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)

    return max_len
```

---

## 6. Prefix / Suffix Sum (`6. Prefix Suffix Sum`)

### Somme de plage en O(1) & Prefix Sum + Hashing
```python
from collections import defaultdict

def squelette_prefix_sum_hashing(nums, k):
    compte_prefixes = defaultdict(int)
    compte_prefixes[0] = 1
    somme_courante = 0
    total_sous_tableaux = 0

    for num in nums:
        somme_courante += num
        total_sous_tableaux += compte_prefixes[somme_courante - k]
        compte_prefixes[somme_courante] += 1

    return total_sous_tableaux
```

---

## 7. Greedy (`7. Greedy (Glouton)`)

### Choix local optimal après tri
```python
def squelette_greedy(elements):
    elements.sort(key=lambda x: ...)
    resultat = 0
    for item in elements:
        if ...:  # Vérifier si le choix local est possible
            resultat += 1
    return resultat
```

---

## 8. Sorting Intervals (`8. Sorting Intervals`)

### Fusion d'intervalles qui se chevauchent
```python
def squelette_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    fusionnes = [intervals[0]]

    for debut, fin in intervals[1:]:
        dernier_fin = fusionnes[-1][1]
        if debut <= dernier_fin:
            fusionnes[-1][1] = max(dernier_fin, fin)
        else:
            fusionnes.append([debut, fin])

    return fusionnes
```

---

## 9. Heap (`9. Heap (Tas Binaire)`)

### Top K éléments (Min-Heap de taille K)
```python
import heapq

def squelette_heap_top_k(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]
```

---

## 10. Linked Lists (`10. Linked Lists`)

### Inversion sur place (In-place Reversal) & Fast/Slow Pointers
```python
def squelette_reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next      # 1. Sauvegarder la suite
        curr.next = prev     # 2. Inverser le pointeur
        prev = curr          # 3. Avancer prev
        curr = nxt           # 4. Avancer curr
    return prev

def squelette_fast_slow(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if ...:  # Condition de rencontre (cycle)
            return True
    return slow  # Milieu de la liste
```

---

## 11. Trees (`11. Trees`)

### DFS Récursif (Profondeur)
```python
def squelette_dfs(root):
    if not root:
        return ...  # Cas de base (0, True, None, [])

    gauche = squelette_dfs(root.left)
    droite = squelette_dfs(root.right)

    return ...  # Combiner gauche, droite et root.val
```

### BFS Itératif par Niveau (Largeur)
```python
from collections import deque

def squelette_bfs(root):
    if not root:
        return []
    resultat = []
    queue = deque([root])

    while queue:
        taille_niveau = len(queue)
        niveau_courant = []
        for _ in range(taille_niveau):
            noeud = queue.popleft()
            niveau_courant.append(noeud.val)
            if noeud.left:
                queue.append(noeud.left)
            if noeud.right:
                queue.append(noeud.right)
        resultat.append(niveau_courant)

    return resultat
```
