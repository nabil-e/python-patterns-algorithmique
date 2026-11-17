# 💻 Pattern 10 : Linked Lists — Squelettes, Code & Astuces

## 1. Squelettes Génériques (Boilerplates)

### Squelette A : Inversion sur place (In-place Reversal)
```python
def squelette_reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next      # 1. Sauvegarder la suite
        curr.next = prev     # 2. Inverser le pointeur
        prev = curr          # 3. Avancer prev
        curr = nxt           # 4. Avancer curr
    return prev              # Nouvelle tête de liste
```

### Squelette B : Fast & Slow Pointers + Dummy Node
```python
def squelette_fast_slow(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if ...:  # Condition de rencontre (cycle)
            return True
    return slow  # Milieu de la liste si pas de cycle
```

---

## 2. Templates Python Exécutables (Prêts à lancer)

Ce fichier inclut des fonctions utilitaires (`creer_liste` et `afficher_liste`) pour tester tes algorithmes localement dans `main.py` sans LeetCode.

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


# --- Utilitaires de test local ---
def creer_liste(valeurs: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    for v in valeurs:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def afficher_liste(head: Optional[ListNode]) -> list[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


# --- Template 1 : Inverser une liste chaînée (LeetCode 206) ---
def inverser_liste(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


# --- Template 2 : Fusionner deux listes triées avec Dummy Node (LeetCode 21) ---
def fusionner_listes_triees(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
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

    # Rattacher le reste de la liste non vide en O(1)
    tail.next = l1 if l1 else l2
    return dummy.next


# --- Template 3 : Trouver le milieu (LeetCode 876) ---
def milieu_liste(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    # Test 1 : Inversion
    l1 = creer_liste([1, 2, 3, 4, 5])
    inv = inverser_liste(l1)
    print("Inversion :", afficher_liste(inv))  # [5, 4, 3, 2, 1]

    # Test 2 : Fusion
    a = creer_liste([1, 3, 5])
    b = creer_liste([2, 4, 6])
    fusion = fusionner_listes_triees(a, b)
    print("Fusion :", afficher_liste(fusion))  # [1, 2, 3, 4, 5, 6]

    # Test 3 : Milieu
    m = creer_liste([10, 20, 30, 40, 50])
    print("Milieu :", milieu_liste(m).val)  # 30
```

---

## 3. Trucs et Astuces Python
- **Toujours utiliser un `dummy = ListNode()`** dès que la liste résultante peut avoir une nouvelle tête (suppression, fusion, filtrage). Retourne simplement `dummy.next`.
- **Rattachement final en une ligne :** Lors de la fusion de deux listes, inutile de faire deux boucles `while` à la fin : `tail.next = l1 or l2` rattache directement toute la chaîne restante en O(1).
- **Échange Pythonique (tuple unpacking) :** L'inversion peut s'écrire de façon très concise en Python :
  ```python
  prev, curr.next, curr = curr, prev, curr.next
  ```
  *(Attention à l'ordre d'évaluation de gauche à droite : `curr.next` doit être assigné avant que `curr` ne change).*

---

## 4. Pièges à éviter
- **Perdre la référence vers la suite (`nxt`) :** Si tu écris `curr.next = prev` avant de sauvegarder `nxt = curr.next`, tu coupes définitivement le reste de la liste en mémoire.
- **`AttributeError: 'NoneType' object has no attribute 'next'` :** Dans la boucle `while fast and fast.next:`, vérifie **toujours** `fast` avant `fast.next`. Si `fast` vaut `None`, évaluer `fast.next` lève une exception.
- **Oublier de couper un ancien lien lors d'une réorganisation :** Quand tu déplaces des nœuds existants, assure-toi que le dernier nœud pointe bien vers `None`, sinon tu crées une boucle infinie lors de l'affichage.
