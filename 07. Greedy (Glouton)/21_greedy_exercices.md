# 🏋️ Pattern 07 : Greedy (Glouton) — Plan d'Entraînement

Coche les cases `[x]` au fur et à mesure de ta progression et note tes observations clés.

---

## Série 1 : Tes Exercices Prioritaires (Simulations & Choix Locaux)
*Objectif : Identifier le critère local optimal qui garantit le résultat global.*

- [ ] **605. Can Place Flowers** (Easy) — [Lien LeetCode](https://leetcode.com/problems/can-place-flowers/)
  <details><summary>💡 Indice d'approche</summary>Parcours le parterre de gauche à droite et plante dès qu'une case est vide avec ses voisins gauche et droit vides (ou hors limites).</details>
  > Notes : 

- [ ] **860. Lemonade Change** (Easy) — [Lien LeetCode](https://leetcode.com/problems/lemonade-change/)
  <details><summary>💡 Indice d'approche</summary>Pour rendre 15 $, privilégie toujours un billet de 10 $ + un billet de 5 $ plutôt que trois billets de 5 $, car le billet de 5 $ est plus polyvalent.</details>
  > Notes : 

- [ ] **122. Best Time to Buy and Sell Stock II** (Medium) — [Lien LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
  <details><summary>💡 Indice d'approche</summary>Additionne toutes les hausses consécutives positives : chaque fois que `prices[i] > prices[i - 1]`, ajoute la différence au profit total.</details>
  > Notes : 

- [ ] **169. Majority Element** (Easy) — [Lien LeetCode](https://leetcode.com/problems/majority-element/)
  <details><summary>💡 Indice d'approche</summary>Algorithme de vote de Boyer-Moore en O(1) espace : maintiens un `candidate` et un `count` (+1 si égal, -1 sinon, changement de candidat quand `count == 0`).</details>
  > Notes : 

- [ ] **409. Longest Palindrome** (Easy) — [Lien LeetCode](https://leetcode.com/problems/longest-palindrome/)
  <details><summary>💡 Indice d'approche</summary>Combinaison <b>Hashing + Greedy</b> : compte les fréquences avec `Counter`. Prends toutes les paires paires (`freq // 2 * 2`), et ajoute +1 au centre s'il reste au moins un caractère impair.</details>
  > Notes : 

---

## Série 2 : Tri Glouton & Optimisation
*Objectif : Trouver le bon critère de tri avant de dérouler la boucle gloutonne.*

- [ ] **455. Assign Cookies** (Easy) — [Lien LeetCode](https://leetcode.com/problems/assign-cookies/)
  <details><summary>💡 Indice d'approche</summary>Combinaison <b>Greedy + Two Pointers</b> : trie `g` (appétits) et `s` (tailles) par ordre croissant et satisfais l'enfant le moins gourmand avec le plus petit biscuit suffisant.</details>
  > Notes : 

- [ ] **1710. Maximum Units on a Truck** (Easy) — [Lien LeetCode](https://leetcode.com/problems/maximum-units-on-a-truck/)
  <details><summary>💡 Indice d'approche</summary>Trie `boxTypes` par nombre d'unités par boîte décroissant (`key=lambda x: x, reverse=True`) et charge le maximum possible jusqu'à remplir `truckSize`.</details>
  > Notes : 

- [ ] **55. Jump Game** (Medium) — [Lien LeetCode](https://leetcode.com/problems/jump-game/)
  <details><summary>💡 Indice d'approche</summary>Maintiens l'index maximal atteignable `max_reach`. Si à un index `i` tu as `i > max_reach`, la fin est inaccessible.</details>
  > Notes : 

- [ ] **134. Gas Station** (Medium) — [Lien LeetCode](https://leetcode.com/problems/gas-station/)
  <details><summary>💡 Indice d'approche</summary>Si `sum(gas) < sum(cost)`, retourne `-1`. Sinon, parcours le circuit : dès que le réservoir courant devient négatif, réinitialise le point de départ à `i + 1`.</details>
  > Notes : 
