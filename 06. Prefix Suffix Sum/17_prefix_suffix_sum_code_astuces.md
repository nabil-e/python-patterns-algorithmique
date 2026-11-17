# 17. Prefix & Suffix Sum — Code, Astuces et Pièges

## 1. Templates Python (Prêts à exécuter)

### Template A : Précalcul des requêtes de plage (Prefix Sum classique)
Idéal pour répondre en $O(1)$ à des requêtes de somme entre `left` et `right` inclus.

```python
from itertools import accumulate


class RequeteSommePlage:
    def __init__(self, nums: list[int]):
        # initial=0 ajoute automatiquement le 0 en tête de liste
        self.prefix = list(accumulate(nums, initial=0))

    def somme_plage(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    requeteur = RequeteSommePlage(nums)
    print("Somme [0, 2] :", requeteur.somme_plage(0, 2))  # Attendu : 1
    print("Somme [2, 5] :", requeteur.somme_plage(2, 5))  # Attendu : -1
```

### Template B : Prefix + Suffix (Calcul gauche et droite sans l'élément courant)
Idéal pour calculer une valeur basée sur tous les éléments sauf `nums[i]`, sans utiliser la division.

```python
def produit_sauf_soi_meme(nums: list[int]) -> list[int]:
    n = len(nums)
    resultat = [1] * n

    # 1. Passe gauche -> droite (Prefix)
    prefix = 1
    for i in range(n):
        resultat[i] = prefix
        prefix *= nums[i]

    # 2. Passe droite -> gauche (Suffix)
    suffix = 1
    for i in range(n - 1, -1, -1):
        resultat[i] *= suffix
        suffix *= nums[i]

    return resultat


if __name__ == "__main__":
    entree = [1, 2, 3, 4]
    print("Entrée  :", entree)
    print("Sortie  :", produit_sauf_soi_meme(entree))  # Attendu : [24, 12, 8, 6]
```

### Template C : Prefix Sum + Hashing (Sous-tableaux de somme égale à K)
Indispensable dès que le tableau contient des nombres **négatifs** (où Sliding Window échoue).

```python
from collections import defaultdict


def compter_sous_tableaux_somme_k(nums: list[int], k: int) -> int:
    compteur_prefixes = defaultdict(int)
    compteur_prefixes[0] = 1  # Cas où le sous-tableau démarre à l'index 0

    somme_courante = 0
    total_sous_tableaux = 0

    for num in nums:
        somme_courante += num
        # Si (somme_courante - k) a déjà été vue, alors un sous-tableau intermédiaire vaut k
        total_sous_tableaux += compteur_prefixes[somme_courante - k]
        compteur_prefixes[somme_courante] += 1

    return total_sous_tableaux


if __name__ == "__main__":
    nums = [1, 2, 3, -2, 2]
    k = 3
    print("Nombre de sous-tableaux de somme", k, ":", compter_sous_tableaux_somme_k(nums, k))  # Attendu : 4
```

## 2. Trucs et Astuces (Bibliothèque Standard)
* **`itertools.accumulate(nums, initial=0)` :** Génère le tableau préfixe de taille `n + 1` en une seule ligne en C pur, bien plus rapide qu'une boucle `for` manuelle.
* **Le `0` initial sauve la vie :** Toujours créer un tableau `prefix` de taille `n + 1` avec `prefix[0] = 0`. Cela évite d'écrire une condition `if left == 0:` dans la formule `prefix[right + 1] - prefix[left]`.
* **Somme totale = `prefix[-1]` :** Pas besoin de refaire `sum(nums)` si tu as déjà construit `prefix`. La somme de droite à partir de `i` vaut simplement `prefix[-1] - prefix[i + 1]`.

## 3. Pièges à Éviter
* **Confusion d'indices (+1 / -1) :** Dans un tableau `prefix` de taille `n + 1`, `prefix[i]` représente la somme des `i` premiers éléments (indices `0` à `i - 1`). La somme inclusive de `left` à `right` est toujours `prefix[right + 1] - prefix[left]`.
* **Utiliser Sliding Window avec des nombres négatifs :** Si l'énoncé demande un sous-tableau de somme `k` et que `nums` contient des négatifs, Sliding Window ne fonctionne pas car la somme n'est pas monotone. Utilise le **Template C (Prefix Sum + Hashing)**.
* **Oublier `compteur_prefixes[0] = 1` :** Dans le Template C, oublier cette initialisation rate tous les sous-tableaux valides qui commencent dès l'index `0`.
