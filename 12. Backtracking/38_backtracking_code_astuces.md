# 💻 Pattern 12 : Backtracking — Squelettes, Code & Astuces

## 1. Squelette Générique (Boilerplate)

```python
def backtrack_skeleton(candidates: list[int], target: int) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []

    def backtrack(start_index: int, current_state: int) -> None:
        # 1. Condition d'arrêt (solution valide trouvée)
        if current_state == target:
            result.append(path.copy())  # TOUJOURS copier path !
            return

        # 2. Élagage (pruning) si l'état devient invalide
        if current_state > target:
            return

        # 3. Exploration des choix possibles
        for i in range(start_index, len(candidates)):
            path.append(candidates[i])                 # Choisir
            backtrack(i + 1, current_state + candidates[i])  # Explorer
            path.pop()                                 # Annuler (Backtrack)

    backtrack(0, 0)
    return result
```

---

## 2. Démos Exécutables (Prêtes à lancer dans `main.py`)

```python
# --- Démo 1 : Tous les sous-ensembles (LeetCode 78 - Subsets) ---
def subsets(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []

    def backtrack(start: int) -> None:
        # Chaque état intermédiaire est un sous-ensemble valide
        result.append(path.copy())
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return result


# --- Démo 2 : Toutes les permutations (LeetCode 46 - Permutations) ---
def permute(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []
    used: list[bool] = [False] * len(nums)

    def backtrack() -> None:
        if len(path) == len(nums):
            result.append(path.copy())
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return result


# --- Démo 3 : Recherche de mot dans une grille (LeetCode 79 - Word Search) ---
def exist(board: list[list[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def backtrack(r: int, c: int, index: int) -> bool:
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False

        # Sauvegarder et marquer la cellule comme visitée sur place
        temp = board[r][c]
        board[r][c] = "#"

        found = (
            backtrack(r + 1, c, index + 1)
            or backtrack(r - 1, c, index + 1)
            or backtrack(r, c + 1, index + 1)
            or backtrack(r, c - 1, index + 1)
        )

        # Restaurer la cellule (Backtrack)
        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False


if __name__ == "__main__":
    print("Subsets [1, 2, 3] :", subsets([1, 2, 3]))
    print("Permutations [1, 2, 3] :", permute([1, 2, 3]))

    grid = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    print("Word Search 'ABCCED' :", exist(grid, "ABCCED"))  # True
    print("Word Search 'ABCB'   :", exist(grid, "ABCB"))    # False
```

---

## 3. Bac à Sable Exercice (À compléter dans `main.py`)

```python
# Exercice : LeetCode 39 - Combination Sum
# Trouve toutes les combinaisons uniques de candidates qui somment à target.
# Un même nombre peut être choisi un nombre illimité de fois.
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    # TODO : Implémenter avec Backtracking (indice : passer `i` et non `i + 1` pour réutiliser)
    pass


if __name__ == "__main__":
    # Décommente pour tester ton implémentation :
    # assert sorted(combination_sum([2, 3, 6, 7], 7)) == [[2, 2, 3], [7]]
    pass
```

---

## 4. Trucs et Astuces Python
- **Passer `path + [nums[i]]` vs `append` / `pop` :** Sur de petits arbres, écrire `backtrack(i + 1, path + [nums[i]])` évite d'avoir à appeler `.pop()` et copie automatiquement la liste, au prix d'une légère allocation mémoire supplémentaire.
- **Élagage rapide par tri :** Pour les problèmes de somme (`Combination Sum`), trier `candidates.sort()` au début permet d'écrire `if current_sum + candidates[i] > target: break` pour couper toute la suite de la boucle `for` d'un coup.
- **Marquage in-place sur grille 2D :** Remplacer temporairement la lettre par `"#"` dans `board[r][c]` évite d'allouer un `set()` de coordonnées `(r, c)`.

## 5. Pièges à éviter
- **Oublier `path.copy()` :** L'erreur numéro 1 en Python. `result.append(path)` ajoute une référence vers la liste qui sera vidée par les `.pop()` successifs.
- **Confondre `i + 1` et `start + 1` :** Dans la boucle `for i in range(start, len(nums)):`, l'appel récursif doit avancer à **`i + 1`** (l'élément suivant dans la boucle), et jamais `start + 1` (qui générerait des doublons).
