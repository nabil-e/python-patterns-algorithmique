# Heap (Tas Binaire / Priority Queue) — Théorie et Mécanique

## 1. Principe Fondamental
Un **Heap** (ou file de priorité) est une structure d'arbre binaire presque complet qui maintient à tout moment **l'élément le plus petit** (Min-Heap) ou **le plus grand** (Max-Heap) à sa racine.

Contrairement à un tri complet à chaque modification ($O(n \log n)$), un Heap permet d'**insérer** un élément ou d'**extraire le minimum/maximum** en temps **$O(\log n)$**, et de consulter le sommet en **$O(1)$**. En Python, la bibliothèque standard `heapq` implémente nativement un **Min-Heap**.

---

## 2. Schéma Visuel : Min-Heap et Top K

```
Arbre Min-Heap (chaque parent <= ses enfants) :
           [ 2 ]          <-- Sommet : heap[0] (toujours le minimum en O(1))
          /     \
       [ 5 ]   [ 3 ]
      /    \
   [ 9 ]  [ 8 ]

Représentation interne en liste Python : [2, 5, 3, 9, 8]

Astuce "Top K plus grands" avec un Min-Heap de taille K = 3 :
Flux d'entrée : 4, 1, 9, 2, 7
- Ajout 4, 1, 9  -> Heap (taille 3) : [1, 4, 9]
- Ajout 2 (> 1)  -> On éjecte 1, on insère 2 -> [2, 4, 9]
- Ajout 7 (> 2)  -> On éjecte 2, on insère 7 -> [4, 7, 9]
-> Sommet heap[0] = 4 est le 3ème plus grand élément !
```

---

## 3. Mots-Clés Déclencheurs dans les Énoncés
Repère ces indices pour identifier immédiatement le pattern **Heap** :
* **"Kth largest"** ou **"Kth smallest"** (le K-ième plus grand ou plus petit élément).
* **"Top K frequent"** ou **"K closest points"** (les K meilleurs/plus proches éléments).
* **"Stream of data"** ou **"continuously"** (ajout dynamique d'éléments avec recherche répétée du min/max).
* **"Merge K sorted lists / arrays"** (fusionner K listes triées).
* **"Take the heaviest / largest / smallest element repeatedly"** (simulation où l'on modifie et réinsère le max à chaque tour).

---

## 4. Quand l'utiliser ?
1. **Simulations répétitives sur le max/min :** Extraire les deux plus grosses pierres, les écraser et réinsérer le reste (**1046**), ou diviser la plus grande pile par sa racine carrée (**2558**).
2. **Problèmes de type "Top K" :** Maintenir un **Min-Heap de taille fixe $K$** pour trouver les $K$ plus grands éléments en $O(n \log K)$ sans trier tout le tableau.
3. **Flux continu (Streaming) :** Répondre à des requêtes `add(val)` en temps logarithmique (**703**).
