# 🧠 Patterns Algorithmiques & Préparation LeetCode (Python)

Bienvenue dans mon dépôt d'apprentissage et de révision des **patterns algorithmiques** en Python. Ce référentiel est organisé par dossiers thématiques et regroupe la théorie, des schémas visuels, des squelettes abstraits, des templates exécutables (bibliothèque standard uniquement), un système de flashcards (112 cartes) ainsi qu'un programme d'entraînement progressif sur LeetCode.

---

## 🎯 Objectifs du dépôt

- **Maîtriser les mécaniques fondamentales** derrière les problèmes d'entretiens techniques.
- **Identifier le bon algorithme face à un énoncé brut** grâce à un paquet dédié de mini-énoncés sans indice de thème.
- **S'entraîner avec des squelettes purs** et des templates Python idiomatiques (`collections`, `heapq`, `bisect`, `itertools`) sans dépendance externe.
- **Expérimenter en local** grâce au fichier `main.py` présent dans chaque dossier.
- **Mémoriser durablement** via les 112 flashcards (Markdown, Anki et quiz interactif en ligne de commande).
- **Suivre sa progression** via un carnet de bord centralisé avec cases à cocher et prise de notes personnelles.

---

## 🗂️ Structure du dépôt (9 dossiers & outils transversaux)

Chaque dossier de pattern contient **4 fichiers** :
- `*_theorie.md` : Mécanique détaillée, schémas ASCII, mots-clés déclencheurs et cas d'usage.
- `*_code_astuces.md` : Templates Python exécutables (`if __name__ == "__main__":`), astuces de la bibliothèque standard et pièges à éviter.
- `*_exercices.md` : Sélection d'exercices LeetCode classés par difficulté, incluant les exercices mixtes et une progression répétitive.
- `main.py` : Bac à sable Python local pour tester les exemples et coder les solutions aux exercices.

### Outils transversaux (à la racine)
- 🧩 **[00_squelettes_patterns.md](./00_squelettes_patterns.md)** : Recueil des squelettes purs (boilerplates génériques à trous) des 9 patterns pour démarrer un exercice sans partir d'une feuille blanche.
- 📋 **[28_revision_mixte_et_carnet_de_bord.md](./28_revision_mixte_et_carnet_de_bord.md)** : Carnet de bord complet regroupant l'ensemble des **56 exercices**, avec cases à cocher `[ ]` et espace dédié aux notes personnelles.
- 🗂️ **[29_flashcards_patterns.md](./29_flashcards_patterns.md)** : Paquet de **112 flashcards** à réponses courtes et directes, structuré en deux parties :
  - **`0_Deviner_Pattern` (40 cartes)** : Mini-énoncés mélangés à l'aveugle pour s'entraîner à reconnaître le bon pattern sans indice.
  - **`1_Hashing` à `9_Heap` (72 cartes)** : Questions techniques ciblées par thème (code Python, complexité, pièges classiques).
- 📥 **[30_flashcards_anki.csv](./30_flashcards_anki.csv)** : Export CSV prêt à importer dans **Anki** (encodage UTF-8, balises HTML et tags `0_Deviner_Pattern`, `1_Hashing`, etc.).
- 🖥️ **[quiz_cli.py](./quiz_cli.py)** : Script Python interactif en terminal pour s'auto-évaluer sur le paquet `0_Deviner_Pattern`, sur un thème précis ou en mode aléatoire complet à partir de `30_flashcards_anki.csv`.

---

### Vague 1 : Les Fondamentaux

| Dossier | Théorie & Mécanique | Code, Astuces & Pièges | Plan d'Entraînement | Bac à sable |
| :--- | :--- | :--- | :--- | :--- |
| **1. Hashing** | [01_hashing_theorie.md](./1.%20Hashing/01_hashing_theorie.md) | [02_hashing_code_astuces.md](./1.%20Hashing/02_hashing_code_astuces.md) | [03_hashing_exercices.md](./1.%20Hashing/03_hashing_exercices.md) | [main.py](./1.%20Hashing/main.py) |
| **2. Two Pointers** | [04_two_pointers_theorie.md](./2.%20Two%20Pointers/04_two_pointers_theorie.md) | [05_two_pointers_code_astuces.md](./2.%20Two%20Pointers/05_two_pointers_code_astuces.md) | [06_two_pointers_exercices.md](./2.%20Two%20Pointers/06_two_pointers_exercices.md) | [main.py](./2.%20Two%20Pointers/main.py) |
| **3. Stack** | [07_stack_theorie.md](./3.%20Stack/07_stack_theorie.md) | [08_stack_code_astuces.md](./3.%20Stack/08_stack_code_astuces.md) | [09_stack_exercices.md](./3.%20Stack/09_stack_exercices.md) | [main.py](./3.%20Stack/main.py) |
| **4. Binary Search** | [10_binary_search_theorie.md](./4.%20Binary%20Search/10_binary_search_theorie.md) | [11_binary_search_code_astuces.md](./4.%20Binary%20Search/11_binary_search_code_astuces.md) | [12_binary_search_exercices.md](./4.%20Binary%20Search/12_binary_search_exercices.md) | [main.py](./4.%20Binary%20Search/main.py) |
| **5. Sliding Window** | [13_sliding_window_theorie.md](./5.%20Sliding%20Window/13_sliding_window_theorie.md) | [14_sliding_window_code_astuces.md](./5.%20Sliding%20Window/14_sliding_window_code_astuces.md) | [15_sliding_window_exercices.md](./5.%20Sliding%20Window/15_sliding_window_exercices.md) | [main.py](./5.%20Sliding%20Window/main.py) |

### Vague 2 : Précalculs, Glouton, Intervalles & Tas

| Dossier | Théorie & Mécanique | Code, Astuces & Pièges | Plan d'Entraînement | Bac à sable |
| :--- | :--- | :--- | :--- | :--- |
| **6. Prefix Suffix Sum** | [16_prefix_suffix_sum_theorie.md](./6.%20Prefix%20Suffix%20Sum/16_prefix_suffix_sum_theorie.md) | [17_prefix_suffix_sum_code_astuces.md](./6.%20Prefix%20Suffix%20Sum/17_prefix_suffix_sum_code_astuces.md) | [18_prefix_suffix_sum_exercices.md](./6.%20Prefix%20Suffix%20Sum/18_prefix_suffix_sum_exercices.md) | [main.py](./6.%20Prefix%20Suffix%20Sum/main.py) |
| **7. Greedy (Glouton)** | [19_greedy_theorie.md](./7.%20Greedy%20(Glouton)/19_greedy_theorie.md) | [20_greedy_code_astuces.md](./7.%20Greedy%20(Glouton)/20_greedy_code_astuces.md) | [21_greedy_exercices.md](./7.%20Greedy%20(Glouton)/21_greedy_exercices.md) | [main.py](./7.%20Greedy%20(Glouton)/main.py) |
| **8. Sorting Intervals** | [22_sorting_intervals_theorie.md](./8.%20Sorting%20Intervals/22_sorting_intervals_theorie.md) | [23_sorting_intervals_code_astuces.md](./8.%20Sorting%20Intervals/23_sorting_intervals_code_astuces.md) | [24_sorting_intervals_exercices.md](./8.%20Sorting%20Intervals/24_sorting_intervals_exercices.md) | [main.py](./8.%20Sorting%20Intervals/main.py) |
| **9. Heap (Tas Binaire)** | [25_heap_theorie.md](./9.%20Heap%20(Tas%20Binaire)/25_heap_theorie.md) | [26_heap_code_astuces.md](./9.%20Heap%20(Tas%20Binaire)/26_heap_code_astuces.md) | [27_heap_exercices.md](./9.%20Heap%20(Tas%20Binaire)/27_heap_exercices.md) | [main.py](./9.%20Heap%20(Tas%20Binaire)/main.py) |

---

## 🚀 Workflow d'entraînement

1. **Comprendre :** Lire `*_theorie.md` dans le dossier du pattern ciblé.
2. **Visualiser :** Exécuter les exemples de `*_code_astuces.md` dans le fichier `main.py` du dossier.
3. **Pratiquer :** Copier le squelette correspondant depuis `00_squelettes_patterns.md` dans `main.py` et résoudre les problèmes listés dans `*_exercices.md`.
4. **Réviser :** Lancer `python quiz_cli.py` dans le terminal (en commençant par le thème **`0 Deviner Pattern`** pour entraîner son diagnostic) ou importer `30_flashcards_anki.csv` dans Anki.
5. **Suivre :** Cocher l'exercice dans `28_revision_mixte_et_carnet_de_bord.md` et noter les pièges ou astuces retenus.

---

## 🛠️ Prérequis techniques

- **Langage** : Python 3.10+
- **Dépendances** : Aucune (100 % bibliothèque standard Python : `collections`, `heapq`, `bisect`, `itertools`, `math`, `csv`, `random`).

---

## 🔮 Évolutions futures

- [ ] **10. Linked Lists** (Listes chaînées, Fast & Slow Pointers, In-place Reversal)
- [ ] **11. Trees** (Arbres binaires & BST, DFS & BFS)
- [ ] **12. Backtracking, Graphs & Dynamic Programming**
