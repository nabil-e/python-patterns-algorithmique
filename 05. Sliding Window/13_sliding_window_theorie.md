# Sliding Window — Théorie et Mécanique

## 1. Principe Fondamental

Le pattern **Sliding Window** (Fenêtre Glissante) permet de transformer des boucles imbriquées en $O(n^2)$ en un seul passage linéaire en $O(n)$ sur des séquences (tableaux ou chaînes de caractères).

Au lieu de recalculer la somme ou le contenu de chaque sous-tableau depuis zéro, on maintient une **fenêtre** délimitée par deux pointeurs (`left` et `right`) qui glisse vers la droite :
* On **ajoute** l'élément entrant à droite (`right`).
* On **retire** l'élément sortant à gauche (`left`).

---

## 2. Les Deux Variantes et Schémas ASCII

### Variante A : Fenêtre de Taille Fixe ($k$)
La taille de la fenêtre (`right - left + 1`) reste toujours égale à $k$. À chaque pas vers la droite, on ajoute 1 élément et on en retire 1.

```text
Tableau : [ 2,  1,  5,  1,  3,  2 ]   (k = 3)

Étape 1 : [ 2,  1,  5 ] 1,  3,  2     -> Somme = 8
            L       R

Étape 2 :   2 [ 1,  5,  1 ] 3,  2     -> Somme = 8 - 2 (sortant) + 1 (entrant) = 7
                L       R

Étape 3 :   2,  1 [ 5,  1,  3 ] 2     -> Somme = 7 - 1 (sortant) + 3 (entrant) = 9 (Max !)
                    L       R
```

### Variante B : Fenêtre de Taille Variable (Dynamique)
La fenêtre grandit vers la droite (`right`) tant qu'une condition est respectée (ou jusqu'à ce qu'elle le soit), puis rétrécit depuis la gauche (`left`) pour rétablir la validité.

```text
Objectif : Plus petit sous-tableau avec somme >= 7
Tableau  : [ 2,  3,  1,  2,  4,  3 ]

1. On étend R : [ 2, 3, 1, 2 ] (Somme = 8 >= 7, taille = 4) -> Valide !
                  L        R

2. On réduit L :  2 [ 3, 1, 2 ] (Somme = 6 < 7) -> Invalide, on ré-étend R...
                      L     R
```

---

## 3. Mots-Clés et Déclencheurs dans les Énoncés

Repère ces indices pour identifier immédiatement le Sliding Window :

* **Sous-structures continues :** *"Subarray"* (sous-tableau contigu), *"Substring"* (sous-chaîne contiguë), *"Consecutive"* (consécutifs).
* **Taille fixée :** *"of size k"*, *"k consecutive elements"*, *"within distance k"*.
* **Optimisation :** *"Maximum sum"*, *"Minimum length"*, *"Longest substring without repeating characters"*, *"Maximum average"*.
* **Contraintes sur le contenu :** *"At most k distinct characters"*, *"Contains all characters"*.

> **Attention :** Si l'énoncé parle de *"Subsequence"* (sous-séquence non contiguë), ce n'est **pas** du Sliding Window (c'est généralement Two Pointers ou Dynamic Programming).
---

## ⚠️ Cas limites à vérifier
- **Taille de fenêtre $k$ supérieure à la taille du tableau (`k > len(nums)`) :** Toujours vérifier `if len(nums) < k: return 0` (ou `None`) avant d'initialiser la première fenêtre.
- **Aucun sous-tableau valide trouvé (fenêtre variable minimale) :** Si `min_len` est initialisé à `float("inf")`, penser à retourner `0` (et non `inf`) si aucune fenêtre n'a satisfait la condition.
- **Fenêtre de taille 1 (`k = 1`) :** S'assurer que l'ajout puis le retrait immédiat de l'élément ne corrompt pas l'état de la fenêtre.

## 🚫 Quand éviter ce pattern
- **Somme exacte $K$ en présence de nombres négatifs ou de zéros :** La fenêtre glissante repose sur la monotonie (agrandir = augmenter la somme, rétrécir = diminuer la somme). Avec des négatifs, cette règle casse : utiliser obligatoirement **Prefix Sum + Hashing**.
- **Sous-séquences non contiguës :** Sliding Window ne fonctionne que sur des éléments **adjacents** (*subarray* / *substring*). Si l'on peut sauter des éléments (*subsequence*), passer aux **Two Pointers**, **Greedy** ou à la **Programmation Dynamique (DP)**.
