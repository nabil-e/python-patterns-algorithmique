# 💻 Pattern 1 : Hashing — Code Typé, Astuces & Pièges

## 1. Templates Python Exécutables (Anglais Typé)

```python
from collections import Counter, defaultdict


# --- Template 1 : Recherche de complément en O(1) (LeetCode 1 - Two Sum) ---
def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], idx]
        seen[num] = idx
    return []


# --- Template 2 : Comptage de fréquences avec Counter (LeetCode 387) ---
def first_unique_char(s: str) -> int:
    counts = Counter(s)
    for idx, char in enumerate(s):
        if counts[char] == 1:
            return idx
    return -1


# --- Template 3 : Regroupement par signature canonique (LeetCode 49) ---
def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for word in strs:
        signature = tuple(sorted(word))
        groups[signature].append(word)
    return list(groups.values())


# --- Bac à sable : Stubs à compléter pour t'entraîner ---
def is_pangram(sentence: str) -> bool:
    # TODO: LeetCode 1832 - Utilise un set()
    pass


if __name__ == "__main__":
    print("Two Sum :", two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print("Premier unique :", first_unique_char("leetcode"))  # 0
    print("Anagrammes :", group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
```

---

## 2. Trucs et Astuces (Bibliothèque Standard)
- **`collections.Counter(iterable)` :** Compte instantanément les occurrences en C en O(n). Permet aussi de soustraire deux compteurs (`c1 - c2`).
- **`collections.defaultdict(list)` ou `defaultdict(int)` :** Évite d'écrire `if key not in d: d[key] = []` avant chaque ajout.
- **Clés immuables uniquement :** Une `list` n'est pas hachable (`TypeError: unhashable type: 'list'`). Convertis toujours une liste en `tuple` avant de l'utiliser comme clé d'un `dict` ou d'un `set`.
- **Conversion en `set` pour le lookup O(1) :** Tester `x in my_list` prend $O(n)$, alors que `x in my_set` prend $O(1)$.

---

## 3. Pièges à éviter
- **Modifier un `dict` ou `set` pendant son itération :** Itérer sur `for k in my_dict:` tout en faisant `del my_dict[k]` lève une `RuntimeError`. Itère sur `list(my_dict.keys())` si tu dois supprimer des clés à la volée.
- **Utiliser le même élément deux fois dans Two Sum :** Insère `seen[num] = idx` **après** avoir vérifié `if complement in seen:`, sinon `target = 6` avec `num = 3` matcherait l'élément avec lui-même.
