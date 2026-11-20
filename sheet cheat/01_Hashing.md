# 01. HASHING (DICT / SET / COUNTER)
*Échanger de l'espace O(n) contre une recherche instantanée O(1)*

- **Complexité :** `Temps: O(n) | Espace: O(n)`

---

## 1. IDÉE CENTRALE
Mémoriser les éléments déjà vus, leurs index ou leurs fréquences dans une table de hachage (`dict`, `set`, `Counter`) afin d'éliminer les boucles imbriquées O(n²) lors de la recherche de compléments ou de doublons.

---

## 2. INDICES DANS L'ÉNONCÉ
| Indice dans l'énoncé | Mots-clés (Anglais) | Approche recommandée |
| :--- | :--- | :--- |
| Vérifier la présence de doublons ou éléments uniques | `duplicates, distinct, unique, contains` | **set** |
| Trouver une paire dont la somme vaut une cible | `two sum, pair sum, complement, target` | **dict {val: index}** |
| Compter les occurrences ou vérifier des anagrammes | `frequency, anagram, majority, count` | **Counter / defaultdict(int)** |
| Regrouper des éléments selon une signature commune | `group anagrams, isomorphic, pattern` | **defaultdict(list)** |

---

## 3. VARIANTES & PIÈGES COURANTS
### Variantes principales
- **Set de présence :** Détection de doublons ou vérification d'appartenance en O(1) moyen.
- **Map Valeur → Index :** Retrouver la position exacte d'un complément (*Two Sum*).
- **Compteur de fréquences :** `collections.Counter` pour comparer deux distributions.

### Pièges à éviter
- **Clé mutable :** Une `list` ne peut pas être clé de dictionnaire ; convertir en `tuple(list)`.
- **Ordre non garanti sur d'anciennes versions :** Ne pas supposer un tri automatique ; utiliser `sorted()` si nécessaire.
- **Collision / pire cas :** O(1) en moyenne, mais O(n) théorique en cas de collisions massives.

---

## 4. SQUELETTES PYTHON (TYPÉS)

### Variante A : Recherche de complément (Valeur → Index)
```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}  # {valeur: index}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Variante B : Regroupement par signature (defaultdict)
```python
from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for word in strs:
        signature = tuple(sorted(word))  # Clé immuable hachable
        groups[signature].append(word)
    return list(groups.values())
```
