# 09. Heap (Tas Binaire / Priority Queue)

## 💡 Idée Centrale
Maintenir une collection dynamique où l'élément le plus petit (**Min-Heap**) ou le plus grand (**Max-Heap**) est toujours accessible en $O(1)$ et extractible en $O(\log n)$. C'est l'outil idéal pour suivre les « $k$ meilleurs » éléments sans avoir à trier tout l'ensemble à chaque modification.

* **Complexité Temporelle :** $O(n \log k)$ pour trouver un Top $K$ (beaucoup plus rapide que $O(n \log n)$ si $k \ll n$)
* **Complexité Spatiale :** $O(k)$ ou $O(n)$

---

## 🔍 Indices dans l'énoncé & Mots-clés
| Ce que dit l'énoncé | Mots-clés anglais fréquents |
| :--- | :--- |
| Trouver les $k$ plus grands, plus petits, plus proches ou plus fréquents éléments. | *top k frequent*, *kth largest element*, *k closest points* |
| Fusionner $k$ listes ou tableaux déjà triés. | *merge k sorted lists*, *smallest range covering elements* |
| Calculer la médiane en temps réel sur un flux continu de données. | *find median from data stream*, *running median*, *continuous stream* |
| Simuler un processus en prenant toujours le plus grand/petit élément restant. | *last stone weight*, *task scheduler*, *reorganize string*, *connect ropes* |

---

## 🧩 Variantes Principales

### 1. Top K Largest $ightarrow$ Utiliser un Min-Heap de taille K
* **Astuce contre-intuitive :** Pour garder les $k$ **plus grands** éléments, utilisez un **Min-Heap** limité à la taille $k$. Le sommet du tas est ainsi le « plus petit des grands » (le seuil d'entrée). Dès qu'un élément dépasse le sommet, on éjecte le sommet (`heappushpop`).

### 2. Top K Smallest $ightarrow$ Utiliser un Max-Heap de taille K
Même logique inversée : le sommet contient le plus grand des $k$ petits éléments.

### 3. Deux Tas (Two Heaps) pour la Médiane
Maintenir un **Max-Heap** pour la moitié inférieure des nombres et un **Min-Heap** pour la moitié supérieure, en équilibrant leurs tailles pour que la différence ne dépasse jamais 1.

---

## ⚠️ Pièges à éviter
* **Python n'a que des Min-Heaps :** Le module `heapq` place toujours le plus petit élément à l'indice `0`. Pour simuler un **Max-Heap**, il faut **inverser le signe des nombres** (`-num`) à l'insertion et ré-inverser (`-heapq.heappop(heap)`) à la sortie.
* **Tuples dans un Heap :** Si vous insérez des tuples `(priorité, élément)`, Python compare le premier élément, puis le second en cas d'égalité. Si `élément` n'est pas comparable (ex: un nœud de liste chaînée), ajoutez un compteur unique `(priorité, id, élément)` pour éviter une `TypeError`.

---

## 💻 Squelettes de Code (Python)

### Variante A : K-ième plus grand élément (Min-Heap de taille K)
```python
import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        # Si le tas dépasse la taille k, on éjecte le plus petit élément
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Le sommet du Min-Heap de taille k est le k-ième plus grand
    return min_heap[0]
```

### Variante B : Simuler un Max-Heap en Python (Ex: Last Stone Weight)
```python
import heapq

def last_stone_weight(stones: list[int]) -> int:
    # 1. Négation pour simuler un Max-Heap
    max_heap = [-s for s in stones]
    heapq.heapify(max_heap)  # Construction en O(n)

    while len(max_heap) > 1:
        first = -heapq.heappop(max_heap)   # Plus lourde
        second = -heapq.heappop(max_heap)  # Deuxième plus lourde

        if first != second:
            heapq.heappush(max_heap, -(first - second))

    return -max_heap[0] if max_heap else 0
```
