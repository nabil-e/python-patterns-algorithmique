# 🧠 Patterns Algorithmiques & Préparation LeetCode (Python)

Bienvenue dans mon dépôt d'apprentissage et de révision des **patterns algorithmiques** en Python. Ce référentiel est organisé par dossiers thématiques et regroupe la théorie, des schémas visuels, des squelettes abstraits, des templates exécutables (bibliothèque standard uniquement), des cheat sheets (Markdown & PDF), un système de flashcards (177 cartes) ainsi qu'un programme d'entraînement progressif sur LeetCode.

---

## 🎯 Objectifs du dépôt

- **Maîtriser les mécaniques fondamentales** derrière les problèmes d'entretiens techniques.
- **Identifier le bon algorithme face à un énoncé brut** grâce à un arbre de décision et un paquet dédié de mini-énoncés sans indice de thème.
- **Réviser en un coup d'œil** grâce aux fiches synthétiques (Cheat Sheets) disponibles en `.md` et `.pdf`.
- **S'entraîner avec des squelettes purs** et des templates Python idiomatiques (`collections`, `heapq`, `bisect`, `itertools`) sans dépendance externe.
- **Expérimenter en local** grâce au fichier `main.py` présent dans chaque dossier.
- **Mémoriser durablement** via les 177 flashcards (Markdown, Anki et quiz interactif en ligne de commande).
- **Suivre sa progression** via un parcours guidé sur 4 semaines et un carnet de bord centralisé avec cases à cocher et prise de notes personnelles.

---

## 🗂️ Structure du dépôt

### Outils transversaux (à la racine)
- 🗺️ **[LEARNING_PATH.md](./LEARNING_PATH.md)** : Programme d'entraînement structuré jour par jour sur **4 semaines (28 jours)** avec les 4 critères objectifs de maîtrise d'un pattern.
- 🧩 **[00_squelettes_patterns.md](./00_squelettes_patterns.md)** : Recueil des squelettes purs (boilerplates génériques à trous en Python typé) des **14 patterns** pour démarrer un exercice sans partir d'une feuille blanche.
- 📋 **[28_revision_mixte_et_carnet_de_bord.md](./28_revision_mixte_et_carnet_de_bord.md)** : Carnet de bord complet regroupant l'ensemble des **126 exercices** sans spoiler, avec cases à cocher `[ ]` et espace dédié aux notes personnelles.
- 🗂️ **[29_flashcards_patterns.md](./29_flashcards_patterns.md)** : Paquet de **177 flashcards** à réponses courtes et directes (`0_Deviner_Pattern` + 14 thèmes).
- 📥 **[30_flashcards_anki.csv](./30_flashcards_anki.csv)** : Export CSV prêt à importer dans **Anki**.
- 🖥️ **[quiz_cli.py](./quiz_cli.py)** : Script Python interactif en terminal (avec score, pourcentage de réussite, chronomètre et relance des cartes ratées) à partir de `30_flashcards_anki.csv`.

---

### ⚡ Cheat Sheets & Arbre de Décision (`sheet cheat/`)

Fiches mémo ultra-synthétiques pour réviser rapidement ou imprimer, incluant un **arbre de décision** pour choisir le bon algorithme face à un problème inconnu :

| Sujet | Version Markdown | Version PDF |
| :--- | :--- | :--- |
| **🌳 Arbre de Décision des Patterns** | [00_Arbre_Decision_Patterns.md](./sheet%20cheat/00_Arbre_Decision_Patterns.md) | [00_Arbre_Decision_Patterns.pdf](./sheet%20cheat/00_Arbre_Decision_Patterns.pdf) |
| **1. Hashing** | [01_Hashing.md](./sheet%20cheat/01_Hashing.md) | [01_Hashing.pdf](./sheet%20cheat/01_Hashing.pdf) |
| **2. Two Pointers** | [02_Two_Pointers.md](./sheet%20cheat/02_Two_Pointers.md) | [02_Two_Pointers.pdf](./sheet%20cheat/02_Two_Pointers.pdf) |
| **3. Stack** | [03_Stack.md](./sheet%20cheat/03_Stack.md) | [03_Stack.pdf](./sheet%20cheat/03_Stack.pdf) |
| **4. Binary Search** | [04_Binary_Search.md](./sheet%20cheat/04_Binary_Search.md) | [04_Binary_Search.pdf](./sheet%20cheat/04_Binary_Search.pdf) |
| **5. Sliding Window** | [05_Sliding_Window.md](./sheet%20cheat/05_Sliding_Window.md) | [05_Sliding_Window.pdf](./sheet%20cheat/05_Sliding_Window.pdf) |
| **6. Prefix Suffix Sum** | [06_Prefix_Suffix_Sum.md](./sheet%20cheat/06_Prefix_Suffix_Sum.md) | [06_Prefix_Suffix_Sum.pdf](./sheet%20cheat/06_Prefix_Suffix_Sum.pdf) |
| **7. Greedy (Glouton)** | [07_Greedy.md](./sheet%20cheat/07_Greedy.md) | [07_Greedy.pdf](./sheet%20cheat/07_Greedy.pdf) |
| **8. Sorting Intervals** | [08_Sorting_Intervals.md](./sheet%20cheat/08_Sorting_Intervals.md) | [08_Sorting_Intervals.pdf](./sheet%20cheat/08_Sorting_Intervals.pdf) |
| **9. Heap (Tas Binaire)** | [09_Heap.md](./sheet%20cheat/09_Heap.md) | [09_Heap.pdf](./sheet%20cheat/09_Heap.pdf) |
| **10. Linked Lists** | [10_Linked_Lists.md](./sheet%20cheat/10_Linked_Lists.md) | [10_Linked_Lists.pdf](./sheet%20cheat/10_Linked_Lists.pdf) |
| **11. Trees** | [11_Trees.md](./sheet%20cheat/11_Trees.md) | [11_Trees.pdf](./sheet%20cheat/11_Trees.pdf) |

---

### 📚 Modules d'apprentissage complet (14 dossiers)

Chaque dossier de pattern contient **4 fichiers** (`*_theorie.md` avec cas limites et contre-indications, `*_code_astuces.md` en Python typé, `*_exercices.md` au format anti-spoiler et `main.py`).

#### Vague 1 : Les Fondamentaux

| Dossier | Théorie & Mécanique | Code, Astuces & Pièges | Plan d'Entraînement | Bac à sable |
| :--- | :--- | :--- | :--- | :--- |
| **01. Hashing** | [01_hashing_theorie.md](./01.%20Hashing/01_hashing_theorie.md) | [02_hashing_code_astuces.md](./01.%20Hashing/02_hashing_code_astuces.md) | [03_hashing_exercices.md](./01.%20Hashing/03_hashing_exercices.md) | [main.py](./01.%20Hashing/main.py) |
| **02. Two Pointers** | [04_two_pointers_theorie.md](./02.%20Two%20Pointers/04_two_pointers_theorie.md) | [05_two_pointers_code_astuces.md](./02.%20Two%20Pointers/05_two_pointers_code_astuces.md) | [06_two_pointers_exercices.md](./02.%20Two%20Pointers/06_two_pointers_exercices.md) | [main.py](./02.%20Two%20Pointers/main.py) |
| **03. Stack** | [07_stack_theorie.md](./03.%20Stack/07_stack_theorie.md) | [08_stack_code_astuces.md](./03.%20Stack/08_stack_code_astuces.md) | [09_stack_exercices.md](./03.%20Stack/09_stack_exercices.md) | [main.py](./03.%20Stack/main.py) |
| **04. Binary Search** | [10_binary_search_theorie.md](./04.%20Binary%20Search/10_binary_search_theorie.md) | [11_binary_search_code_astuces.md](./04.%20Binary%20Search/11_binary_search_code_astuces.md) | [12_binary_search_exercices.md](./04.%20Binary%20Search/12_binary_search_exercices.md) | [main.py](./04.%20Binary%20Search/main.py) |
| **05. Sliding Window** | [13_sliding_window_theorie.md](./05.%20Sliding%20Window/13_sliding_window_theorie.md) | [14_sliding_window_code_astuces.md](./05.%20Sliding%20Window/14_sliding_window_code_astuces.md) | [15_sliding_window_exercices.md](./05.%20Sliding%20Window/15_sliding_window_exercices.md) | [main.py](./05.%20Sliding%20Window/main.py) |

#### Vague 2 : Précalculs, Glouton, Intervalles & Tas

| Dossier | Théorie & Mécanique | Code, Astuces & Pièges | Plan d'Entraînement | Bac à sable |
| :--- | :--- | :--- | :--- | :--- |
| **06. Prefix Suffix Sum** | [16_prefix_suffix_sum_theorie.md](./06.%20Prefix%20Suffix%20Sum/16_prefix_suffix_sum_theorie.md) | [17_prefix_suffix_sum_code_astuces.md](./06.%20Prefix%20Suffix%20Sum/17_prefix_suffix_sum_code_astuces.md) | [18_prefix_suffix_sum_exercices.md](./06.%20Prefix%20Suffix%20Sum/18_prefix_suffix_sum_exercices.md) | [main.py](./06.%20Prefix%20Suffix%20Sum/main.py) |
| **07. Greedy (Glouton)** | [19_greedy_theorie.md](./07.%20Greedy%20(Glouton)/19_greedy_theorie.md) | [20_greedy_code_astuces.md](./07.%20Greedy%20(Glouton)/20_greedy_code_astuces.md) | [21_greedy_exercices.md](./07.%20Greedy%20(Glouton)/21_greedy_exercices.md) | [main.py](./07.%20Greedy%20(Glouton)/main.py) |
| **08. Sorting Intervals** | [22_sorting_intervals_theorie.md](./08.%20Sorting%20Intervals/22_sorting_intervals_theorie.md) | [23_sorting_intervals_code_astuces.md](./08.%20Sorting%20Intervals/23_sorting_intervals_code_astuces.md) | [24_sorting_intervals_exercices.md](./08.%20Sorting%20Intervals/24_sorting_intervals_exercices.md) | [main.py](./08.%20Sorting%20Intervals/main.py) |
| **09. Heap (Tas Binaire)** | [25_heap_theorie.md](./09.%20Heap%20(Tas%20Binaire)/25_heap_theorie.md) | [26_heap_code_astuces.md](./09.%20Heap%20(Tas%20Binaire)/26_heap_code_astuces.md) | [27_heap_exercices.md](./09.%20Heap%20(Tas%20Binaire)/27_heap_exercices.md) | [main.py](./09.%20Heap%20(Tas%20Binaire)/main.py) |

#### Vague 3 : Listes Chaînées & Arbres

| Dossier | Théorie & Mécanique | Code, Astuces & Pièges | Plan d'Entraînement | Bac à sable |
| :--- | :--- | :--- | :--- | :--- |
| **10. Linked Lists** | [31_linked_lists_theorie.md](./10.%20Linked%20Lists/31_linked_lists_theorie.md) | [32_linked_lists_code_astuces.md](./10.%20Linked%20Lists/32_linked_lists_code_astuces.md) | [33_linked_lists_exercices.md](./10.%20Linked%20Lists/33_linked_lists_exercices.md) | [main.py](./10.%20Linked%20Lists/main.py) |
| **11. Trees** | [34_trees_theorie.md](./11.%20Trees/34_trees_theorie.md) | [35_trees_code_astuces.md](./11.%20Trees/35_trees_code_astuces.md) | [36_trees_exercices.md](./11.%20Trees/36_trees_exercices.md) | [main.py](./11.%20Trees/main.py) |

#### Vague 4 : Exploration, Graphes & Programmation Dynamique

| Dossier | Théorie & Mécanique | Code, Astuces & Pièges | Plan d'Entraînement | Bac à sable |
| :--- | :--- | :--- | :--- | :--- |
| **12. Backtracking** | [37_backtracking_theorie.md](./12.%20Backtracking/37_backtracking_theorie.md) | [38_backtracking_code_astuces.md](./12.%20Backtracking/38_backtracking_code_astuces.md) | [39_backtracking_exercices.md](./12.%20Backtracking/39_backtracking_exercices.md) | [main.py](./12.%20Backtracking/main.py) |
| **13. Graphs** | [40_graphs_theorie.md](./13.%20Graphs/40_graphs_theorie.md) | [41_graphs_code_astuces.md](./13.%20Graphs/41_graphs_code_astuces.md) | [42_graphs_exercices.md](./13.%20Graphs/42_graphs_exercices.md) | [main.py](./13.%20Graphs/main.py) |
| **14. Dynamic Programming** | [43_dynamic_programming_theorie.md](./14.%20Dynamic%20Programming/43_dynamic_programming_theorie.md) | [44_dynamic_programming_code_astuces.md](./14.%20Dynamic%20Programming/44_dynamic_programming_code_astuces.md) | [45_dynamic_programming_exercices.md](./14.%20Dynamic%20Programming/45_dynamic_programming_exercices.md) | [main.py](./14.%20Dynamic%20Programming/main.py) |

---

## 🚀 Workflow d'entraînement

1. **Planifier :** Suivre le calendrier jour par jour de `LEARNING_PATH.md` (Semaines 1 à 4).
2. **Comprendre :** Lire `*_theorie.md` dans le dossier du pattern ciblé (en portant une attention particulière aux *Cas limites* et à *Quand éviter*).
3. **Visualiser :** Exécuter les démos typées de `*_code_astuces.md` dans le fichier `main.py` du dossier.
4. **Pratiquer :** Copier le squelette correspondant depuis `00_squelettes_patterns.md` dans `main.py` et résoudre les problèmes listés dans `*_exercices.md` sans ouvrir les indices `<details>` avant 15 minutes de recherche.
5. **Réviser :** Lancer `python quiz_cli.py` dans le terminal (en commençant par le thème **`0 Deviner Pattern`** pour entraîner son diagnostic et viser ≥ 85 % au 1er passage) ou importer `30_flashcards_anki.csv` dans Anki.
6. **Suivre :** Cocher l'exercice dans `28_revision_mixte_et_carnet_de_bord.md` et noter les pièges ou astuces retenus.

---

## 🛠️ Prérequis techniques

- **Langage** : Python 3.10+ (annotations de types natives `list[int]`, `dict[str, int]`, etc.)
- **Dépendances** : Aucune (100 % bibliothèque standard Python : `collections`, `heapq`, `bisect`, `itertools`, `functools`, `math`, `csv`, `random`).
