# 03. Stack (Pile & Pile Monotone)

## 💡 Idée Centrale
Utiliser une structure **LIFO** (*Last In, First Out* — dernier entré, premier sorti) pour mémoriser l'historique récent des éléments non encore résolus. Dès qu'un nouvel élément permet de résoudre ou d'annuler le sommet de la pile, on dépile (`pop`).

* **Complexité temporelle :** $O(n)$ (chaque élément est empilé et dépilé au maximum une fois).
* **Complexité spatiale :** $O(n)$ dans le pire cas.

---

## 🔍 Indices dans l'énoncé & Mots-clés

| Ce que demande l'énoncé | Mots-clés en anglais | Variante à choisir |
| :--- | :--- | :--- |
| Vérifier l'imbrication de symboles, balises ou évaluer une expression. | *valid parentheses*, *nested*, *reverse polish notation*, *decode string* | **Pile classique** |
| Simuler des collisions ou des annulations adjacentes en chaîne. | *asteroid collision*, *remove adjacent duplicates*, *backspace* | **Pile classique** |
| Trouver, pour chaque élément, le premier élément plus grand ou plus petit à sa droite/gauche. | *next greater element*, *daily temperatures*, *stock span*, *largest rectangle* | **Pile Monotone** (*Monotonic Stack*) |

---

## 🛠️ Variantes Principales

1. **Pile d'appariement / annulation :** On empile les éléments ouvrants/entrants. Lorsqu'un élément fermant/opposé arrive, on vérifie le sommet (`stack[-1]`) et on dépile (`stack.pop()`).
2. **Pile Monotone (croissante ou décroissante) :** On maintient les éléments de la pile dans un ordre strict. Avant d'ajouter un nouvel élément, une boucle `while` dépile tous les éléments qui brisent cet ordre (ce qui permet de calculer immédiatement la distance ou la différence avec eux). *Astuce : stockez souvent les **indices** plutôt que les valeurs.*

---

## 💻 Squelette de Code (Python)

```python
# Variante 1 : Annulation / Appariement
def stack_matching(items):
    stack = []
    for item in items:
        if stack and can_cancel(stack[-1], item):
            stack.pop()
        else:
            stack.append(item)
    return stack

# Variante 2 : Pile Monotone (Next Greater Element)
def monotonic_stack(nums):
    n = len(nums)
    res = [-1] * n
    stack = []  # Stocke les INDICES des éléments en attente
    
    for i, num in enumerate(nums):
        # Tant que l'élément actuel est plus grand que celui au sommet de la pile
        while stack and nums[stack[-1]] < num:
            prev_index = stack.pop()
            res[prev_index] = num  # Ou (i - prev_index) pour une distance
        stack.append(i)
        
    return res
```
