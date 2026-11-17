# Sliding Window — Plan d'Entraînement & Note Hors-Pattern

## 1. Tes Exercices Prioritaires

### Niveau 1 : Fenêtre de Taille Fixe (Mécanique pure)
* **643. Maximum Average Subarray I** *(Ta liste)*
  * **Mécanique :** Applique directement le Template A (fenêtre fixe de taille `k`). Calcule la somme des `k` premiers éléments, glisse jusqu'à `len(nums)`, puis retourne `max_sum / k`.
  * **Pattern secondaire :** Aucun.
* **1876. Substrings of Size Three with Distinct Characters** *(Ta liste)*
  * **Mécanique :** Fenêtre fixe de taille `3`. Pour chaque position `i` de `0` à `len(s) - 3`, vérifie si `len(set(s[i:i+3])) == 3` (ou compare simplement `s[i] != s[i+1] != s[i+2] != s[i]`).
  * **Pattern secondaire :** Hashing (`set`) sur une micro-fenêtre.
* **2379. Minimum Recolors to Get K Consecutive Black Blocks** *(Ta liste)*
  * **Mécanique :** Fenêtre fixe de taille `k`. Compte le nombre de blocs blancs `'W'` dans la fenêtre initiale. Fais glisser la fenêtre : incrémente si `'W'` entre, décrémente si `'W'` sort, et garde le minimum de `'W'` observé.
  * **Pattern secondaire :** Aucun.

### Niveau 2 : Fenêtre Fixe + Hashing
* **219. Contains Duplicate II** *(Ta liste — déjà vu dans Hashing)*
  * **Mécanique :** Maintiens un `set` représentant une fenêtre glissante de taille maximale `k`. Si `nums[right]` est déjà dans le `set`, retourne `True`. Si `len(window) > k`, supprime `nums[right - k]`.
  * **Pattern secondaire :** Hashing (`set`).

---

## 2. Note Spéciale sur l'Exercice 14 de ta liste

* **14. Longest Common Prefix** *(Ta liste)*
  * **Diagnostic :** Cet exercice **n'appartient à aucun des 5 patterns** de ta liste (ni Hashing, ni Two Pointers, ni Stack, ni Binary Search, ni Sliding Window). Il relève de la **manipulation de chaînes / balayage vertical (String Scanning)**.
  * **Comment le résoudre efficacement en Python :**
    * **Approche idiomatique (Tri) :** Trie la liste `strs.sort()`. Le préfixe commun à tous les mots est forcément le préfixe commun entre le **premier** mot (`strs[0]`) et le **dernier** mot (`strs[-1]`) après tri alphabétique. Compare-les caractère par caractère en $O(n \log n)$.
    * **Approche optimale (Balayage vertical) :** Parcours les caractères du premier mot `strs[0]` à l'index `i` et vérifie que tous les autres mots ont le même caractère à l'index `i` en $O(S)$ où $S$ est la somme des caractères.

---

## 3. Entraînement Répétitif (Pour ancrer le pattern)

Fais ces exercices dans l'ordre pour passer de la fenêtre fixe à la fenêtre variable :

### Série A — Maîtriser la Fenêtre Fixe
1. **1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold** *(Moyen)* — Très proche de `643`, consolide le glissement de somme fixe.
2. **1456. Maximum Number of Vowels in a Substring of Given Length** *(Moyen)* — Identique à `2379` dans sa logique de comptage entrant/sortant.

### Série B — Maîtriser la Fenêtre Variable (Indispensable en entretien)
3. **3. Longest Substring Without Repeating Characters** *(Moyen)* — Le problème LeetCode le plus célèbre sur le Sliding Window variable combiné à un `set` ou `dict`.
4. **1004. Max Consecutive Ones III** *(Moyen)* — Apprend à gérer un budget d'erreurs (`k` zéros autorisés) dans une fenêtre dynamique.
5. **209. Minimum Size Subarray Sum** *(Moyen)* — Le classique pour apprendre à rétrécir la fenêtre avec une boucle `while` afin de trouver une longueur minimale.
