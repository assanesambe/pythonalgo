def recherche_binaire(liste, clé):
    gauche, droite = 0, len(liste) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if liste[milieu] == clé:
            return True
        elif liste[milieu] < clé:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return False

print(recherche_binaire([1, 2, 3, 5, 8], 6))  
print(recherche_binaire([1, 2, 3, 5, 8], 5))  
def puissance(a, b):
    return a ** b

print(puissance(3, 4)) 

def tri_bulles(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

print(tri_bulles([29, 13, 22, 37, 52, 49, 46, 71, 56]))

def fusion(gauche, droite):
    resultat = []
    i = j = 0
    while i < len(gauche) and j < len(droite):
        if gauche[i] < droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])
    return resultat

def tri_fusion(liste):
    if len(liste) <= 1:
        return liste
    milieu = len(liste) // 2
    gauche = tri_fusion(liste[:milieu])
    droite = tri_fusion(liste[milieu:])
    return fusion(gauche, droite)

print(tri_fusion([29, 13, 22, 37, 52, 49, 46, 71, 56]))

def partitionner(liste, bas, haut):
    pivot = liste[haut]
    i = bas - 1
    for j in range(bas, haut):
        if liste[j] <= pivot:
            i += 1
            # Échange
            temp = liste[i]
            liste[i] = liste[j]
            liste[j] = temp
    temp = liste[i + 1]
    liste[i + 1] = liste[haut]
    liste[haut] = temp
    return i + 1

def tri_rapide_recursif(liste, bas, haut):
    if bas < haut:
        pivot_index = partitionner(liste, bas, haut)
        tri_rapide_recursif(liste, bas, pivot_index - 1)
        tri_rapide_recursif(liste, pivot_index + 1, haut)

def tri_rapide(liste):
    tri_rapide_recursif(liste, 0, len(liste) - 1)
    return liste

print(tri_rapide([29, 13, 22, 37, 52, 49, 46, 71, 56]))
