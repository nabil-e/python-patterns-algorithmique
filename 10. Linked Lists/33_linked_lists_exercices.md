# 🏋️ Pattern 10 : Linked Lists — Plan d'Entraînement

Coche les cases `[x]` au fur et à mesure de ta progression et note tes observations clés.

---

## Série 1 : Les Fondamentaux (Fast & Slow + Dummy Node)
*Objectif : Maîtriser le déplacement des pointeurs sans provoquer de `NoneType` error.*

- [ ] **876. Middle of the Linked List** (Easy) — [Lien LeetCode](https://leetcode.com/problems/middle-of-the-linked-list/)
  - *Technique :* Fast & Slow Pointers.
  > Notes : 

- [ ] **141. Linked List Cycle** (Easy) — [Lien LeetCode](https://leetcode.com/problems/linked-list-cycle/)
  - *Technique :* Fast & Slow Pointers (rencontre dans un cycle).
  > Notes : 

- [ ] **21. Merge Two Sorted Lists** (Easy) — [Lien LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)
  - *Technique :* Dummy Node + deux pointeurs.
  > Notes : 

- [ ] **83. Remove Duplicates from Sorted List** (Easy) — [Lien LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
  - *Technique :* Saut de pointeur (`curr.next = curr.next.next`).
  > Notes : 

- [ ] **203. Remove Linked List Elements** (Easy) — [Lien LeetCode](https://leetcode.com/problems/remove-linked-list-elements/)
  - *Technique :* Dummy Node indispensable si la tête doit être supprimée.
  > Notes : 

---

## Série 2 : Inversion & Combinaisons de Patterns
*Objectif : Combiner inversion sur place, pointeurs décalés et recherche de milieu.*

- [ ] **206. Reverse Linked List** (Easy) — [Lien LeetCode](https://leetcode.com/problems/reverse-linked-list/)
  - *Technique :* In-place Reversal classique (3 pointeurs).
  > Notes : 

- [ ] **234. Palindrome Linked List** (Easy) — [Lien LeetCode](https://leetcode.com/problems/palindrome-linked-list/)
  - *Technique :* Mix **Fast & Slow** (trouver le milieu) + **In-place Reversal** (inverser la 2e moitié) + comparaison.
  > Notes : 

- [ ] **19. Remove Nth Node From End of List** (Medium) — [Lien LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
  - *Technique :* Dummy Node + Deux pointeurs avec un écart fixe de $N$ nœuds.
  > Notes : 

- [ ] **143. Reorder List** (Medium) — [Lien LeetCode](https://leetcode.com/problems/reorder-list/)
  - *Technique :* Mix **Milieu** + **Inversion de la 2e moitié** + **Fusion alternée**.
  > Notes : 

- [ ] **142. Linked List Cycle II** (Medium) — [Lien LeetCode](https://leetcode.com/problems/linked-list-cycle-ii/)
  - *Technique :* Algorithme de Floyd (trouver le point d'entrée exact du cycle).
  > Notes : 
