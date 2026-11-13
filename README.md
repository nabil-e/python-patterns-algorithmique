# 🧠 Patterns Algorithmiques & Préparation LeetCode (Python)

Bienvenue dans mon dépôt d'apprentissage et de révision des **patterns algorithmiques** en Python. Ce référentiel regroupe la théorie, des schémas visuels, des templates prêts à exécuter (utilisant en priorité la bibliothèque standard Python), des astuces, les pièges classiques à éviter ainsi qu'un programme d'entraînement progressif sur LeetCode.

---

## 🎯 Objectifs du dépôt

- **Maîtriser les mécaniques fondamentales** derrière les problèmes d'entretiens techniques.
- **Repérer les mots-clés déclencheurs** dans les énoncés pour identifier immédiatement le bon pattern.
- **Appliquer des templates Python idiomatiques** (`collections`, `heapq`, `bisect`, `itertools`) sans dépendance externe.
- **Ancrer les automatismes** grâce à des séries d'exercices progressifs et répétitifs.
- **Suivre sa progression** via un carnet de bord centralisé avec cases à cocher et prise de notes personnelles.

---

## 🗂️ Structure du programme (28 fiches)

Chaque pattern est découpé en **3 modules complémentaires** :
1. **Théorie (`theorie.md`)** : Mécanique détaillée, schémas ASCII, mots-clés déclencheurs et cas d'usage.
2. **Code & Astuces (`code_astuces.md`)** : Templates Python exécutables (`if __name__ == "__main__":`), astuces de la bibliothèque standard et pièges à éviter.
3. **Exercices (`exercices.md`)** : Sélection d'exercices LeetCode classés par difficulté, incluant les exercices mixtes et une progression répétitive.

### Vague 1 : Les Fondamentaux

| Pattern | Théorie & Mécanique | Code, Astuces & Pièges | Plan d'Entraînement |
| :--- | :--- | :--- | :--- |
| **1. Hashing** | [01_hashing_theorie.md](./01_hashing_theorie.md) | [02_hashing_code_astuces.md](./02_hashing_code_astuces.md) | [03_hashing_exercices.md](./03_hashing_exercices.md) |
| **2. Two Pointers** | [04_two_pointers_theorie.md](./04_two_pointers_theorie.md) | [05_two_pointers_code_astuces.md](./05_two_pointers_code_astuces.md) | [06_two_pointers_exercices.md](./06_two_pointers_exercices.md) |
| **3. Stack** | [07_stack_theorie.md](./07_stack_theorie.md) | [08_stack_code_astuces.md](./08_stack_code_astuces.md) | [09_stack_exercices.md](./09_stack_exercices.md) |
| **4. Binary Search** | [10_binary_search_theorie.md](./10_binary_search_theorie.md) | [11_binary_search_code_astuces.md](./11_binary_search_code_astuces.md) | [12_binary_search_exercices.md](./12_binary_search_exercices.md) |
| **5. Sliding Window** | [13_sliding_window_theorie.md](./13_sliding_window_theorie.md) | [14_sliding_window_code_astuces.md](./14_sliding_window_code_astuces.md) | [15_sliding_window_exercices.md](./15_sliding_window_exercices.md) |

### Vague 2 : Précalculs, Glouton, Intervalles & Tas

| Pattern | Théorie & Mécanique | Code, Astuces & Pièges | Plan d'Entraînement |
| :--- | :--- | :--- | :--- |
| **6. Prefix / Suffix Sum** | [16_prefix_suffix_sum_theorie.md](./16_prefix_suffix_sum_theorie.md) | [17_prefix_suffix_sum_code_astuces.md](./17_prefix_suffix_sum_code_astuces.md) | [18_prefix_suffix_sum_exercices.md](./18_prefix_suffix_sum_exercices.md) |
| **7. Greedy (Glouton)** | [19_greedy_theorie.md](./19_greedy_theorie.md) | [20_greedy_code_astuces.md](./20_greedy_code_astuces.md) | [21_greedy_exercices.md](./21_greedy_exercices.md) |
| **8. Sorting Intervals** | [22_sorting_intervals_theorie.md](./22_sorting_intervals_theorie.md) | [23_sorting_intervals_code_astuces.md](./23_sorting_intervals_code_astuces.md) | [24_sorting_intervals_exercices.md](./24_sorting_intervals_exercices.md) |
| **9. Heap (Tas Binaire)** | [25_heap_theorie.md](./25_heap_theorie.md) | [26_heap_code_astuces.md](./26_heap_code_astuces.md) | [27_heap_exercices.md](./27_heap_exercices.md) |

### Suivi Global & Révisions
- 📋 **[28_revision_mixte_et_carnet_de_bord.md](./28_revision_mixte_et_carnet_de_bord.md)** : Carnet de bord complet regroupant l'ensemble des **56 exercices** (incluant les problèmes multi-patterns), avec cases à cocher et espace dédié aux notes personnelles.

---

## 🚀 Comment utiliser ce dépôt ?

1. **Suivre l'ordre numérique (`01` à `27`)** : Les patterns sont organisés de manière progressive (ex. : le *Hashing* appris en premier sert ensuite dans *Sliding Window*, *Prefix Sum* et *Heap*).
2. **Lire et expérimenter** : Pour chaque pattern, lire la théorie, copier-coller les templates de `code_astuces.md` dans un environnement Python local (Python 3.10+ recommandé) et les exécuter pour observer leur comportement.
3. **Pratiquer par répétition** : Résoudre les exercices dans l'ordre indiqué dans `exercices.md` sans regarder la solution immédiatement.
4. **Tracer sa progression** : Cocher les cases `[x]` dans `28_revision_mixte_et_carnet_de_bord.md` et noter sous chaque exercice l'astuce clé ou le piège rencontré.

---

## 🛠️ Prérequis techniques

- **Langage** : Python 3.10+
- **Dépendances** : Aucune. Tous les exemples reposent exclusivement sur la **bibliothèque standard Python** (`collections`, `heapq`, `bisect`, `itertools`, `math`).

---

## 🔮 Évolutions futures

- [ ] **Vague 3** : Linked Lists (Listes chaînées), Fast & Slow Pointers, In-place Reversal.
- [ ] **Vague 4** : Trees (Arbres binaires & BST), DFS & BFS.
- [ ] **Vague 5** : Backtracking, Graphs & Dynamic Programming (Programmation Dynamique).
