# Binary Search (Recherche Binaire) — Théorie & Mécanique

## 1. Principe fondamental
La **Binary Search** permet de trouver une cible ou une frontière dans un espace de recherche **trié** (ou monotone) en divisant par 2 la zone candidate à chaque étape. On passe ainsi d'une complexité linéaire $O(n)$ à une complexité logarithmique **$O(\log n)$**.

---

## 2. Schémas visuels (ASCII)

### Variantes essentielles
Il existe deux grandes familles à maîtriser :

#### A. Recherche exacte (`left <= right`)
Chercher `target = 23` dans `[2, 5, 8, 12, 16, 23, 38, 56]` :

```text
Étape 1: [ 2,  5,  8, 12, 16, 23, 38, 56 ]
           L           M               R     -> 12 < 23 : L = M + 1

Étape 2: [ 2,  5,  8, 12, 16, 23, 38, 56 ]
                           L   M       R     -> 23 == 23 : Trouvé à l'index 5 !
```

#### B. Recherche de frontière / Premier `True` (`left < right`)
Trouver la première mauvaise version dans `[False, False, False, True, True]` :

```text
Index:     0      1      2      3      4
Valeurs: [ F,     F,     F,     T,     T ]
           L             M             R     -> isBad(2) == False : L = M + 1 (3)

Index:     0      1      2      3      4
Valeurs: [ F,     F,     F,     T,     T ]
                                L      R     -> M = 3, isBad(3) == True : R = M (3)
                                L==R         -> Arrêt ! Réponse = 3
```

---

## 3. Mots-clés et déclencheurs dans les énoncés

Repère ces indices pour identifier **Binary Search** :
- *"Sorted array"* (tableau trié par ordre croissant ou décroissant)
- *"$O(\log n)$ time complexity"* (exigence explicite de temps logarithmique)
- *"Search insert position"* (trouver l'index où insérer un élément)
- *"First / Last occurrence"* (première ou dernière apparition d'une valeur ou condition)
- *"Minimum / Maximum value such that condition holds"* (recherche binaire sur la réponse, ex: racine carrée entière `Sqrt(x)`)

---

## 4. Quand l'utiliser ?
- Dès que les données d'entrée sont **triées**.
- Dès qu'une fonction booléenne `condition(x)` sépare l'espace de recherche en deux blocs contigus : `[False, False, ..., True, True]` (propriété de **monotonie**).
