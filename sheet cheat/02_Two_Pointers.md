# 02. TWO POINTERS (DEUX POINTEURS)
*Parcourir ou partitionner linéairement sans mémoire supplémentaire*

- **Complexité :** `Temps: O(n) | Espace: O(1)`

---

## 1. IDÉE CENTRALE
Utiliser deux indices qui évoluent selon une règle logique (convergents depuis les extrémités, ou lent/rapide dans le même sens) pour réduire une recherche quadratique O(n²) en un seul passage O(n) sur place.

---

## 2. INDICES DANS L'ÉNONCÉ
| Indice dans l'énoncé | Mots-clés (Anglais) | Approche recommandée |
| :--- | :--- | :--- |
| Tableau trié + chercher une paire ou un triplet | `sorted array, pair sum, 3sum, closest` | **Opposés (left, right)** |
| Vérifier une symétrie sur une chaîne ou un tableau | `palindrome, reverse, symmetric` | **Opposés (left, right)** |
| Modifier un tableau sur place sans copie | `in-place, O(1) extra space, remove duplicates` | **Lent / Rapide (slow, fast)** |
| Fusionner deux tableaux triés avec espace libre à droite | `merge sorted, non-decreasing order` | **Parcours inversé (fin → début)** |

---

## 3. VARIANTES & PIÈGES COURANTS
### Variantes principales
- **Pointeurs opposés :** `left = 0`, `right = n - 1` ; avancent l'un vers l'autre sur donnée triée.
- **Lent / Rapide (Lecture/Écriture) :** `fast` explore, `slow` écrit les éléments valides sur place.
- **3 Pointeurs :** 1 index fixe (boucle `for`) + 2 pointeurs opposés (*3Sum*) ou partition en 3 zones.

### Pièges à éviter
- **Oublier de trier :** Les pointeurs opposés sur sommes exigent un tableau trié au préalable.
- **Boucle infinie :** Toujours garantir qu'au moins un pointeur bouge à chaque itération (`left += 1` ou `right -= 1`).
- **Doublons dans 3Sum :** Sauter les valeurs identiques consécutives après avoir trouvé un triplet valide.

---

## 4. SQUELETTES PYTHON (TYPÉS)

### Variante A : Pointeurs opposés (Tableau trié)
```python
def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

### Variante B : Lent / Rapide (Déplacement sur place)
```python
def move_zeroes(nums: list[int]) -> None:
    slow = 0  # Position d'écriture du prochain élément non nul
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```
