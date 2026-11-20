# 10. Linked Lists (Listes Chaînées)
> **Manipuler des séquences dynamiques par redirection de pointeurs sans mémoire supplémentaire**

**Principe clé :** Contrairement aux tableaux (`list`), une liste chaînée ne stocke pas ses éléments de manière contiguë. L'accès par index est en $O(n)$, mais l'insertion ou la suppression d'un nœud (une fois positionné) se fait en $O(1)$. On utilise un nœud sentinelle (`dummy`), deux pointeurs à vitesses différentes (`slow`/`fast`) ou l'inversion sur place (`prev`/`curr`/`nxt`).  
**Complexité cible :** Temps : $O(n)$ | Espace : $O(1)$

---

## 1. INDICES DANS L'ÉNONCÉ & MOTS-CLÉS

| Ce que l'énoncé demande | Mots-clés (Anglais) | Approche à adopter |
| :--- | :--- | :--- |
| Trouver le milieu d'une liste ou détecter une boucle | `middle of linked list`, `cycle`, `loop` | **Fast & Slow Pointers** (`slow` +1, `fast` +2) |
| Inverser tout ou partie d'une liste sur place | `reverse linked list`, `in-place`, `O(1) space` | **In-place Reversal** (`prev`, `curr`, `nxt`) |
| Supprimer la tête, filtrer ou fusionner deux listes | `merge two sorted lists`, `remove elements` | **Dummy Node** (`dummy = ListNode(0, head)`) |
| Supprimer le N-ième nœud en partant de la fin | `remove nth node from end` | **Gap Pointers** (décaler `fast` de $N$ pas avant) |

---

## 2. VARIANTES & ASTUCES DE DÉCISION

* **Dummy Node :** Créez `dummy = ListNode(0, head)` dès que la tête de la liste peut être supprimée ou déplacée. Retournez `dummy.next`.
* **Fast & Slow Pointers :** Quand `fast` atteint la fin (`while fast and fast.next:`), `slow` pointe exactement sur le milieu. En cas de cycle, `fast` rattrape obligatoirement `slow`.
* **Attention aux `NoneType` :** Toujours sauvegarder `nxt = curr.next` avant de modifier `curr.next = prev`, et toujours vérifier `fast` avant `fast.next`.

---

## 3. SQUELETTE DE CODE (PYTHON)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseAndMiddle(head):
    # 1. Trouver le milieu avec Fast & Slow
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2. Inverser sur place à partir de slow
    prev, curr = None, slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```
