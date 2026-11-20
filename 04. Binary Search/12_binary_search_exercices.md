# 🏋️ Pattern 4 : Binary Search — Plan d'Entraînement

Coche les cases `[x]` au fur et à mesure de ta progression. Essaie de résoudre chaque exercice sans ouvrir l'indice avant 15 minutes de réflexion.

---

## Série 1 : Recherche Classique & Frontière Monotone (Easy)
*Objectif : Maîtriser les bornes `left`, `right`, `mid` sans boucle infinie.*

- [ ] **704. Binary Search** (Easy) — [Lien LeetCode](https://leetcode.com/problems/binary-search/)
  <details><summary>💡 Indice d'approche</summary>Template standard avec <code>while left &lt;= right:</code> et retour immédiat dès que <code>nums[mid] == target</code>.</details>
  > Notes : 

- [ ] **35. Search Insert Position** (Easy) — [Lien LeetCode](https://leetcode.com/problems/search-insert-position/)
  <details><summary>💡 Indice d'approche</summary>Si la cible n'est pas trouvée à la sortie de <code>while left &lt;= right:</code>, le pointeur <code>left</code> indique exactement l'index d'insertion (équivalent à <code>bisect_left</code>).</details>
  > Notes : 

- [ ] **278. First Bad Version** (Easy) — [Lien LeetCode](https://leetcode.com/problems/first-bad-version/)
  <details><summary>💡 Indice d'approche</summary>Recherche de frontière monotone : si <code>isBadVersion(mid)</code> est vrai, garde <code>mid</code> (<code>right = mid</code>), sinon exclus-le (<code>left = mid + 1</code>).</details>
  > Notes : 

- [ ] **374. Guess Number Higher or Lower** (Easy) — [Lien LeetCode](https://leetcode.com/problems/guess-number-higher-or-lower/)
  <details><summary>💡 Indice d'approche</summary>Recherche dichotomique directe sur l'intervalle <code>[1, n]</code> guidée par le retour de l'API <code>guess(mid)</code>.</details>
  > Notes : 

---

## Série 2 : Espace de Réponses & Tableaux Modifiés (Easy / Medium)
*Objectif : Appliquer la recherche binaire sur des fonctions mathématiques, des matrices ou des tableaux pivotés.*

- [ ] **69. Sqrt(x)** (Easy) — [Lien LeetCode](https://leetcode.com/problems/sqrtx/)
  <details><summary>💡 Indice d'approche</summary>Cherche le plus grand entier <code>mid</code> dans <code>[0, x]</code> tel que <code>mid * mid &lt;= x</code>.</details>
  > Notes : 

- [ ] **367. Valid Perfect Square** (Easy) — [Lien LeetCode](https://leetcode.com/problems/valid-perfect-square/)
  <details><summary>💡 Indice d'approche</summary>Recherche binaire sur <code>[1, num]</code> en testant si <code>mid * mid == num</code>.</details>
  > Notes : 

- [ ] **74. Search a 2D Matrix** (Medium) — [Lien LeetCode](https://leetcode.com/problems/search-a-2d-matrix/)
  <details><summary>💡 Indice d'approche</summary>Considère la matrice $m 	imes n$ comme un unique tableau trié de taille $m 	imes n$ en convertissant l'index via <code>ligne = mid // cols</code> et <code>col = mid % cols</code>.</details>
  > Notes : 

- [ ] **875. Koko Eating Bananas** (Medium) — [Lien LeetCode](https://leetcode.com/problems/koko-eating-bananas/)
  <details><summary>💡 Indice d'approche</summary>Binary Search sur la vitesse <code>k</code> dans <code>[1, max(piles)]</code> : vérifie si le temps total <code>sum(ceil(p / k)) &lt;= h</code>.</details>
  > Notes : 

- [ ] **153. Find Minimum in Rotated Sorted Array** (Medium) — [Lien LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
  <details><summary>💡 Indice d'approche</summary>Compare <code>nums[mid]</code> avec <code>nums[right]</code> pour savoir dans quelle moitié triée se trouve le point de rupture.</details>
  > Notes : 

- [ ] **33. Search in Rotated Sorted Array** (Medium) — [Lien LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)
  <details><summary>💡 Indice d'approche</summary>À chaque étape, au moins une des deux moitiés (gauche ou droite de <code>mid</code>) est parfaitement triée : vérifie si <code>target</code> se situe dans ses bornes.</details>
  > Notes : 
