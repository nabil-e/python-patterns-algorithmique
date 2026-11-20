# 07. Greedy (Algorithmes Gloutons)
> **Pattern 07 / 14** • **Temps :** `O(n)` ou `O(n log n)` • **Espace :** `O(1)`

---

## 1. Idée Centrale
Construire la solution étape par étape en choisissant systématiquement l'option qui semble la plus avantageuse **sur le moment**, sans jamais revenir en arrière. Cette approche s'applique uniquement lorsque le choix local optimal ne compromet pas les choix futurs.

---

## 2. Indices dans l'énoncé

| Indice dans l'énoncé | Mots-clés (Anglais) | Approche recommandée |
| :--- | :--- | :--- |
| Atteindre la fin d'un tableau ou minimiser le nombre de sauts | `jump game`, `minimum jumps`, `can reach end` | Suivi de la portée maximale (`max_reach`) |
| Maximiser des profits, des attributions ou satisfaire un max d'éléments | `assign cookies`, `max profit`, `maximize tasks` | Tri préalable + double pointeur glouton |
| Vérifier un trajet circulaire avec gains et coûts à chaque étape | `gas station`, `circular route`, `starting index` | Reset du point de départ dès que le cumul devient négatif |
| Construire le plus petit/grand nombre ou chaîne lexicographique | `smallest subsequence`, `remove k digits`, `lexicographical` | Pile monotone gloutonne (supprimer les plus grands à gauche) |

---

## 3. Variantes & Pièges Courants

### Variantes principales
* **Portée maximale (Reachability) :** Maintenir la frontière la plus lointaine atteignable (`max_reach = max(max_reach, i + nums[i])`) en un seul passage `O(n)`.
* **Tri + Appariement :** Trier les ressources et les demandes par ordre croissant pour associer la plus petite ressource suffisante à la plus petite demande.
* **Cumul avec réinitialisation :** Vérifier d'abord que la somme globale est valide (`sum(gain) >= sum(cost)`), puis réinitialiser l'index de départ dès que le réservoir local passe sous 0.

### Pièges à éviter
* **Confondre Greedy et Programmation Dynamique (DP) :** Si un choix local apparemment optimal bloque une meilleure combinaison globale (ex. rendre la monnaie avec des pièces `[1, 3, 4]` pour faire `6`), le Greedy échoue : utilisez la DP.
* **Oublier de tester un contre-exemple :** Avant de coder un algorithme glouton, testez toujours 2 ou 3 petits cas limites à la main pour vérifier que le choix local reste toujours sûr.
* **Oublier le tri initial :** Beaucoup de problèmes gloutons nécessitent d'ordonner les données en `O(n log n)` avant d'appliquer la règle de décision locale.

---

## 4. Squelettes de Code (Python)

### Variante 1 : Jump Game II (Nombre minimum de sauts en O(n))
```python
def min_jumps(nums: list[int]) -> int:
    jumps = 0
    current_end = 0   # Fin de la plage couverte par le saut actuel
    farthest = 0      # Point le plus loin atteignable depuis cette plage

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:      # On doit déclencher un nouveau saut
            jumps += 1
            current_end = farthest
            if current_end >= len(nums) - 1:
                break
    return jumps
```

### Variante 2 : Gas Station (Point de départ d'un circuit en O(n))
```python
def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1                 # Impossible globalement

    tank = 0
    start_index = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:              # Départ invalide : on repart de la station suivante
            start_index = i + 1
            tank = 0
    return start_index
```
