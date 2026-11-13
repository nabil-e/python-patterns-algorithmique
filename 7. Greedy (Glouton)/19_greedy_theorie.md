# 19. Greedy (Algorithmes Gloutons) — Théorie et Mécanique

## 1. Principe Fondamental
Un algorithme **Greedy** (glouton) construit une solution étape par étape en prenant à chaque instant **le choix qui semble le meilleur localement** (le plus grand, le plus petit, le plus tôt), sans jamais revenir en arrière ni explorer toutes les combinaisons possibles.

Contrairement à la Programmation Dynamique (DP), le glouton ne sauvegarde pas d'états passés : il fait confiance à une règle de décision immédiate.

### Schéma Visuel : Stratégie Gloutonne après Tri
```
Problème : Satisfaire un maximum d'enfants avec des biscuits de tailles données.
Enfants (appétit)   : [ 1, 2, 3 ]  (trié)
Biscuits (tailles)  : [ 1, 1 ]     (trié)

Étape 1 : Enfant 0 (appétit 1) <--- Biscuit 0 (taille 1) -> Satisfait ! (Choix minimal suffisant)
Étape 2 : Enfant 1 (appétit 2) <--- Biscuit 1 (taille 1) -> Trop petit, on jette le biscuit.
Plus de biscuits -> Fin. Total = 1.
```

## 2. Mots-Clés et Déclencheurs dans les Énoncés
Repère ces indices dans les énoncés :
* **"Maximum / Minimum de..."** (`maximum units`, `minimum coins`, `maximum profit`, `assign maximum`).
* **"Stratégie optimale locale évidente"** (donner le plus petit biscuit suffisant, prendre les boîtes avec le plus d'unités par boîte, rendre la monnaie avec les plus gros billets).
* **"Transactions illimitées / Choix indépendants"** (`buy and sell stock II` où chaque hausse consécutive est prise).
* **"Placement sans chevauchement"** (`can place flowers`, `jump game`).

## 3. Quand l'utiliser ?
* **Recommandé :** Quand un **tri préalable** (`sort`) permet d'ordonner les éléments du meilleur au pire candidat, ou quand prendre le gain immédiat ne bloque jamais une meilleure solution future.
* **À éviter :** Quand un choix localement attrayant pénalise fortement la suite (ex: rendu de monnaie avec des pièces `[1, 3, 4]` pour faire `6` : le glouton prend `4 + 1 + 1` (3 pièces) alors que l'optimal est `3 + 3` (2 pièces) -> ici il faut de la Programmation Dynamique).

## 4. Complexité
* **Temps :** Souvent **$O(n \log n)$** lorsqu'un tri initial est nécessaire, ou **$O(n)$** si les données sont déjà ordonnées ou traitées en une passe.
* **Espace :** **$O(1)$** (hors espace utilisé par le tri de Python).
