# 🧭 Arbre de Décision : Identifier le bon Pattern Algorithmique

Ce guide récapitulatif vous permet d'identifier la structure de données ou l'algorithme optimal dès la première lecture de l'énoncé.

---

## 1. Tableau de Décision Rapide

| Indices dans l'énoncé | Mots-clés en anglais | Pattern à utiliser | Complexité visée |
| :--- | :--- | :--- | :--- |
| Chercher un élément, un complément ou compter des fréquences en $O(1)$. | *duplicates*, *frequency*, *anagram*, *pair sum*, *count* | **Hashing** (`dict`, `set`) | Temps : $O(n)$<br>Espace : $O(n)$ |
| Tableau **trié**, comparer une paire aux extrémités, ou modifier sur place. | *sorted array*, *in-place*, *palindrome*, *triplet* | **Two Pointers** | Temps : $O(n)$<br>Espace : $O(1)$ |
| Imbrication (parenthèses), annulation, ou trouver le prochain élément plus grand/petit. | *valid parentheses*, *next greater*, *daily temperatures*, *nested* | **Stack** (Pile / Pile Monotone) | Temps : $O(n)$<br>Espace : $O(n)$ |
| Tableau **trié** (ou partiellement trié) ou recherche d'une valeur seuil optimale. | *sorted*, *rotated array*, *minimum capacity*, *search in O(log n)* | **Binary Search** | Temps : $O(\log n)$<br>Espace : $O(1)$ |
| Sous-tableau ou sous-chaîne **contiguë** avec une condition de taille ou de somme (positifs). | *contiguous subarray*, *longest substring*, *window of size k* | **Sliding Window** | Temps : $O(n)$<br>Espace : $O(1)$ ou $O(k)$ |
| Requêtes répétées de sommes sur des plages, ou sous-tableau avec somme exacte (avec **négatifs**). | *range sum*, *subarray sum equals k*, *product except self* | **Prefix / Suffix Sum** | Temps : $O(n)$<br>Espace : $O(n)$ |
| Choix local optimal à chaque étape sans revenir en arrière (sauts, monnaie, planification). | *minimum jumps*, *maximum profit*, *can reach*, *assign* | **Greedy (Glouton)** | Temps : $O(n \log n)$ ou $O(n)$<br>Espace : $O(1)$ |
| Plages horaires, réunions, segments qui se chevauchent ou à fusionner. | *intervals*, *overlapping*, *merge*, *meeting rooms* | **Sorting Intervals** | Temps : $O(n \log n)$<br>Espace : $O(n)$ |
| Extraire dynamiquement les $K$ plus grands/petits éléments ou la médiane d'un flux. | *top k*, *kth largest*, *k closest*, *median stream* | **Heap (Tas Binaire)** | Temps : $O(n \log k)$<br>Espace : $O(k)$ |

---

## 2. Les 4 Duels Classiques (Comment trancher ?)

* **Sliding Window vs Prefix Sum + Hash Map :**
  * Utilisez **Sliding Window** si tous les nombres sont **positifs** (agrandir augmente la somme, rétrécir la diminue).
  * Utilisez **Prefix Sum + Hash Map** s'il y a des **nombres négatifs** ou des zéros qui brisent la monotonie de la fenêtre.
* **Two Pointers vs Binary Search :**
  * Utilisez **Two Pointers** si vous devez examiner *tous* les éléments ou combiner *deux* éléments (ex. : somme d'une paire).
  * Utilisez **Binary Search** si vous cherchez *un* élément précis ou une limite en coupant l'espace de recherche en deux à chaque étape.
* **Heap vs Sorting :**
  * Utilisez **Sorting** si vous avez besoin de **tout** le tableau trié une seule fois.
  * Utilisez un **Heap** si vous n'avez besoin que des **$K$ meilleurs éléments** ($K \ll N$) ou si des éléments arrivent **en continu** (flux).
* **Greedy vs Dynamic Programming (DP) :**
  * Essayez **Greedy** si un choix local évident ne bloque jamais l'optimum global.
  * Passez à la **DP** si un choix apparemment avantageux maintenant peut vous pénaliser plus tard.

---

## 3. L'astuce des contraintes de taille ($N$)

Regardez la taille maximale de l'entrée ($N$) en bas de l'énoncé pour deviner la complexité attendue :
* $N \le 10^5$ ou $10^6$ $ightarrow$ Il faut impérativement du **$O(n)$** ou **$O(n \log n)$** (Hashing, Two Pointers, Sliding Window, Binary Search, Sorting, Heap).
* $N \le 10^3$ $ightarrow$ Un algorithme en **$O(n^2)$** est accepté.
* $N \le 20$ $ightarrow$ Force brute, Backtracking ou Bitmasking en **$O(2^n)$**.
