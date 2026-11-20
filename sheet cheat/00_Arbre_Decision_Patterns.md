# 00. ARBRE DE DÉCISION : CHOISIR LE BON PATTERN
*Méthode rapide en 10 secondes pour identifier l'algorithme optimal face à un énoncé LeetCode*

---

## 1. GUIDE DE DÉCISION RAPIDE (SI L'ÉNONCÉ MENTIONNE...)

| Indice dans l'énoncé | Mots-clés (Anglais) | Pattern à choisir | Complexité visée |
| :--- | :--- | :--- | :--- |
| Tableau trié (ou triable) + chercher une paire / triplet ou un élément | `sorted array`, `target sum`, `closest`, `O(log n)` | **Binary Search** (1 cible)<br>**Two Pointers** (paire) | $O(\log n)$<br>$O(n)$ |
| Sous-tableau contigu ou sous-chaîne avec taille fixe ou condition min/max | `contiguous subarray`, `substring`, `longest/shortest` | **Sliding Window** (positifs)<br>**Prefix Sum + Hash** (négatifs) | $O(n)$ |
| Somme sur plage(s) répétée ou produit sauf soi-même | `range sum`, `subarray sum equals k`, `product except self` | **Prefix / Suffix Sum** | $O(n)$ temps, $O(n)$ ou $O(1)$ espace |
| Doublons, fréquences, anagrammes ou recherche instantanée en O(1) | `duplicates`, `frequency`, `anagram`, `two sum`, `lookup` | **Hashing (Dict / Set)** | $O(n)$ temps, $O(n)$ espace |
| Modifier sur place sans mémoire extra, palindrome ou fusion de listes triées | `in-place`, `O(1) extra space`, `palindrome`, `merge sorted` | **Two Pointers** (Lent/Rapide ou Opposés) | $O(n)$ temps, $O(1)$ espace |
| Prochain élément plus grand/petit, parenthèses ou annulations en chaîne | `next greater`, `valid parentheses`, `nested`, `collision` | **Stack (Pile)** (Monotone) | $O(n)$ temps, $O(n)$ espace |
| Top K éléments, K-ième plus grand/petit, médiane ou fusion de K listes | `top k`, `kth largest/smallest`, `closest points`, `median` | **Heap (Tas Binaire)** | $O(n \log k)$ |
| Intervalles qui se chevauchent, plages horaires ou fusion de créneaux | `intervals`, `overlap`, `merge`, `meeting rooms`, `schedule` | **Sorting Intervals** | $O(n \log n)$ |
| Choix local optimal, sauts minimaux, atteindre la fin ou maximiser un profit | `minimum jumps`, `max profit`, `can reach`, `assign` | **Greedy (Glouton)** | $O(n)$ ou $O(n \log n)$ |
| Manipulation de nœuds `ListNode`, inversion sur place, milieu ou cycle | `linked list`, `ListNode`, `cycle`, `reverse`, `middle` | **Linked Lists** (Dummy / Fast & Slow) | $O(n)$ temps, $O(1)$ espace |
| Arbre binaire ou BST, profondeur, parcours par niveau ou ancêtres | `binary tree`, `BST`, `root`, `depth`, `level order` | **Trees** (DFS récursif / BFS `deque`) | $O(n)$ temps, $O(h)$ ou $O(w)$ espace |
| Générer toutes les combinaisons, permutations ou sous-ensembles ($N \le 20$) | `all subsets`, `permutations`, `combinations`, `word search` | **Backtracking** (Choisir / Explorer / Annuler) | $O(2^n)$ ou $O(n!)$ |
| Grille 2D d'îles, plus court chemin non pondéré ou dépendances/prérequis | `islands`, `grid`, `shortest path`, `prerequisites`, `graph` | **Graphs** (DFS / BFS `deque` / Kahn) | $O(V + E)$ |
| Nombre de façons ou coût min/max où un choix local glouton échoue | `min cost`, `number of ways`, `longest subsequence`, `DP` | **Dynamic Programming** (`@cache` / Tabulation) | $O(n)$ ou $O(n \times m)$ |

---

## 2. LES DUELS CLASSIQUES (COMMENT ÉVITER LE PIÈGE)

- **Sliding Window vs Prefix Sum + Hash**
  - **Sliding Window :** Uniquement si tous les nombres sont positifs (ajouter agrandit la somme, retirer la réduit).
  - **Prefix Sum + Hash :** Obligatoire dès qu'il y a des nombres **négatifs ou des zéros** pour une somme exacte $k$.
- **Two Pointers vs Binary Search**
  - **Binary Search :** On cherche une seule valeur (ou un seuil optimal sur une réponse) en coupant l'espace en deux.
  - **Two Pointers :** On combine deux éléments (ex: `a + b == target`) en réduisant l'intervalle pas à pas.
- **Heap vs Sorting (Tri complet)**
  - **Sorting :** Trie tout le tableau en $O(n \log n)$. Idéal si on a besoin de tout l'ordre.
  - **Heap :** Garde seulement les $K$ meilleurs en $O(n \log k)$. Indispensable si les données arrivent en flux continu (*stream*).
- **Greedy vs Programmation Dynamique (DP)**
  - **Greedy :** Un choix local évident ne compromet jamais l'avenir (ex: prendre l'intervalle qui finit le plus tôt).
  - **DP :** Si un choix immédiat bloque une meilleure combinaison plus tard (ex: rendre la monnaie avec des pièces arbitraires).
- **Trees / Graphs : DFS vs BFS**
  - **DFS (Récursif) :** Idéal pour explorer jusqu'aux feuilles, tester un chemin complet ou compter des composantes connexes.
  - **BFS (`deque`) :** Obligatoire pour un parcours niveau par niveau ou pour garantir le **plus court chemin** en nombre de pas.
- **Backtracking vs Programmation Dynamique (DP)**
  - **Backtracking :** On doit construire et retourner **toutes** les solutions explicites (arbre complet).
  - **DP :** On demande uniquement un **décompte** ou un **optimum** sans reconstruire les chemins (évite de recalculer les sous-problèmes).

---

## 3. L'INDICE ULTIME : LIRE LES CONTRAINTES DE TAILLE ($N$)

*Astuce LeetCode : Regardez toujours `N = len(nums)` en bas de l'énoncé pour éliminer les mauvaises pistes :*
- **$N \le 20$ :** Forte probabilité d'algorithme exponentiel (**Backtracking** en $O(2^n)$ ou $O(n!)$).
- **$N \le 10^3$ :** Une double boucle $O(n^2)$ ou une **DP 2D** passe généralement sans problème.
- **$N \le 10^5$ :** Une boucle imbriquée $O(n^2)$ fera *Time Limit Exceeded*. Il faut obligatoirement du **$O(n)$** (Hashing, Two Pointers, Sliding Window, Stack, Prefix Sum, Linked Lists, Trees, Graphs, DP 1D) ou du **$O(n \log n)$** (Sorting, Heap, Binary Search).
- **$N \ge 10^9$ :** Même parcourir le tableau une fois est trop lent. C'est presque toujours du **$O(\log n)$** (**Binary Search**) ou des maths.
