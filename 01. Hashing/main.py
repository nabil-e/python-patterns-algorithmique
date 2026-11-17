from collections import Counter

def trouver_premier_unique(texte: str) -> int:
    # 1. Compter toutes les occurrences en un seul passage O(n)
    compteur = Counter(texte)
    
    # 2. Trouver le premier caractère avec une fréquence de 1
    for index, caractere in enumerate(texte):
        if compteur[caractere] == 1:
            return index
    return -1

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    chaine_test = "loveleetcode"
    resultat = trouver_premier_unique(chaine_test)
    print(f"Entrée : '{chaine_test}'")
    print(f"Index du premier caractère unique : {resultat} ('{chaine_test[resultat]}')")
    # Sortie attendue : Index du premier caractère unique : 2 ('v')

def deux_sommes(nombres: list[int], cible: int) -> list[int]:
    vus = {}  # valeur -> index
    
    for i, num in enumerate(nombres):
        complement = cible - num
        if complement in vus:
            return [vus[complement], i]
        vus[num] = i
    return []

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    indices = deux_sommes(nums, target)
    print(f"Tableau : {nums}, Cible : {target}")
    print(f"Indices trouvés : {indices} -> {nums[indices[0]]} + {nums[indices[1]]} = {target}")
    # Sortie attendue : Indices trouvés : [0, 1] -> 2 + 7 = 9

from collections import defaultdict

def grouper_anagrammes(mots: list[str]) -> list[list[str]]:
    groupes = defaultdict(list)
    print(groupes)
    for mot in mots:
        # La signature triée sert de clé immuable (tuple)
        cle = tuple(sorted(mot))
        groupes[cle].append(mot)
        
    return list(groupes.values())

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    liste_mots = ["eat", "tea", "tan", "ate", "nat", "bat"]
    resultat = grouper_anagrammes(liste_mots)
    print(f"Mots : {liste_mots}")
    print(f"Groupes d'anagrammes : {resultat}")
    # Sortie attendue : [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# EXERCICES

### 1832. Check if the Sentence Is Pangram
def checkIfPangram(sentence: str) -> bool:
    return len(set(sentence)) == 26

### 349. Intersection of Two Arrays
def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1) & set(nums2))

### 387. First Unique Character in a String
def firstUniqChar(s: str) -> int:
    seen = {}
    for i in s:
        if i not in seen:
            seen[i] = 1
        else:
            seen[i] += 1
    for i,char in enumerate(s):
        if seen[char] == 1:
            return i
    return -1

### 219. Contains Duplicate II
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    seen = set()
    for i, num in enumerate(nums):
        if num in seen:
            return True
        seen.add(num)
        if len(seen) > k:
            seen.remove(nums[i-k])
    return False

### 217. Contains Duplicate
def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

### 242. Valid Anagram
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

### 1. Two Sum
def two_sum(nums: list[int], target: int):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

### 383. Ransom Note
from collections import Counter
def canConstruct(ransomNote: str, magazine: str) -> bool:
    note = Counter(ransomNote)
    magazine = Counter(magazine)
    if len(note - magazine) == 0:
        return True
    return False

### 49. Group Anagrams
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groupes = {}
    for char in strs:
        key = tuple(sorted(char))
        groupes[key] = groupes.get(key, []) + [char]
    return list(groupes.values())

### 128. Longest Consecutive Sequence
def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0
    seen = set(nums)
    res = 0
    for num in seen:
        if num - 1 not in seen:
            current = num
            current_res = 1
            while current + 1 in seen:
                current += 1
                current_res += 1
            res = max(res, current_res)
    return res

def trouver_paire_somme_mille(nombres):
    complements = {}
    for i in nombres:
        complement = 1000 - i
        if complement in complements:
            return [i, complements[complement]]
        complements[i] = complement
    print(complements)
    return []

if __name__ == "__main__":
    resultat = trouver_paire_somme_mille([1, 2, 999])
    print(resultat)
    assert resultat == [1, 999] or resultat == [999, 1], "Le test avec une solution simple a échoué"

    assert trouver_paire_somme_mille([1, 2, 3]) == [], "Le test sans solution possible a échoué"