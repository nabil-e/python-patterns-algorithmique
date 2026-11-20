# 💻 Pattern 2 : Two Pointers — Code Typé, Astuces & Pièges

## 1. Templates Python Exécutables (Anglais Typé)

```python
# --- Template 1 : Pointeurs convergents (LeetCode 977 - Squares of a Sorted Array) ---
def sorted_squares(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    write_idx = n - 1

    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2
        if left_sq > right_sq:
            result[write_idx] = left_sq
            left += 1
        else:
            result[write_idx] = right_sq
            right -= 1
        write_idx -= 1

    return result


# --- Template 2 : Pointeurs lent et rapide en place (LeetCode 283 - Move Zeroes) ---
def move_zeroes(nums: list[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


# --- Template 3 : Deux séquences parallèles (LeetCode 392 - Is Subsequence) ---
def is_subsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


# --- Bac à sable : Stubs à compléter pour t'entraîner ---
def max_area(height: list[int]) -> int:
    # TODO: LeetCode 11 - Container With Most Water
    pass


if __name__ == "__main__":
    print("Carrés triés :", sorted_squares([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
    arr = [0, 1, 0, 3, 12]
    move_zeroes(arr)
    print("Zéros déplacés :", arr)  # [1, 3, 12, 0, 0]
    print("Sous-séquence :", is_subsequence("abc", "ahbgdc"))  # True
```

---

## 2. Trucs et Astuces Python
- **Parcours de la fin vers le début :** Lorsqu'on fusionne deux tableaux triés en place (ex. : LeetCode 88) ou qu'on remplit des carrés triés (LeetCode 977), partir de `write_idx = n - 1` évite d'écraser des valeurs non lues.
- **Échange en place sans variable temporaire :** `nums[slow], nums[fast] = nums[fast], nums[slow]` est atomique, lisible et idiomatique en Python.
- **Sauter les doublons après un tri (ex. : 3Sum) :** Utilise `while left < right and nums[left] == nums[left - 1]: left += 1` pour éviter les triplets identiques en O(1) espace.

---

## 3. Pièges à éviter
- **Condition `left < right` vs `left <= right` :** Utilise `left < right` quand tu compares une **paire** de deux éléments distincts (ex. : Two Sum trié). Utilise `left <= right` quand l'élément central doit aussi être traité individuellement (ex. : carré du nombre central).
- **Oublier de trier avant d'appliquer Two Pointers :** Les pointeurs convergents ne fonctionnent que si le tableau possède une propriété de monotonie (trié). Vérifie si l'énoncé demande les valeurs (tri autorisé) ou les **index d'origine** (tri interdit -> utilise Hashing).
