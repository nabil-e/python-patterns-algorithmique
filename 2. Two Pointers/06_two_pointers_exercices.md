# Two Pointers — Plan d'Entraînement

## 1. Tes exercices prioritaires (à faire en premier)

Ces 4 exercices de ta liste utilisent directement les variantes de Two Pointers :

1. **[LC 392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)** — *Deux séquences (un pointeur par chaîne)*
   - **Objectif :** Vérifier si `s` est une sous-séquence de `t`.
   - **Approche :** Avance `j` sur `t` à chaque tour. Avance `i` sur `s` uniquement si `s[i] == t[j]`. Vérifie à la fin si `i == len(s)`.
   - **Complexité :** Temps $O(|t|)$ | Espace $O(1)$.

2. **[LC 283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)** — *Lent / Rapide (écriture sur place)*
   - **Objectif :** Déplacer tous les `0` à la fin tout en gardant l'ordre relatif des autres éléments, sans copier le tableau.
   - **Approche :** `slow` pointe vers la prochaine case libre pour un non-zéro. Quand `nums[fast] != 0`, échange `nums[slow]` et `nums[fast]`, puis incrémente `slow`.
   - **Complexité :** Temps $O(n)$ | Espace $O(1)$.

3. **[LC 977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)** — *Pointeurs convergents*
   - **Objectif :** Renvoyer les carrés d'un tableau trié (contenant des négatifs) dans l'ordre croissant.
   - **Approche :** Les plus grands carrés sont forcément aux extrémités (`left = 0`, `right = n - 1`). Compare `abs(nums[left])` et `abs(nums[right])`, et remplis le tableau résultat par la fin (`pos = n - 1`).
   - **Complexité :** Temps $O(n)$ | Espace $O(n)$ pour la sortie.

4. **[LC 88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)** — *Deux séquences à rebours*
   - **Objectif :** Fusionner `nums2` dans `nums1` (qui dispose de zéros tampon à la fin) sans espace supplémentaire.
   - **Approche :** Pars de la fin des données valides (`p1 = m - 1`, `p2 = n - 1`) et écris à l'index `p = m + n - 1` en reculant. Si `p2 >= 0` à la fin, copie le reste de `nums2`.
   - **Complexité :** Temps $O(m + n)$ | Espace $O(1)$.

*(Note : **LC 844. Backspace String Compare** est traité dans le module **Stack**, mais peut aussi se résoudre en $O(1)$ d'espace avec Two Pointers en partant de la fin des chaînes).*

---

## 2. Entraînement répétitif (ancrage du pattern)

Enchaîne ces exercices pour automatiser chaque variante :

### Série A — Pointeurs convergents (Extremités)
- **[LC 125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)** *(Facile)* : Ignorer les caractères non alphanumériques avec `.isalnum()` et comparer `left` et `right`.
- **[LC 344. Reverse String](https://leetcode.com/problems/reverse-string/)** *(Facile)* : Échange simple `s[left], s[right] = s[right], s[left]` jusqu'au croisement.
- **[LC 167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)** *(Moyen)* : Ajuster `left` ou `right` selon que la somme est trop petite ou trop grande.
- **[LC 11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)** *(Moyen)* : Déplacer toujours le pointeur ayant la plus petite hauteur.

### Série B — Lent / Rapide (Modification sur place)
- **[LC 26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)** *(Facile)* : Même logique que Move Zeroes, comparer `nums[fast] != nums[slow]`.
- **[LC 27. Remove Element](https://leetcode.com/problems/remove-element/)** *(Facile)* : Écraser les valeurs égales à `val` à l'aide du pointeur d'écriture `slow`.
