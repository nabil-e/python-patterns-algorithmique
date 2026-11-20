# 🌳 Pattern 12 : Backtracking (Exploration avec Retour Arrière)

## 1. Principe et Mécanique
Le **Backtracking** est une technique d'exploration systématique de toutes les configurations possibles pour résoudre un problème de décision, de combinatoire ou de recherche de chemin. On construit une solution **étape par étape** sous forme d'un arbre de décision : dès qu'une branche ne peut plus mener à une solution valide (élagage / *pruning*), on annule le dernier choix (**retour arrière**) et on explore la branche suivante.

Le cycle fondamental tient toujours en **3 étapes** dans la boucle récursive :
1. **Choisir** : Ajouter un élément au chemin courant (`path.append(choice)`).
2. **Explorer** : Appeler récursivement la fonction pour l'étape suivante (`backtrack(...)`).
3. **Annuler** : Retirer l'élément ajouté (`path.pop()`) pour restaurer l'état exact avant d'essayer le choix suivant.

```text
Exemple : Générer tous les sous-ensembles (Subsets) de [1, 2]

                        []
                     /      \
          (prendre 1)        (ignorer 1)
               [1]                []
             /     \            /    \
      (prendre 2) (ignorer 2) (prendre 2) (ignorer 2)
          [1, 2]      [1]         [2]         []
```

---

## 2. Mots-clés et Déclencheurs dans les énoncés
Repère ces indices pour identifier immédiatement ce pattern :
- **"All possible subsets / combinations / permutations"** (tous les sous-ensembles, combinaisons ou permutations)
- **"Generate all valid..."** (générer toutes les parenthèses valides, adresses IP, partitions de palindromes)
- **"Word Search" / "N-Queens" / "Sudoku Solver"** (recherche de chemin dans une grille avec contraintes de visite)
- **"Combination Sum"** (trouver toutes les combinaisons qui somment à une cible `target`)
- **Petite taille d'entrée ($N \le 15$ ou $N \le 20$)** : La complexité étant souvent exponentielle ($O(2^n)$ ou $O(n!)$), LeetCode impose de très petites contraintes sur $N$.

---

## 3. Quand l'utiliser & Complexités

| Variante | Cas d'usage typique | Temps | Espace (pile récursive) |
| :--- | :--- | :--- | :--- |
| **Subsets (Sous-ensembles)** | Inclure ou exclure chaque élément (`start` index) | $O(n \cdot 2^n)$ | $O(n)$ |
| **Permutations** | Tous les ordres possibles (`used` set ou booléens) | $O(n \cdot n!)$ | $O(n)$ |
| **Combination Sum** | Somme cible avec/sans réutilisation d'éléments | $O(2^t)$ | $O(t)$ |
| **Grid Backtracking** | Chercher un mot ou chemin dans une matrice 2D | $O(M \cdot N \cdot 4^L)$ | $O(L)$ |

---

## ⚠️ Cas limites à vérifier
- **Copie superficielle (`result.append(path)` au lieu de `path.copy()`) :** En Python, `path` est une liste mutable modifiée tout au long de la récursion. Si tu ajoutes `path` sans `.copy()` (ou `list(path)`), `result` ne contiendra à la fin que des listes vides `[]` !
- **Doublons dans l'entrée (ex: `Subsets II` ou `Combination Sum II`) :** Si l'entrée contient des valeurs identiques (`[1, 2, 2]`) et que l'énoncé interdit les combinaisons en double, il faut **trier le tableau d'abord** puis ignorer les éléments identiques consécutifs au même niveau (`if i > start and nums[i] == nums[i - 1]: continue`).
- **Marquage sur grille 2D :** Ne jamais oublier de restaurer la cellule de la grille (`board[r][c] = temp`) après l'appel récursif pour ne pas bloquer d'autres chemins.

## 🚫 Quand éviter ce pattern
- **On demande uniquement le *nombre* de façons ou le *coût minimal/maximal* (sans lister les configurations) :** Si $N = 50$ ou $N = 1000$, le Backtracking explosera en temps (*Time Limit Exceeded*). Basculer immédiatement sur la **Programmation Dynamique (DP)**.
- **Recherche du plus court chemin dans un graphe/grille sans contrainte combinatoire :** Utiliser **BFS** en $O(V + E)$ plutôt qu'une exploration exhaustive.
