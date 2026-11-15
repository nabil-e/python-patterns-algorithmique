# 04. Binary Search (Recherche Binaire)

## 💡 Idée Centrale
Diviser par deux l'espace de recherche à chaque étape en éliminant la moitié qui ne peut pas contenir la solution. Applicable dès qu'il existe une propriété **monotone** (une frontière nette entre `Faux` et `Vrai`).

* **Complexité temporelle :** $O(\log n)$ (ou $O(n \log(	ext{Max}))$ pour une recherche sur la réponse).
* **Complexité spatiale :** $O(1)$.

---

## 🔍 Indices dans l'énoncé & Mots-clés

| Ce que demande l'énoncé | Mots-clés en anglais | Variante à choisir |
| :--- | :--- | :--- |
| Chercher une cible ou sa position d'insertion dans un tableau **trié**. | *sorted array*, *search in O(log n)*, *first/last position* | **Classique** ou **Bornes** |
| Chercher dans un tableau trié ayant subi une rotation ou ayant un pic. | *rotated sorted array*, *peak element*, *minimum in rotated* | **Recherche modifiée** |
| Trouver la capacité minimale ou la vitesse maximale permettant d'accomplir une tâche. | *minimum capacity*, *koko eating bananas*, *split array largest sum*, *minimize the maximum* | **Binary Search on Answer** |

---

## 🛠️ Variantes & Pièges à éviter

1. **Classique (`while left <= right`) :** Cherche une valeur exacte. Retourne `mid` dès qu'on la trouve.
2. **Recherche de borne (`left < right`) :** Cherche la *première* ou *dernière* occurrence d'une condition. Ne fait pas de `return` dans la boucle, mais resserre `right = mid` ou `left = mid + 1`.
3. **Binary Search on Answer :** On ne cherche pas dans un tableau, mais dans un intervalle de réponses possibles `[min_ans, max_ans]` à l'aide d'une fonction `is_valid(mid)`.

---

## 💻 Squelette de Code (Python)

```python
# Variante 1 : Recherche exacte classique
def binary_search_exact(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Variante 2 : Recherche de la borne minimale (Binary Search on Answer)
def binary_search_boundary(low, high, is_valid):
    while low < high:
        mid = low + (high - low) // 2
        if is_valid(mid):
            high = mid      # mid fonctionne, on essaie de trouver encore plus petit
        else:
            low = mid + 1   # mid est trop petit, on augmente la borne inférieure
    return low
```
