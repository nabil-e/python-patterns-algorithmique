# Greedy (Glouton) — Plan d'Entraînement

## 1. Tes Exercices Prioritaires (à cocher)

### Série 1 : Glouton pur et simulation locale
* [ ] **605. Can Place Flowers** — Vérifier simplement si la case courante ainsi que ses deux voisines immédiates (gauche et droite) sont vides avant de planter.
* [ ] **860. Lemonade Change** — Suivre le stock de billets de 5 $ et 10 $ et toujours rendre la monnaie avec les plus grosses coupures disponibles en priorité (10 + 5 avant 5 + 5 + 5).
* [ ] **122. Best Time to Buy and Sell Stock II** — Additionner chaque hausse quotidienne positive entre le jour `i-1` et le jour `i` (`prices[i] - prices[i-1] > 0`).
* [ ] **169. Majority Element** — Appliquer l'algorithme de vote de Boyer-Moore en maintenant un candidat et un compteur en temps $O(n)$ et mémoire $O(1)$. *(Alternative possible : Hashing avec `Counter`).*

### Série 2 : Glouton avec Tri (Sorting)
* [ ] **455. Assign Cookies** — Trier les enfants et les biscuits par ordre croissant, puis satisfaire chaque enfant avec le plus petit biscuit suffisant. *(Pattern secondaire : Two Pointers).*
* [ ] **1710. Maximum Units on a Truck** — Trier les types de boîtes par nombre d'unités décroissant (`key=lambda x: x[1], reverse=True`) et charger le camion jusqu'à sa capacité maximale.

### Série 3 : Exercice Mixte (Hashing + Glouton)
* [ ] **409. Longest Palindrome** — Compter les fréquences de chaque lettre avec `Counter`, prendre toutes les paires paires (`freq // 2 * 2`), et ajouter `1` au centre s'il reste au moins un caractère impair. *(Pattern secondaire : Hashing).*

---

## 2. Entraînement Répétitif Complémentaire

### Niveau 1 : Consolidation des réflexes gloutons
* [ ] **1323. Maximum 69 Number** — Remplacer uniquement le tout premier `'6'` rencontré en partant de la gauche par un `'9'`.
* [ ] **1221. Split a String in Balanced Strings** — Maintenir un compteur d'équilibre (`+1` pour `'L'`, `-1` pour `'R'`) et incrémenter le résultat dès que l'équilibre atteint `0`.
* [ ] **942. DI String Match** — Attribuer le plus petit nombre disponible pour `'I'` et le plus grand disponible pour `'D'` à l'aide de deux pointeurs.

### Niveau 2 : Intervalles et Sauts (Préparation aux entretiens)
* [ ] **55. Jump Game** — Maintenir l'indice maximal atteignable à chaque étape et vérifier qu'on ne reste jamais bloqué avant la fin.
* [ ] **45. Jump Game II** — Compter le nombre minimum de sauts en délimitant la portée maximale de chaque palier.
* [ ] **134. Gas Station** — Vérifier que le bilan total d'essence est positif, puis réinitialiser le point de départ dès que le réservoir courant passe sous zéro.
