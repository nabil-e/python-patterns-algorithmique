# A. Pointeurs convergents (Gauche / Droite sur tableau trié)
# Idéal pour trouver une paire, inverser un tableau ou comparer des extrémités en O(n) temps et O(1) espace.
def carres_tries(nums: list[int]) -> list[int]:
    n = len(nums)
    resultat = [0] * n
    gauche, droite = 0, n - 1
    
    # On remplit le tableau résultat de la fin vers le début (du plus grand carré au plus petit)
    for pos in range(n - 1, -1, -1):
        if abs(nums[gauche]) > abs(nums[droite]):
            resultat[pos] = nums[gauche] ** 2
            gauche += 1
        else:
            resultat[pos] = nums[droite] ** 2
            droite -= 1
            
    return resultat

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    entree = [-7, -3, 2, 3, 11]
    sortie = carres_tries(entree)
    print(f"Entrée : {entree}")
    print(f"Carrés triés : {sortie}")
    # Sortie attendue : [4, 9, 9, 49, 121]

# B. Pointeurs Lent / Rapide (Modification sur place / In-place)
# Le pointeur rapide explore le tableau tandis que lent marque la position où écrire le prochain élément valide.
def deplacer_zeros(nums: list[int]) -> None:
    lent = 0  # Position du prochain élément non nul
    
    for rapide in range(len(nums)):
        if nums[rapide] != 0:
            # Échange les éléments
            nums[lent], nums[rapide] = nums[rapide], nums[lent]
            lent += 1

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    tableau = [0, 1, 0, 3, 12]
    print(f"Avant : {tableau}")
    deplacer_zeros(tableau)
    print(f"Après : {tableau}")
    # Sortie attendue : [1, 3, 12, 0, 0]

# C. Deux séquences en parallèle (Sous-séquence ou fusion)
# Chaque tableau possède son propre pointeur qui avance selon une condition précise.
def est_sous_sequence(s: str, t: str) -> bool:
    i, j = 0, 0  # i pour s (la cible), j pour t (le texte complet)
    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
        
    return i == len(s)

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    s1, t1 = "abc", "ahbgdc"
    s2, t2 = "axc", "ahbgdc"
    print(f"'{s1}' dans '{t1}' ? -> {est_sous_sequence(s1, t1)}")
    print(f"'{s2}' dans '{t2}' ? -> {est_sous_sequence(s2, t2)}")
    # Sortie attendue : True, puis False

# EXERCICES

# 392. Is Subsequence
def isSubsequence(s: str, t: str) -> bool:
    p1 = p2 = 0
    while p1 < len(s) and p2 < len(t):
        if s[p1] == t[p2]:
            p1 += 1
        p2 += 1
    return p1 == len(s)

# 283. Move Zeroes
def moveZeroes(nums: list[int]) -> list[int]:
    num_0 = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[num_0], nums[i] = nums[i], nums[num_0]
            num_0 += 1
    return nums

# 977. Squares of a Sorted Array
def sortedSquares(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [0] * n
    left, right = 0, n - 1

    for pos in range(n-1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            res[pos] = nums[left] ** 2
            left += 1
        else:
            res[pos] = nums[right] ** 2
            right -= 1
    return res

# 88. Merge Sorted Array
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    r1 = m -1
    r2 = n -1
    w = m + n -1
    while r2 >= 0:
        if r1 >= 0 and nums1[r1] > nums2[r2]:
            nums1[w] = nums1[r1]
            r1 -= 1
        else:
            nums1[w] = nums2[r2]
            r2 -= 1
        w -= 1

# 125. Valid Palindrome
def isPalindrome(s: str) -> bool:
    s = [x.lower() for x in s if x.isalnum()]
    return s == s[::-1]

# 344. Reverse String
def reverseString(s: list[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

# 167. Two Sum II - Input Array Is Sorted
def twoSum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left+1, right+1]
        elif numbers[left] + numbers[right] > target:
            right -= 1
        elif numbers[left] + numbers[right] < target:
            left += 1

# 11. Container With Most Water
def maxArea(height: list[int]) -> int:
    max_area = 0
    left, right = 0, len(height) - 1
    while left < right:
        width = right - left
        min_height = min(height[left], height[right])
        max_area = max(max_area, min_height * width)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

# 26. Remove Duplicates from Sorted Array
def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    lent = 1
    for num in range(1, len(nums)):
        if nums[num] != nums[num - 1]:
            nums[lent] = nums[num]
            lent += 1
    return lent

# 27. Remove Element
def removeElement(self, nums: list[int], val: int) -> int:
    write = 0
    for num in nums:
        if num != val:
            nums[write] = num
            write += 1
    return write