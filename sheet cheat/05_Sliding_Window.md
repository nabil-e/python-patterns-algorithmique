# 05. Sliding Window (Fenêtre Glissante)

## 💡 Idée Centrale
Maintenir une sous-section contiguë (une « fenêtre » délimitée par deux pointeurs `left` et `right`) qui glisse de gauche à droite sur un tableau ou une chaîne. Au lieu de recalculer toute la fenêtre à chaque étape, on ajoute l'élément entrant à droite et on retire l'élément sortant à gauche.

* **Complexité Temporelle :** $O(n)$ (chaque élément entre et sort de la fenêtre au maximum une fois)
* **Complexité Spatiale :** $O(1)$ ou $O(k)$ (si utilisation d'un dictionnaire/set pour suivre le contenu de la fenêtre)

---

## 🔍 Indices dans l'énoncé & Mots-clés
| Ce que dit l'énoncé | Mots-clés anglais fréquents |
| :--- | :--- |
| On cherche une sous-partie **contiguë** optimale (plus longue, plus courte). | *contiguous subarray*, *substring*, *longest*, *shortest* |
| Une taille fixe $k$ est imposée pour le sous-tableau ou la sous-chaîne. | *subarray of size k*, *window of size k*, *consecutive elements* |
| On cherche le plus long sous-tableau respectant une condition (ex: au plus $k$ zéros). | *at most k*, *without repeating characters*, *maximum consecutive* |
| On cherche le plus petit sous-tableau dont la somme dépasse une cible (nombres positifs). | *minimum size subarray*, *sum >= target* (positive numbers) |

---

## 🧩 Variantes Principales

### 1. Fenêtre de taille fixe (Fixed Size)
La taille $k$ est connue. À chaque pas, on ajoute `nums[right]` et, dès que `right >= k`, on retire `nums[right - k]`.

### 2. Fenêtre dynamique - Chercher le PLUS LONG (Dynamic - Longest)
On agrandit `right` à chaque itération. Tant que la fenêtre devient **invalide** (ex: trop de doublons), on rétrécit par la gauche (`left += 1`) jusqu'à ce qu'elle redevienne valide, puis on met à jour le maximum.

### 3. Fenêtre dynamique - Chercher le PLUS COURT (Dynamic - Shortest)
On agrandit `right` jusqu'à ce que la fenêtre devienne **valide** (ex: somme $\ge$ cible). Tant qu'elle reste valide, on enregistre la taille minimale et on essaie de la réduire au maximum par la gauche (`left += 1`).

---

## ⚠️ Pièges à éviter
* **Nombres négatifs :** Si le tableau contient des nombres négatifs et qu'on cherche une somme exacte, la fenêtre glissante échoue (rétrécir la fenêtre peut augmenter la somme). Utilisez **Prefix Sum + Hash Map**.
* **Sous-séquence vs Sous-chaîne :** Le *Sliding Window* ne fonctionne que sur des éléments **contigus** (*subarray* / *substring*), jamais sur des *subsequences*.

---

## 💻 Squelettes de Code (Python)

### Variante A : Fenêtre Dynamique (Plus Longue)
```python
def longest_sliding_window(s: str) -> int:
    window = {}  # Pour compter les fréquences dans la fenêtre
    left = 0
    max_len = 0

    for right in range(len(s)):
        # 1. Ajouter l'élément entrant (à droite)
        char = s[right]
        window[char] = window.get(char, 0) + 1

        # 2. Tant que la fenêtre est INVALIDE, rétrécir par la gauche
        while window[char] > 1:  # Exemple : pas de doublons autorisés
            left_char = s[left]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            left += 1

        # 3. La fenêtre est garantie valide : mettre à jour le résultat
        max_len = max(max_len, right - left + 1)

    return max_len
```

### Variante B : Fenêtre Dynamique (Plus Courte)
```python
def shortest_sliding_window(target: int, nums: list[int]) -> int:
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        # 1. Ajouter l'élément entrant
        current_sum += nums[right]

        # 2. Tant que la fenêtre est VALIDE, enregistrer et réduire
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_len if min_len != float('inf') else 0
```
