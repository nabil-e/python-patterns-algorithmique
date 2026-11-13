# Two Pointers — Code, Astuces et Pièges

## 1. Templates Python (Prêts à exécuter)

### A. Pointeurs convergents (Gauche / Droite sur tableau trié)
Idéal pour trouver une paire, inverser un tableau ou comparer des extrémités en $O(n)$ temps et $O(1)$ espace.

```python
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
```

---

### B. Pointeurs Lent / Rapide (Modification sur place / In-place)
Le pointeur `rapide` explore le tableau tandis que `lent` marque la position où écrire le prochain élément valide.

```python
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
```

---

### C. Deux séquences en parallèle (Sous-séquence ou fusion)
Chaque tableau possède son propre pointeur qui avance selon une condition précise.

```python
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
```

---

## 2. Trucs et Astuces (Bibliothèque Standard)

* **Parcours par la fin pour fusionner sans écraser :** Lorsque tu dois fusionner deux tableaux triés dans le premier (ex: LeetCode 88 `Merge Sorted Array`), pars toujours de la fin (`p = m + n - 1`) pour éviter d'écraser les éléments non lus.
* **Échange Pythonique en une ligne :** Utilise `nums[i], nums[j] = nums[j], nums[i]` sans variable temporaire.
* **Saut des doublons sur tableau trié :** Après avoir trouvé une solution valide, avance tes pointeurs tant que la valeur suivante est identique : `while gauche < droite and nums[gauche] == nums[gauche + 1]: gauche += 1`.

---

## 3. Pièges à éviter

* **Condition de boucle `<` vs `<=` :** Sur des pointeurs convergents, utilise `while gauche < droite:` si deux éléments distincts sont requis (ex: paire). Utilise `<=` uniquement si l'élément central doit aussi être traité (ex: palindrome ou carrés triés).
* **Oublier de faire avancer au moins un pointeur dans chaque branche `if/else` :** C'est la cause numéro 1 de boucle infinie (`Time Limit Exceeded`).
* **Dépassement d'index (`IndexError`) lors du saut de doublons :** Vérifie toujours `gauche < droite` **avant** d'accéder à `nums[gauche + 1]`.
