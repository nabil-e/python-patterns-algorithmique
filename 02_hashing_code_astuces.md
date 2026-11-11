# Hashing — Code, Astuces et Pièges

## 1. Templates Python (Prêts à exécuter)

### A. Comptage de fréquences et recherche de doublons
Utilise `collections.Counter` ou un `dict` classique pour compter les occurrences en $O(n)$.

```python
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
```

---

### B. Recherche de complément (Pattern Two Sum / Lookup O(1))
Stocke les éléments déjà vus dans un dictionnaire (`valeur: index`) ou un ensemble (`set`) pour vérifier l'existence d'un complément instantanément.

```python
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
```

---

### C. Regroupement par clé canonique (`defaultdict`)
Regroupe des éléments partageant une même signature (anagrammes, catégories, restes de division).

```python
from collections import defaultdict

def grouper_anagrammes(mots: list[str]) -> list[list[str]]:
    groupes = defaultdict(list)
    
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
```

---

## 2. Trucs et Astuces (Bibliothèque Standard)

* **Utilise `set` pour tester l'appartenance :** Vérifier `x in mon_set` prend un temps moyen de $O(1)$, contre $O(n)$ sur une `list`.
* **Opérations ensemblistes natives :** Pour trouver l'intersection de deux tableaux (ex: LeetCode 349), utilise directement `list(set(nums1) & set(nums2))`.
* **Évite `KeyError` avec `.get()` ou `defaultdict` :** `compteur[x] = compteur.get(x, 0) + 1` évite de tester `if x in compteur:` à chaque tour de boucle.
* **Clés composites immuables :** Une `list` ne peut pas être clé de dictionnaire (`TypeError: unhashable type: 'list'`). Convertis-la toujours en `tuple(ma_liste)`.

---

## 3. Pièges à éviter

* **Modifier un dictionnaire pendant qu'on itère dessus :** Faire `for k in mon_dict: del mon_dict[k]` lève une `RuntimeError`. Itère sur `list(mon_dict.keys())` si tu dois supprimer des clés.
* **Oublier la contrainte d'index dans les doublons proches :** Si l'énoncé demande un doublon à une distance maximale $k$ (ex: LeetCode 219), un simple `set` global ne suffit pas ; il faut stocker le **dernier index vu** dans un `dict` (`vus[val] = i`).
* **Confondre `set()` et `{}` :** `{}` crée un dictionnaire vide, pas un ensemble vide. Utilise toujours `set()` pour initialiser un ensemble.
