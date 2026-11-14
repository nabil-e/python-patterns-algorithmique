# 🗂️ Flashcards Algorithmiques — Par Thème & Identification d'Énoncés (112 Cartes)

Ce paquet est divisé en deux parties :
1. **Identification d'énoncés (`0. Deviner le Pattern`)** : 40 mini-énoncés mélangés pour entraîner ton réflexe de détection d'algorithme.
2. **Révision technique par thème (`1` à `9`)** : 72 cartes ciblées sur le code Python, les complexités et les pièges à éviter.

---

## 🎯 0. Deviner le Pattern (40 Énoncés Mélangés)

### Carte 1 — Énoncé : Trouver deux indices dans un tableau non trié dont la somme vaut `target` en O(n).
<details>
<summary>👉 Voir la réponse</summary>

**Hashing** (stocker les compléments `target - num` dans un `dict`).
</details>

### Carte 2 — Énoncé : Vérifier si une phrase contient au moins une fois chaque lettre de l'alphabet.
<details>
<summary>👉 Voir la réponse</summary>

**Hashing** (comparer `len(set(phrase)) == 26`).
</details>

### Carte 3 — Énoncé : Trouver le premier caractère qui apparaît une seule fois dans une chaîne.
<details>
<summary>👉 Voir la réponse</summary>

**Hashing** (compter les fréquences avec `Counter` puis parcourir la chaîne).
</details>

### Carte 4 — Énoncé : Regrouper ensemble tous les mots d'une liste qui sont des anagrammes.
<details>
<summary>👉 Voir la réponse</summary>

**Hashing** (utiliser `tuple(sorted(mot))` comme clé d'un `defaultdict(list)`).
</details>

### Carte 5 — Énoncé : Trouver l'intersection sans doublons de deux tableaux d'entiers.
<details>
<summary>👉 Voir la réponse</summary>

**Hashing** (conversion en `set` et opérateur `&`).
</details>

### Carte 6 — Énoncé : Vérifier si deux chaînes `s` et `t` sont isomorphes (correspondance bijective de caractères).
<details>
<summary>👉 Voir la réponse</summary>

**Hashing** (deux dictionnaires de mappage `s -> t` et `t -> s`).
</details>

### Carte 7 — Énoncé : Vérifier si un tableau contient des doublons séparés d'au plus `k` indices.
<details>
<summary>👉 Voir la réponse</summary>

**Sliding Window + Hashing** (fenêtre glissante de taille `k` maintenue dans un `set`).
</details>

### Carte 8 — Énoncé : Renvoyer les carrés triés d'un tableau déjà trié contenant des nombres négatifs et positifs.
<details>
<summary>👉 Voir la réponse</summary>

**Two Pointers** (pointeurs convergents aux deux extrémités comparant les valeurs absolues).
</details>

### Carte 9 — Énoncé : Déplacer tous les zéros d'un tableau à la fin en place sans changer l'ordre des autres éléments.
<details>
<summary>👉 Voir la réponse</summary>

**Two Pointers** (pointeurs `slow` pour l'écriture et `fast` pour l'exploration).
</details>

### Carte 10 — Énoncé : Fusionner deux tableaux triés dans le premier tableau en place sans mémoire supplémentaire.
<details>
<summary>👉 Voir la réponse</summary>

**Two Pointers** (parcours inversé depuis la fin des deux tableaux).
</details>

### Carte 11 — Énoncé : Vérifier si une chaîne `s` est une sous-séquence d'une chaîne `t`.
<details>
<summary>👉 Voir la réponse</summary>

**Two Pointers** (un pointeur sur chaque chaîne avançant lors d'une correspondance).
</details>

### Carte 12 — Énoncé : Trouver tous les triplets uniques `[a, b, c]` d'un tableau dont la somme vaut 0.
<details>
<summary>👉 Voir la réponse</summary>

**Sorting + Two Pointers** (trier, fixer `a`, puis Two Pointers convergents pour `b + c`).
</details>

### Carte 13 — Énoncé : Trouver deux barres verticales formant un récipient contenant le maximum d'eau.
<details>
<summary>👉 Voir la réponse</summary>

**Two Pointers** (convergents depuis les extrémités en déplaçant la plus petite hauteur).
</details>

### Carte 14 — Énoncé : Supprimer les doublons d'un tableau trié en place et renvoyer le nombre d'éléments uniques.
<details>
<summary>👉 Voir la réponse</summary>

**Two Pointers** (pointeurs `slow` et `fast`).
</details>

### Carte 15 — Énoncé : Vérifier si une chaîne composée de `()`, `[]` et `{}` est correctement fermée et imbriquée.
<details>
<summary>👉 Voir la réponse</summary>

**Stack** (empiler les ouvrants, dépiler et comparer sur les fermants).
</details>

### Carte 16 — Énoncé : Supprimer récursivement toutes les paires de lettres adjacentes identiques dans une chaîne (ex: `'abbaca' -> 'ca'`).
<details>
<summary>👉 Voir la réponse</summary>

**Stack** (comparer chaque caractère au sommet `stack[-1]` et dépiler si identique).
</details>

### Carte 17 — Énoncé : Calculer le score d'un jeu de baseball avec des opérations d'annulation (`'C'`) et de doublement (`'D'`).
<details>
<summary>👉 Voir la réponse</summary>

**Stack** (historique des scores valides dans une pile).
</details>

### Carte 18 — Énoncé : Supprimer chaque étoile `'*'` ainsi que le caractère valide immédiatement à sa gauche.
<details>
<summary>👉 Voir la réponse</summary>

**Stack** (empiler les lettres et `pop()` à chaque étoile).
</details>

### Carte 19 — Énoncé : Trouver l'index d'une cible ou sa position d'insertion dans un tableau trié en O(log n).
<details>
<summary>👉 Voir la réponse</summary>

**Binary Search** (recherche binaire classique / `bisect_left`).
</details>

### Carte 20 — Énoncé : Identifier la toute première version défectueuse parmi `n` versions en minimisant les appels API.
<details>
<summary>👉 Voir la réponse</summary>

**Binary Search** (recherche de frontière monotone `False -> True`).
</details>

### Carte 21 — Énoncé : Calculer la racine carrée entière d'un entier positif `x` sans fonction mathématique.
<details>
<summary>👉 Voir la réponse</summary>

**Binary Search** (sur l'espace de réponses `[0, x]`).
</details>

### Carte 22 — Énoncé : Rechercher une valeur cible dans une matrice 2D où chaque ligne est triée et supérieure à la précédente.
<details>
<summary>👉 Voir la réponse</summary>

**Binary Search** (traiter la matrice `m x n` comme un tableau 1D virtuel).
</details>

### Carte 23 — Énoncé : Trouver la moyenne maximale d'un sous-tableau contigu de longueur fixe `k`.
<details>
<summary>👉 Voir la réponse</summary>

**Sliding Window** (fenêtre de taille fixe `k`).
</details>

### Carte 24 — Énoncé : Compter le nombre de sous-chaînes de taille 3 composées uniquement de caractères distincts.
<details>
<summary>👉 Voir la réponse</summary>

**Sliding Window + Hashing** (fenêtre fixe de taille 3 avec `set` ou compteur).
</details>

### Carte 25 — Énoncé : Trouver le nombre minimum de blocs à recolorer pour obtenir `k` blocs noirs consécutifs.
<details>
<summary>👉 Voir la réponse</summary>

**Sliding Window** (fenêtre fixe de taille `k` comptant les blocs blancs).
</details>

### Carte 26 — Énoncé : Trouver la longueur de la plus longue sous-chaîne sans aucun caractère répété.
<details>
<summary>👉 Voir la réponse</summary>

**Sliding Window + Hashing** (fenêtre variable rétrécie par la gauche dès qu'un doublon apparaît).
</details>

### Carte 27 — Énoncé : Trouver le nombre maximum de voyelles dans une sous-chaîne de longueur fixe `k`.
<details>
<summary>👉 Voir la réponse</summary>

**Sliding Window** (fenêtre fixe de taille `k`).
</details>

### Carte 28 — Énoncé : Répondre à des milliers de requêtes demandant la somme entre l'index `left` et `right` d'un tableau immuable.
<details>
<summary>👉 Voir la réponse</summary>

**Prefix Sum** (précalcul des sommes cumulées pour répondre en O(1)).
</details>

### Carte 29 — Énoncé : Trouver l'altitude maximale atteinte lors d'un trajet défini par une liste de dénivelés nets.
<details>
<summary>👉 Voir la réponse</summary>

**Prefix Sum** (somme cumulée courante et suivi du maximum).
</details>

### Carte 30 — Énoncé : Calculer le produit de tous les éléments d'un tableau sauf `nums[i]` en O(n) sans division.
<details>
<summary>👉 Voir la réponse</summary>

**Prefix & Suffix Product** (passe gauche-droite puis passe droite-gauche).
</details>

### Carte 31 — Énoncé : Compter le nombre total de sous-tableaux contigus dont la somme vaut `k` (avec des nombres négatifs).
<details>
<summary>👉 Voir la réponse</summary>

**Prefix Sum + Hashing** (compter les occurrences de `somme_courante - k`).
</details>

### Carte 32 — Énoncé : Déterminer si l'on peut planter `n` fleurs dans un parterre sans deux fleurs adjacentes.
<details>
<summary>👉 Voir la réponse</summary>

**Greedy** (planter dès qu'une case et ses deux voisines sont libres).
</details>

### Carte 33 — Énoncé : Maximiser le nombre d'enfants satisfaits en distribuant au plus un biscuit par enfant.
<details>
<summary>👉 Voir la réponse</summary>

**Greedy** (trier enfants et biscuits par taille croissante et associer le plus petit biscuit suffisant).
</details>

### Carte 34 — Énoncé : Trouver l'élément majoritaire (apparaissant plus de `n/2` fois) en O(n) temps et O(1) espace.
<details>
<summary>👉 Voir la réponse</summary>

**Greedy** (algorithme de vote de Boyer-Moore).
</details>

### Carte 35 — Énoncé : Maximiser le profit total en achetant et vendant une action autant de fois que souhaité.
<details>
<summary>👉 Voir la réponse</summary>

**Greedy** (cumuler toutes les hausses positives entre deux jours consécutifs).
</details>

### Carte 36 — Énoncé : Fusionner tous les créneaux horaires qui se chevauchent dans un emploi du temps.
<details>
<summary>👉 Voir la réponse</summary>

**Sorting Intervals** (trier par heure de début et fusionner si `debut <= fin_precedente`).
</details>

### Carte 37 — Énoncé : Trouver le nombre minimum de flèches à tirer pour éclater tous les ballons représentés par des intervalles.
<details>
<summary>👉 Voir la réponse</summary>

**Sorting Intervals + Greedy** (trier par borne de fin et tirer à la fin du premier ballon).
</details>

### Carte 38 — Énoncé : Trouver l'intersection de deux listes d'intervalles disjoints et triés.
<details>
<summary>👉 Voir la réponse</summary>

**Sorting Intervals + Two Pointers** (avancer le pointeur de l'intervalle qui finit en premier).
</details>

### Carte 39 — Énoncé : Simuler un jeu où l'on détruit à chaque tour les deux pierres les plus lourdes.
<details>
<summary>👉 Voir la réponse</summary>

**Heap** (Max-Heap via négation avec `heapq`).
</details>

### Carte 40 — Énoncé : Trouver les `k` éléments les plus fréquents d'un tableau en mieux que O(n log n).
<details>
<summary>👉 Voir la réponse</summary>

**Hashing + Heap** (`Counter` puis Min-Heap de taille `k`).
</details>

---

## 📌 1. Hashing (8 cartes)

### Carte 1 [Code] — Code : Quelle structure standard Python permet de compter les fréquences en une ligne ?
<details>
<summary>👉 Voir la réponse</summary>

`from collections import Counter; Counter(nums)`
</details>

### Carte 2 [Theorie] — Théorie : Quelle est la complexité temporelle moyenne d'une recherche dans un `set` ou `dict` ?
<details>
<summary>👉 Voir la réponse</summary>

O(1) en moyenne (O(n) dans le pire cas de collisions).
</details>

### Carte 3 [Piege] — Piège : Pourquoi faut-il convertir une liste `[1, 2]` en `tuple((1, 2))` avant de la mettre dans un `set` ?
<details>
<summary>👉 Voir la réponse</summary>

Parce qu'une liste est mutable (non hachable) et lève une `TypeError`.
</details>

### Carte 4 [Code] — Code : Quelle structure évite de vérifier `if k not in d:` avant d'ajouter à une liste ?
<details>
<summary>👉 Voir la réponse</summary>

`defaultdict(list)` du module `collections`.
</details>

### Carte 5 [Code] — Code : Comment vérifier en O(1) si une chaîne `s` contient les 26 lettres de l'alphabet ?
<details>
<summary>👉 Voir la réponse</summary>

`len(set(s)) == 26` (après filtrage des lettres).
</details>

### Carte 6 [Code] — Code : Comment obtenir l'intersection unique de deux listes `a` et `b` en Python ?
<details>
<summary>👉 Voir la réponse</summary>

`list(set(a) & set(b))`
</details>

### Carte 7 [Piege] — Piège : Que renvoie `d[cle]` sur un `defaultdict(int)` si la clé n'existe pas encore ?
<details>
<summary>👉 Voir la réponse</summary>

Il crée la clé avec la valeur `0` (attention à ne pas polluer le dictionnaire en lecture).
</details>

### Carte 8 [Code] — Code : Quelle clé canonique utiliser dans un dictionnaire pour regrouper des anagrammes ?
<details>
<summary>👉 Voir la réponse</summary>

`tuple(sorted(mot))` ou un tuple de 26 compteurs.
</details>

---

## 📌 2. Two Pointers (8 cartes)

### Carte 1 [Theorie] — Théorie : Quelle condition préalable est obligatoire pour utiliser deux pointeurs convergents sur une recherche de somme ?
<details>
<summary>👉 Voir la réponse</summary>

Le tableau doit être trié.
</details>

### Carte 2 [Code] — Code : Quelle condition de boucle utilise-t-on pour deux pointeurs convergents ?
<details>
<summary>👉 Voir la réponse</summary>

`while left < right:` (ou `<=` si l'élément central doit être traité).
</details>

### Carte 3 [Code] — Code : Dans le pattern Lent/Rapide (Slow/Fast), que représente le pointeur `slow` ?
<details>
<summary>👉 Voir la réponse</summary>

L'index d'écriture du prochain élément valide à conserver.
</details>

### Carte 4 [Code] — Code : Dans quel sens parcourt-on pour fusionner deux tableaux triés en place sans écraser les données ?
<details>
<summary>👉 Voir la réponse</summary>

De la fin vers le début (index décroissants).
</details>

### Carte 5 [Piege] — Piège : Que se passe-t-il si on oublie de faire avancer `left` ou `right` dans une branche du `while` ?
<details>
<summary>👉 Voir la réponse</summary>

Une boucle infinie (Time Limit Exceeded).
</details>

### Carte 6 [Theorie] — Théorie : Quelle est la complexité spatiale d'un algorithme Two Pointers en place ?
<details>
<summary>👉 Voir la réponse</summary>

O(1) (aucune structure auxiliaire allouée).
</details>

### Carte 7 [Code] — Code : Comment comparer deux chaînes avec des caractères d'effacement `'#'` en O(1) espace ?
<details>
<summary>👉 Voir la réponse</summary>

En parcourant les deux chaînes à l'envers (de la droite vers la gauche) avec un compteur d'effacements.
</details>

### Carte 8 [Code] — Code : Sur un tableau trié contenant des négatifs, où se trouvent les plus grands carrés ?
<details>
<summary>👉 Voir la réponse</summary>

Aux deux extrémités (`left` et `right`).
</details>

---

## 📌 3. Stack (8 cartes)

### Carte 1 [Theorie] — Théorie : Quel principe régit une pile (Stack) ?
<details>
<summary>👉 Voir la réponse</summary>

LIFO (Last In, First Out — dernier entré, premier sorti).
</details>

### Carte 2 [Code] — Code : Quelles méthodes de la `list` Python utilise-t-on pour empiler et dépiler en O(1) ?
<details>
<summary>👉 Voir la réponse</summary>

`stack.append(x)` pour empiler et `stack.pop()` pour dépiler.
</details>

### Carte 3 [Code] — Code : Comment consulter le sommet de la pile sans le retirer ?
<details>
<summary>👉 Voir la réponse</summary>

`stack[-1]` (après avoir vérifié que `stack` n'est pas vide).
</details>

### Carte 4 [Piege] — Piège : Que faire avant d'appeler `stack.pop()` ou `stack[-1]` lors de la validation de parenthèses ?
<details>
<summary>👉 Voir la réponse</summary>

Vérifier `if not stack:` pour éviter une `IndexError`.
</details>

### Carte 5 [Code] — Code : Quelle condition finale vérifie qu'une chaîne de parenthèses est entièrement valide ?
<details>
<summary>👉 Voir la réponse</summary>

`return len(stack) == 0` (ou `return not stack`).
</details>

### Carte 6 [Code] — Code : Comment convertir une pile de caractères `['a', 'b', 'c']` en chaîne finale ?
<details>
<summary>👉 Voir la réponse</summary>

`''.join(stack)`
</details>

### Carte 7 [Theorie] — Théorie : Comment simuler une file (FIFO) avec des piles (LIFO) en O(1) amorti ?
<details>
<summary>👉 Voir la réponse</summary>

Avec deux piles : une pile d'entrée (`in_stack`) et une pile de sortie (`out_stack`).
</details>

### Carte 8 [Piege] — Piège : Pourquoi faut-il éviter `list.pop(0)` en Python ?
<details>
<summary>👉 Voir la réponse</summary>

Sa complexité est O(n) car elle décale tous les éléments en mémoire.
</details>

---

## 📌 4. Binary Search (8 cartes)

### Carte 1 [Theorie] — Théorie : Quelle est la complexité temporelle d'une recherche binaire ?
<details>
<summary>👉 Voir la réponse</summary>

O(log n).
</details>

### Carte 2 [Code] — Code : Quelle formule évite tout dépassement d'entier lors du calcul du milieu ?
<details>
<summary>👉 Voir la réponse</summary>

`mid = left + (right - left) // 2`
</details>

### Carte 3 [Code] — Code : Quel module standard Python implémente la recherche binaire sur une liste triée ?
<details>
<summary>👉 Voir la réponse</summary>

Le module `bisect` (`bisect_left` et `bisect_right`).
</details>

### Carte 4 [Code] — Code : Quelle est la différence entre `bisect_left` et `bisect_right` en cas de doublons ?
<details>
<summary>👉 Voir la réponse</summary>

`bisect_left` renvoie l'index avant le premier doublon ; `bisect_right` après le dernier.
</details>

### Carte 5 [Piege] — Piège : Dans `while left < right:`, si on écrit `left = mid` sans `+ 1`, quel est le risque ?
<details>
<summary>👉 Voir la réponse</summary>

Une boucle infinie lorsque `right == left + 1`.
</details>

### Carte 6 [Theorie] — Théorie : Quelle propriété mathématique permet d'appliquer Binary Search sur un espace de réponses (sans tableau) ?
<details>
<summary>👉 Voir la réponse</summary>

La monotonie d'une fonction booléenne (tous les `False` suivis de tous les `True`).
</details>

### Carte 7 [Code] — Code : Comment traiter une matrice 2D triée de taille `m x n` comme un seul tableau 1D trié ?
<details>
<summary>👉 Voir la réponse</summary>

Convertir l'index 1D `mid` en coordonnées 2D via `row = mid // n` et `col = mid % n`.
</details>

### Carte 8 [Code] — Code : Dans `while left <= right:`, que vaut `left` à la fin de la boucle si la cible n'est pas trouvée ?
<details>
<summary>👉 Voir la réponse</summary>

L'index exact où la cible doit être insérée.
</details>

---

## 📌 5. Sliding Window (8 cartes)

### Carte 1 [Code] — Code : Pour une fenêtre fixe de taille `k` se terminant à `right`, quel est l'index de l'élément qui sort ?
<details>
<summary>👉 Voir la réponse</summary>

`right - k + 1` (ou `right - k` juste avant d'ajouter `right`).
</details>

### Carte 2 [Code] — Code : Quelle structure interne maintient une fenêtre variable tant qu'elle est invalide ?
<details>
<summary>👉 Voir la réponse</summary>

Une boucle `while condition_invalide:` qui incrémente `left += 1`.
</details>

### Carte 3 [Code] — Code : Comment calculer la longueur courante d'une fenêtre délimitée par `left` et `right` inclus ?
<details>
<summary>👉 Voir la réponse</summary>

`right - left + 1`
</details>

### Carte 4 [Piege] — Piège : Dans un `defaultdict(int)` représentant la fenêtre, que faire quand `count[s[left]]` tombe à 0 ?
<details>
<summary>👉 Voir la réponse</summary>

Exécuter `del count[s[left]]` si l'algorithme teste `len(count)`.
</details>

### Carte 5 [Theorie] — Théorie : Quelle est la complexité temporelle d'une fenêtre glissante variable malgré le `while` imbriqué dans le `for` ?
<details>
<summary>👉 Voir la réponse</summary>

O(n), car `left` et `right` avancent chacun au maximum `n` fois.
</details>

### Carte 6 [Code] — Code : Comment détecter un doublon dans une fenêtre de taille au plus `k` en O(1) ?
<details>
<summary>👉 Voir la réponse</summary>

Maintenir un `set` des éléments de la fenêtre et supprimer `nums[i - k]` quand `len(window) > k`.
</details>

### Carte 7 [Piege] — Piège : Pourquoi faut-il mettre à jour le résultat maximum APRES la boucle `while` dans une fenêtre variable ?
<details>
<summary>👉 Voir la réponse</summary>

Parce que la fenêtre n'est garantie valide qu'une fois la boucle de rétrécissement terminée.
</details>

### Carte 8 [Code] — Code : Comment initialiser la somme d'une première fenêtre de taille `k` en Python ?
<details>
<summary>👉 Voir la réponse</summary>

`window_sum = sum(nums[:k])`
</details>

---

## 📌 6. Prefix Suffix Sum (8 cartes)

### Carte 1 [Code] — Code : Quelle fonction de `itertools` calcule directement les sommes cumulées d'une liste ?
<details>
<summary>👉 Voir la réponse</summary>

`itertools.accumulate(nums)`
</details>

### Carte 2 [Code] — Code : Avec un tableau `prefix` de taille `n + 1` (commençant par 0), comment calculer la somme de `left` à `right` inclus ?
<details>
<summary>👉 Voir la réponse</summary>

`prefix[right + 1] - prefix[left]`
</details>

### Carte 3 [Piege] — Piège : Pourquoi ajoute-t-on un `0` au début du tableau `prefix` ?
<details>
<summary>👉 Voir la réponse</summary>

Pour éviter un cas particulier lorsque `left == 0`.
</details>

### Carte 4 [Code] — Code : Dans « Subarray Sum Equals K », quelle valeur initiale doit avoir le dictionnaire `compte_prefixes` ?
<details>
<summary>👉 Voir la réponse</summary>

`{0: 1}` (pour compter les sous-tableaux commençant à l'index 0).
</details>

### Carte 5 [Theorie] — Théorie : Pourquoi Sliding Window échoue-t-il sur « Sous-tableau de somme K » si le tableau contient des nombres négatifs ?
<details>
<summary>👉 Voir la réponse</summary>

Parce que la somme n'est plus monotone quand on agrandit ou rétrécit la fenêtre.
</details>

### Carte 6 [Code] — Code : Comment calculer le produit de tous les éléments sauf `nums[i]` sans division et en O(1) espace extra ?
<details>
<summary>👉 Voir la réponse</summary>

Faire une passe gauche-droite pour les produits préfixes, puis une passe droite-gauche en accumulant le suffixe dans le résultat.
</details>

### Carte 7 [Theorie] — Théorie : Quelle est la complexité d'une requête de somme de plage après précalcul du Prefix Sum ?
<details>
<summary>👉 Voir la réponse</summary>

O(1) par requête (après O(n) de précalcul).
</details>

### Carte 8 [Code] — Code : Dans « Subarray Sum Equals K », quelle clé recherche-t-on dans le dictionnaire des préfixes ?
<details>
<summary>👉 Voir la réponse</summary>

`somme_courante - k`
</details>

---

## 📌 7. Greedy (8 cartes)

### Carte 1 [Theorie] — Théorie : Quelle est la règle d'or d'un algorithme glouton (Greedy) ?
<details>
<summary>👉 Voir la réponse</summary>

Faire le choix localement optimal à chaque étape sans jamais revenir en arrière.
</details>

### Carte 2 [Code] — Code : Comment fonctionne l'algorithme de Boyer-Moore pour l'élément majoritaire en O(1) espace ?
<details>
<summary>👉 Voir la réponse</summary>

Maintenir un `candidat` et un `compteur` (+1 si identique, -1 sinon, changer de candidat si compteur == 0).
</details>

### Carte 3 [Theorie] — Théorie : Quelle est la complexité temporelle typique d'un algorithme glouton basé sur un tri préalable ?
<details>
<summary>👉 Voir la réponse</summary>

O(n log n).
</details>

### Carte 4 [Piege] — Piège : Quand faut-il rejeter une approche gloutonne au profit de la programmation dynamique ?
<details>
<summary>👉 Voir la réponse</summary>

Quand un choix local optimal bloque la meilleure solution globale (ex: rendu de monnaie avec pièces [1, 3, 4] pour faire 6).
</details>

### Carte 5 [Code] — Code : Comment maximiser le profit sur « Best Time to Buy and Sell Stock II » (transactions illimitées) ?
<details>
<summary>👉 Voir la réponse</summary>

Additionner toutes les différences positives consécutives : `max(0, prices[i] - prices[i-1])`.
</details>

### Carte 6 [Code] — Code : Dans « Lemonade Change », quel billet faut-il rendre en priorité pour un billet de 20$ ?
<details>
<summary>👉 Voir la réponse</summary>

Un billet de 10$ + un billet de 5$ (pour économiser les billets de 5$ plus polyvalents).
</details>

### Carte 7 [Code] — Code : Pour maximiser le nombre d'enfants satisfaits (« Assign Cookies »), dans quel ordre trie-t-on ?
<details>
<summary>👉 Voir la réponse</summary>

Trier les enfants et les biscuits par ordre croissant.
</details>

### Carte 8 [Code] — Code : Pour maximiser les unités dans un camion (« Maximum Units on a Truck »), selon quel critère trier les boîtes ?
<details>
<summary>👉 Voir la réponse</summary>

Par nombre d'unités par boîte décroissant : `key=lambda x: -x[1]`.
</details>

---

## 📌 8. Sorting Intervals (8 cartes)

### Carte 1 [Code] — Code : Comment trier une liste d'intervalles `[start, end]` par borne de début en Python ?
<details>
<summary>👉 Voir la réponse</summary>

`intervals.sort(key=lambda x: x[0])`
</details>

### Carte 2 [Code] — Code : Quelle condition vérifie si deux intervalles triés `A` et `B` se chevauchent ?
<details>
<summary>👉 Voir la réponse</summary>

`B[0] <= A[1]`
</details>

### Carte 3 [Code] — Code : Comment mettre à jour la fin du dernier intervalle fusionné lors d'un chevauchement ?
<details>
<summary>👉 Voir la réponse</summary>

`merged[-1][1] = max(merged[-1][1], current[1])`
</details>

### Carte 4 [Code] — Code : Comment calculer l'intersection exacte de deux intervalles `[s1, e1]` et `[s2, e2]` ?
<details>
<summary>👉 Voir la réponse</summary>

`debut = max(s1, s2)` et `fin = min(e1, e2)` (valide si `debut <= fin`).
</details>

### Carte 5 [Code] — Code : Pour minimiser le nombre de flèches (« Burst Balloons »), selon quelle borne vaut-il mieux trier ?
<details>
<summary>👉 Voir la réponse</summary>

La borne de fin croissante : `key=lambda x: x[1]`.
</details>

### Carte 6 [Piege] — Piège : Dans l'intersection de deux listes d'intervalles triées, quel pointeur avancer à chaque étape ?
<details>
<summary>👉 Voir la réponse</summary>

Celui dont l'intervalle se termine le plus tôt (`e1 < e2`).
</details>

### Carte 7 [Theorie] — Théorie : Quelle est la complexité dominante des problèmes d'intervalles ?
<details>
<summary>👉 Voir la réponse</summary>

O(n log n) à cause du tri initial.
</details>

### Carte 8 [Code] — Code : Comment insérer un nouvel intervalle dans une liste déjà triée en O(n) sans re-trier ?
<details>
<summary>👉 Voir la réponse</summary>

Ajouter ceux avant, fusionner ceux qui chevauchent avec `min`/`max`, puis ajouter ceux après.
</details>

---

## 📌 9. Heap (8 cartes)

### Carte 1 [Theorie] — Théorie : Quel type de tas est implémenté par défaut dans le module standard `heapq` ?
<details>
<summary>👉 Voir la réponse</summary>

Un Min-Heap (le plus petit élément est toujours à l'index 0).
</details>

### Carte 2 [Code] — Code : Comment simuler un Max-Heap avec `heapq` sur des nombres ?
<details>
<summary>👉 Voir la réponse</summary>

Insérer leurs opposés (`-x`) et inverser le signe à la sortie (`-heapq.heappop(h)`).
</details>

### Carte 3 [Code] — Code : Quelle fonction transforme une liste existante en tas valide en O(n) en place ?
<details>
<summary>👉 Voir la réponse</summary>

`heapq.heapify(liste)`
</details>

### Carte 4 [Code] — Code : Quelle structure utiliser pour trouver le **K-ième plus grand** élément en O(n log k) ?
<details>
<summary>👉 Voir la réponse</summary>

Un **Min-Heap** maintenu à une taille maximale de `k` (le résultat final est `heap[0]`).
</details>

### Carte 5 [Piege] — Piège : Pourquoi faut-il évincer `heapq.heappop(h)` dès que `len(h) > k` pour le Top K plus grands ?
<details>
<summary>👉 Voir la réponse</summary>

Pour éliminer les plus petits éléments et ne conserver que les `k` champions.
</details>

### Carte 6 [Code] — Code : Quelle fonction dédiée de `heapq` renvoie directement les `k` plus grands éléments d'un itérable ?
<details>
<summary>👉 Voir la réponse</summary>

`heapq.nlargest(k, iterable, key=...)`
</details>

### Carte 7 [Theorie] — Théorie : Quelle est la complexité d'une insertion (`heappush`) ou d'une extraction (`heappop`) ?
<details>
<summary>👉 Voir la réponse</summary>

O(log n).
</details>

### Carte 8 [Piege] — Piège : Que se passe-t-il si deux tuples dans un tas ont la même priorité `(prio, objet)` et que `objet` n'est pas comparable ?
<details>
<summary>👉 Voir la réponse</summary>

Python lève une `TypeError` (solution : ajouter un index briseur d'égalité `(prio, idx, objet)`).
</details>

---

