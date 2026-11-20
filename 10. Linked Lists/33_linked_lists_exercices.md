# 🏋️ Pattern 10 : Linked Lists — Plan d'Entraînement

Coche les cases `[x]` au fur et à mesure de ta progression et note tes observations clés.

---

## Série 1 : Les Fondamentaux (Fast & Slow + Dummy Node)
*Objectif : Maîtriser le déplacement des pointeurs sans provoquer de `NoneType` error.*

- [ ] **876. Middle of the Linked List** (Easy) — [Lien LeetCode](https://leetcode.com/problems/middle-of-the-linked-list/)
  <details><summary>💡 Indice d'approche</summary><b>Fast & Slow Pointers</b> : avance `slow` de 1 pas et `fast` de 2 pas tant que `fast` et `fast.next` existent.</details>
  > Notes : 

- [ ] **141. Linked List Cycle** (Easy) — [Lien LeetCode](https://leetcode.com/problems/linked-list-cycle/)
  <details><summary>💡 Indice d'approche</summary><b>Fast & Slow Pointers</b> : s'il y a un cycle, `fast` finit obligatoirement par rattraper `slow` (`slow is fast`).</details>
  > Notes : 

- [ ] **21. Merge Two Sorted Lists** (Easy) — [Lien LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)
  <details><summary>💡 Indice d'approche</summary>Crée un `dummy = ListNode()` et un pointeur `tail`, compare `l1.val` et `l2.val` à chaque étape, puis rattache `tail.next = l1 or l2`.</details>
  > Notes : 

- [ ] **83. Remove Duplicates from Sorted List** (Easy) — [Lien LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
  <details><summary>💡 Indice d'approche</summary>Si `curr.val == curr.next.val`, saute le doublon avec `curr.next = curr.next.next` sans avancer `curr`.</details>
  > Notes : 

- [ ] **203. Remove Linked List Elements** (Easy) — [Lien LeetCode](https://leetcode.com/problems/remove-linked-list-elements/)
  <details><summary>💡 Indice d'approche</summary>Utilise un `dummy = ListNode(0, head)` pour gérer proprement le cas où la tête elle-même doit être supprimée.</details>
  > Notes : 

---

## Série 2 : Inversion & Combinaisons de Patterns
*Objectif : Combiner inversion sur place, pointeurs décalés et recherche de milieu.*

- [ ] **206. Reverse Linked List** (Easy) — [Lien LeetCode](https://leetcode.com/problems/reverse-linked-list/)
  <details><summary>💡 Indice d'approche</summary><b>In-place Reversal</b> : utilise 3 pointeurs (`prev = None`, `curr = head`, `nxt = curr.next`) pour retourner chaque lien.</details>
  > Notes : 

- [ ] **234. Palindrome Linked List** (Easy) — [Lien LeetCode](https://leetcode.com/problems/palindrome-linked-list/)
  <details><summary>💡 Indice d'approche</summary>Combinaison <b>Fast & Slow</b> (trouver le milieu) + <b>In-place Reversal</b> (inverser la seconde moitié) + comparaison des deux moitiés.</details>
  > Notes : 

- [ ] **19. Remove Nth Node From End of List** (Medium) — [Lien LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
  <details><summary>💡 Indice d'approche</summary>Place un `dummy` avant `head`, avance `fast` de `n + 1` pas, puis avance `slow` et `fast` ensemble jusqu'à la fin : `slow` s'arrête juste avant le nœud à supprimer.</details>
  > Notes : 

- [ ] **143. Reorder List** (Medium) — [Lien LeetCode](https://leetcode.com/problems/reorder-list/)
  <details><summary>💡 Indice d'approche</summary>Enchaîne 3 briques : trouve le milieu (`slow`/`fast`), coupe et inverse la seconde moitié, puis fusionne les deux listes en alternance.</details>
  > Notes : 

- [ ] **142. Linked List Cycle II** (Medium) — [Lien LeetCode](https://leetcode.com/problems/linked-list-cycle-ii/)
  <details><summary>💡 Indice d'approche</summary>Algorithme de Floyd : une fois que `slow == fast`, replace un pointeur sur `head` et avance les deux d'un pas à la fois ; ils se croisent à l'entrée du cycle.</details>
  > Notes : 
