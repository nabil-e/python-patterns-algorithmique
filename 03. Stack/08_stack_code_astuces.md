# 💻 Pattern 3 : Stack — Squelettes, Code & Astuces

## 1. Squelette Générique (Boilerplate)

```python
def stack_skeleton(sequence: str) -> bool:
    stack: list[str] = []
    # Optionnel : dictionnaire de correspondance pour les fermetures
    pairs: dict[str, str] = {")": "(", "]": "[", "}": "{"}

    for item in sequence:
        if item not in pairs:  # Ouverture ou élément à empiler
            stack.append(item)
        else:
            # Vérifier que la pile n'est pas vide avant de consulter stack[-1]
            if not stack or stack[-1] != pairs[item]:
                return False
            stack.pop()

    return len(stack) == 0
```

---

## 2. Démos Exécutables (`main.py` — Section 1)

Code typé en anglais avec commentaires en français, prêt à être copié-collé et exécuté localement :

```python
# --- 1. DÉMOS DU PATTERN (Exécutables) ---

def is_valid_parentheses(s: str) -> bool:
    """LeetCode 20 : Valide l'imbrication correcte des parenthèses."""
    stack: list[str] = []
    closing_to_opening: dict[str, str] = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in closing_to_opening:
            # Si la pile est vide ou le sommet ne correspond pas, c'est invalide
            if not stack or stack[-1] != closing_to_opening[char]:
                return False
            stack.pop()
        else:
            # Caractère ouvrant : on l'empile
            stack.append(char)

    return not stack


def remove_adjacent_duplicates(s: str) -> str:
    """LeetCode 1047 : Supprime les paires de caractères identiques adjacents."""
    stack: list[str] = []

    for char in s:
        # Si le sommet de la pile est identique au caractère courant, on annule les deux
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


def backspace_compare(s: str, t: str) -> bool:
    """LeetCode 844 : Compare deux chaînes après simulation de la touche retour arrière (#)."""
    def build_final_string(text: str) -> str:
        stack: list[str] = []
        for char in text:
            if char != "#":
                stack.append(char)
            elif stack:
                # On efface le dernier caractère uniquement si la pile n'est pas vide
                stack.pop()
        return "".join(stack)

    return build_final_string(s) == build_final_string(t)


if __name__ == "__main__":
    print("20. Valid Parentheses :", is_valid_parentheses("({[]})"))  # True
    print("1047. Remove Duplicates :", remove_adjacent_duplicates("abbaca"))  # "ca"
    print("844. Backspace Compare :", backspace_compare("ab#c", "ad#c"))  # True
```

---

## 3. Bac à Sable Exercices (`main.py` — Section 2)

```python
# --- 2. BAC À SABLE EXERCICES (À compléter) ---

def cal_points(operations: list[str]) -> int:
    """LeetCode 682 : Baseball Game."""
    # TODO : Utiliser une pile pour enregistrer les scores et gérer 'C', 'D', '+'
    pass


if __name__ == "__main__":
    # Décommente pour tester ton code :
    # assert cal_points(["5", "2", "C", "D", "+"]) == 30
    pass
```

---

## 4. Trucs et Astuces Python
- **Utiliser une simple `list` Python :** En Python, `list.append()` et `list.pop()` (sans argument) s'exécutent en **$O(1)$ amorti**. Inutile d'importer `collections.deque` pour une pile simple.
- **Vérification booléenne idiomatique :** Écris `if stack:` au lieu de `if len(stack) > 0:`, et `return not stack` au lieu de `return len(stack) == 0`.
- **Reconstruction rapide de chaîne :** Accumule les caractères dans une liste `stack` et fais `"".join(stack)` tout à la fin en $O(n)$, plutôt que de concaténer des chaînes (`res += char`) qui coûte $O(n^2)$.

---

## 5. Pièges à éviter
- **`IndexError: pop from empty list` :** Toujours vérifier `if stack:` avant d'appeler `stack.pop()` ou de lire le sommet `stack[-1]` (par exemple sur `"]"` ou `"#"` en début de chaîne).
- **Oublier les éléments restants :** Sur un problème de parenthèses comme `"((("`, la boucle se termine sans erreur, mais la pile n'est pas vide. Le retour doit toujours vérifier `not stack`.
