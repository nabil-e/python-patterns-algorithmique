# 🔗 Pattern 10 : Linked Lists (Listes Chaînées)

## 1. Principe et Mécanique
Contrairement aux tableaux (`list`), une **liste chaînée** ne stocke pas ses éléments de manière contiguë en mémoire. Chaque nœud (`ListNode`) contient une valeur (`val`) et un pointeur vers le nœud suivant (`next`). L'accès par index est donc en O(n), mais l'insertion ou la suppression d'un nœud (une fois positionné) se fait en **O(1)** par simple redirection de pointeurs.

Pour résoudre la quasi-totalité des problèmes sur les listes chaînées sans mémoire supplémentaire (O(1) espace), on utilise **3 techniques fondamentales** :

### A. Le Dummy Node (Nœud Sentinelle)
On crée un faux nœud `dummy = ListNode(0, head)` placé juste avant la tête (`head`). Il élimine tous les cas particuliers lorsque la tête de la liste doit être supprimée, déplacée ou fusionnée.

```text
dummy ---> ---> ---> ---> None
  ^          ^
  |          +-- head (peut être supprimé sans casser le retour : dummy.next)
  +-- point de départ fixe
```

### B. Fast & Slow Pointers (Lièvre et Tortue)
Deux pointeurs avancent à des vitesses différentes : `slow` avance de 1 pas (`slow = slow.next`), `fast` avance de 2 pas (`fast = fast.next.next`).
- **Trouver le milieu :** Quand `fast` atteint la fin, `slow` est exactement au milieu.
- **Détecter un cycle :** S'il y a une boucle, `fast` finit obligatoirement par rattraper `slow` (`slow == fast`).

```text
Étape 0 : ---> ---> ---> ---> ---> None
           S,F

Étape 1 : ---> ---> ---> ---> ---> None
                      S          F

Étape 2 : ---> ---> ---> ---> ---> None
                                 S                     F (fin -> S est au milieu !)
```

### C. In-place Reversal (Inversion sur place)
On inverse le sens des flèches (`curr.next = prev`) en maintenant 3 pointeurs : `prev`, `curr`, et une sauvegarde temporaire `nxt`.

```text
Avant :   None <---      ---> ---> None
                     prev       curr       nxt

Action :  curr.next = prev  puis on décale prev et curr d'un cran

Après :   None <--- <---      ---> None
                                prev       curr
```

---

## 2. Mots-clés et Déclencheurs dans les énoncés
Repère ces indices pour identifier immédiatement ce pattern :
- **"Singly-linked list"** / **"ListNode"** / **"head"**
- **"In-place"** / **"O(1) extra space"** (interdiction de copier les valeurs dans un tableau Python)
- **"Reverse a linked list"** (inverser tout ou partie d'une liste)
- **"Middle of the linked list"** (milieu de liste)
- **"Cycle"** / **"Loop"** (détection de boucle)
- **"Merge two sorted lists"** (fusion de listes triées)
- **"Remove Nth node from end"** (suppression par rapport à la fin -> deux pointeurs décalés de $N$)

---

## 3. Quand l'utiliser & Complexités

| Technique | Cas d'usage typique | Temps | Espace |
| :--- | :--- | :--- | :--- |
| **Dummy Node** | Fusionner des listes, supprimer la tête, partitionner | $O(n)$ | $O(1)$ |
| **Fast & Slow** | Milieu de liste, cycle, palindrome sur liste chaînée | $O(n)$ | $O(1)$ |
| **In-place Reversal** | Inverser une liste entière ou un sous-segment | $O(n)$ | $O(1)$ |
| **Gap Pointers** | Supprimer le $N$-ième élément depuis la fin | $O(n)$ | $O(1)$ |
---

## ⚠️ Cas limites à vérifier
- **Liste vide (`head is None`) :** Toujours tester `if not head:` en tout début de fonction.
- **Liste à un seul nœud (`head.next is None`) :** Vérifier que les pointeurs `slow` et `fast` (ou `prev` et `curr`) ne tentent pas d'accéder à `head.next.next` sans garde-fou.
- **Suppression ou modification de la tête (`head`) :** Sans `dummy = ListNode(0, head)`, supprimer le premier élément oblige à écrire un `if` séparé qui est souvent source de bugs.

## 🚫 Quand éviter ce pattern
- **Besoin d'accès direct par index (`nums[i]`) ou de recherche binaire :** Une liste chaînée n'offre pas d'accès aléatoire en $O(1)$. Si l'algorithme nécessite de sauter d'un index à l'autre, convertir ou utiliser un tableau (`list`).
