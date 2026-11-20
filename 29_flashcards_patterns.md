# 🗂️ Flashcards Algorithmiques (138 cartes)

Clique sur **Voir la réponse** pour révéler la solution. Ce paquet est synchronisé avec `30_flashcards_anki.csv` et `quiz_cli.py`.

---

## 🎯 0. Deviner le Pattern (Énoncés mélangés à l'aveugle) (50 cartes)

**Carte 1** `[Diag]` : Trouver deux nombres dans un tableau non trié dont la somme vaut K en O(n). Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Hashing (dictionnaire pour stocker les compléments déjà vus).**

</details>

**Carte 2** `[Diag]` : Vérifier rapidement si une liste contient au moins un doublon. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Hashing (comparer len(nums) et len(set(nums))).**

</details>

**Carte 3** `[Diag]` : Regrouper une liste de mots par anagrammes. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Hashing (defaultdict(list) avec le mot trié ou le tuple de fréquences comme clé).**

</details>

**Carte 4** `[Diag]` : Trouver le premier caractère non répétitif d'une chaîne. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Hashing (Counter(s) puis premier caractère avec fréquence == 1).**

</details>

**Carte 5** `[Diag]` : Vérifier si deux chaînes sont isomorphes (bijection de caractères). Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Hashing (deux dictionnaires pour vérifier la correspondance dans les deux sens).**

</details>

**Carte 6** `[Diag]` : Trouver deux éléments dont la somme vaut K dans un tableau DÉJÀ TRIÉ en O(1) espace. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Two Pointers (pointeurs convergents left=0 et right=n-1).**

</details>

**Carte 7** `[Diag]` : Déplacer tous les zéros à la fin d'un tableau en place tout en gardant l'ordre relatif. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Two Pointers (pointeurs lent/rapide : slow écrit les non-zéros, fast explore).**

</details>

**Carte 8** `[Diag]` : Mettre au carré les éléments d'un tableau trié contenant des négatifs, en O(n). Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Two Pointers (convergents aux extrémités pour comparer les plus grandes valeurs absolues).**

</details>

**Carte 9** `[Diag]` : Trouver le conteneur d'eau d'aire maximale entre deux lignes verticales. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Two Pointers (convergents en déplaçant toujours le pointeur de la plus petite hauteur).**

</details>

**Carte 10** `[Diag]` : Trouver tous les triplets uniques dans un tableau dont la somme vaut zéro. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Sorting + Two Pointers (trier le tableau, fixer i, puis deux pointeurs convergents).**

</details>

**Carte 11** `[Diag]` : Vérifier si une chaîne de parenthèses, crochets et accolades est bien équilibrée. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Stack (empiler les ouvrants, dépiler et comparer sur chaque fermant).**

</details>

**Carte 12** `[Diag]` : Supprimer en chaîne toutes les paires de lettres adjacentes identiques dans une chaîne. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Stack (comparer le caractère courant avec le sommet de la pile stack[-1]).**

</details>

**Carte 13** `[Diag]` : Simuler un éditeur de texte où '#' efface le caractère précédent. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Stack (append sur lettre, pop si '#' et pile non vide).**

</details>

**Carte 14** `[Diag]` : Implémenter une file FIFO uniquement à l'aide de deux piles LIFO. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Stack (une pile d'entrée in_stack et une pile de sortie out_stack).**

</details>

**Carte 15** `[Diag]` : Trouver l'index d'une cible dans un tableau trié en O(log n). Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Binary Search (recherche classique avec low, high et mid).**

</details>

**Carte 16** `[Diag]` : Trouver la première version défectueuse d'un logiciel via une API isBadVersion(v). Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Binary Search (recherche de frontière monotone : high = mid si True, sinon low = mid + 1).**

</details>

**Carte 17** `[Diag]` : Calculer la racine carrée entière d'un nombre x sans fonction intégrée. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Binary Search sur l'espace des réponses entre 0 et x.**

</details>

**Carte 18** `[Diag]` : Rechercher une valeur dans une matrice 2D où chaque ligne et colonne est triée globalement. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Binary Search (traiter la matrice 2D comme un tableau 1D trié de taille m*n).**

</details>

**Carte 19** `[Diag]` : Trouver la moyenne maximale d'un sous-tableau contigu de taille fixe K. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Sliding Window à taille fixe (ajouter nums[right], retirer nums[right - k]).**

</details>

**Carte 20** `[Diag]` : Trouver la longueur de la plus longue sous-chaîne sans caractère répétitif. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Sliding Window variable + Hashing (rétrécir par left tant qu'un doublon est dans le set).**

</details>

**Carte 21** `[Diag]` : Compter les sous-chaînes de taille 3 composées uniquement de caractères distincts. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Sliding Window à taille fixe + Hashing (set ou Counter sur fenêtre de taille 3).**

</details>

**Carte 22** `[Diag]` : Trouver le nombre minimum de blocs à repeindre pour obtenir K blocs noirs consécutifs. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Sliding Window à taille fixe de taille K (minimiser le nombre de 'W' dans la fenêtre).**

</details>

**Carte 23** `[Diag]` : Répondre à des milliers de requêtes de somme sur des plages [left, right] d'un tableau fixe. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Prefix Sum (précalculer les sommes cumulées pour répondre en O(1)).**

</details>

**Carte 24** `[Diag]` : Calculer le produit de tous les éléments d'un tableau sauf soi-même sans division. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Prefix & Suffix Product (deux passes : produits à gauche puis produits à droite).**

</details>

**Carte 25** `[Diag]` : Compter le nombre de sous-tableaux contigus (avec nombres négatifs) dont la somme vaut K. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Prefix Sum + Hashing (stocker les fréquences des sommes préfixes et chercher prefix - k).**

</details>

**Carte 26** `[Diag]` : Trouver l'altitude maximale atteinte lors d'un trajet défini par des variations nettes. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Prefix Sum (somme cumulée en maintenant le maximum rencontré).**

</details>

**Carte 27** `[Diag]` : Distribuer des biscuits à des enfants selon leur facteur de gourmandise pour en satisfaire un max. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Greedy (trier enfants et biscuits, attribuer le plus petit biscuit suffisant).**

</details>

**Carte 28** `[Diag]` : Maximiser le profit en achetant et revendant une action autant de fois que voulu. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Greedy (additionner toutes les variations positives consécutives prices[i] - prices[i-1]).**

</details>

**Carte 29** `[Diag]` : Vérifier si on peut rendre la monnaie exacte à chaque client avec des billets de 5, 10 et 20. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Greedy (toujours rendre le billet de 10 en priorité avant d'utiliser les billets de 5).**

</details>

**Carte 30** `[Diag]` : Trouver l'élément majoritaire (> n/2) d'un tableau en O(n) temps et O(1) espace. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Greedy / Boyer-Moore Voting (incrémenter un compteur si identique, décrémenter sinon).**

</details>

**Carte 31** `[Diag]` : Fusionner toutes les plages horaires qui se chevauchent dans un emploi du temps. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Sorting Intervals (trier par heure de début et fusionner si debut <= dernier_fin).**

</details>

**Carte 32** `[Diag]` : Trouver le nombre minimum de flèches pour éclater tous les ballons représentés par [x_start, x_end]. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Sorting Intervals + Greedy (trier par fin croissant et tirer à la fin du ballon).**

</details>

**Carte 33** `[Diag]` : Insérer un nouvel intervalle dans une liste d'intervalles triés et fusionner si nécessaire. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Sorting Intervals (ajouter avant, fusionner les chevauchements, ajouter après).**

</details>

**Carte 34** `[Diag]` : Trouver l'intersection entre deux listes d'intervalles déjà triées et disjointes. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Sorting Intervals + Two Pointers (avancer le pointeur qui a la plus petite fin).**

</details>

**Carte 35** `[Diag]` : Trouver le K-ième plus grand élément d'un tableau non trié en O(n log k). Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Heap (Min-Heap de taille fixe K : le sommet heap[0] est la réponse).**

</details>

**Carte 36** `[Diag]` : Trouver les K éléments les plus fréquents d'un tableau. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Hashing + Heap (Counter pour les fréquences, puis Min-Heap de taille K).**

</details>

**Carte 37** `[Diag]` : Simuler un jeu où l'on écrase répétitivement les deux plus grosses pierres ensemble. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Heap (Max-Heap via négation des valeurs dans heapq).**

</details>

**Carte 38** `[Diag]` : Trouver les K points les plus proches de l'origine (0, 0) sur un plan 2D. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Heap (Max-Heap de taille K sur la distance au carré x^2 + y^2).**

</details>

**Carte 39** `[Diag]` : Maintenir en continu le K-ième plus grand score dans un flux de données en temps réel. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Heap (classe avec un Min-Heap de taille K mis à jour à chaque appel de add).**

</details>

**Carte 40** `[Diag]` : Construire le plus long palindrome possible à partir des lettres d'une chaîne donnée. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Hashing + Greedy (compter les paires paires via Counter + 1 caractère central impair max).**

</details>

**Carte 41** `[Diag]` : Trouver le nœud du milieu d'une liste chaînée en une seule passe et O(1) espace. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Linked Lists — Fast & Slow Pointers (slow avance de 1, fast de 2).**

</details>

**Carte 42** `[Diag]` : Détecter si une liste chaînée contient une boucle infinie (cycle) sans mémoire extra. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Linked Lists — Fast & Slow Pointers (Floyd : slow == fast s'il y a un cycle).**

</details>

**Carte 43** `[Diag]` : Inverser l'ordre des nœuds d'une liste chaînée sur place en O(1) espace. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Linked Lists — In-place Reversal (3 pointeurs : prev, curr, nxt).**

</details>

**Carte 44** `[Diag]` : Supprimer le N-ième nœud en partant de la fin d'une liste chaînée en une passe. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Linked Lists — Dummy Node + Deux pointeurs décalés de N pas.**

</details>

**Carte 45** `[Diag]` : Vérifier si une liste chaînée est un palindrome en O(n) temps et O(1) espace. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Linked Lists — Mix Fast & Slow (milieu) + In-place Reversal (2e moitié).**

</details>

**Carte 46** `[Diag]` : Calculer la profondeur maximale (hauteur) d'un arbre binaire. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Trees — DFS récursif (1 + max(profondeur(gauche), profondeur(droite))).**

</details>

**Carte 47** `[Diag]` : Regrouper les valeurs d'un arbre binaire niveau par niveau (de haut en bas). Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Trees — BFS avec collections.deque (traiter len(queue) nœuds par niveau).**

</details>

**Carte 48** `[Diag]` : Vérifier si un arbre binaire est symétrique (miroir de lui-même autour du centre). Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Trees — DFS comparant deux sous-arbres en miroir (g.left == d.right et g.right == d.left).**

</details>

**Carte 49** `[Diag]` : Vérifier si un arbre est un Binary Search Tree (BST) valide. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Trees — DFS avec bornes (min_val < node.val < max_val) ou parcours In-order trié.**

</details>

**Carte 50** `[Diag]` : Trouver l'ancêtre commun le plus proche (LCA) de deux nœuds dans un BST. Quel pattern ?
<details>
<summary>Voir la réponse</summary>

👉 **Trees — Propriété BST (descendre à gauche si p,q < root, à droite si p,q > root, sinon root).**

</details>

---

## 1. Hashing (8 cartes)

**Carte 51** `[Complexité]` : Quelle est la complexité moyenne de recherche (in), insertion et suppression dans un dict ou set Python ?
<details>
<summary>Voir la réponse</summary>

👉 **O(1) en temps moyen.**

</details>

**Carte 52** `[Code]` : Comment compter en une ligne toutes les occurrences des éléments d'une liste nums ?
<details>
<summary>Voir la réponse</summary>

👉 **from collections import Counter; freq = Counter(nums)**

</details>

**Carte 53** `[Code]` : Quelle structure utiliser pour éviter les KeyError lors de l'ajout dans une liste associée à une clé ?
<details>
<summary>Voir la réponse</summary>

👉 **defaultdict(list) depuis le module collections.**

</details>

**Carte 54** `[Code]` : Comment récupérer les 3 éléments les plus fréquents d'un Counter c ?
<details>
<summary>Voir la réponse</summary>

👉 **c.most_common(3)**

</details>

**Carte 55** `[Piège]` : Pourquoi une liste Python [1, 2] ne peut-elle pas être utilisée comme clé d'un dictionnaire ?
<details>
<summary>Voir la réponse</summary>

👉 **Parce qu'elle est mutable (non hashable). Il faut la convertir en tuple (1, 2).**

</details>

**Carte 56** `[Piège]` : Quelle est la différence de comportement entre d[cle] et d.get(cle, 0) si la clé est absente ?
<details>
<summary>Voir la réponse</summary>

👉 **d[cle] lève une KeyError, tandis que d.get(cle, 0) retourne 0 sans erreur.**

</details>

**Carte 57** `[Théorie]` : Comment obtenir l'intersection de deux ensembles set_a et set_b en Python ?
<details>
<summary>Voir la réponse</summary>

👉 **set_a & set_b (ou set_a.intersection(set_b)).**

</details>

**Carte 58** `[Piège]` : Que se passe-t-il si on modifie la taille d'un dictionnaire pendant qu'on itère dessus avec for k in d ?
<details>
<summary>Voir la réponse</summary>

👉 **Python lève une RuntimeError: dictionary changed size during iteration.**

</details>

---

## 2. Two Pointers (8 cartes)

**Carte 59** `[Théorie]` : Quelle condition préalable est presque toujours requise pour utiliser des pointeurs convergents ?
<details>
<summary>Voir la réponse</summary>

👉 **Le tableau doit être trié (ou avoir une propriété monotone).**

</details>

**Carte 60** `[Code]` : Comment initialiser deux pointeurs convergents sur un tableau nums ?
<details>
<summary>Voir la réponse</summary>

👉 **left, right = 0, len(nums) - 1**

</details>

**Carte 61** `[Code]` : Dans un parcours lent/rapide pour filtrer en place, que représente le pointeur slow à la fin ?
<details>
<summary>Voir la réponse</summary>

👉 **La nouvelle longueur valide du tableau (les éléments valides sont dans nums[:slow]).**

</details>

**Carte 62** `[Théorie]` : Comment fusionner deux tableaux triés nums1 et nums2 dans nums1 sans écraser les données ?
<details>
<summary>Voir la réponse</summary>

👉 **Partir de la fin (de droite à gauche) en plaçant les plus grands éléments en premier.**

</details>

**Carte 63** `[Piège]` : Dans une boucle while left < right, pourquoi faut-il éviter while left <= right pour comparer des paires ?
<details>
<summary>Voir la réponse</summary>

👉 **Si left == right, on compare un élément avec lui-même (paire invalide).**

</details>

**Carte 64** `[Piège]` : Dans 3Sum, comment éviter de générer des triplets en double sans utiliser un set ?
<details>
<summary>Voir la réponse</summary>

👉 **Trier le tableau et sauter les valeurs identiques : if i > 0 and nums[i] == nums[i-1]: continue**

</details>

**Carte 65** `[Complexité]` : Quelle est la complexité spatiale typique du pattern Two Pointers ?
<details>
<summary>Voir la réponse</summary>

👉 **O(1) (modification en place ou simples variables d'index).**

</details>

**Carte 66** `[Code]` : Comment inverser une liste de caractères s en place en Python avec deux pointeurs ?
<details>
<summary>Voir la réponse</summary>

👉 **s[left], s[right] = s[right], s[left] puis left += 1; right -= 1**

</details>

---

## 3. Stack (8 cartes)

**Carte 67** `[Théorie]` : Quel principe d'accès régit une Stack (pile) ?
<details>
<summary>Voir la réponse</summary>

👉 **LIFO : Last In, First Out (Dernier entré, premier sorti).**

</details>

**Carte 68** `[Code]` : Quelle structure native Python utilise-t-on pour une pile et avec quelles méthodes ?
<details>
<summary>Voir la réponse</summary>

👉 **Une list standard avec stack.append(x) pour empiler et stack.pop() pour dépiler en O(1).**

</details>

**Carte 69** `[Code]` : Comment consulter le sommet d'une pile sans le retirer en Python ?
<details>
<summary>Voir la réponse</summary>

👉 **stack[-1] (après avoir vérifié que la pile n'est pas vide).**

</details>

**Carte 70** `[Piège]` : Que se passe-t-il si on appelle stack.pop() ou stack[-1] sur une pile vide ?
<details>
<summary>Voir la réponse</summary>

👉 **Python lève une IndexError: pop from empty list.**

</details>

**Carte 71** `[Code]` : Dans la validation de parenthèses, que faut-il vérifier à la toute fin de la boucle ?
<details>
<summary>Voir la réponse</summary>

👉 **Que la pile est totalement vide : return len(stack) == 0 (ou return not stack).**

</details>

**Carte 72** `[Piège]` : Pourquoi éviter list.pop(0) ou list.insert(0, x) sur une liste Python ?
<details>
<summary>Voir la réponse</summary>

👉 **Ces opérations coûtent O(n) car elles décalent tous les éléments en mémoire.**

</details>

**Carte 73** `[Code]` : Comment reconvertir une pile de caractères stack en chaîne de caractères finale ?
<details>
<summary>Voir la réponse</summary>

👉 **"".join(stack)**

</details>

**Carte 74** `[Complexité]` : Quelle est la complexité temporelle d'un algorithme d'élimination adjacente par pile sur une chaîne de taille n ?
<details>
<summary>Voir la réponse</summary>

👉 **O(n), car chaque caractère est empilé au plus une fois et dépilé au plus une fois.**

</details>

---

## 4. Binary Search (8 cartes)

**Carte 75** `[Complexité]` : Quelle est la complexité temporelle d'une recherche binaire sur n éléments ?
<details>
<summary>Voir la réponse</summary>

👉 **O(log n).**

</details>

**Carte 76** `[Code]` : Comment calculer l'index du milieu mid sans risque de dépassement d'entier ?
<details>
<summary>Voir la réponse</summary>

👉 **mid = low + (high - low) // 2**

</details>

**Carte 77** `[Code]` : Quel module de la bibliothèque standard Python implémente la recherche binaire sur liste triée ?
<details>
<summary>Voir la réponse</summary>

👉 **Le module bisect (bisect_left et bisect_right).**

</details>

**Carte 78** `[Théorie]` : Quelle est la différence entre bisect_left(a, x) et bisect_right(a, x) si x est déjà dans a ?
<details>
<summary>Voir la réponse</summary>

👉 **bisect_left retourne l'index avant la première occurrence de x ; bisect_right après la dernière.**

</details>

**Carte 79** `[Piège]` : Pourquoi while low < high avec low = mid peut-il provoquer une boucle infinie ?
<details>
<summary>Voir la réponse</summary>

👉 **Quand high = low + 1, mid vaut low. Si low = mid, l'intervalle ne rétrécit jamais.**

</details>

**Carte 80** `[Code]` : Dans une recherche de frontière monotone (while low < high), comment mettre à jour les bornes si condition(mid) est vraie ?
<details>
<summary>Voir la réponse</summary>

👉 **high = mid (on conserve mid car il peut être la première occurrence valide).**

</details>

**Carte 81** `[Piège]` : Dans une recherche exacte (while low <= high), pourquoi écrire low = mid + 1 et high = mid - 1 ?
<details>
<summary>Voir la réponse</summary>

👉 **Parce que mid a déjà été testé et n'est pas la cible, il faut l'exclure pour garantir la terminaison.**

</details>

**Carte 82** `[Théorie]` : Peut-on appliquer Binary Search sur un espace de réponses même sans tableau en entrée ?
<details>
<summary>Voir la réponse</summary>

👉 **Oui, dès qu'une fonction booléenne is_valid(x) est monotone (False...False, True...True).**

</details>

---

## 5. Sliding Window (8 cartes)

**Carte 83** `[Code]` : Dans une fenêtre de taille fixe k, quel est l'index exact de l'élément qui sort à gauche quand on est à right ?
<details>
<summary>Voir la réponse</summary>

👉 **right - k (si on retire avant d'ajouter) ou right - k + 1 (pour le début de la fenêtre actuelle).**

</details>

**Carte 84** `[Code]` : Quelle formule donne la longueur actuelle d'une fenêtre délimitée par left et right inclus ?
<details>
<summary>Voir la réponse</summary>

👉 **right - left + 1**

</details>

**Carte 85** `[Théorie]` : Dans une fenêtre variable, utilise-t-on un if ou un while pour rétrécir la fenêtre par la gauche ?
<details>
<summary>Voir la réponse</summary>

👉 **Un while, car il faut parfois avancer left plusieurs fois avant que la fenêtre redevienne valide.**

</details>

**Carte 86** `[Piège]` : Dans un Counter ou defaultdict de fenêtre variable, pourquoi supprimer la clé quand son compteur atteint 0 ?
<details>
<summary>Voir la réponse</summary>

👉 **Pour que len(compteur) reflète exactement le nombre d'éléments distincts présents dans la fenêtre.**

</details>

**Carte 87** `[Complexité]` : Pourquoi une boucle for right contenant un while left reste-t-elle en O(n) et non O(n²) ?
<details>
<summary>Voir la réponse</summary>

👉 **Parce que left ne recule jamais et avance au maximum n fois sur toute la durée de l'algorithme.**

</details>

**Carte 88** `[Piège]` : Pourquoi Sliding Window échoue-t-il souvent pour trouver une somme cible avec des nombres négatifs ?
<details>
<summary>Voir la réponse</summary>

👉 **Parce que rétrécir la fenêtre peut augmenter la somme (perte de monotonie). Utiliser Prefix Sum + Hashing.**

</details>

**Carte 89** `[Code]` : Dans une fenêtre fixe de taille k, à partir de quel index right commence-t-on à enregistrer les résultats ?
<details>
<summary>Voir la réponse</summary>

👉 **Dès que right >= k - 1.**

</details>

**Carte 90** `[Théorie]` : Quel mot-clé dans un énoncé indique presque toujours Sliding Window plutôt que sous-séquence ?
<details>
<summary>Voir la réponse</summary>

👉 **Contigu (contiguous subarray ou substring).**

</details>

---

## 6. Prefix / Suffix Sum (8 cartes)

**Carte 91** `[Code]` : Quelle fonction de la bibliothèque standard calcule directement les sommes cumulées d'un itérable ?
<details>
<summary>Voir la réponse</summary>

👉 **itertools.accumulate(nums)**

</details>

**Carte 92** `[Code]` : Avec un tableau prefix de taille n+1 (prefix[0]=0), quelle est la somme entre left et right inclus ?
<details>
<summary>Voir la réponse</summary>

👉 **prefix[right + 1] - prefix[left]**

</details>

**Carte 93** `[Piège]` : Dans Subarray Sum Equals K (Prefix Sum + Hashing), pourquoi initialiser le dictionnaire avec {0: 1} ?
<details>
<summary>Voir la réponse</summary>

👉 **Pour comptabiliser les sous-tableaux valides qui démarrent dès l'index 0 (quand somme_courante == k).**

</details>

**Carte 94** `[Théorie]` : Quel est l'avantage de faire un tableau prefix de taille n + 1 au lieu de taille n ?
<details>
<summary>Voir la réponse</summary>

👉 **Cela évite d'écrire une condition if left == 0 pour éviter un index négatif prefix[-1].**

</details>

**Carte 95** `[Complexité]` : Quel est le coût en temps de précalcul et de requête pour une Range Sum Query ?
<details>
<summary>Voir la réponse</summary>

👉 **O(n) pour le précalcul, puis O(1) par requête.**

</details>

**Carte 96** `[Code]` : Comment calculer le tableau des produits sans soi-même en O(1) espace supplémentaire (hors sortie) ?
<details>
<summary>Voir la réponse</summary>

👉 **Faire une passe gauche->droite dans res, puis une passe droite->gauche avec une variable suffix.**

</details>

**Carte 97** `[Théorie]` : Quelle égalité mathématique permet de trouver un sous-tableau de somme K avec les sommes préfixes ?
<details>
<summary>Voir la réponse</summary>

👉 **prefix[j] - prefix[i] == K, soit chercher prefix[j] - K dans les préfixes déjà vus.**

</details>

**Carte 98** `[Piège]` : Dans Subarray Sum Equals K, faut-il mettre à jour compteur[somme] avant ou après avoir ajouté au résultat ?
<details>
<summary>Voir la réponse</summary>

👉 **Après, sinon si K == 0 le sous-tableau vide courant se compterait lui-même.**

</details>

---

## 7. Greedy (Glouton) (8 cartes)

**Carte 99** `[Théorie]` : Quel est le principe fondamental d'un algorithme glouton (Greedy) ?
<details>
<summary>Voir la réponse</summary>

👉 **Faire à chaque étape le choix localement optimal en espérant atteindre l'optimum global, sans retour en arrière.**

</details>

**Carte 100** `[Théorie]` : Quelle est la principale différence entre Greedy et la Programmation Dynamique (DP) ?
<details>
<summary>Voir la réponse</summary>

👉 **Greedy ne revient jamais sur ses choix (un seul chemin), alors que la DP explore et mémorise tous les sous-problèmes.**

</details>

**Carte 101** `[Code]` : Quelle est la première étape de 80 % des problèmes gloutons sur tableaux ?
<details>
<summary>Voir la réponse</summary>

👉 **Trier les données (nums.sort()) selon un critère stratégique (taille, ratio, fin, etc.).**

</details>

**Carte 102** `[Théorie]` : Dans Maximum Units on a Truck, selon quel critère trier les types de boîtes ?
<details>
<summary>Voir la réponse</summary>

👉 **Par nombre d'unités par boîte décroissant (key=lambda x: x[1], reverse=True).**

</details>

**Carte 103** `[Piège]` : Quand un algorithme glouton échoue-t-il sur le problème du rendu de monnaie (Coin Change) ?
<details>
<summary>Voir la réponse</summary>

👉 **Quand les pièces ne sont pas canoniques (ex: pièces [1, 3, 4] pour rendre 6 : glouton donne 4+1+1 (3 pièces) au lieu de 3+3 (2 pièces)).**

</details>

**Carte 104** `[Code]` : Comment fonctionne l'algorithme de vote de Boyer-Moore pour l'élément majoritaire ?
<details>
<summary>Voir la réponse</summary>

👉 **Maintenir un candidat et un compteur : +1 si num == candidat, -1 sinon, changer de candidat quand compteur == 0.**

</details>

**Carte 105** `[Complexité]` : Quelle est la complexité temporelle typique d'un algorithme glouton nécessitant un tri ?
<details>
<summary>Voir la réponse</summary>

👉 **O(n log n) à cause du tri, suivi d'un parcours linéaire en O(n).**

</details>

**Carte 106** `[Piège]` : Dans Can Place Flowers, pourquoi modifier le tableau en place (flowerbed[i] = 1) quand on plante une fleur ?
<details>
<summary>Voir la réponse</summary>

👉 **Pour que la vérification de la case adjacente suivante (i + 1) sache qu'une fleur vient d'être plantée.**

</details>

---

## 8. Sorting Intervals (8 cartes)

**Carte 107** `[Code]` : Comment trier une liste d'intervalles [[debut, fin], ...] par heure de début croissante ?
<details>
<summary>Voir la réponse</summary>

👉 **intervals.sort(key=lambda x: x[0])**

</details>

**Carte 108** `[Théorie]` : Après tri par début croissant, quelle condition indique que deux intervalles A et B se chevauchent ?
<details>
<summary>Voir la réponse</summary>

👉 **B[0] <= A[1] (le début du second est inférieur ou égal à la fin du premier).**

</details>

**Carte 109** `[Code]` : Lors de la fusion de deux intervalles qui se chevauchent, comment calculer la nouvelle fin ?
<details>
<summary>Voir la réponse</summary>

👉 **nouvelle_fin = max(A[1], B[1])**

</details>

**Carte 110** `[Piège]` : Pourquoi utiliser max(A[1], B[1]) et non simplement B[1] lors d'une fusion ?
<details>
<summary>Voir la réponse</summary>

👉 **Parce que l'intervalle B peut être totalement englobé à l'intérieur de A (ex: [1, 10] et [2, 5]).**

</details>

**Carte 111** `[Théorie]` : Pour minimiser le nombre d'intervalles à supprimer (ou de flèches à tirer), faut-il trier par début ou par fin ?
<details>
<summary>Voir la réponse</summary>

👉 **Par heure de fin croissante (key=lambda x: x[1]) pour libérer de l'espace au plus tôt.**

</details>

**Carte 112** `[Code]` : Comment calculer l'intervalle d'intersection entre deux intervalles A et B ?
<details>
<summary>Voir la réponse</summary>

👉 **debut = max(A[0], B[0]) et fin = min(A[1], B[1]) (valide si debut <= fin).**

</details>

**Carte 113** `[Piège]` : Dans Insert Interval, que faire si la liste d'intervalles initiale est vide [] ?
<details>
<summary>Voir la réponse</summary>

👉 **Retourner directement [newInterval] sans erreur d'index.**

</details>

**Carte 114** `[Complexité]` : Quelle est la complexité temporelle de Merge Intervals ?
<details>
<summary>Voir la réponse</summary>

👉 **O(n log n) pour le tri initial, puis O(n) pour la fusion en une seule passe.**

</details>

---

## 9. Heap (Tas Binaire) (8 cartes)

**Carte 115** `[Théorie]` : Par défaut, quel type de tas implémente le module heapq en Python ?
<details>
<summary>Voir la réponse</summary>

👉 **Un Min-Heap (le plus petit élément est toujours à la racine heap[0]).**

</details>

**Carte 116** `[Code]` : Comment simuler un Max-Heap en Python avec le module heapq ?
<details>
<summary>Voir la réponse</summary>

👉 **Insérer l'opposé des valeurs (-x) lors du push, et reprendre -heapq.heappop(h) lors du pop.**

</details>

**Carte 117** `[Complexité]` : Quelle est la complexité de heapq.heappush et heapq.heappop sur un tas de taille n ?
<details>
<summary>Voir la réponse</summary>

👉 **O(log n).**

</details>

**Carte 118** `[Complexité]` : Quelle est la complexité de heapq.heapify(liste) pour transformer une liste existante en tas ?
<details>
<summary>Voir la réponse</summary>

👉 **O(n) en place (plus rapide que n insertions successives en O(n log n)).**

</details>

**Carte 119** `[Théorie]` : Pour trouver les K PLUS GRANDS éléments, utilise-t-on un Min-Heap ou un Max-Heap de taille K ?
<details>
<summary>Voir la réponse</summary>

👉 **Un Min-Heap de taille K (pour éjecter facilement le plus petit des K meilleurs candidats).**

</details>

**Carte 120** `[Code]` : Quelle fonction de heapq permet d'ajouter un élément et d'éjecter le plus petit en une seule opération ?
<details>
<summary>Voir la réponse</summary>

👉 **heapq.heappushpop(heap, item)**

</details>

**Carte 121** `[Piège]` : Comment éviter une TypeError lors du tri de tuples (priorite, objet) dans heapq en cas d'égalité de priorité ?
<details>
<summary>Voir la réponse</summary>

👉 **Ajouter un compteur unique en deuxième position du tuple : (priorite, idx, objet).**

</details>

**Carte 122** `[Code]` : Comment lire le plus petit élément d'un tas sans le supprimer ?
<details>
<summary>Voir la réponse</summary>

👉 **heap[0] en O(1).**

</details>

---

## 10. Linked Lists (8 cartes)

**Carte 123** `[Théorie]` : Quel est l'intérêt principal d'un Dummy Node (nœud sentinelle) dans une liste chaînée ?
<details>
<summary>Voir la réponse</summary>

👉 **Éviter tous les cas particuliers lorsque la tête (head) doit être supprimée ou déplacée.**

</details>

**Carte 124** `[Code]` : Comment initialiser un nœud sentinelle pointant vers head et que retourner à la fin ?
<details>
<summary>Voir la réponse</summary>

👉 **dummy = ListNode(0, head) et retourner dummy.next à la fin.**

</details>

**Carte 125** `[Code]` : Quelle condition exacte écrire dans la boucle while pour avancer un pointeur fast de 2 pas ?
<details>
<summary>Voir la réponse</summary>

👉 **while fast and fast.next: (toujours vérifier fast avant fast.next).**

</details>

**Carte 126** `[Code]` : Quelles sont les 4 lignes classiques pour inverser un pointeur dans In-place Reversal ?
<details>
<summary>Voir la réponse</summary>

👉 **nxt = curr.next; curr.next = prev; prev = curr; curr = nxt**

</details>

**Carte 127** `[Piège]` : Que se passe-t-il si on écrit curr.next = prev avant d'avoir sauvegardé nxt = curr.next ?
<details>
<summary>Voir la réponse</summary>

👉 **On perd définitivement la référence vers le reste de la liste chaînée.**

</details>

**Carte 128** `[Code]` : Lors de la fusion de deux listes triées l1 et l2, comment rattacher le reste en O(1) après la boucle while ?
<details>
<summary>Voir la réponse</summary>

👉 **tail.next = l1 if l1 else l2 (ou tail.next = l1 or l2).**

</details>

**Carte 129** `[Théorie]` : Comment supprimer le N-ième nœud depuis la fin d'une liste en une seule passe ?
<details>
<summary>Voir la réponse</summary>

👉 **Avancer un pointeur fast de N pas, puis avancer slow et fast ensemble jusqu'à la fin.**

</details>

**Carte 130** `[Complexité]` : Quelle est la complexité spatiale de l'inversion sur place et de la détection de cycle (Floyd) ?
<details>
<summary>Voir la réponse</summary>

👉 **O(1) en espace auxiliaire.**

</details>

---

## 11. Trees (Arbres Binaires & BST) (8 cartes)

**Carte 131** `[Théorie]` : Quelle structure de données utilise-t-on pour implémenter un parcours en largeur (BFS) par niveau ?
<details>
<summary>Voir la réponse</summary>

👉 **Une file FIFO : collections.deque avec append() et popleft().**

</details>

**Carte 132** `[Code]` : Dans un BFS par niveau, comment savoir combien de nœuds appartiennent au niveau courant ?
<details>
<summary>Voir la réponse</summary>

👉 **Stocker taille = len(queue) au début du tour de boucle while et itérer avec for _ in range(taille).**

</details>

**Carte 133** `[Théorie]` : Dans quel ordre le parcours In-order visite-t-il les nœuds d'un arbre binaire ?
<details>
<summary>Voir la réponse</summary>

👉 **Gauche -> Racine -> Droite (ce qui donne les valeurs triées par ordre croissant sur un BST).**

</details>

**Carte 134** `[Théorie]` : Dans quel ordre le parcours Post-order visite-t-il les nœuds et quand l'utilise-t-on ?
<details>
<summary>Voir la réponse</summary>

👉 **Gauche -> Droite -> Racine (idéal pour calculer une propriété de bas en haut, comme la hauteur).**

</details>

**Carte 135** `[Piège]` : Pour valider un BST, pourquoi vérifier uniquement node.left.val < node.val < node.right.val est-il faux ?
<details>
<summary>Voir la réponse</summary>

👉 **Parce que TOUS les nœuds du sous-arbre gauche doivent être strictement inférieurs à la racine, pas seulement l'enfant direct.**

</details>

**Carte 136** `[Code]` : Quel est le cas de base universel d'une fonction DFS récursive sur un arbre binaire ?
<details>
<summary>Voir la réponse</summary>

👉 **if not root: return ... (ex: return 0 pour la hauteur, return None pour une recherche).**

</details>

**Carte 137** `[Complexité]` : Quelle est la complexité spatiale d'un parcours DFS sur un arbre binaire équilibré vs dégénéré ?
<details>
<summary>Voir la réponse</summary>

👉 **O(log n) sur un arbre équilibré, et O(n) au pire cas (arbre dégénéré en ligne) à cause de la pile d'appels.**

</details>

**Carte 138** `[Piège]` : Dans un BFS avec deque, pourquoi éviter d'utiliser une list Python avec queue.pop(0) ?
<details>
<summary>Voir la réponse</summary>

👉 **Parce que list.pop(0) est en O(n), alors que deque.popleft() est en O(1).**

</details>

---

## 12. Backtracking

<details><summary><b>Q113 :</b> Quelles sont les 3 étapes fondamentales d'une fonction de Backtracking ?</summary><br><b>R :</b> <b>1. Choisir</b> (<code>path.append</code>) → <b>2. Explorer</b> (appel récursif) → <b>3. Annuler</b> (<code>path.pop</code>).</details>

<details><summary><b>Q114 :</b> Pourquoi écrit-on <code>res.append(path.copy())</code> au lieu de <code>res.append(path)</code> en Backtracking ?</summary><br><b>R :</b> Car <code>path</code> est une liste mutable modifiée sur place : sans copie, <code>res</code> contiendra uniquement des références vers une liste vide à la fin.</details>

<details><summary><b>Q115 :</b> Comment éviter les combinaisons en double dans <code>Subsets II</code> ou <code>Combination Sum II</code> ?</summary><br><b>R :</b> Trier le tableau au préalable (<code>nums.sort()</code>) et sauter les doublons au même niveau avec <code>if i > start and nums[i] == nums[i-1]: continue</code>.</details>

<details><summary><b>Q116 :</b> Quelle est la complexité temporelle typique pour générer tous les sous-ensembles ou toutes les permutations ?</summary><br><b>R :</b> Sous-ensembles : <b>O(n × 2^n)</b>. Permutations : <b>O(n × n!)</b>.</details>

<details><summary><b>Q117 :</b> Comment marquer temporairement une case visitée dans <code>Word Search</code> sans allouer un <code>set</code> supplémentaire ?</summary><br><b>R :</b> Sauvegarder <code>temp = board[r][c]</code>, remplacer par <code>'#'</code> avant l'appel récursif, puis restaurer <code>board[r][c] = temp</code>.</details>

<details><summary><b>Q118 :</b> Quelle est la différence clé entre Backtracking et Programmation Dynamique ?</summary><br><b>R :</b> Le Backtracking explore <b>toutes les solutions</b> valides (arbre complet), tandis que la DP cherche une <b>valeur optimale ou un dénombrement</b> en évitant de recalculer les sous-problèmes identiques.</details>

---

## 13. Graphs

<details><summary><b>Q119 :</b> Dans quel cas préférer le Tri Topologique (algorithme de Kahn) au DFS sur un graphe orienté ?</summary><br><b>R :</b> Pour ordonner des tâches avec dépendances (prérequis) et détecter un cycle : on traite les nœuds dont le degré entrant (<code>in_degree</code>) vaut <code>0</code>.</details>

<details><summary><b>Q120 :</b> Comment éviter d'explorer plusieurs fois le même nœud dans un graphe contenant des cycles ?</summary><br><b>R :</b> Maintenir un ensemble <code>visited = set()</code> et marquer le nœud comme visité <b>dès son ajout</b> dans la file (BFS) ou à l'entrée de la fonction (DFS).</details>

<details><summary><b>Q121 :</b> Quelle structure de données Python est obligatoire pour un BFS efficace sur un graphe ?</summary><br><b>R :</b> <code>collections.deque</code> avec <code>popleft()</code> en <b>O(1)</b> (<code>list.pop(0)</code> est en O(n) et provoque un TLE).</details>

<details><summary><b>Q122 :</b> Comment parcourir les 4 voisins orthogonaux d'une cellule <code>(r, c)</code> dans une grille 2D en Python propre ?</summary><br><b>R :</b> <code>for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)): nr, nc = r + dr, c + dc</code> en vérifiant <code>0 <= nr < rows and 0 <= nc < cols</code>.</details>

<details><summary><b>Q123 :</b> Quand utiliser un BFS multi-sources plutôt que de lancer un BFS depuis chaque case ?</summary><br><b>R :</b> Quand on cherche la distance minimale depuis <b>n'importe quel point de départ</b> parmi plusieurs (ex: <code>Rotting Oranges</code>) : on met toutes les sources dans la <code>deque</code> dès le départ.</details>

<details><summary><b>Q124 :</b> Quelle est la complexité temporelle et spatiale d'un parcours DFS ou BFS sur un graphe de V sommets et E arêtes ?</summary><br><b>R :</b> Temps : <b>O(V + E)</b>. Espace : <b>O(V)</b> pour le set <code>visited</code> et la pile/file.</details>

---

## 14. Dynamic Programming

<details><summary><b>Q125 :</b> Quelle est la différence entre l'approche Top-Down et Bottom-Up en Programmation Dynamique ?</summary><br><b>R :</b> <b>Top-Down</b> : récursion + mémoïsation (<code>@cache</code>). <b>Bottom-Up</b> : boucle itérative remplissant un tableau <code>dp</code> du cas de base vers la cible.</details>

<details><summary><b>Q126 :</b> Quel décorateur de la bibliothèque standard Python permet d'activer la mémoïsation en une ligne ?</summary><br><b>R :</b> <code>from functools import cache</code> (ou <code>@lru_cache(None)</code>) placé juste au-dessus de la fonction récursive.</details>

<details><summary><b>Q127 :</b> Pourquoi ne faut-il jamais utiliser <code>@cache</code> sur une fonction récursive qui prend une <code>list</code> en paramètre ?</summary><br><b>R :</b> Car une <code>list</code> est un type mutable non hachable (<code>TypeError: unhashable type: 'list'</code>). Il faut passer des index entiers ou des tuples.</details>

<details><summary><b>Q128 :</b> Comment optimiser l'espace mémoire d'une DP 1D (ex: <code>Climbing Stairs</code> ou <code>House Robber</code>) de O(n) à O(1) ?</summary><br><b>R :</b> Si <code>dp[i]</code> ne dépend que de <code>dp[i-1]</code> et <code>dp[i-2]</code>, remplacer le tableau entier par deux variables glissantes <code>prev1, prev2</code>.</details>

<details><summary><b>Q129 :</b> Dans <code>Coin Change</code> (minimiser le nombre de pièces), par quelle valeur initiale remplir le tableau <code>dp</code> ?</summary><br><b>R :</b> Par <code>float('inf')</code> (ou <code>amount + 1</code>), avec le cas de base <code>dp[0] = 0</code>.</details>

<details><summary><b>Q130 :</b> Quelles sont les 2 conditions pour qu'un problème soit résoluble par Programmation Dynamique ?</summary><br><b>R :</b> <b>1. Sous-structure optimale</b> (solution construite à partir de sous-problèmes) et <b>2. Chevauchement des sous-problèmes</b> (mêmes états recalculés plusieurs fois).</details>
