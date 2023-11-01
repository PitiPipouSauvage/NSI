# NSI
Ce dépôt contient toutes les implémentations python des structures et algorithmes vus en cours. Le but est de faciliter la réutilisation d'algorithmes ou de structures dans d'autres algorithmes et de fournir un exemple d'implémentation de ceux-ci. Ce fichier est un guide d'utilisation des classes et fonctions présentes dans les différents fichiers.

## Structures
Dans le fichier `structure.py` on retrouve 4 classes utiles :
• `Liste` représentant la structure linéaire "liste chainée" (ou linked-list en anglais)
• `Pile` représentant la structure linéaire "pile" (ou stack en anglais)
• `File` représentant la structure linéaire "file" (ou queue en anglais)
• `ABR` représentant la structure "arbre binaire de recherche"

### Liste
Pour la classe `Liste`, elle regroupe la majorité des fonction des `list` de python.
Pour en créer une instance, on peut utiliser toutes les méthodes du bloc suivant : 

```python
# créer une liste vide
liste0 = Liste() # équivalent à : liste0 = []

# créer une liste avec un élément
liste1 = Liste(1) # équivalent à : liste1 = [1]

# créer une liste contenant des éléments par défaut
liste2 = Liste(['a', 'ab', 'abc']) # équivalent à : liste1 = ['a', 'ab', 'abc']

liste3 = Liste(liste1) # remplis la liste avec les élements de liste1
# cela marche avec tous les classes itérables
```

