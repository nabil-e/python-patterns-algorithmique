# Sorting Intervals — Théorie et Mécanique

## 1. Principe Fondamental
Un **intervalle** est représenté par une paire `[debut, fin]`. Lorsque les intervalles sont en désordre, comparer chaque paire avec toutes les autres prend un temps $O(n^2)$.

En **triant d'abord les intervalles** (généralement par heure de début ou par heure de fin) en $O(n \log n)$, tous les intervalles qui se chevauchent deviennent **adjacents**. Un seul parcours linéaire $O(n)$ suffit ensuite pour les fusionner, les insérer ou compter les conflits.

---

## 2. Schéma Visuel : Fusion et Chevauchement

```
Intervalles triés par début :
A : [1 -------- 4]
B :       [3 -------- 6]
C :                      [8 ---- 10]

Condition de chevauchement entre A et B :
B.debut <= A.fin   (3 <= 4  -> VRAI, ils se touchent ou se chevauchent)

Fusion de A et B :
[min(1, 3), max(4, 6)]  =>  [1 ------------- 6]

Comparaison avec C :
C.debut <= 6       (8 <= 6  -> FAUX, pas de chevauchement)
Résultat final : [[1, 6], [8, 10]]
```

### Variante Gloutonne (Tri par fin)
Pour maximiser le nombre d'intervalles sans chevauchement (ou minimiser les flèches pour éclater des ballons) :
```
Ballon 1 : [1 ---- 6]
Ballon 2 :   [2 ------ 8]
Ballon 3 :         [7 ------ 12]

Triés par FIN croissante : [1, 6], [2, 8], [7, 12]
-> Flèche 1 tirée à x = 6 (éclate Ballon 1 et Ballon 2 car 2 <= 6)
-> Ballon 3 commence à 7 > 6 : nouvelle flèche tirée à x = 12
```

---

## 3. Mots-Clés Déclencheurs dans les Énoncés
Repère ces indices pour identifier immédiatement le pattern **Sorting Intervals** :
* **"Intervals"**, **"start and end times"**, **"meetings"**, **"ranges"**, **"schedule"**.
* **"Merge overlapping intervals"** (fusionner les intervalles qui se chevauchent).
* **"Insert a new interval"** (insérer un nouvel intervalle dans une liste triée).
* **"Non-overlapping"** ou **"minimum number of arrows / meeting rooms"**.
* **"Total time covered"** (temps total d'empoisonnement, de connexion ou d'occupation).

---

## 4. Quand l'utiliser ?
1. **Fusion d'intervalles :** Trier par `start` croissant (`intervals.sort(key=lambda x: x[0])`), puis fusionner tant que `curr[0] <= prev[1]`.
2. **Intersection de deux listes d'intervalles triées :** Utiliser deux pointeurs (`i` et `j`), calculer `lo = max(A[i][0], B[j][0])` et `hi = min(A[i][1], B[j][1])`, et avancer le pointeur qui se termine le plus tôt.
3. **Sélection maximale / Flèches minimales :** Trier par `end` croissant (`intervals.sort(key=lambda x: x[1])`) pour libérer l'espace le plus vite possible.
