# 18. Prefix & Suffix Sum — Plan d'Entraînement

Coche chaque case `[x]` au fur et à mesure de ta progression.

## 1. Tes Exercices Prioritaires (Maîtrise des bases et variantes)
- [ ] **1480. Running Sum of 1d Array** *(Easy)* — Application directe de `itertools.accumulate` ou d'une somme cumulée en place.
- [ ] **1732. Find the Highest Altitude** *(Easy)* — Calculer la somme préfixe à la volée et suivre le maximum rencontré (en partant de `0`).
- [ ] **303. Range Sum Query - Immutable** *(Easy)* — Implémentation exacte du **Template A** (`prefix[right + 1] - prefix[left]`).
- [ ] **1413. Minimum Value to Get Positive Step by Step Sum** *(Easy)* — Trouver la somme préfixe minimale `min_pref` ; la réponse vaut `max(1, 1 - min_pref)`.
- [ ] **2574. Left and Right Sum Differences** *(Easy)* — Utiliser le tableau préfixe pour déduire en $O(1)$ la somme à gauche et la somme à droite de chaque index.
- [ ] **238. Product of Array Except Self** *(Medium)* — Application exacte du **Template B** (passe préfixe puis passe suffixe en espace $O(1)$).
- [ ] **560. Subarray Sum Equals K** *(Medium)* — **Exercice Mixte (Prefix Sum + Hashing)** : application directe du **Template C** avec `defaultdict(int)`.

## 2. Entraînement Répétitif (Consolidation)
* **Série A — Équilibre et Plages :**
  - [ ] **724. Find Pivot Index** *(Easy)* — Trouver l'index où `left_sum == total_sum - left_sum - nums[i]`.
  - [ ] **1991. Find the Middle Index in Array** *(Easy)* — Variante directe du 724 pour ancrer le réflexe.
  - [ ] **2485. Find the Pivot Integer** *(Easy)* — Équilibre entre somme de `1..x` et `x..n`.
* **Série B — Prefix Sum + Hashing (Niveau Entretien) :**
  - [ ] **525. Contiguous Array** *(Medium)* — Remplacer les `0` par `-1` et chercher le plus long sous-tableau de somme `0` avec un dictionnaire d'indices.
  - [ ] **974. Subarray Sums Divisible by K** *(Medium)* — Stocker les restes `somme_courante % k` dans un `defaultdict(int)`.
