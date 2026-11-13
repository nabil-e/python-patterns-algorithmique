# Sorting Intervals — Plan d'Entraînement

## 1. Tes Exercices Prioritaires (à cocher)

### Série 1 : Plages contiguës et durées cumulées
* [ ] **228. Summary Ranges** — Parcourir le tableau trié en repérant les ruptures (`nums[i] + 1 != nums[i+1]`) pour formater chaque plage `"debut->fin"` ou `"debut"`. *(Pattern secondaire : Two Pointers).*
* [ ] **495. Teemo Attacking** — Pour chaque attaque `timeSeries[i]`, ajouter `min(duration, timeSeries[i+1] - timeSeries[i])` afin de ne pas compter deux fois le temps d'empoisonnement qui se chevauche.

### Série 2 : Insertion, Intersection et Glouton sur Intervalles
* [ ] **57. Insert Interval** — Parcourir la liste triée en ajoutant d'abord les intervalles strictement avant `newInterval`, fusionner tous ceux qui le chevauchent avec `min` et `max`, puis ajouter les suivants.
* [ ] **986. Interval List Intersections** — Utiliser deux pointeurs sur `firstList` et `secondList` pour extraire `[max(start1, start2), min(end1, end2)]` lorsque `start <= end`, puis avancer le pointeur ayant la plus petite fin. *(Pattern secondaire : Two Pointers).*
* [ ] **452. Minimum Number of Arrows to Burst Balloons** — Trier les ballons par coordonnées de fin croissante (`x_end`) et tirer une flèche à la fin du premier ballon non éclaté. *(Pattern secondaire : Greedy).*

---

## 2. Entraînement Répétitif Complémentaire

### Niveau 1 : Les grands classiques indispensables
* [ ] **56. Merge Intervals** — Le problème de référence absolu pour maîtriser le tri par début et la fusion linéaire.
* [ ] **252. Meeting Rooms** *(ou équivalent)* — Trier les réunions par début et vérifier si une réunion commence avant que la précédente ne se termine (`intervals[i][0] < intervals[i-1][1]`).

### Niveau 2 : Niveau Entretien Confirmé
* [ ] **435. Non-overlapping Intervals** — Trier par heure de fin croissante et compter le minimum d'intervalles à supprimer pour éviter tout conflit (très proche du **452**).
* [ ] **1288. Remove Covered Intervals** — Trier par début croissant puis par fin décroissante (`key=lambda x: (x[0], -x[1])`) pour compter les intervalles totalement englobés.
* [ ] **253. Meeting Rooms II** *(ou gestion de capacité)* — Utiliser un **Min-Heap** pour suivre l'heure de fin la plus proche parmi les salles occupées. *(Pattern secondaire : Heap).*
