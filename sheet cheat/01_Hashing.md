# 01. Hashing (Tables de hachage & Ensembles)

## 💡 Idée Centrale
Utiliser une table de hachage (`dict` en Python) ou un ensemble (`set`) pour stocker des éléments déjà vus afin de vérifier leur existence ou leur fréquence en temps constant **$O(1)$**, échangeant un peu de mémoire contre un gain de vitesse massif.

* **Complexité temporelle :** $O(n)$ en moyenne (au lieu de $O(n^2)$ avec des boucles imbriquées).
* **Complexité spatiale :** $O(n)$ pour stocker les clés/valeurs.

---

## 🔍 Indices dans l'énoncé & Mots-clés

| Ce que demande l'énoncé | Mots-clés en anglais | Structure à choisir |
| :--- | :--- | :--- |
| Vérifier si un élément existe déjà ou éliminer les doublons. | *contains duplicate*, *unique elements*, *first repeating* | `set()` |
| Trouver deux éléments qui forment une somme ou une différence cible. | *two sum*, *pair with given sum*, *complement* | `dict` (`valeur: index`) |
| Compter le nombre d'occurrences ou comparer deux chaînes/tableaux. | *frequency*, *anagram*, *majority element*, *count* | `dict` ou `collections.Counter` |
| Regrouper des éléments partageant une caractéristique commune. | *group anagrams*, *categorize*, *isomorphic* | `collections.defaultdict(list)` |

---

## 🛠️ Variantes Principales

1. **Le Set de présence (`seen = set()`) :** Idéal pour détecter un doublon ou un cycle en un seul passage.
2. **La Hash Map de recherche (`seen = {val: idx}`) :** On cherche le complément (`target - num`) dans le dictionnaire avant d'y insérer l'élément actuel.
3. **La Map de fréquences (`Counter`) :** On compte les occurrences de chaque caractère/nombre pour comparer deux collections.

---

## 💻 Squelette de Code (Python)

```python
from collections import Counter, defaultdict

# Variante 1 : Recherche de complément (type Two Sum)
def hash_lookup(nums, target):
    seen = {}  # Stocke {valeur: index}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Variante 2 : Comptage de fréquences & Regroupement
def hash_grouping(items):
    groups = defaultdict(list)
    for item in items:
        # Créer une clé immuable (ex: tuple trié pour les anagrammes)
        key = tuple(sorted(item))
        groups[key].append(item)
    return list(groups.values())
```
