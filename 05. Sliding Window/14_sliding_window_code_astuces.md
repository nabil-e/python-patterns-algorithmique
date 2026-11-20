# 💻 Pattern 5 : Sliding Window — Squelettes, Code & Astuces

## 1. Squelettes Génériques (Boilerplates)

### Squelette A : Fenêtre de taille fixe `k`
```python
def sliding_window_fixed_skeleton(nums: list[int], k: int) -> float:
    window_sum: int = 0
    best: float = float("-inf")

    for right in range(len(nums)):
        window_sum += nums[right]  # 1. Entrée à droite

        if right >= k - 1:         # 2. Taille k atteinte
            best = max(best, window_sum)
            window_sum -= nums[right - k + 1]  # 3. Sortie à gauche

    return best
```

### Squelette B : Fenêtre de taille variable (dynamique)
```python
from collections import defaultdict

def sliding_window_variable_skeleton(s: str) -> int:
    counts: dict[str, int] = defaultdict(int)
    left: int = 0
    max_len: int = 0

    for right in range(len(s)):
        counts[s[right]] += 1  # 1. Agrandir par la droite

        while len(counts) > 2:  # 2. Rétrécir tant que la condition est violée
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)  # 3. Mettre à jour le record

    return max_len
```

---

## 2. Démos Exécutables (`main.py` — Section 1)

Code typé en anglais avec commentaires en français, prêt à être copié-collé et exécuté localement :

```python
from collections import defaultdict

# --- 1. DÉMOS DU PATTERN (Exécutables) ---

def find_max_average(nums: list[int], k: int) -> float:
    """LeetCode 643 : Moyenne maximale d'un sous-tableau contigu de taille k."""
    current_sum: int = sum(nums[:k])
    max_sum: int = current_sum

    for right in range(k, len(nums)):
        # On ajoute le nouvel élément entrant et on retire l'élément sortant à gauche
        current_sum += nums[right] - nums[right - k]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum / k


def count_good_substrings(s: str) -> int:
    """LeetCode 1876 : Sous-chaînes de taille 3 avec 3 caractères distincts."""
    counts: dict[str, int] = defaultdict(int)
    good_count: int = 0

    for right, char in enumerate(s):
        counts[char] += 1

        if right >= 3:
            left_char: str = s[right - 3]
            counts[left_char] -= 1
            if counts[left_char] == 0:
                del counts[left_char]

        # À partir de l'index 2, la fenêtre contient exactement 3 caractères
        if right >= 2 and len(counts) == 3:
            good_count += 1

    return good_count


def length_of_longest_substring(s: str) -> int:
    """LeetCode 3 : Plus longue sous-chaîne sans caractère répété (fenêtre variable)."""
    seen: set[str] = set()
    left: int = 0
    max_length: int = 0

    for right, char in enumerate(s):
        # Tant que le caractère entrant est déjà présent, on rétrécit par la gauche
        while char in seen:
            seen.remove(s[left])
            left += 1

        seen.add(char)
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    print("643. Max Average :", find_max_average([1, 12, -5, -6, 50, 3], 4))  # 12.75
    print("1876. Good Substrings :", count_good_substrings("xyzzaz"))  # 1
    print("3. Longest Substring :", length_of_longest_substring("abcabcbb"))  # 3
```

---

## 3. Bac à Sable Exercices (`main.py` — Section 2)

```python
# --- 2. BAC À SABLE EXERCICES (À compléter) ---

def minimum_recolors(blocks: str, k: int) -> int:
    """LeetCode 2379 : Minimum Recolors to Get K Consecutive Black Blocks."""
    # TODO : Compter les 'W' dans une fenêtre glissante de taille fixe k
    pass


if __name__ == "__main__":
    # Décommente pour tester ton code :
    # assert minimum_recolors("WBBWWBBWBW", 7) == 3
    pass
```

---

## 4. Trucs et Astuces Python
- **Formule de longueur de fenêtre :** Entre `left` et `right` inclus, il y a toujours `right - left + 1` éléments.
- **Nettoyage des clés à zéro :** Quand tu utilises `defaultdict(int)` ou `Counter` pour compter les éléments distincts dans la fenêtre via `len(counts)`, n'oublie jamais de faire `del counts[left_char]` dès que son compteur tombe à `0`.
- **Optimisation par saut d'index :** Pour LeetCode 3, stocker le dernier index vu dans un `dict[str, int]` permet de faire `left = max(left, last_seen[char] + 1)` en $O(1)$ au lieu d'une boucle `while`.

---

## 5. Pièges à éviter
- **Utiliser Sliding Window variable avec des nombres négatifs :** Si la condition porte sur une somme cible et que le tableau contient des négatifs, agrandir la fenêtre ne garantit plus d'augmenter la somme. Utilise **Prefix Sum + Hashing** à la place.
- **Décalage d'index de sortie (`right - k` vs `right - k + 1`) :**
  - Si tu mets à jour le résultat **avant** de retirer l'élément sortant : l'élément qui sort est à `right - k + 1`.
  - Si tu retires l'élément sortant **avant** d'évaluer la fenêtre courante (comme dans `count_good_substrings` ci-dessus) : l'élément qui sort est à `right - k`.
