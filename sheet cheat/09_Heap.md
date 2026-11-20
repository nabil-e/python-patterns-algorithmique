# 09. HEAP (TAS BINAIRE / FILE DE PRIORITÉ)
*Pattern 09 / 14 • Temps : $O(n \log k)$ ou $O(n \log n)$ • Espace : $O(k)$ ou $O(n)$*

---

## 1. IDÉE CENTRALE
Maintenir dynamiquement l'élément minimum ou maximum d'une collection en constante évolution en $O(1)$ pour la consultation et $O(\log k)$ pour l'insertion ou la suppression, sans avoir à retrier tout le tableau à chaque étape.

---

## 2. INDICES DANS L'ÉNONCÉ & MOTS-CLÉS

| Indice dans l'énoncé | Mots-clés (Anglais) | Variante à appliquer |
| :--- | :--- | :--- |
| Trouver les $K$ plus grands, plus petits ou plus fréquents éléments | `top k`, `kth largest`, `kth smallest`, `most frequent` | Min-Heap de taille $K$ (pour les $K$ plus grands) |
| Trouver les $K$ points les plus proches de l'origine ou d'une cible | `k closest points`, `nearest` | Max-Heap de taille $K$ (avec distances négatives) |
| Fusionner $K$ listes triées ou parcourir une matrice triée | `merge k sorted lists`, `kth smallest in matrix` | Min-Heap de taille $K$ (1 élément par liste) |
| Calculer la médiane d'un flux continu de données en temps réel | `find median from data stream`, `running median` | Double Heap (Max-Heap gauche + Min-Heap droit) |
| Planifier des tâches avec délais de récupération (*cooldown*) | `task scheduler`, `reorganize string` | Max-Heap de fréquences + File d'attente |

---

## 3. VARIANTES & PIÈGES COURANTS

### Variantes principales
- **Top-K avec taille fixe $K$ :** Pour trouver les $K$ **plus grands** éléments, utilisez un **Min-Heap** de taille $K$ : le sommet (`heap[0]`) agit comme un seuil minimal et élimine les plus petits éléments en $O(n \log k)$.
- **Fusion multi-sources ($K$-way merge) :** Stocker des tuples `(valeur, index_liste, index_element)` pour extraire toujours le minimum global parmi $K$ flux triés.
- **Double Tas (Two Heaps) :** Un Max-Heap pour la moitié inférieure et un Min-Heap pour la moitié supérieure donnent accès à la médiane en $O(1)$.

### Pièges à éviter
- **Python n'a que des Min-Heaps (`heapq`) :** Pour simuler un **Max-Heap**, il faut multiplier les valeurs numériques par `-1` à l'insertion (`heappush(h, -val)`) et à l'extraction (`-heappop(h)`).
- **Égalité sur les tuples :** Si deux tuples `(priorite, objet)` ont la même priorité, Python compare `objet`. Si `objet` n'est pas comparable (ex: `ListNode`), ajoutez un compteur unique `(priorite, idx, objet)` pour éviter un `TypeError`.

---

## 4. SQUELETTES DE CODE (PYTHON)

### Variante A : Top-K plus grands éléments (Min-Heap de taille K)
```python
import heapq

def top_k_largest(nums: list[int], k: int) -> list[int]:
    min_heap: list[int] = []
    
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            # Remplace le plus petit du Top-K en une seule opération O(log k)
            heapq.heapreplace(min_heap, num)
            
    return min_heap  # min_heap[0] est le K-ième plus grand élément
```

### Variante B : Fusionner K listes triées (K-Way Merge)
```python
import heapq

def merge_k_sorted_arrays(arrays: list[list[int]]) -> list[int]:
    min_heap: list[tuple[int, int, int]] = []
    result: list[int] = []
    
    # 1. Initialiser avec le 1er élément de chaque liste non vide
    for arr_idx, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], arr_idx, 0))
            
    # 2. Extraire le minimum global et avancer dans la liste correspondante
    while min_heap:
        val, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, arr_idx, elem_idx + 1))
            
    return result
```
