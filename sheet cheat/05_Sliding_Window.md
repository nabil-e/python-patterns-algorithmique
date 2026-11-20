# 05. Sliding Window (Fenêtre Glissante)

> **Complexité visée :** Temps $O(n)$ (chaque élément entre et sort au plus une fois) | Espace $O(1)$ ou $O(k)$

---

## 1. Idée Centrale
Maintenir une sous-section contiguë délimitée par deux pointeurs `[left, right]`. Plutôt que de recalculer la somme ou les fréquences depuis zéro à chaque décalage, on **ajoute l'élément entrant à droite** et on **retire l'élément sortant à gauche** en temps constant.

---

## 2. Indices dans l'énoncé & Mots-clés (LeetCode)

| Indice dans l'énoncé | Mots-clés (Anglais) | Approche / Variante |
| :--- | :--- | :--- |
| Sous-tableau ou sous-chaîne contiguë de longueur fixe $K$ | `subarray of size k`, `fixed window`, `average` | **Fenêtre Fixe** |
| Plus longue sous-chaîne sans doublons ou avec au plus $K$ caractères distincts | `longest substring`, `without repeating`, `at most k` | **Fenêtre Dynamique (Max)** |
| Plus court sous-tableau dont la somme est $\ge S$ (nombres positifs) | `shortest subarray`, `minimum window`, `sum >= target` | **Fenêtre Dynamique (Min)** |
| Trouver tous les anagrammes ou permutations d'un motif dans un texte | `find all anagrams`, `permutation in string` | **Fenêtre Fixe + Fréquences** |

---

## 3. Variantes & Pièges Courants

### Variantes Clés
* **Fenêtre de Taille Fixe :** Dès que `right - left + 1 == k`, on met à jour le résultat puis on fait glisser `left += 1` simultanément à `right`.
* **Fenêtre Dynamique (Variable) :** `right` avance toujours pour agrandir la fenêtre ; une boucle interne `while` rétrécit `left` tant que la fenêtre est invalide (pour maximiser) ou tant qu'elle reste valide (pour minimiser).

### Pièges à Éviter
* **Nombres négatifs avec somme cible :** Si le tableau contient des nombres négatifs, agrandir la fenêtre ne fait pas toujours augmenter la somme ! Dans ce cas, abandonnez la fenêtre glissante au profit de **Prefix Sum + Hash Map**.
* **Oublier de nettoyer le dictionnaire :** Lorsqu'un caractère sort à gauche (`count[s[left]] -= 1`), pensez à supprimer sa clé (`del count[s[left]]`) si son compteur tombe à `0` lorsque vous testez `len(count) > k`.

---

## 4. Squelettes Python

### Variante A : Fenêtre Dynamique Maximale (Au plus K distincts)
```python
from collections import defaultdict

def longest_subarray_at_most_k(nums: list[int], k: int) -> int:
    counts: dict[int, int] = defaultdict(int)
    left = 0
    max_len = 0

    for right, num in enumerate(nums):
        counts[num] += 1  # 1. Entrée à droite

        while len(counts) > k:  # 2. Rétrécir tant qu'invalide
            left_num = nums[left]
            counts[left_num] -= 1
            if counts[left_num] == 0:
                del counts[left_num]
            left += 1

        max_len = max(max_len, right - left + 1)  # 3. Mise à jour

    return max_len
```

### Variante B : Fenêtre Dynamique Minimale (Somme >= Target, positifs)
```python
def min_subarray_len(target: int, nums: list[int]) -> int:
    left = 0
    window_sum = 0
    min_len = float("inf")

    for right, num in enumerate(nums):
        window_sum += num

        while window_sum >= target:  # Rétrécir tant que valide
            min_len = min(min_len, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return 0 if min_len == float("inf") else int(min_len)
```
