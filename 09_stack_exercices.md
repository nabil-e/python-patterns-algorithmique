# Stack (Pile) — Plan d'Entraînement

## 1. Tes exercices prioritaires (à faire en premier)

Ces 4 exercices de ta liste s'appuient directement sur une Stack :

1. **[LC 20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)** — *Classique absolu*
   - **Objectif :** Vérifier si une chaîne contenant `()`, `{}`, `[]` est bien formée.
   - **Approche :** Utilise le Template A avec le dictionnaire `pairs = {')': '(', ']': '[', '}': '{'}`.
   - **Complexité :** Temps $O(n)$ | Espace $O(n)$.

2. **[LC 1047. Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)** — *Élimination en chaîne*
   - **Objectif :** Supprimer de manière répétée deux lettres identiques adjacentes.
   - **Approche :** Utilise le Template B. Si `stack[-1] == char`, fais `stack.pop()`, sinon `stack.append(char)`.
   - **Complexité :** Temps $O(n)$ | Espace $O(n)$.

3. **[LC 682. Baseball Game](https://leetcode.com/problems/baseball-game/)** — *Simulation d'historique*
   - **Objectif :** Calculer le score final selon des opérations (`+`, `D`, `C`, ou un entier).
   - **Approche :** Maintiens l'historique des scores valides dans `stack`.
     - `"C"` : `stack.pop()`
     - `"D"` : `stack.append(2 * stack[-1])`
     - `"+"` : `stack.append(stack[-1] + stack[-2])`
     - Sinon : `stack.append(int(op))`
     - Retourne `sum(stack)`.
   - **Complexité :** Temps $O(n)$ | Espace $O(n)$.

4. **[LC 844. Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)** — *Simulation de saisie*
   - **Objectif :** Comparer deux chaînes après application des caractères d'effacement `#`.
   - **Approche :** Écris une fonction helper `build(string)` utilisant une pile (`pop()` sur `#` si non vide, `append(c)` sinon) et compare `build(s) == build(t)`.
   - **Pattern secondaire :** *Two Pointers* (parcours inversé depuis la fin pour une solution en $O(1)$ d'espace).
   - **Complexité :** Temps $O(n + m)$ | Espace $O(n + m)$ avec Stack.

---

## 2. Entraînement répétitif (ancrage du pattern)

Pratique ces exercices complémentaires pour consolider le réflexe Stack :

- **[LC 1544. Make The String Great](https://leetcode.com/problems/make-the-string-great/)** *(Facile)* : Variante directe de LC 1047 où l'on supprime les paires `'a'`/`'A'` (indice : `abs(ord(stack[-1]) - ord(char)) == 32`).
- **[LC 2696. Minimum String Length After Removing Substrings](https://leetcode.com/problems/minimum-string-length-after-removing-substrings/)** *(Facile)* : Supprimer `"AB"` ou `"CD"` de façon répétée avec une pile.
- **[LC 71. Simplify Path](https://leetcode.com/problems/simplify-path/)** *(Moyen)* : Nettoyer un chemin Unix (`/a/./b/../../c/`) en découpant par `'/'` et en dépilant sur `'..'`.
- **[LC 150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)** *(Moyen)* : Empiler les nombres et dépiler deux opérandes à chaque opérateur (`+`, `-`, `*`, `/`).
