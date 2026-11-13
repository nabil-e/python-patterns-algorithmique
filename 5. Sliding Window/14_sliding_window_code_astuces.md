# Sliding Window — Code, Astuces et Pièges

## 1. Templates Python (Prêts à exécuter)

### A. Fenêtre de taille fixe $k$ (Somme ou moyenne maximale)
Calcule la première fenêtre de taille $k$, puis fais-la glisser d'un cran à chaque itération en ajoutant l'élément entrant et en retirant l'élément sortant.

```python
def moyenne_maximale(nums: list[int], k: int) -> float:
    # 1. Initialiser la première fenêtre [0 ... k-1]
    somme_fenetre = sum(nums[:k])
    max_somme = somme_fenetre
    
    # 2. Faire glisser la fenêtre de l'index k jusqu'à la fin
    for droite in range(k, len(nums)):
        # Ajoute le nouvel élément à droite, retire l'ancien à gauche (droite - k)
        somme_fenetre += nums[droite] - nums[droite - k]
        if somme_fenetre > max_somme:
            max_somme = somme_fenetre
            
    return max_somme / k

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    donnees = [1, 12, -5, -6, 50, 3]
    k = 4
    resultat = moyenne_maximale(donnees, k)
    print(f"Tableau : {donnees}, k = {k}")
    print(f"Moyenne maximale sur {k} éléments : {resultat}")
    # Sortie attendue : 12.75 (sous-tableau [12, -5, -6, 50])
```

---

### B. Fenêtre de taille fixe avec suivi d'unicité (Hashing + Fenêtre)
Maintient un dictionnaire de fréquences sur une fenêtre de taille $k$ pour vérifier rapidement si tous les éléments sont distincts.

```python
from collections import defaultdict

def compter_sous_chaines_distinctes(s: str, k: int = 3) -> int:
    if len(s) < k:
        return 0
        
    compteur = defaultdict(int)
    resultat = 0
    
    for droite in range(len(s)):
        # 1. Entrée du caractère de droite
        compteur[s[droite]] += 1
        
        # 2. Si la fenêtre dépasse la taille k, on retire le caractère de gauche
        if droite >= k:
            char_gauche = s[droite - k]
            compteur[char_gauche] -= 1
            if compteur[char_gauche] == 0:
                del compteur[char_gauche]  # Crucial pour que len(compteur) reste exact
                
        # 3. Une fois la taille k atteinte, on vérifie la validité
        if droite >= k - 1 and len(compteur) == k:
            resultat += 1
            
    return resultat

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    chaine = "aababcabc"
    nb = compter_sous_chaines_distinctes(chaine, 3)
    print(f"Chaîne : '{chaine}'")
    print(f"Nombre de sous-chaînes de taille 3 avec caractères distincts : {nb}")
    # Sortie attendue : 4 ('abc', 'bca', 'cab', 'abc')
```

---

### C. Fenêtre de taille variable (Plus long sous-tableau sans doublon)
Étend la borne `droite` à chaque tour et contracte la borne `gauche` avec une boucle `while` dès qu'une contrainte est violée.

```python
def longueur_max_sans_doublon(s: str) -> int:
    vus = set()
    gauche = 0
    max_longueur = 0
    
    for droite in range(len(s)):
        # Tant que la fenêtre est invalide (doublon présent), on rétrécit par la gauche
        while s[droite] in vus:
            vus.remove(s[gauche])
            gauche += 1
            
        # On ajoute le nouvel élément et on met à jour le record
        vus.add(s[droite])
        max_longueur = max(max_longueur, droite - gauche + 1)
        
    return max_longueur

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    texte = "abcabcbb"
    longueur = longueur_max_sans_doublon(texte)
    print(f"Texte : '{texte}' -> Plus longue sous-chaîne sans doublon : {longueur}")
    # Sortie attendue : 3 ('abc')
```

---

## 2. Trucs et Astuces (Bibliothèque Standard)

* **Formule d'or de la taille d'une fenêtre :** Entre deux index inclusifs `gauche` et `droite`, le nombre d'éléments est toujours `droite - gauche + 1`.
* **Calcul de l'index sortant sur fenêtre fixe :** Si ta fenêtre a une taille fixe $k$ et que ton pointeur courant est `droite`, l'élément qui sort tout à gauche est toujours à l'index `droite - k`.
* **Privilégie le glissement incrémental au slicing :** Ne fais jamais `sum(nums[i:i+k])` à l'intérieur d'une boucle, car le slicing copie $k$ éléments et dégrade ton algorithme de $O(n)$ à $O(n 	imes k)$.

---

## 3. Pièges à éviter

* **Oublier de supprimer les clés à zéro dans le dictionnaire :** Si tu utilises `len(compteur)` pour connaître le nombre d'éléments uniques dans la fenêtre, un caractère tombé à `0` restera compté dans `len()` si tu ne fais pas `del compteur[char]`.
* **Mettre à jour le résultat avant de réparer la fenêtre :** Dans une fenêtre variable, exécute toujours la boucle `while` de contraction **avant** de calculer `max_longueur = max(max_longueur, droite - gauche + 1)`.
* **Utiliser une fenêtre glissante sur des nombres négatifs pour une somme cible :** Si l'énoncé demande un sous-tableau dont la somme vaut $K$ et que le tableau contient des nombres négatifs, agrandir la fenêtre n'augmente pas forcément la somme. Utilise alors **Prefix Sum + Hashing**.
