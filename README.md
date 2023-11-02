# NSI
Ce dépôt contient toutes les implémentations python des structures et algorithmes vus en cours. Le but est de faciliter la réutilisation d'algorithmes ou de structures dans d'autres algorithmes et de fournir un exemple d'implémentation de ceux-ci.   
Ce fichier est un guide d'utilisation des classes et fonctions présentes dans les différents fichiers.
= Lol
## Les algorithmes

### I - Première

Le fichier _"algorithmes.py"_ rassemble les algorithmes vus au cours de l'année.  
J'ai tout de même inclus les algorithmes de trie et la recherche dichotomique du programme de première :  

• la fonction `recherche_dichotomique(liste, element)` renvoie l'indice de l'élement recherché ou `None` s'il n'existe pas  
• la fonction `trie_selection(liste)` trie la liste en utilisant l'algorithme de trie par séléction  
• la fonction `trie_insertion(liste)` trie la liste en utilisant l'algorithme de trie par insertion  

Vous pouvez aller voir l'implémentation des fonctions dans le fichier python.

## II - Terminale 

Pour l'instant le néan ...

## III - Utilisation

Il suffit d'avoir le fichier _"algorithmes.py"_ dans le dossier du fichier de test et d'inclure la ligne suivante en haut de celui-ci : 
```python
from algorithmes import * 
```
et vous pouvez utiliser les fonctions décrites auparvant.

## Les structures
Dans le fichier _"structure.py"_ on retrouve 4 classes utiles :  

• `Liste` représentant la structure linéaire _liste chainée_ (ou _linked-list_ en anglais)  
• `Pile` représentant la structure linéaire _pile_ (ou _stack_ en anglais)  
• `File` représentant la structure linéaire _file_ (ou _queue_ en anglais)  
• `ABR` représentant la structure _arbre binaire de recherche_  (ou _binary tree_ en anglais)

### I - La _liste chainée_
Pour la classe `Liste`, elle regroupe la majorité des fonction des `list` de python. Des exemples d'utilisation sont fournis dans le bloc de code suivant :

```python 
liste0 = Liste() # créer une liste chainée vide

liste1 = Liste(1) # créer une liste chainée avec un élément
liste2 = Liste(['abc', 2, ('taple', 0)]) # créer une liste chainée contenant des éléments par défaut

liste3 = Liste(liste1) # remplis liste3 avec les éléments de liste1
# cela marche avec tous les classes itérables

# accéder à un élément
liste = List(...)
i = ...
print(liste[i])

# traverser la liste
for valeur in liste: 
  print(valeur)    

# toutes les slices à pas positifs fonctionnent
print(liste[i:]) # elle renvoie une liste chainée

# ajouter des valeurs à la fin de la liste
liste.etendre('je')
liste.etendre(['suis', 'con'])

# ajouter des valeurs n'importe où
liste.inserer(1, 'ne')
liste.inserer(4, 'pas') # tout cela marche également avec plusieurs valeurs

liste.est_vide() # liste est-elle vide ?
len(liste) # nombre d'éléments de liste
liste.vider() # vide liste

print(liste) # produit l'affichage suivant : "(Liste:...,...,...)"
# si elle est vide cela l'affichage est : "(Liste)"
```

### II - La _pile_

Les fonctionnalités de la classe `Pile` se trouvent dans les bloc suivant :    

```python
pile = Pile(...) # fonctionne comme les liste chainées
# les valeurs sont empilées dans l'ordre de l'itérable

pile.emplier('assiette') # ajoute un élément
pile.empiler(['assiette0', 'assiette1']) # plusieurs éléments

dernier = pile.depiler() # depile un élément
derniers = pile.depiler(2) # renvoie un liste des éléments enlevés (du premier enlevé au dernier)

pile.est_vide() 
len(pile) 
pile.vider() 

print(pile) # affiche : (Pile:...,...,...), du premier à dépiler jusqu'au dernier
```

### III - La _file_

Les fonctionnalités de la classe `File` sont montrées dans le code suivant : 

```python
file = File(...) # vous avez compris

file.enfiler(...)  # comme pour les piles
derniers = file.defiler(...) 

file.est_vide()
len(file)
file.vider()

print(file) # produit l'affichage : (File:...,...,...), l'avant de la queue est à droite 
```

### VI - L'_arbre binaire de recherche_

Dans le bloc de code suivant est détaillé le fonctionnement de la classe `ARB` :  

```python
arbre = ARB(...) # avec des nombres car sinon les valeurs ne sont pas comparables
arbre.inserer(...)

arbre.est_vide()
arbre.vider()

arbre.taille() # 0 s'il est vide, 1 s'il possède une racine, en général le nombre de noeuds
arbre.hauteur() # la taille de la plus longue branche

arbre.rechercher(9) # renvoie la profondeur de la valeur 9 dans l'arbre (et 0 si elle n'y est pas) 

# les parcours prennent en argument une fonction qui décide ce qu'elle fait de la valeur
# voici des exemples :

arbre.parcours_prefixe(lambda valeur : print(valeur)) # affiche toutes les valeurs

liste = []
arbre.parcours_infixe(lambda valeur : liste.append(valeur)) # ajoute toutes la valeurs à liste

def fonction(valeur):
  if (valeur % 2) == 0:
    print(valeur)

arbre.parcours_suffixe(fonction)

arbre.parcours_largeur(lambda x : print(x**3))

# enfin on peut afficher l'arbre à l'aide de la méthode suivante
arbre.afficher()
```

Voilà le type d'affichage que produit la fonction :  

```console
            955
           /
          /
         /
        /
       /
      /
     /
    /
   /
  /
 /
901
 \
  \
   \                 467
    \               /
     \             /
      \           44
       \         / \   -152
        \       /   \ /
         \     /     -235
          \   /       \
           \ /         -354
            -413
             \
              \
               \     -591
                \   /
                 \ /
                  -651
```

### V - Utilisation

Pour utiliser les classes vues auparavant, il vous suffit d'avoir le fichier _"structures.py"_ dans le même dossier que votre fichier de test python. 
```python
# écrire cette ligne de code en haut de votre fichier
from structures import * 
```
## En progrès

J'essairai d'ajouter les algorithmes ou structures au fur et à mesure de l'année ...
