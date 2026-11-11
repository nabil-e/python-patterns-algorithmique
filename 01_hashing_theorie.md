# Pattern 1 : Hashing (Tables de Hachage) — Théorie et Déclencheurs

## 1. Principe et Mécanisme
Le **Hashing** consiste à transformer une clé (nombre, chaîne, tuple) en un indice mémoire via une fonction de hachage pour obtenir un accès, une insertion et une suppression en temps moyen **O(1)**. En Python, ce mécanisme repose sur les types natifs `dict` (clé -> valeur) et `set` (collection de clés uniques).

### Schéma de fonctionnement (Lookup O(1))
```text
Tableau d'entrée : [4, 7, 1, 9]   |   Cible : 10 (Complément = 10 - x)

Étape 1 : x = 4 -> Complément 6 dans set ? Non -> Ajouter 4 : {4}
Étape 2 : x = 7 -> Complément 3 dans set ? Non -> Ajouter 7 : {4, 7}
Étape 3 : x = 1 -> Complément 9 dans set ? Non -> Ajouter 1 : {4, 7, 1}
Étape 4 : x = 9 -> Complément 1 dans set ? OUI ! Paire trouvée (1, 9)
```

---

## 2. Mots-clés et Indices dans les Énoncés
Repère ces expressions dans les problèmes LeetCode pour déclencher immédiatement le réflexe Hashing :
* **Existence et unicité :** *"contains duplicate"*, *"distinct"*, *"unique"*, *"seen before"*, *"all letters of the alphabet"*.
* **Fréquence et comptage :** *"frequency"*, *"count"*, *"anagram"*, *"majority element"*, *"first unique"*, *"most frequent"*.
* **Association et correspondance :** *"two sum"*, *"pair with sum"*, *"mapping"*, *"isomorphic"*, *"intersection"*.
* **Contraintes de temps :** Lorsque la solution naïve demande deux boucles imbriquées en **O(n²)** et que l'énoncé exige **O(n)** sans trier le tableau.

---

## 3. Quand l'utiliser ?
1. **Remplacer une recherche linéaire O(n) par O(1) :** Dès que tu fais `if x in liste:` à l'intérieur d'une boucle, remplace `liste` par un `set`.
2. **Compter des occurrences :** Pour comparer deux chaînes (anagrammes) ou trouver un élément selon sa fréquence.
3. **Mémoriser le passé (One-Pass) :** Stocker les valeurs déjà rencontrées (ou leur dernier index) pendant le parcours unique d'un tableau.
4. **Grouper des éléments :** Regrouper des objets partageant une même signature (ex. : tuple de fréquences ou chaîne triée).
