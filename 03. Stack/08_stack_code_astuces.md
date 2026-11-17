# Stack (Pile) — Code, Astuces et Pièges

## 1. Templates Python (Prêts à exécuter)

### A. Validation de paires et imbrication (Parenthèses, balises)
Empile les symboles ouvrants et vérifie la correspondance avec le sommet de la pile dès qu'un symbole fermant apparaît.

```python
def est_valide(s: str) -> bool:
    pile = []
    correspondances = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in correspondances:
            # Si la pile est vide ou que le sommet ne correspond pas -> invalide
            sommet = pile.pop() if pile else '#'
            if correspondances[char] != sommet:
                return False
        else:
            pile.append(char)
            
    # La chaîne est valide uniquement si toutes les ouvertures ont été fermées
    return len(pile) == 0

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    tests = ["()[]{}", "([)]", "{[]}", "((("]
    for t in tests:
        print(f"'{t}' -> {est_valide(t)}")
    # Sortie attendue : True, False, True, False
```

---

### B. Élimination de doublons adjacents ou annulations en chaîne
Compare chaque nouvel élément avec le sommet de la pile (`pile[-1]`). S'ils s'annulent, dépile au lieu d'empiler.

```python
def supprimer_doublons_adjacents(s: str) -> str:
    pile = []
    
    for char in s:
        if pile and pile[-1] == char:
            pile.pop()  # Annulation avec le caractère précédent
        else:
            pile.append(char)
            
    return "".join(pile)

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    chaine = "abbaca"
    resultat = supprimer_doublons_adjacents(chaine)
    print(f"Entrée : '{chaine}' -> Résultat : '{resultat}'")
    # Détail : 'bb' s'annule -> 'aaca', puis 'aa' s'annule -> 'ca'
    # Sortie attendue : 'ca'
```

---

### C. Simulation d'historique et d'opérations (Score / Backspace)
Garde une trace séquentielle des états précédents pour pouvoir annuler ou combiner les dernières actions.

```python
def traiter_effacements(s: str) -> str:
    pile = []
    for char in s:
        if char == '#':
            if pile:  # Toujours vérifier que la pile n'est pas vide avant pop()
                pile.pop()
        else:
            pile.append(char)
    return "".join(pile)

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    s1, s2 = "ab#c", "ad#c"
    res1, res2 = traiter_effacements(s1), traiter_effacements(s2)
    print(f"'{s1}' devient '{res1}' | '{s2}' devient '{res2}'")
    print(f"Sont-ils identiques ? -> {res1 == res2}")
    # Sortie attendue : 'ac' == 'ac' -> True
```

---

## 2. Trucs et Astuces (Bibliothèque Standard)

* **Utilise une `list` Python standard :** En Python, `pile.append(x)` (push) et `pile.pop()` (pop) s'exécutent en temps amorti $O(1)$. N'utilise pas `queue.LifoQueue` en algorithmie (trop lent à cause des verrous de threads).
* **Reconstruction rapide de chaîne :** Si ta pile contient des caractères, utilise `"".join(pile)` à la fin plutôt que de concaténer avec `+=` dans une boucle.
* **Consultation du sommet :** Utilise `pile[-1]` pour lire le dernier élément sans le retirer, toujours précédé d'un test `if pile:`.

---

## 3. Pièges à éviter

* **Appeler `pile.pop()` ou `pile[-1]` sur une pile vide :** Cela provoque immédiatement une `IndexError: pop from empty list`. Protège toujours l'accès avec `if pile:`.
* **Oublier de vérifier `not pile` à la fin :** Dans un problème de validation de parenthèses, une entrée comme `"((("` passera toute la boucle sans erreur mais laissera des éléments dans la pile. Retourne toujours `not pile` (ou `len(pile) == 0`).
* **Confondre file (FIFO) et pile (LIFO) :** Si tu fais `pile.pop(0)`, la complexité chute à $O(n)$ car tous les éléments sont décalés en mémoire. Pour une file, utilise `collections.deque` avec `popleft()`.
