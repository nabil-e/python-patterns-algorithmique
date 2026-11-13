# 16. Prefix & Suffix Sum — Théorie et Mécanique

## 1. Principe Fondamental
Le pattern **Prefix Sum** (somme préfixe) consiste à précalculer les sommes cumulées d'un tableau dans un tableau auxiliaire `prefix`, de sorte que la somme de n'importe quel sous-tableau contigu entre les indices `i` et `j` soit calculable en temps constant **$O(1)$** au lieu de parcourir les éléments en $O(n)$.

Le **Suffix Sum** applique exactement la même logique en partant de la fin du tableau vers le début.

### Schéma Visuel : Construction et Requête en $O(1)$
```
Tableau original (nums) : [  2,   4,   1,   5,   3 ]
Indices                 :    0    1    2    3    4

Tableau Prefix (taille n + 1, commence toujours par 0) :
prefix : [ 0,   2,   6,   7,  12,  15 ]
Indices:   0    1    2    3    4    5

Requête : Somme de nums[1..3] (soit 4 + 1 + 5 = 10)
Formule : prefix[j + 1] - prefix[i]
Calcul  : prefix[4] - prefix[1] = 12 - 2 = 10  --> O(1) !
```

### Schéma Visuel : Combinaison Prefix & Suffix (Produit ou Somme hors élément `i`)
```
Pour calculer une valeur autour de i sans inclure nums[i] :
Tableau : [ a,   b,   c,   d ]
Prefix  : [ 1,   a,  a*b, a*b*c ]  (tout ce qui est à GAUCHE de i)
Suffix  : [b*c*d, c*d,  d,   1   ]  (tout ce qui est à DROITE de i)
Résultat: Prefix[i] * Suffix[i]
```

## 2. Mots-Clés et Déclencheurs dans les Énoncés
Repère ces indices pour identifier immédiatement ce pattern :
* **"Somme d'un sous-tableau contigu"** (`subarray sum`, `range sum`).
* **"Plusieurs requêtes de somme sur un tableau fixe"** (`immutable`, `multiple queries`).
* **"Somme à gauche / somme à droite"** (`left sum`, `right sum`, `pivot index`, `equilibrium`).
* **"Sous-tableau dont la somme vaut K"** (`subarray sum equals K` — souvent combiné avec **Hashing**).
* **"Produit / Somme de tous les éléments sauf soi-même"** (`except self`).
* **"Altitude / Solde cumulé étape par étape"** (`running sum`, `highest altitude`, `step by step sum`).

## 3. Quand l'utiliser ?
* **Recommandé :** Dès que tu dois calculer répétitivement des sommes (ou produits) sur des plages d'un tableau qui ne change pas, ou lorsque tu as besoin de connaître l'état cumulé avant et après chaque index en $O(n)$.
* **À éviter :** Si le tableau subit fréquemment des modifications entre les requêtes (préférer alors un *Segment Tree* ou un *Fenwick Tree*).

## 4. Complexité
* **Temps :** $O(n)$ pour construire le tableau préfixe, puis $O(1)$ par requête.
* **Espace :** $O(n)$ pour stocker le tableau préfixe (parfois réductible à $O(1)$ si on modifie le tableau en place ou si l'on n'a besoin que d'une somme courante).
