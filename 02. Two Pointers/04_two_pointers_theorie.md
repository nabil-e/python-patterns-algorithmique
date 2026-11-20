# Pattern 2 : Two Pointers (Deux Pointeurs) — Théorie et Déclencheurs

## 1. Principe et Mécanisme
Le pattern **Two Pointers** utilise deux indices (pointeurs) qui se déplacent sur une structure linéaire (tableau ou chaîne de caractères) de manière coordonnée. Cela permet de réduire une complexité temporelle de **O(n²)** à **O(n)** tout en conservant une complexité spatiale **O(1)** (in-place).

### Les 3 Variantes Principales

#### Variante A : Pointeurs Convergents (Gauche / Droite)
Les pointeurs partent des deux extrémités et avancent l'un vers l'autre jusqu'à se croiser (`left < right`).
```text
Tableau trié : [-4, -1, 0, 3, 10]
                 ^             ^
               left          right   --> Comparaison des extrêmes (ex: carrés, somme)
```

#### Variante B : Pointeurs Parallèles (Lent / Rapide - Same Direction)
Les deux pointeurs partent du début et avancent dans le même sens à des vitesses différentes. `slow` marque la position d'écriture valide, `fast` explore le tableau.
```text
Tableau : [0, 1, 0, 3, 12]
           ^  ^
         slow fast   --> Quand fast trouve un élément non nul, on échange avec slow
```

#### Variante C : Deux Tableaux / Chaînes en Parallèle
Un pointeur `i` sur la structure A et un pointeur `j` sur la structure B pour les comparer ou les fusionner simultanément.
```text
s = "abc"   (i = 0)
t = "ahbgdc" (j = 0)  --> j avance toujours ; i avance seulement si s[i] == t[j]
```

---

## 2. Mots-clés et Indices dans les Énoncés
* **Manipulation en place :** *"in-place"*, *"O(1) extra space"*, *"modify the input array"*, *"without allocating extra space"*.
* **Tableaux triés :** *"sorted array"*, *"non-decreasing order"*, *"pair with target sum"*.
* **Symétrie et comparaison :** *"palindrome"*, *"reverse"*, *"subsequence"*, *"merge two sorted"*.
* **Partitionnement :** *"move zeroes"*, *"remove duplicates"*, *"sort colors"*, *"partition"*.

---

## 3. Quand l'utiliser ?
1. **Tableau déjà trié :** Dès qu'un tableau est trié et qu'on cherche une paire ou un triplet, pense immédiatement aux pointeurs convergents (`left`, `right`).
2. **Nettoyage ou réorganisation d'un tableau sans mémoire supplémentaire :** Utilise le duo `slow` (zone propre) et `fast` (lecture).
3. **Fusion ou comparaison de deux séquences :** Parcours synchronisé avec deux indices indépendants (`i` et `j`).
4. **Parcours depuis la fin :** Quand l'écriture au début écraserait des données non lues (ex. : fusionner deux tableaux triés dans le premier qui possède de l'espace libre à la fin).
---

## ⚠️ Cas limites à vérifier
- **Tableau de taille 0 ou 1 :** Les boucles `while left < right:` s'arrêtent immédiatement sans erreur, vérifier que la valeur retournée par défaut est valide.
- **Doublons dans un tableau trié (ex: 3Sum) :** Après avoir trouvé une combinaison valide, il faut faire avancer `left` (et/ou reculer `right`) tant que la valeur suivante est identique pour éviter les résultats en double.
- **Condition d'arrêt `left < right` vs `left <= right` :** Utiliser `<` quand on compare deux éléments distincts (ex: somme d'une paire), et `<=` quand l'élément central doit aussi être traité seul (ex: carré d'un tableau trié).

## 🚫 Quand éviter ce pattern
- **Tableau non trié où l'on doit retourner les index d'origine :** Trier le tableau détruit les positions initiales. Utiliser plutôt le **Hashing** (`dict` valeur -> index).
- **Sous-tableaux contigus avec condition complexe (ex: nombres négatifs) :** Two Pointers suppose une progression monotone. Si ajouter un élément peut réduire ou augmenter la somme de façon imprévisible, passer à **Prefix Sum + Hashing**.
