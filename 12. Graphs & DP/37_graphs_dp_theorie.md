# Pattern 12 : Graphs, Backtracking & Programmation Dynamique — Théorie (amorce)

Amorce issue de la fiche **BFS, DFS & Programmation Dynamique**. Les parcours d'**arbres** restent dans `11. Trees` ; ici on traite grilles / graphes, backtracking et DP.

---

## 1. BFS (parcours en largeur) — rappel graphe / grille

Explorer **niveau par niveau** avec une `collections.deque` (FIFO). Première atteinte d'une cible dans un graphe non pondéré = **plus court chemin**.

**Déclencheurs :** *shortest path*, *minimum distance*, *level by level*, *propagation*.

---

## 2. DFS & Backtracking

Plonger au maximum dans une branche puis revenir (pile d'appels). Cas de base : hors bornes, déjà visité, nœud nul. Sur une grille, restaurer l'état de la case après l'essai (backtracking).

**Déclencheurs :** *connected components*, *all paths*, *exist a path*, *word search*, *islands*.

---

## 3. Programmation Dynamique (DP)

Découper en sous-problèmes qui se chevauchent et **mémoriser** les résultats.

1. **État** — que représente `dp[i]` (ou `dp[r][c]`) ?
2. **Récurrence** — comment le calculer à partir d'états précédents ?
3. **Initialisation** — cas de base.

**Déclencheurs :** *nombre de façons*, *coût minimal / maximal*, choix séquentiels interdépendants.

| Approche | Quand |
| :--- | :--- |
| **Top-Down** | Récursion + `@cache` / mémo |
| **Bottom-Up** | Tableau itératif rempli dans le bon ordre |

---

## 4. Synthèse rapide

| Pattern | Structure | Indices |
| :--- | :--- | :--- |
| **BFS** | File | Plus court chemin non pondéré, niveau par niveau |
| **DFS / BT** | Récursion | Exploration complète, composantes, backtracking |
| **DP** | Tableau / cache | Combinaisons, optimum séquentiel |
