# 🏋️ Pattern 1 : Hashing — Plan d'Entraînement

Coche les cases `[x]` au fur et à mesure de ta progression. Essaie de résoudre chaque exercice sans ouvrir l'indice avant 15 minutes de réflexion.

---

## Série 1 : Présence & Comptage de base (Easy)
*Objectif : Automatiser l'utilisation de `set` et `collections.Counter` pour passer en $O(n)$.*

- [ ] **1832. Check if the Sentence Is Pangram** (Easy) — [Lien LeetCode](https://leetcode.com/problems/check-if-the-sentence-is-pangram/)
  <details><summary>💡 Indice d'approche</summary>Un <code>set</code> sur la chaîne élimine les doublons ; vérifie simplement sa taille par rapport aux 26 lettres de l'alphabet.</details>
  > Notes : 

- [ ] **771. Jewels and Stones** (Easy) — [Lien LeetCode](https://leetcode.com/problems/jewels-and-stones/)
  <details><summary>💡 Indice d'approche</summary>Convertis <code>jewels</code> en <code>set</code> pour vérifier chaque pierre de <code>stones</code> en $O(1)$.</details>
  > Notes : 

- [ ] **349. Intersection of Two Arrays** (Easy) — [Lien LeetCode](https://leetcode.com/problems/intersection-of-two-arrays/)
  <details><summary>💡 Indice d'approche</summary>Transforme les deux listes en ensembles (<code>set</code>) et utilise l'opérateur d'intersection <code>&amp;</code>.</details>
  > Notes : 

- [ ] **387. First Unique Character in a String** (Easy) — [Lien LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/)
  <details><summary>💡 Indice d'approche</summary>Deux passes : compte d'abord toutes les fréquences avec <code>Counter(s)</code>, puis parcours la chaîne pour trouver le premier caractère de fréquence 1.</details>
  > Notes : 

- [ ] **1. Two Sum** (Easy) — [Lien LeetCode](https://leetcode.com/problems/two-sum/)
  <details><summary>💡 Indice d'approche</summary>Mémorise chaque nombre vu et son index dans un dictionnaire <code>{valeur: index}</code> et cherche <code>target - num</code>.</details>
  > Notes : 

---

## Série 2 : Correspondances & Contraintes de distance (Easy / Medium)
*Objectif : Manipuler des dictionnaires de mapping et des fenêtres ou états mémorisés.*

- [ ] **205. Isomorphic Strings** (Easy) — [Lien LeetCode](https://leetcode.com/problems/isomorphic-strings/)
  <details><summary>💡 Indice d'approche</summary>Assure-toi que la correspondance est bijective (deux caractères différents ne peuvent pas pointer vers le même) avec deux dictionnaires ou <code>len(set(zip(s, t)))</code>.</details>
  > Notes : 

- [ ] **219. Contains Duplicate II** (Easy) — [Lien LeetCode](https://leetcode.com/problems/contains-duplicate-ii/)
  <details><summary>💡 Indice d'approche</summary>Stocke le dernier index vu de chaque nombre dans un dictionnaire et vérifie si <code>i - dernier_index &lt;= k</code> (combinable aussi avec Sliding Window).</details>
  > Notes : 

- [ ] **409. Longest Palindrome** (Easy) — [Lien LeetCode](https://leetcode.com/problems/longest-palindrome/)
  <details><summary>💡 Indice d'approche</summary>Compte les fréquences : toutes les paires contribuent entièrement, et un seul caractère impair peut être placé au centre.</details>
  > Notes : 

- [ ] **49. Group Anagrams** (Medium) — [Lien LeetCode](https://leetcode.com/problems/group-anagrams/)
  <details><summary>💡 Indice d'approche</summary>Utilise un <code>defaultdict(list)</code> avec comme clé immuable soit <code>tuple(sorted(mot))</code>, soit un tuple de 26 compteurs de lettres.</details>
  > Notes : 

- [ ] **128. Longest Consecutive Sequence** (Medium) — [Lien LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)
  <details><summary>💡 Indice d'approche</summary>Mets tout dans un <code>set</code>. Ne lance le comptage <code>num + 1, num + 2...</code> que si <code>num - 1</code> n'est pas dans l'ensemble (début de séquence).</details>
  > Notes : 
