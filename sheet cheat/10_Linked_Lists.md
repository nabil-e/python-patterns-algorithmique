# 10. LINKED LISTS (LISTES CHAÎNÉES)
*Pattern 10 / 14 • Manipulation de nœuds `ListNode` en place et parcours par pointeurs*

---

## 1. IDÉE CENTRALE & COMPLEXITÉ
Une liste chaînée est une suite de nœuds (`ListNode(val, next)`) reliés par des pointeurs, sans accès direct par index (`O(1)`). La clé consiste à **manipuler les références `next` sur place** plutôt que de créer de nouvelles structures, en utilisant un **nœud fictif (`dummy`)** pour simplifier les cas limites sur la tête de liste et des **pointeurs rapides/lents (`fast` / `slow`)** pour repérer les milieux ou les cycles.

- **Complexité en temps :** $O(n)$ (parcours linéaire des $n$ nœuds en une ou deux passes).
- **Complexité en espace :** $O(1)$ (manipulation des pointeurs existants sans allocation supplémentaire).

---

## 2. INDICES DANS L'ÉNONCÉ & MOTS-CLÉS LEETCODE

| Indice dans l'énoncé | Mots-clés (Anglais) | Technique à appliquer |
| :--- | :--- | :--- |
| Suppression, insertion ou fusion pouvant modifier la tête de liste | `remove nth node`, `merge two sorted lists`, `partition`, `head` | **Nœud fictif (`dummy = ListNode(0, head)`)** |
| Inverser une liste complète, un segment ou des groupes de $k$ nœuds | `reverse linked list`, `in-place`, `O(1) extra memory` | **3 Pointeurs (`prev`, `curr`, `nxt`)** |
| Détecter une boucle infinie ou trouver le point d'entrée d'un cycle | `linked list cycle`, `has cycle`, `cycle starts` | **Tortue & Lièvre (Floyd : `slow` +1, `fast` +2)** |
| Trouver le milieu de la liste ou vérifier un palindrome en $O(1)$ espace | `middle of the linked list`, `palindrome linked list`, `reorder` | **`fast` / `slow` jusqu'à `not fast or not fast.next`** |
| Trouver le $k$-ième élément depuis la fin en une seule passe | `kth from end`, `one pass`, `remove nth from end` | **2 Pointeurs décalés de $k$ pas** |

---

## 3. VARIANTES & PIÈGES COURANTS

### Les 3 techniques fondamentales
1. **Le Dummy Node (`dummy`) :** Toujours créer `dummy = ListNode(0, head)` dès que `head` risque d'être supprimé, déplacé ou fusionné. On retourne systématiquement `dummy.next` à la fin.
2. **Fast & Slow Pointers (Floyd) :** `slow` avance de 1 nœud (`slow = slow.next`), `fast` avance de 2 nœuds (`fast = fast.next.next`). Quand `fast` atteint la fin, `slow` est exactement au milieu. S'ils se rencontrent, il y a un cycle.
3. **Inversion en place (3 pointeurs) :** Sauvegarder le suivant (`nxt = curr.next`), inverser le lien (`curr.next = prev`), puis avancer (`prev = curr`, `curr = nxt`).

### Les pièges classiques à éviter
- **Perdre le reste de la liste :** Avant de modifier `curr.next`, toujours sauvegarder `nxt = curr.next` dans une variable temporaire, sinon la suite de la liste est perdue.
- **Accéder à `fast.next.next` sans vérifier `fast.next` :** Provoque une `AttributeError: 'NoneType' object has no attribute 'next'`. Toujours écrire : `while fast and fast.next:`.
- **Oublier de couper le lien lors d'un découpage :** Quand on sépare une liste en deux moitiés (ex: *Merge Sort* ou *Palindrome*), penser à mettre `prev.next = None` pour éviter de créer un cycle accidentel.

---

## 4. SQUELETTES DE CODE PYTHON

### Variante A : Inversion en place & Milieu (Fast / Slow)
```python
from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev: Optional[ListNode] = None
    curr: Optional[ListNode] = head

    while curr:
        nxt = curr.next      # 1. Sauvegarder la suite
        curr.next = prev     # 2. Inverser le pointeur
        prev = curr          # 3. Avancer prev
        curr = nxt           # 4. Avancer curr

    return prev              # Nouvelle tête de liste

def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow              # Milieu exact (2e milieu si longueur paire)
```

### Variante B : Nœud fictif (`dummy`) pour fusion ou suppression
```python
def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Rattacher le reliquat non vide en O(1)
    tail.next = l1 if l1 else l2
    return dummy.next
```
