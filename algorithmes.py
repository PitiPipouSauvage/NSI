# ------- Première ------- #

def recherche_dichotomique(liste, element):
    a = 0
    b = len(liste)
    while a < b:
        m = (a + b)//2
        if  liste[m] < element:
            a = m + 1
        elif liste[m] > element:
            b = m-1
        else:
            return m
        
        
    if liste[a] == element:
       return a

    return None

def trie_selection(liste):
    for i in range(len(liste)-1):
        minimum = liste[i]
        index = i
        for j in range(i, len(liste)):
            if liste[j] < minimum:
                minimum = liste[j]
                index = j
        liste[i], liste[index] = liste[index], liste[i]
        
def trie_insertion(liste):
    for i in range(1, len(liste)):
        j = i
        while j > 0 and liste[j] < liste[j-1]:
            liste[j-1], liste[j] = liste[j], liste[j-1]
            j -= 1

# ------- Terminale ------- #
