# A. Validation de paires et imbrication (Parenthèses, balises)
# Empile les symboles ouvrants et vérifie la correspondance avec le sommet de la pile dès qu'un symbole fermant apparaît.
def est_valide(s: str) -> bool:
    pile = []
    correspondances = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in correspondances:
            # Si la pile est vide ou que le sommet ne correspond pas -> invalide
            sommet = pile.pop() if pile else '#'
            if correspondances[char] != sommet:
                return False
        else:
            pile.append(char)
            
    # La chaîne est valide uniquement si toutes les ouvertures ont été fermées
    return len(pile) == 0

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    tests = ["()[]{}", "([)]", "{[]}", "((("]
    for t in tests:
        print(f"'{t}' -> {est_valide(t)}")
    # Sortie attendue : True, False, True, False

# B. Élimination de doublons adjacents ou annulations en chaîne
# Compare chaque nouvel élément avec le sommet de la pile (pile[-1]). S'ils s'annulent, dépile au lieu d'empiler.
def supprimer_doublons_adjacents(s: str) -> str:
    pile = []
    
    for char in s:
        if pile and pile[-1] == char:
            pile.pop()  # Annulation avec le caractère précédent
        else:
            pile.append(char)
            
    return "".join(pile)

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    chaine = "abbaca"
    resultat = supprimer_doublons_adjacents(chaine)
    print(f"Entrée : '{chaine}' -> Résultat : '{resultat}'")
    # Détail : 'bb' s'annule -> 'aaca', puis 'aa' s'annule -> 'ca'
    # Sortie attendue : 'ca'

# C. Simulation d'historique et d'opérations (Score / Backspace)
# Garde une trace séquentielle des états précédents pour pouvoir annuler ou combiner les dernières actions.
def traiter_effacements(s: str) -> str:
    pile = []
    for char in s:
        if char == '#' and pile:
            # if pile:  # Toujours vérifier que la pile n'est pas vide avant pop()
            pile.pop()
        else:
            pile.append(char)
    return "".join(pile)

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    s1, s2 = "ab#c", "ad#c"
    res1, res2 = traiter_effacements(s1), traiter_effacements(s2)
    print(f"'{s1}' devient '{res1}' | '{s2}' devient '{res2}'")
    print(f"Sont-ils identiques ? -> {res1 == res2}")
    # Sortie attendue : 'ac' == 'ac' -> True

#  682. Baseball Game
def calculer_score(operations: list[str]) -> int:
    pile = []
    
    for op in operations:
        if op == "+":
            # On COMBINE les deux dernières actions (les 2 derniers scores)
            nouveau_score = pile[-1] + pile[-2]
            pile.append(nouveau_score)
            
        elif op == "D":
            # On réutilise la dernière action en la doublant
            pile.append(pile[-1] * 2)
            
        elif op == "C":
            # On ANNULE la dernière action (comme le '#' du backspace)
            pile.pop()
            
        else:
            # On garde une TRACE du nouveau score
            pile.append(int(op))
            
    return sum(pile)

# --- EXEMPLE PRÊT À LANCER ---
if __name__ == "__main__":
    ops = ["5", "2", "C", "D", "+"]
    print(calculer_score(ops))  # Résultat : 30

# EXERCICES

# 20. Valid Parentheses
def isValid(s: str) -> bool:
        parentheses = {"(":")","[":"]","{":"}"}
        stack = []
        if len(s) % 2 != 0:
            return False
        for parenthese in s:
            if parenthese in parentheses:
                stack.append(parenthese)
            elif not stack or parentheses[stack.pop()] != parenthese:
                return False
        return not stack
# 1047. Remove All Adjacent Duplicates In String
def removeDuplicates(s: str) -> str:
    res = []
    for i in range(len(s)):
        if res and s[i] == res[-1]:
            res.pop()
        else:
            res.append(s[i])
    return "".join(res)

# 682. Baseball Game
def calPoints(operations: list[str]) -> int:
    res = []
    for i in operations:
        if i == "+":
            res.append(res[-1] + res[-2])
        elif i == "D":
            res.append(res[-1] * 2)
        elif i == "C":
            res.pop()
        else:
            res.append(int(i))
    return sum(res)

# 844. Backspace String Compare
def backspaceCompare(s: str, t: str) -> bool:
    l1 = []
    l2 = []
    for i in s:
        if i == "#":
            if l1:
                l1.pop()
            continue
        l1.append(i)
    for i in t:
        if i == "#":
            if l2:
                l2.pop()
            continue
        l2.append(i)
    return l1 == l2

# 1544. Make The String Great
def makeGood(s: str) -> str:
    res = []
    for i in range(len(s)):
        if res and abs(ord(s[i]) - ord(res[-1])) ==  32:
            res.pop()
        else:
            res.append(s[i])
    return "".join(res)

# 2696. Minimum String Length After Removing Substrings
def minLength(s: str) -> int:
    res = []
    for i in s:
        if res and (res[-1] + i) in ("AB", "CD"):
            res.pop()
        else:
            res.append(i)
    return len(res)

# 71. Simplify Path
