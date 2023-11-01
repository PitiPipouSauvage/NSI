# NSI
Ce dépôt contient toutes les implémentations python des structures et algorithmes vus en cours. Le but est de faciliter la réutilisation d'algorithmes ou de structures dans d'autres algorithmes et de fournir un exemple d'implémentation de ceux-ci.   
Ce fichier est un guide d'utilisation des classes et fonctions présentes dans les différents fichiers.

## Les structures
Dans le fichier _"structure.py"_ on retrouve 4 classes utiles :  
• `Liste` représentant la structure linéaire _liste chainée_ (ou _linked-list_ en anglais)  
• `Pile` représentant la structure linéaire _pile_ (ou _stack_ en anglais)  
• `File` représentant la structure linéaire _file_ (ou _queue_ en anglais)  
• `ABR` représentant la structure _arbre binaire de recherche_  (ou _binary tree_ en anglais)
  
### La _liste chainée_
Pour la classe `Liste`, elle regroupe la majorité des fonction des `list` de python.
Pour en créer une instance, on peut utiliser toutes les méthodes du bloc suivant :   
   
```python 
# créer une liste chainée vide
liste0 = Liste()

# créer une liste chainée avec un élément
liste1 = Liste(1) 

# créer une liste chainée contenant des éléments par défaut
liste2 = Liste(['abc', 2, ('taple', 0)])

liste3 = Liste(liste1) # remplis liste3 avec les éléments de liste1
# cela marche avec tous les classes itérables
```  
  
On peut accéder aux valeurs d'une instance de la classe `Liste` des manières suivantes :  
  
```python
liste = Liste(...) # une liste chainée contenant des élements (ou non)

# accéder à un élément
i = ...
print(liste[i])

# traverser la liste
for valeur in liste: 
  print(valeur)    

# toutes les slices à pas positifs fonctionnent
print(liste[i:]) # elle renvoie une liste chainée
```
   
On peut ajouter des valeurs à la liste comme suit :
```python

```
