# 📅 Pattern 8 : Sorting Intervals — Plan d'Entraînement

Coche les cases `[x]` au fur et à mesure de ta progression. Les indices sont masqués pour te permettre de réfléchir sans spoiler.

---

## Série 1 : Tes Exercices Prioritaires

- [ ] **228. Summary Ranges** (Easy) — [LeetCode](https://leetcode.com/problems/summary-ranges/)
  <details><summary>💡 Indice d'approche</summary>Tableau déjà trié : maintiens un pointeur de début de plage et avance tant que `nums[i + 1] == nums[i] + 1`.</details>
  > Notes : 

- [ ] **495. Teemo Attacking** (Easy) — [LeetCode](https://leetcode.com/problems/teemo-attacking/)
  <details><summary>💡 Indice d'approche</summary>Pour chaque attaque consécutive, ajoute `min(duration, timeSeries[i + 1] - timeSeries[i])`, puis ajoute `duration` pour la dernière attaque.</details>
  > Notes : 

- [ ] **2446. Determine if Two Events Have Conflict** (Easy) — [LeetCode](https://leetcode.com/problems/determine-if-two-events-have-conflict/)
  <details><summary>💡 Indice d'approche</summary>Les heures `"HH:MM"` se comparent lexicographiquement : il y a conflit si `max(start1, start2) <= min(end1, end2)`.</details>
  > Notes : 

- [ ] **57. Insert Interval** (Medium) — [LeetCode](https://leetcode.com/problems/insert-interval/)
  <details><summary>💡 Indice d'approche</summary>Trois phases linéaires : ajoute les intervalles strictement avant `newInterval`, fusionne ceux qui chevauchent (`min` des débuts, `max` des fins), puis ajoute le reste.</details>
  > Notes : 

- [ ] **986. Interval List Intersections** (Medium) — [LeetCode](https://leetcode.com/problems/interval-list-intersections/)
  <details><summary>💡 Indice d'approche</summary>Two Pointers sur les deux listes : l'intersection existe si `max(start1, start2) <= min(end1, end2)`. Avance le pointeur dont l'intervalle finit le plus tôt.</details>
  > Notes : 

- [ ] **452. Minimum Number of Arrows to Burst Balloons** (Medium) — [LeetCode](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)
  <details><summary>💡 Indice d'approche</summary>Trie par **borne de fin croissante** (`x[1]`) et tire une flèche à la fin du ballon courant tant que les suivants commencent avant ou sur cette coordonnée.</details>
  > Notes : 

---

## Série 2 : Entraînement Répétitif & Compléments

- [ ] **56. Merge Intervals** (Medium) — [LeetCode](https://leetcode.com/problems/merge-intervals/)
  <details><summary>💡 Indice d'approche</summary>Trie par heure de début (`x[0]`), puis fusionne avec le dernier intervalle retenu si `start <= merged[-1][1]`.</details>
  > Notes : 

- [ ] **435. Non-overlapping Intervals** (Medium) — [LeetCode](https://leetcode.com/problems/non-overlapping-intervals/)
  <details><summary>💡 Indice d'approche</summary>Trie par **heure de fin croissante** (choix glouton) et conserve toujours l'intervalle qui se termine le plus tôt pour minimiser les suppressions.</details>
  > Notes : 

- [ ] **729. My Calendar I** (Medium) — [LeetCode](https://leetcode.com/problems/my-calendar-i/)
  <details><summary>💡 Indice d'approche</summary>Maintiens une liste triée des créneaux et utilise la recherche binaire (`bisect`) pour vérifier l'absence de chevauchement avec les voisins.</details>
  > Notes :
