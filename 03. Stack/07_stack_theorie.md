# Stack (Pile) — Théorie & Mécanique

## 1. Principe fondamental
Une **Stack (pile)** est une structure de données linéaire qui suit la règle **LIFO** (*Last In, First Out* : dernier entré, premier sorti). 

En Python, on utilise simplement une `list` standard :
- **Empiler (`push`) :** `stack.append(x)` en $O(1)$ amorti.
- **Dépiler (`pop`) :** `stack.pop()` en $O(1)$.
- **Consulter le sommet (`peek`) :** `stack[-1]` en $O(1)$.

---

## 2. Schémas visuels (ASCII)

### Cas 1 : Validation de paires (Parenthèses)
Entrée : `"({[]})"`

```text
Lecture '(' -> push '('   | Stack: ['(']
Lecture '{' -> push '{'   | Stack: ['(', '{']
Lecture '[' -> push '['   | Stack: ['(', '{', '[']
Lecture ']' -> match '['  | pop() -> Stack: ['(', '{']
Lecture '}' -> match '{'  | pop() -> Stack: ['(']
Lecture ')' -> match '('  | pop() -> Stack: []  --> Vide = VALIDE
```

### Cas 2 : Annulation / Élimination adjacente
Entrée : `"abbaca"` (supprimer les doublons adjacents)

```text
'a' -> Stack: ['a']
'b' -> Stack: ['a', 'b']
'b' == sommet ('b') -> pop() -> Stack: ['a']
'a' == sommet ('a') -> pop() -> Stack: []
'c' -> Stack: ['c']
'a' -> Stack: ['c', 'a']
Résultat : "".join(stack) -> "ca"
```

---

## 3. Mots-clés et déclencheurs dans les énoncés

Repère ces indices pour identifier le pattern **Stack** :
- *"Valid parentheses / brackets"* (parenthèses, crochets ou balises imbriquées)
- *"Adjacent duplicates"* (supprimer des doublons côte à côte qui déclenchent des réactions en chaîne)
- *"Undo / Backspace / History"* (annuler la dernière action, touche retour arrière `#`)
- *"Evaluate expression / Reverse Polish Notation"* (calculatrice, opérateurs et opérandes)
- *"Next greater / smaller element"* (prochain élément plus grand -> variante **Monotonic Stack**)
- *"Nested structure"* (profondeur d'imbrication, dossiers/chemins comme `/a/../b`)

---

## 4. Quand l'utiliser ?
- Lorsque le traitement de l'élément courant dépend **uniquement de l'élément non résolu le plus récent**.
- Lorsque la suppression d'une paire crée une **nouvelle adjacence** qu'il faut immédiatement revérifier.
- Pour remplacer une récursion par une approche itérative explicite.
---

## ⚠️ Cas limites à vérifier
- **Dépiler sur une pile vide (`IndexError`) :** Toujours tester `if not stack:` avant d'accéder à `stack[-1]` ou d'appeler `stack.pop()` (ex: chaîne commençant par une parenthèse fermante `")("`).
- **Pile non vide à la fin du parcours :** Une chaîne comme `"((("` traverse toute la boucle sans erreur. Ne jamais retourner `True` directement à la fin : toujours vérifier `return len(stack) == 0`.
- **Chaîne vide `""` :** Une chaîne vide est généralement considérée comme valide (`True`).

## 🚫 Quand éviter ce pattern
- **Un seul type de symbole sans imbrication complexe :** Si l'énoncé ne comporte qu'un seul type de parenthèse `(` et `)`, un simple compteur entier `balance += 1 / -= 1` résout le problème en **$O(1)$ espace** au lieu de $O(n)$.
- **Besoin d'accéder aux éléments du milieu :** Une pile ne donne accès qu'au sommet (`stack[-1]`). Si l'algorithme exige de retirer des éléments des deux côtés (tête et queue), utiliser `collections.deque`.
