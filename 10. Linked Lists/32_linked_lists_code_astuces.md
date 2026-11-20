# 💻 Pattern 10 : Linked Lists — Squelettes, Code & Astuces

## 1. Squelettes Génériques (Boilerplates)

### Squelette A : Inversion sur place (In-place Reversal)
```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def reverse_list_skeleton(head: Optional[ListNode]) -> Optional[ListNode]:
    prev: Optional[ListNode] = None
    curr: Optional[ListNode] = head
    while curr:
        nxt = curr.next      # 1. Sauvegarder la suite
        curr.next = prev     # 2. Inverser le pointeur
        prev = curr          # 3. Avancer prev
        curr = nxt           # 4. Avancer curr
    return prev              # Nouvelle tête de liste
```

### Squelette B : Fast & Slow Pointers
```python
def fast_slow_skeleton(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # Condition de rencontre (cycle)
            return slow
    return slow  # Milieu de la liste si pas de cycle
```

---

## 2. Démos Exécutables & Bac à Sable (`main.py`)

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


# --- Utilitaires de test local ---
def build_linked_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    result: list[int] = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# --- 1. DÉMOS DU PATTERN (Exécutables) ---

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """LeetCode 206 : Inverse une liste chaînée en O(1) espace."""
    prev: Optional[ListNode] = None
    curr: Optional[ListNode] = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def merge_two_lists(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    """LeetCode 21 : Fusionne deux listes triées avec Dummy Node."""
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """LeetCode 876 : Retourne le nœud du milieu."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# --- 2. BAC À SABLE EXERCICES (À compléter) ---

def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """LeetCode 19 : Remove Nth Node From End of List. À compléter !"""
    pass


if __name__ == "__main__":
    l1 = build_linked_list([1, 2, 3, 4, 5])
    print("Inversion :", linked_list_to_list(reverse_list(l1)))

    a = build_linked_list([1, 2, 4])
    b = build_linked_list([1, 3, 4])
    print("Fusion :", linked_list_to_list(merge_two_lists(a, b)))

    m = build_linked_list([10, 20, 30, 40, 50])
    mid = middle_node(m)
    print("Milieu :", mid.val if mid else None)  # 30
```

---

## 3. Trucs et Astuces Python
- **Toujours utiliser `dummy = ListNode()`** dès que la tête de liste (`head`) peut être supprimée ou déplacée. Retourne simplement `dummy.next`.
- **Rattachement final en O(1) :** Lors d'une fusion, `tail.next = l1 or l2` raccroche d'un coup toute la fin de la liste restante sans boucle supplémentaire.
- **Décalage de $N$ pas :** Pour atteindre le $N$-ième élément depuis la fin en une seule passe, avance `fast` de $N$ pas depuis `dummy`, puis avance `slow` et `fast` ensemble jusqu'à la fin.

---

## 4. Pièges à éviter
- **`AttributeError: 'NoneType' object has no attribute 'next'` :** Écris toujours `while fast and fast.next:` (dans cet ordre exact) pour éviter d'évaluer `.next` sur `None`.
- **Perdre la suite lors d'une inversion :** Sauvegarde toujours `nxt = curr.next` avant de modifier `curr.next = prev`.
- **Boucle infinie lors d'une réorganisation :** Pense à couper l'ancien pointeur `.next` du nœud qui devient le dernier de la liste.
