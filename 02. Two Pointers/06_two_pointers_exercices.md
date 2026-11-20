# 🏋️ Pattern 2 : Two Pointers — Plan d'Entraînement

Coche les cases `[x]` au fur et à mesure de ta progression. Essaie de résoudre chaque exercice sans ouvrir l'indice avant 15 minutes de réflexion.

---

## Série 1 : Pointeurs Lent/Rapide & Deux Séquences (Easy)
*Objectif : Modifier un tableau en place en $O(1)$ espace et parcourir deux séquences en parallèle.*

- [ ] **344. Reverse String** (Easy) — [Lien LeetCode](https://leetcode.com/problems/reverse-string/)
  <details><summary>💡 Indice d'approche</summary>Place <code>left = 0</code> et <code>right = len(s) - 1</code>, échange les éléments et rapproche les pointeurs jusqu'à ce qu'ils se croisent.</details>
  > Notes : 

- [ ] **283. Move Zeroes** (Easy) — [Lien LeetCode](https://leetcode.com/problems/move-zeroes/)
  <details><summary>💡 Indice d'approche</summary>Pointeur <code>slow</code> pour la prochaine position non nulle, pointeur <code>fast</code> pour explorer et échanger dès que <code>nums[fast] != 0</code>.</details>
  > Notes : 

- [ ] **26. Remove Duplicates from Sorted Array** (Easy) — [Lien LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
  <details><summary>💡 Indice d'approche</summary>Le tableau est trié : compare <code>nums[fast]</code> avec le dernier élément unique écrit à <code>nums[slow]</code>.</details>
  > Notes : 

- [ ] **392. Is Subsequence** (Easy) — [Lien LeetCode](https://leetcode.com/problems/is-subsequence/)
  <details><summary>💡 Indice d'approche</summary>Avance le pointeur de <code>s</code> uniquement lorsqu'il correspond au caractère courant du pointeur de <code>t</code>.</details>
  > Notes : 

- [ ] **88. Merge Sorted Array** (Easy) — [Lien LeetCode](https://leetcode.com/problems/merge-sorted-array/)
  <details><summary>💡 Indice d'approche</summary>Remplis <code>nums1</code> en partant de la <b>fin</b> (index <code>m + n - 1</code>) avec le plus grand des deux éléments pour ne pas écraser les valeurs non lues.</details>
  > Notes : 

---

## Série 2 : Pointeurs Convergents & Optimisation (Easy / Medium)
*Objectif : Réduire un espace de recherche de $O(n^2)$ à $O(n)$ sur des données triées ou géométriques.*

- [ ] **977. Squares of a Sorted Array** (Easy) — [Lien LeetCode](https://leetcode.com/problems/squares-of-a-sorted-array/)
  <details><summary>💡 Indice d'approche</summary>Les plus grands carrés se trouvent forcément aux deux extrémités (négatifs à gauche, positifs à droite). Remplis le tableau résultat de droite à gauche.</details>
  > Notes : 

- [ ] **125. Valid Palindrome** (Easy) — [Lien LeetCode](https://leetcode.com/problems/valid-palindrome/)
  <details><summary>💡 Indice d'approche</summary>Pointeurs aux extrémités en ignorant les caractères non alphanumériques avec <code>.isalnum()</code> et en comparant en <code>.lower()</code>.</details>
  > Notes : 

- [ ] **167. Two Sum II - Input Array Is Sorted** (Medium) — [Lien LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
  <details><summary>💡 Indice d'approche</summary>Si <code>nums[left] + nums[right] &gt; target</code>, réduis <code>right</code> ; si c'est inférieur, augmente <code>left</code>.</details>
  > Notes : 

- [ ] **11. Container With Most Water** (Medium) — [Lien LeetCode](https://leetcode.com/problems/container-with-most-water/)
  <details><summary>💡 Indice d'approche</summary>Déplace toujours le pointeur situé sur la hauteur la plus petite : c'est le seul moyen d'espérer compenser la perte de largeur.</details>
  > Notes : 

- [ ] **15. 3Sum** (Medium) — [Lien LeetCode](https://leetcode.com/problems/3sum/)
  <details><summary>💡 Indice d'approche</summary>Trie le tableau, fixe un premier élément <code>nums[i]</code> dans une boucle, puis applique Two Pointers convergent sur le reste du tableau en sautant les doublons.</details>
  > Notes : 
