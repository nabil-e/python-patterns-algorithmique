# Binary Search — Code, Astuces et Pièges

## 1. Templates Python (Prêts à exécuter)

### A. Recherche exacte ou position d'insertion (Lower Bound)
Trouve la cible dans un tableau trié, ou l'index exact où l'insérer pour maintenir l'ordre.

```python
def position_insertion(nums: list[int], cible: int) -> int:
    gauche, droite = 0, len(nums) - 1
    
    while gauche <= droite:
        milieu = gauche + (droite - gauche) // 2
        if nums[milieu] == cible:
            return milieu
        elif nums[milieu] < cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1
            
    # Si non trouvé, 'gauche' pointe exactement sur la position d'insertion
    return gauche

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    tableau = [1, 3, 5, 6]
    print(f"Tableau : {tableau}")
    print(f"Position pour 5 (présent) : {position_insertion(tableau, 5)}")
    print(f"Position pour 2 (absent)  : {position_insertion(tableau, 2)}")
    print(f"Position pour 7 (fin)     : {position_insertion(tableau, 7)}")
    # Sortie attendue : 2, 1, 4
```

---

### B. Recherche de première frontière (First True / First Bad Version)
Trouve le tout premier élément qui satisfait une condition monotone (`False, False, ..., True, True`).

```python
def premiere_version_defectueuse(n: int, est_defectueuse) -> int:
    gauche, droite = 1, n
    
    while gauche < droite:
        milieu = gauche + (droite - gauche) // 2
        if est_defectueuse(milieu):
            # milieu est peut-être la première, on garde milieu dans l'espace de recherche
            droite = milieu
        else:
            # milieu est bonne, la première défectueuse est forcément après
            gauche = milieu + 1
            
    return gauche

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    # Simulation d'une API : les versions >= 4 sont défectueuses
    api_test = lambda v: v >= 4
    total_versions = 10
    premiere = premiere_version_defectueuse(total_versions, api_test)
    print(f"Sur {total_versions} versions, la première défectueuse est : {premiere}")
    # Sortie attendue : 4
```

---

### C. Recherche sur l'espace des réponses (Ex: Racine carrée entière)
Applique la recherche binaire non pas sur un tableau, mais sur un intervalle numérique `[0, x]`.

```python
def racine_entiere(x: int) -> int:
    if x < 2:
        return x
        
    gauche, droite = 1, x // 2
    
    while gauche <= droite:
        milieu = gauche + (droite - gauche) // 2
        carre = milieu * milieu
        if carre == x:
            return milieu
        elif carre < x:
            gauche = milieu + 1
        else:
            droite = milieu - 1
            
    # 'droite' a croisé 'gauche' et pointe sur le plus grand entier dont le carré <= x
    return droite

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    for val in [4, 8, 16, 27]:
        print(f"sqrt({val}) arrondi à l'inférieur = {racine_entiere(val)}")
    # Sortie attendue : 2, 2, 4, 5
```

---

## 2. Trucs et Astuces (Bibliothèque Standard)

* **Le module `bisect` intégré :** En Python, `bisect.bisect_left(nums, cible)` fait exactement le travail du Template A en C optimisé ! Utilise `bisect_left` pour la première occurrence et `bisect_right` pour la position juste après la dernière occurrence.
* **Calcul sécurisé du milieu :** Écris `milieu = gauche + (droite - gauche) // 2`. Même si Python gère les grands entiers sans overflow, cette écriture montre aux recruteurs que tu maîtrises les bonnes pratiques d'ingénierie logicielle.

---

## 3. Pièges à éviter

* **Boucle infinie avec `gauche = milieu` :** Si tu écris `while gauche < droite:` avec `milieu = (gauche + droite) // 2`, lorsque `droite == gauche + 1`, `milieu` vaut `gauche`. Si la branche `else` fait `gauche = milieu`, les bornes ne bougent plus jamais ! Déplace toujours `gauche = milieu + 1`.
* **Mélanger les conditions de sortie :**
  * Utilise `while gauche <= droite:` quand tu retournes directement depuis l'intérieur de la boucle (`if nums[milieu] == cible: return milieu`).
  * Utilise `while gauche < droite:` quand tu réduis l'intervalle jusqu'à un seul élément survivant (`droite = milieu`).
* **Oublier que le tableau doit être trié (ou monotone) :** Si l'énoncé donne un tableau non trié et demande une complexité $O(n)$, ne trie pas le tableau ($O(n \log n)$), utilise plutôt le **Hashing**.
