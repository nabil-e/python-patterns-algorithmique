# 12. Backtracking (Exploration et Retour Arrière)

## 💡 Idée Centrale
Construire une solution pas à pas en explorant toutes les branches possibles d'un arbre de décision. Dès qu'une branche mène à une impasse ou qu'une solution complète est enregistrée, on **annule le dernier choix** (*backtrack*) pour revenir à l'état précédent et tester la possibilité suivante.

* **Complexité Temporelle :** \(O(2^n)\) pour les sous-ensembles ou O(n!) pour les permutations (multiplié par O(n) pour copier le chemin)
* **Complexité Spatiale :** O(n) (profondeur de la pile de récursion et du chemin courant `path`)

---

## 🔍 Indices dans l'énoncé & Mots-clés

| Ce que dit l'énoncé | Mots-clés anglais fréquents |
| :--- | :--- |
| Générer toutes les combinaisons, sous-ensembles ou arrangements possibles. | *all subsets*, *permutations*, *combinations*, *power set* |
| Retourner toutes les configurations valides (parenthèses, partitions, reines). | *return all valid*, *generate parentheses*, *n-queens*, *palindrome partitioning* |
| Chercher un mot ou un chemin dans une grille 2D sans réutiliser une case. | *word search*, *find all paths*, *grid backtracking* |
| Contrainte de taille très faible (N ≤ 15 ou N ≤ 20). | 1 ≤ n ≤ 15, 1 ≤ nums.length ≤ 10 |

---

## 🧩 Variantes Principales

### 1. Sous-ensembles et Combinaisons (Subsets / Combination Sum)
* **Principe :** On avance avec un index `start` pour ne jamais réutiliser les éléments précédents et éviter les permutations identiques (`[1, 2]` et `[2, 1]`).
* **Avec réutilisation :** Appel récursif avec `dfs(i)` (ex: `Combination Sum`).
* **Sans réutilisation :** Appel récursif avec `dfs(i + 1)` (ex: `Subsets`).

### 2. Permutations (Permutations)
* **Principe :** L'ordre compte (`[1, 2] != [2, 1]`). On boucle toujours de `0` à `len(nums) - 1` en maintenant un tableau booléen `used` (ou un `set`) pour ignorer les index déjà présents dans `path`.

### 3. Backtracking sur Grille 2D (Word Search)
* **Principe :** Marquer la case courante comme visitée avant d'explorer les 4 voisins (`board[r][c] = "#"`) puis **restaurer sa valeur d'origine** au retour pour ne pas bloquer les autres chemins.

---

## ⚠️ Pièges à éviter
* **Oublier `.copy()` lors de l'enregistrement :** `path` est une liste mutable modifiée tout au long de la récursion. Écrire `res.append(path)` ajoutera uniquement des références vers une liste vide à la fin. Toujours écrire `res.append(path.copy())` (ou `path[:]`).
* **Doublons avec éléments identiques (`Subsets II`, `Combination Sum II`) :** Si l'entrée contient des doublons, trier d'abord (`nums.sort()`) et ajouter la condition d'élagage : `if i > start and nums[i] == nums[i - 1]: continue`.
* **Oublier de restaurer l'état (`path.pop()`) :** Chaque modification effectuée avant l'appel récursif doit être strictement annulée juste après.

---

## 💻 Squelettes de Code (Python)

### Variante A : Sous-ensembles / Combinaisons (avec index `start`)
```python
def subsets(nums: list[int]) -> list[list[int]]:
    res: list[list[int]] = []
    path: list[int] = []

    def dfs(start: int) -> None:
        # Enregistrer une copie de la solution courante
        res.append(path.copy())

        for i in range(start, len(nums)):
            # Élagage (Pruning) : ignorer les doublons au même niveau
            if i > start_index and nums[i] == nums[i - 1]:
                continue

            # 1. Choisir
            path.append(nums[i])
            # 2. Explorer (i + 1 pour élément unique, i si réutilisable)
            dfs(i + 1)
            # 3. Annuler (Backtrack)
            path.pop()

    dfs(0)
    return res
```

### Variante B : Permutations (avec suivi `used`)
```python
def permute(nums: list[int]) -> list[list[int]]:
    res: list[list[int]] = []
    path: list[int] = []
    used: list[bool] = [False] * len(nums)

    def dfs() -> None:
        if len(path) == len(nums):
            res.append(path.copy())
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            # 1. Choisir
            used[i] = True
            path.append(nums[i])
            # 2. Explorer
            dfs()
            # 3. Annuler
            path.pop()
            used[i] = False

    dfs()
    return res
```
