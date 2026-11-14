# 🧩 Squelettes Génériques des 9 Patterns (Boilerplates)

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
from collections import Counter, defaultdict

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
    while left < right:  # ou <= selon si le centre doit être traité
        # Évaluer la condition avec nums[left] et nums[right]
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
    for fast in range(len(nums)):  # Pointeur d'exploration
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
    correspondances = {")": "(", "]": "[", "}": "{"}  # Optionnel selon le problème

    for item in sequence:
        if ...:  # Condition d'ouverture ou d'ajout
            stack.append(item)
        else:
            if not stack or ...:  # Pile vide ou incompatibilité avec stack[-1]
                return False
            stack.pop()

    return len(stack) == 0  # ou "".join(stack)
```

---

## 4. Binary Search (`4. Binary Search`)

### Recherche de frontière monotone (première occurrence valide)
```python
def squelette_binary_search(low, high):
    def condition(mid):
        # Retourne True si mid satisfait le critère recherché
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
    etat_fenetre = ...  # Somme, compteur, etc.
    resultat = ...

    for right in range(len(nums)):
        # 1. Ajouter nums[right] à etat_fenetre
        ...
        # 2. Une fois la taille k atteinte
        if right >= k - 1:
            resultat = max(resultat, etat_fenetre)  # ou min
            # 3. Retirer l'élément sortant : nums[right - k + 1]
            ...
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
        # 1. Entrée de s[right] dans la fenêtre
        etat[s[right]] += 1

        # 2. Tant que la fenêtre est invalide, rétrécir par la gauche
        while ...:  # Condition d'invalidité
            etat[s[left]] -= 1
            if etat[s[left]] == 0:
                del etat[s[left]]
            left += 1

        # 3. Mise à jour de la meilleure fenêtre valide
        max_len = max(max_len, right - left + 1)

    return max_len
```

---

## 6. Prefix / Suffix Sum (`6. Prefix Suffix Sum`)

### Somme de plage en O(1)
```python
def squelette_prefix_sum(nums):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    # Somme de l'index left à right inclus :
    # somme_plage = prefix[right + 1] - prefix[left]
    return prefix
```

### Prefix Sum + Hashing (Sous-tableaux de somme K)
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

## 7. Greedy (`7. Greedy`)

### Choix local optimal après tri
```python
def squelette_greedy(elements):
    elements.sort(key=lambda x: ...)  # Tri selon le critère glouton
    etat_courant = ...
    resultat = 0

    for item in elements:
        if ...:  # Vérifier si le choix local est possible
            # Appliquer le choix et mettre à jour etat_courant
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
    intervals.sort(key=lambda x: x[0])  # Tri par début d'intervalle
    fusionnes = [intervals[0]]

    for debut, fin in intervals[1:]:
        dernier_fin = fusionnes[-1][1]
        if debut <= dernier_fin:  # Chevauchement
            fusionnes[-1][1] = max(dernier_fin, fin)
        else:  # Disjoint
            fusionnes.append([debut, fin])

    return fusionnes
```

---

## 9. Heap (`9. Heap`)

### Top K éléments (Min-Heap de taille K)
```python
import heapq

def squelette_heap_top_k(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # Éjecte le plus petit pour garder les K plus grands
    return min_heap[0]  # Le K-ième plus grand élément
```

### Simulation dynamique (Max-Heap via négation)
```python
import heapq

def squelette_max_heap(nums):
    max_heap = [-x for x in nums]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        premier = -heapq.heappop(max_heap)
        deuxieme = -heapq.heappop(max_heap)
        if ...:  # Condition de réinsertion
            heapq.heappush(max_heap, -(premier - deuxieme))

    return -max_heap[0] if max_heap else 0
```
