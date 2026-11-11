# Pattern 1 : Hashing — Plan d'Entraînement

## 1. Tes Exercices (Prioritaires)

| # | Problème | Difficulté | Sous-structure / Structure | Patterns secondaires |
|---|---|---|---|---|
| **1832** | [Check if the Sentence Is Pangram](https://leetcode.com/problems/check-if-the-sentence-is-pangram/) | Easy | `set` (taille == 26) | Aucun |
| **349** | [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) | Easy | `set` (`set1 & set2`) | Two Pointers (variante triée) |
| **387** | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | Easy | `Counter` + parcours indexé | Aucun |
| **219** | [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) | Easy | `dict` (`val -> last_idx`) | **Sliding Window** (taille fixe `k`) |

### Notes d'approche sur ta liste
* **1832 (Pangram) :** `len(set(sentence)) == 26` résout le problème en une ligne O(n).
* **349 (Intersection) :** Convertis les deux tableaux en `set` et utilise l'opérateur `&` pour obtenir les éléments communs uniques.
* **387 (First Unique Char) :** Passe 1 avec `Counter(s)`, Passe 2 avec `enumerate(s)` pour retourner le premier index ayant `counts[char] == 1`.
* **219 (Contains Duplicate II) :** Peut se résoudre avec un `dict` stockant le dernier index vu, ou avec un `set` glissant de taille maximale `k` (pont direct vers le pattern **Sliding Window**).

---

## 2. Exercices Complémentaires (Répétition et Ancrage)
Réalise ces exercices dans l'ordre pour automatiser le réflexe Hashing :

1. **217. Contains Duplicate** *(Easy)* — Base pure du `set` pour détecter un doublon.
2. **242. Valid Anagram** *(Easy)* — Comparaison directe de deux `Counter(s) == Counter(t)`.
3. **1. Two Sum** *(Easy)* — Le grand classique de la recherche de complément `target - num` dans un `dict`.
4. **383. Ransom Note** *(Easy)* — Soustraction ou comparaison de fréquences avec `Counter`.
5. **49. Group Anagrams** *(Medium)* — Utilisation de `defaultdict(list)` avec une clé canonique (`tuple(sorted(word))` ou tuple de 26 compteurs).
6. **128. Longest Consecutive Sequence** *(Medium)* — Recherche de débuts de séquences en O(n) grâce à un `set` (`if num - 1 not in num_set:`).
