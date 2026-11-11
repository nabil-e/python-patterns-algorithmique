# Binary Search — Plan d'Entraînement

## 1. Tes Exercices Prioritaires

### Niveau 1 : Les Fondamentaux (Recherche & Frontière)
* **35. Search Insert Position** *(Ta liste)*
  * **Mécanique :** Recherche binaire classique. Si la cible est trouvée, retourne `mid`. Sinon, retourne `left` à la fin de la boucle (position d'insertion).
  * **Pattern secondaire :** Aucun.
* **278. First Bad Version** *(Ta liste)*
  * **Mécanique :** Recherche de frontière (`while left < right`). L'espace de recherche va de `1` à `n`. Si `isBadVersion(mid)` est vrai, la première mauvaise version est à `mid` ou avant (`right = mid`). Sinon, elle est après (`left = mid + 1`).
  * **Pattern secondaire :** Aucun.
* **374. Guess Number Higher or Lower** *(Ta liste)*
  * **Mécanique :** Recherche exacte sur l'intervalle `[1, n]`. Adapte simplement les branches `left = mid + 1` et `right = mid - 1` selon le retour de l'API `guess(mid)` (`1`, `-1` ou `0`).
  * **Pattern secondaire :** Aucun.

### Niveau 2 : Binary Search sur Espace de Réponse
* **69. Sqrt(x)** *(Ta liste)*
  * **Mécanique :** Au lieu de chercher dans un tableau, cherche un entier `mid` entre `1` et `x // 2` tel que `mid * mid <= x`. Retourne `right` à la fin de la boucle `while left <= right`.
  * **Pattern secondaire :** Mathématiques de base.

---

## 2. Entraînement Répétitif (Pour ancrer le pattern)

Fais ces exercices dans l'ordre pour maîtriser la gestion des bornes `left` et `right` :

### Série A — Recherche de Bornes et Exacte
1. **704. Binary Search** *(Facile)* — L'exercice de référence pur pour valider ton template exact sans aucune fioriture.
2. **744. Find Smallest Letter Greater Than Target** *(Facile)* — Variante de recherche de frontière avec gestion du bouclage circulaire (`left % len(letters)`).
3. **367. Valid Perfect Square** *(Facile)* — Quasi identique à `69. Sqrt(x)`, idéal pour répéter le Binary Search sur espace mathématique.

### Série B — Montée en Puissance (Entretiens fréquents)
4. **34. Find First and Last Position of Element in Sorted Array** *(Moyen)* — Oblige à exécuter deux recherches binaires (une pour la borne gauche, une pour la borne droite).
5. **153. Find Minimum in Rotated Sorted Array** *(Moyen)* — Apprend à adapter la condition monotone sur un tableau trié puis pivoté.
6. **875. Koko Eating Bananas** *(Moyen)* — Le grand classique du "Binary Search on Answer" : chercher une vitesse minimale `k` qui valide une contrainte de temps.
