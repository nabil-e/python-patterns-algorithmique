# 03. STACK & MONOTONIC STACK (PILE)
*Gérer les structures imbriquées et trouver le prochain élément supérieur*

- **Complexité :** `Temps: O(n) | Espace: O(n)`

---

## 1. IDÉE CENTRALE
Exploiter le principe LIFO (Last-In, First-Out) pour résoudre les imbrications, ou maintenir une **pile monotone** (strictement croissante/décroissante) afin de trouver en O(1) amorti le prochain élément plus grand ou plus petit.

---

## 2. INDICES DANS L'ÉNONCÉ
| Indice dans l'énoncé | Mots-clés (Anglais) | Approche recommandée |
| :--- | :--- | :--- |
| Parenthèses, balises ou expressions imbriquées | `valid parentheses, nested, brackets, decode` | **Stack classique (LIFO)** |
| Prochain élément plus grand / plus petit à droite | `next greater, warmer temperature, span` | **Monotonic Stack** |
| Collisions ou annulations adjacentes en chaîne | `collision, adjacent duplicates, asteroid` | **Stack de simulation** |
| Plus grand rectangle dans un histogramme | `largest rectangle, histogram, trapping` | **Monotonic Stack (index)** |

---

## 3. VARIANTES & PIÈGES COURANTS
### Variantes principales
- **Stack de validation :** Empiler les ouvrants, dépiler et vérifier la correspondance sur les fermants.
- **Monotonic Decreasing Stack :** Dépiler tant que l'élément courant est plus grand que le sommet (*Next Greater*).
- **Stack d'index :** Stocker les indices plutôt que les valeurs pour calculer facilement les distances.

### Pièges à éviter
- **`IndexError` sur pile vide :** Toujours vérifier `if stack:` avant d'accéder à `stack[-1]` ou `stack.pop()`.
- **Pile non vide à la fin :** Après la boucle, vérifier `return not stack` (des ouvrants non fermés peuvent rester).
- **Condition stricte `<` vs `<=` :** Bien distinguer les doublons selon l'énoncé.

---

## 4. SQUELETTES PYTHON (TYPÉS)

### Variante A : Monotonic Stack (Next Greater Element)
```python
def daily_temperatures(temps: list[int]) -> list[int]:
    res = [0] * len(temps)
    stack: list[int] = []  # Stocke les indices en attente d'un jour plus chaud
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            prev_idx = stack.pop()
            res[prev_idx] = i - prev_idx
        stack.append(i)
    return res
```

### Variante B : Validation de structures imbriquées
```python
def is_valid_parentheses(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for char in s:
        if char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            stack.append(char)
    return not stack
```
