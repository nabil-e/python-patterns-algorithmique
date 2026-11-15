# 07. Greedy (Algorithmes Gloutons)

## 💡 Idée Centrale
Faire à chaque étape le choix qui semble **localement optimal** sur le moment, dans l'espoir qu'il mène à l'**optimum global**, sans jamais revenir en arrière (contrairement au Backtracking ou à la Programmation Dynamique).

* **Complexité Temporelle :** Souvent $O(n)$ ou $O(n \log n)$ (si un tri préalable est nécessaire)
* **Complexité Spatiale :** $O(1)$ (la grande force du Greedy)

---

## 🔍 Indices dans l'énoncé & Mots-clés
| Ce que dit l'énoncé | Mots-clés anglais fréquents |
| :--- | :--- |
| Trouver le minimum ou maximum d'étapes, de sauts, ou de ressources pour atteindre un objectif. | *minimum jumps*, *can reach the end*, *assign cookies*, *gas station* |
| Construire la chaîne la plus grande/petite possible selon l'ordre alphabétique. | *lexicographically smallest*, *largest number*, *remove k digits* |
| Maximiser un profit en achetant/vendant à volonté ou en choisissant les meilleures options. | *maximum profit*, *best time to buy and sell*, *activity selection* |
| Le problème ressemble à de la DP, mais les choix passés n'influencent pas les contraintes futures. | *greedy choice*, *optimal substructure*, *without looking back* |

---

## 🧩 Variantes Principales

### 1. Suivi de portée / Frontière (Jump Game)
Maintenir une variable `max_reach` (l'indice maximal atteignable). À chaque pas `i`, si `i > max_reach`, on est bloqué. Sinon, on met à jour `max_reach = max(max_reach, i + nums[i])`.

### 2. Tri préalable + Sélection gloutonne
Trier les éléments (ex: enfants par gourmandise et biscuits par taille) puis associer le plus petit biscuit suffisant au plus petit enfant.

### 3. Accumulation locale (Kadane / Gas Station)
Accumuler un gain ou un solde tant qu'il reste positif. Dès qu'il devient négatif, le réinitialiser à zéro et repartir de l'indice suivant.

---

## ⚠️ Pièges à éviter
* **Confondre Greedy et Programmation Dynamique (DP) :** Exemple classique du rendu de monnaie (*Coin Change*). Avec des pièces `[1, 3, 4]` pour faire `6`, le Greedy prend `4 + 1 + 1` (3 pièces), alors que l'optimal est `3 + 3` (2 pièces). Testez toujours un contre-exemple avant de valider une approche Greedy.

---

## 💻 Squelettes de Code (Python)

### Variante A : Frontière maximale (Jump Game)
```python
def can_jump(nums: list[int]) -> bool:
    max_reach = 0

    for i, jump in enumerate(nums):
        # Si l'indice actuel dépasse la portée maximale atteignable
        if i > max_reach:
            return False
        # Mettre à jour la nouvelle portée maximale
        max_reach = max(max_reach, i + jump)
        
        if max_reach >= len(nums) - 1:
            return True

    return True
```

### Variante B : Réinitialisation sur solde négatif (Algorithme de Kadane)
```python
def max_subarray(nums: list[int]) -> int:
    max_sum = nums[0]
    curr_sum = 0

    for num in nums:
        # Si la somme accumulée devient un fardeau (< 0), on repart à zéro
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += num
        max_sum = max(max_sum, curr_sum)

    return max_sum
```
