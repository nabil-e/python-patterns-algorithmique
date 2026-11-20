# 🗺️ Parcours d'Apprentissage Guidé (4 Semaines) & Critères de Maîtrise

Ce programme structure ta progression sur **28 jours** à travers les **14 patterns algorithmiques** (Vagues 1 à 3 déjà en place + Vague 4 **Backtracking, Graphs & Dynamic Programming** intégrée en Semaine 4).

---

## 🎯 Critères de Maîtrise d'un Pattern (Definition of Done)

Avant de valider un pattern et de passer au suivant, assure-toi de remplir ces **4 critères objectifs** :

1. **Diagnostic sans aide :** Identifier le pattern en moins de 30 secondes face à un énoncé inconnu (score **≥ 85 %** sur le thème `0_Deviner_Pattern` dans `quiz_cli.py`).
2. **Restitution du squelette :** Écrire le boilerplate de base dans `main.py` de mémoire en moins de 3 minutes, sans erreur de syntaxe ni de bornes.
3. **Autonomie en résolution :** Résoudre au moins **3 exercices Easy** (en < 12 min chacun) et **2 exercices Medium** (en < 25 min chacun) **sans ouvrir l'indice `<details>`**.
4. **Analyse des compromis :** Être capable d'énoncer à voix haute les complexités $O(\text{temps})$ et $O(\text{espace})$, ainsi qu'un cas limite où le pattern échoue.

---

## 📅 Semaine 1 : Les Fondamentaux (Manipulation Linéaire & Recherche)
*Objectif : Acquérir les réflexes de base pour passer d'une solution naïve $O(n^2)$ à une solution optimale $O(n)$ ou $O(n \log n)$.*

- **Jour 1 — Hashing (`1. Hashing`)**
  - Lire `01_hashing_theorie.md` + exécuter les démos de `02_hashing_code_astuces.md`.
  - Résoudre les 4 premiers exercices de `03_hashing_exercices.md`.
- **Jour 2 — Two Pointers (`2. Two Pointers`)**
  - Lire `04_two_pointers_theorie.md` + tester les variantes (convergents vs lent/rapide).
  - Résoudre 4 exercices dans `06_two_pointers_exercices.md`.
- **Jour 3 — Stack (`3. Stack`)**
  - Lire `07_stack_theorie.md` + maîtriser l'élimination adjacente et la pile monotone.
  - Résoudre 4 exercices dans `09_stack_exercices.md`.
- **Jour 4 — Binary Search (`4. Binary Search`)**
  - Lire `10_binary_search_theorie.md` + s'exercer sur `bisect` et la frontière monotone.
  - Résoudre 4 exercices dans `12_binary_search_exercices.md`.
- **Jour 5 — Sliding Window (`5. Sliding Window`)**
  - Lire `13_sliding_window_theorie.md` + distinguer fenêtre fixe et fenêtre variable.
  - Résoudre 4 exercices dans `15_sliding_window_exercices.md`.
- **Jour 6 — Consolidation & Exercices Mixtes (Vague 1)**
  - Terminer les exercices Medium restants des dossiers 1 à 5 (ex. `15. 3Sum`, `3. Longest Substring`, `11. Container With Most Water`).
- **Jour 7 — Bilan Semaine 1 (Check-up)**
  - Session `python quiz_cli.py` sur les thèmes 1 à 5 + 20 cartes de `0_Deviner_Pattern`.
  - Relire `00_Arbre_Decision_Patterns.pdf`.

---

## 📅 Semaine 2 : Précalculs, Glouton, Intervalles & Tas
*Objectif : Maîtriser les structures d'ordonnancement et les précalculs pour optimiser les requêtes répétées et les choix locaux.*

- **Jour 8 — Prefix / Suffix Sum (`6. Prefix Suffix Sum`)**
  - Lire `16_prefix_suffix_sum_theorie.md` + maîtriser la synergie Prefix Sum + Hashing (`560`).
  - Résoudre 4 exercices dans `18_prefix_suffix_sum_exercices.md`.
- **Jour 9 — Greedy (`7. Greedy (Glouton)`)**
  - Lire `19_greedy_theorie.md` + identifier quand un tri préalable garantit l'optimalité locale.
  - Résoudre 4 exercices dans `21_greedy_exercices.md`.
- **Jour 10 — Sorting Intervals (`8. Sorting Intervals`)**
  - Lire `22_sorting_intervals_theorie.md` + coder la fusion d'intervalles de mémoire.
  - Résoudre les exercices de `24_sorting_intervals_exercices.md`.
- **Jour 11 — Heap (`9. Heap (Tas Binaire)`)**
  - Lire `25_heap_theorie.md` + maîtriser le Min-Heap de taille $K$ et la négation pour Max-Heap.
  - Résoudre 4 exercices dans `27_heap_exercices.md`.
- **Jour 12 — Consolidation Vague 2**
  - Résoudre les exercices Medium clés (`238. Product Except Self`, `347. Top K Frequent`, `973. K Closest Points`, `452. Minimum Arrows`).
- **Jour 13 — Simulation d'Entretien (Vagues 1 & 2 mélangées)**
  - Tirer 3 exercices au hasard dans `28_revision_mixte_et_carnet_de_bord.md` (sections 1 à 9) et les résoudre en 45 minutes chrono.
- **Jour 14 — Bilan Semaine 2 (Check-up)**
  - Session `python quiz_cli.py` en mode **Tout mélanger** (objectif : ≥ 85 % au 1er passage).

---

## 📅 Semaine 3 : Structures Pointées & Arborescentes
*Objectif : Manipuler des références mémoire en $O(1)$ espace et maîtriser la récursivité (DFS) ainsi que les files (BFS).*

- **Jour 15 — Linked Lists : Pointeurs & Sentinelle (`10. Linked Lists`)**
  - Lire `31_linked_lists_theorie.md` + maîtriser `dummy = ListNode()` et Fast & Slow.
  - Résoudre la Série 1 de `33_linked_lists_exercices.md` (`876`, `141`, `21`, `83`, `203`).
- **Jour 16 — Linked Lists : Inversion & Combinaisons**
  - Reproduire l'inversion sur place (`prev, curr, nxt`) sans brouillon.
  - Résoudre la Série 2 de `33_linked_lists_exercices.md` (`206`, `234`, `19`, `143`).
- **Jour 17 — Trees : Parcours en Profondeur / DFS (`11. Trees`)**
  - Lire `34_trees_theorie.md` + écrire les 3 parcours récursifs (Pre, In, Post-order).
  - Résoudre les exercices DFS de `36_trees_exercices.md` (`104`, `226`, `100`, `543`, `112`).
- **Jour 18 — Trees : Parcours en Largeur / BFS & BST**
  - Maîtriser `collections.deque` pour le parcours niveau par niveau et les bornes `(min_val, max_val)` des BST.
  - Résoudre les exercices BFS/BST de `36_trees_exercices.md` (`102`, `199`, `98`, `230`, `235`).
- **Jour 19 — Consolidation Vague 3**
  - Terminer les exercices restants de Linked Lists et Trees + mettre à jour les notes dans le carnet de bord.
- **Jour 20 — Simulation d'Entretien (Vagues 1 à 3)**
  - 1 exercice Tableau/Fenêtre + 1 exercice Linked List + 1 exercice Tree en 60 minutes.
- **Jour 21 — Bilan Semaine 3 (Check-up)**
  - Révision des 11 Cheat Sheets (`sheet cheat/*.pdf`) + session complète `quiz_cli.py`.

---

## 📅 Semaine 4 : Paradigmes Avancés (Vague 4 à venir)
*Objectif : Exploration combinatoire, parcours de graphes et optimisation par sous-problèmes.*

- **Jours 22 & 23 — Backtracking (`12. Backtracking`)**
  - *Concepts clés :* Arbre de décision, choix / exploration / annulation (`path.pop()`), permutations, combinaisons et sous-ensembles.
  - *Critère :* Savoir dessiner l'arbre d'appels récursifs et élaguer les branches invalides.
- **Jours 24 & 25 — Graphs (`13. Graphs`)**
  - *Concepts clés :* Listes d'adjacence, ensemble `visited`, DFS/BFS sur grilles 2D (îles) et graphes orientés, tri topologique (Kahn).
  - *Critère :* Éviter toute boucle infinie grâce au marquage immédiat des nœuds visités.
- **Jours 26 & 27 — Dynamic Programming (`14. Dynamic Programming`)**
  - *Concepts clés :* Relation de récurrence, Mémoïsation (Top-Down avec `@lru_cache`) vs Tabulation (Bottom-Up 1D/2D), sac à dos (Knapsack) et sous-séquences.
  - *Critère :* Savoir passer d'une récursion naïve à une solution mémoïsée, puis tabulée.
- **Jour 28 — Grand Bilan Final (14 Patterns)**
  - Simulation complète de 4 exercices variés (1 Easy, 2 Medium, 1 Medium/Hard) en conditions réelles d'entretien.
