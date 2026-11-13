# Heap (Tas Binaire) : Code, Astuces et Pièges

---

## 1. Templates Python Prêts à Lancer

Le module standard `heapq` implémente uniquement un **Min-Heap** (le plus petit élément est toujours à l'index `0`).

### Modèle A : Max-Heap simulé (Négation des valeurs)
Pour simuler un Max-Heap en Python, il suffit d'inverser le signe des nombres avant de les insérer, puis de ré-inverser à la sortie.

```python
import heapq

def derniere_pierre(stones: list[int]) -> int:
    # Transformer en Max-Heap en rendant les valeurs négatives
    max_heap = [-s for s in stones]
    heapq.heapify(max_heap) # O(n)
    
    while len(max_heap) > 1:
        y = -heapq.heappop(max_heap) # La plus lourde
        x = -heapq.heappop(max_heap) # La deuxième plus lourde
        
        if x != y:
            heapq.heappush(max_heap, -(y - x))
            
    return -max_heap[0] if max_heap else 0

if __name__ == "__main__":
    pierres = [2, 7, 4, 1, 8, 1]
    print("Poids de la dernière pierre :", derniere_pierre(pierres))
    # Sortie attendue : 1
```

### Modèle B : Top K Plus Grands Éléments (Min-Heap de taille K)
Pour garder les `K` plus grands éléments sans trier tout le tableau (`O(n log k)`), on utilise un **Min-Heap de taille fixe K**. La racine est le "garde-fou" (le plus petit des K meilleurs).

```python
import heapq

def k_ieme_plus_grand(nums: list[int], k: int) -> int:
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        # Si on dépasse la taille k, on éjecte le plus petit
        if len(min_heap) > k:
            heapq.heappop(min_heap)
            
    # La racine est le k-ième plus grand élément
    return min_heap[0]

if __name__ == "__main__":
    tableau = [3, 2, 1, 5, 6, 4]
    k = 2
    print(f"Le {k}-ième plus grand élément est :", k_ieme_plus_grand(tableau, k))
    # Sortie attendue : 5
```

### Modèle C : Top K Éléments Fréquents (Hashing + Heap)

```python
import heapq
from collections import Counter

def top_k_frequents(nums: list[int], k: int) -> list[int]:
    compteur = Counter(nums)
    min_heap = []
    
    for valeur, freq in compteur.items():
        # Le tas trie selon le premier élément du tuple (la fréquence)
        heapq.heappush(min_heap, (freq, valeur))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
            
    return [valeur for freq, valeur in min_heap]

if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    print("Top 2 fréquents :", top_k_frequents(nums, 2))
    # Sortie attendue : [2, 1] (ordre quelconque)
```

---

## 2. Trucs et Astuces Python (`heapq`)

* **`heapq.heapify(liste)` en O(n) :** Ne fais jamais une boucle `for x in liste: heapq.heappush(tas, x)` pour initialiser un tas (ce qui coûte `O(n log n)`). Utilise `heapify` directement sur la liste en place, c'est linéaire en temps (`O(n)`).
* **`heapq.heappushpop(tas, item)` :** Plus rapide que d'appeler `heappush` puis `heappop` séparément, car il n'effectue qu'un seul rééquilibrage de l'arbre.
* **`heapq.nsmallest(k, iterable)` et `heapq.nlargest(k, iterable)` :** Fonctions natives très pratiques pour un code ultra-concis sur des petits `k`, bien qu'en entretien il soit préférable de montrer la gestion manuelle du tas.
* **Tuples dans un tas :** Python compare les tuples élément par élément de gauche à droite. Mets toujours la clé de tri (priorité, distance, fréquence) en **première position** du tuple : `(priorite, donnee)`.

---

## 3. Pièges à Éviter

1. **Oublier le signe moins `-` au retour d'un Max-Heap :** C'est l'erreur la plus classique. Si tu insères `-val`, n'oublie pas de faire `-heapq.heappop(tas)` ET `-tas[0]` lors de la lecture.
2. **Collision sur le 2e élément d'un tuple :** Si deux éléments ont la même priorité `(priorite, objet_non_comparable)` (par exemple un noeud d'arbre ou un dictionnaire), Python tentera de comparer `objet_non_comparable` et lèvera une `TypeError`. Ajoute un index unique en 2e position : `(priorite, index, objet)`.
3. **Confondre Min-Heap et Max-Heap pour Top K :**
   * Pour les **K plus grands** -> utilise un **Min-Heap** (on élimine les plus petits).
   * Pour les **K plus petits** -> utilise un **Max-Heap** (on élimine les plus grands).
