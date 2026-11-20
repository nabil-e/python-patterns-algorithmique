# 🏋️ Pattern 3 : Stack (Pile) — Plan d'Entraînement

Coche les cases `[x]` au fur et à mesure de ta progression. Essaie de résoudre chaque exercice sans ouvrir l'indice avant 15 minutes de réflexion.

---

## Série 1 : Validation & Éliminations Adjacentes (Easy)
*Objectif : Utiliser une `list` Python en mode LIFO (`append` / `pop`) pour gérer des états imbriqués ou des annulations.*

- [ ] **20. Valid Parentheses** (Easy) — [Lien LeetCode](https://leetcode.com/problems/valid-parentheses/)
  <details><summary>💡 Indice d'approche</summary>Empile les ouvrants ; à chaque fermant, vérifie que la pile n'est pas vide et que le sommet <code>stack[-1]</code> correspond.</details>
  > Notes : 

- [ ] **1047. Remove All Adjacent Duplicates In String** (Easy) — [Lien LeetCode](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)
  <details><summary>💡 Indice d'approche</summary>Compare chaque caractère entrant avec <code>stack[-1]</code> : s'ils sont identiques, fais <code>stack.pop()</code> au lieu d'empiler.</details>
  > Notes : 

- [ ] **1544. Make The String Great** (Easy) — [Lien LeetCode](https://leetcode.com/problems/make-the-string-great/)
  <details><summary>💡 Indice d'approche</summary>Même logique que les doublons adjacents : deux lettres s'annulent si <code>abs(ord(a) - ord(b)) == 32</code> (même lettre, casse opposée).</details>
  > Notes : 

- [ ] **682. Baseball Game** (Easy) — [Lien LeetCode](https://leetcode.com/problems/baseball-game/)
  <details><summary>💡 Indice d'approche</summary>Simule directement les opérations sur une pile de scores en accédant à <code>stack[-1]</code> et <code>stack[-2]</code> pour le <code>'+'</code>.</details>
  > Notes : 

- [ ] **844. Backspace String Compare** (Easy) — [Lien LeetCode](https://leetcode.com/problems/backspace-string-compare/)
  <details><summary>💡 Indice d'approche</summary>Construis le résultat final de chaque chaîne avec une pile (<code>pop</code> si <code>'#'</code> et pile non vide). <i>Bonus : faisable en $O(1)$ espace avec Two Pointers à rebours.</i></details>
  > Notes : 

---

## Série 2 : Piles Monotones & Conception (Medium)
*Objectif : Gérer des relations d'ordre et concevoir des structures composites.*

- [ ] **2390. Removing Stars From a String** (Medium) — [Lien LeetCode](https://leetcode.com/problems/removing-stars-from-a-string/)
  <details><summary>💡 Indice d'approche</summary>Chaque <code>'*'</code> supprime le caractère valide le plus récent (sommet de la pile).</details>
  > Notes : 

- [ ] **232. Implement Queue using Stacks** (Easy) — [Lien LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/)
  <details><summary>💡 Indice d'approche</summary>Utilise deux piles (<code>in_stack</code> et <code>out_stack</code>) : ne transfère de l'une vers l'autre que lorsque <code>out_stack</code> est vide ($O(1)$ amorti).</details>
  > Notes : 

- [ ] **150. Evaluate Reverse Polish Notation** (Medium) — [Lien LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
  <details><summary>💡 Indice d'approche</summary>Empile les nombres ; à chaque opérateur, dépile deux opérandes (attention à l'ordre pour <code>-</code> et <code>/</code>, utilise <code>int(a / b)</code> pour tronquer vers zéro).</details>
  > Notes : 

- [ ] **155. Min Stack** (Medium) — [Lien LeetCode](https://leetcode.com/problems/min-stack/)
  <details><summary>💡 Indice d'approche</summary>Stocke des tuples <code>(valeur, minimum_actuel)</code> dans la pile pour retrouver le minimum en $O(1)$ à tout moment.</details>
  > Notes : 

- [ ] **739. Daily Temperatures** (Medium) — [Lien LeetCode](https://leetcode.com/problems/daily-temperatures/)
  <details><summary>💡 Indice d'approche</summary>Pile monotone décroissante stockant les <b>index</b> des jours en attente d'une température plus élevée.</details>
  > Notes : 
