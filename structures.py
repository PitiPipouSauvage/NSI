from collections.abc import Iterable

# Les noeuds
 
class Noeud:
    def __init__(self, valeur, suivant = None):
        self.valeur = valeur
        self.suivant = suivant

class NoeudBinaire:
    def __init__(self, valeur, gauche = None, droit = None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

# ----- Liste ----- #

class Liste:
    def __init__(self, valeurs = []):
        self.debut = None
        self.etendre(valeurs)
        
    def vider(self, valeurs = []):
        self.__init__(valeurs)
    
    def etendre(self, valeurs):
        self.inserer(len(self), valeurs)
        
    def inserer(self, index, valeurs):
        if not isinstance(valeurs, Iterable):
            valeurs = [valeurs]
        elif not valeurs:
            return

        if self.debut == None:
            self.debut = Noeud(valeurs[0])
            valeurs = valeurs[1:]

        i = 0
        noeud = self.debut
        while i < index-1:
            i += 1
            if noeud.suivant == None:
                raise IndexError
            else:
                noeud = noeud.suivant
            
        for valeur in valeurs:
            noeud.suivant = Noeud(valeur, noeud.suivant)
            noeud = noeud.suivant 
    
    def est_vide(self):
        return len(self) == 0

    # par default

    def __getitem__(self, item):
        if isinstance(item, int):
            
            if item >= len(self):
                raise IndexError
            
            noeud = self.debut
            i = 0

            while i < item:
                noeud = noeud.suivant
                i += 1

            return noeud.valeur

        elif isinstance(item, slice):

            taille = len(self)
            
            if item.start == None: start = 0
            else:
                if -taille <= item.start <= taille:
                    start = item.start % taille               
                else:
                    raise IndexError

            if item.stop == None: stop = taille 
            else:
                if -taille <= item.stop <= taille:
                    stop = item.stop % taille
                else:
                    raise IndexError

            if item.step == None: step = 1
            else:
                if item.step < 1:
                    raise NotImplemented
                step = item.step
            
            liste = Liste()
            noeud = self.debut
            i = 0
            
            while i < start:
                noeud = noeud.suivant
                i += 1
    
            while i < stop:
                if ((i - start) % step) == 0:
                    liste.etendre(noeud.valeur)
                noeud = noeud.suivant
                i += 1

            return liste
        else:
            raise TypeError
        

    def __iter__(self):
        noeud = self.debut
        
        while noeud != None:
            yield noeud.valeur
            noeud = noeud.suivant

    def __repr__(self):
        return str(self)
        
    def __str__(self):
        chaine = '(Liste:'
        
        for valeur in self:
            chaine += f' {valeur},'
            
        chaine = chaine[:-1] + ')'
        return chaine

    def __len__(self):
        i = 0
        
        for valeur in self:
            i += 1

        return i

# ----- Pile ----- #

class Pile: 
    def __init__(self, valeurs = []):
        self.sommet = None
        self.empiler(valeurs)

    def vider(self, valeurs = []):
        self.__init__(valeurs)

    def empiler(self, valeurs):
        if not isinstance(valeurs, Iterable):
            valeurs = [valeurs]
        elif not valeurs:
            return

        if self.sommet == None:
            self.sommet = Noeud(valeurs[0])
            valeurs = valeurs[1:]

        for valeur in valeurs:
            self.sommet = Noeud(valeur, self.sommet)    
        
    def depiler(self, quantite = 1):
        if quantite < 1:
            return

        if quantite > len(self):
            raise IndexError
        
        elements = []
        i = 0
        
        while i < quantite:
            elements.append(self.sommet.valeur)
            self.sommet = self.sommet.suivant
            i += 1

        if quantite == 1:
            return elements[0]
        
        return elements

    def est_vide(self):
        return len(self) == 0
    
    # par default

    def __repr__(self):
        return str(self)

    def __str__(self):
        chaine = '(Pile:' 
        noeud = self.sommet

        while noeud != None:
            chaine += f' {noeud.valeur},'
            noeud = noeud.suivant

        chaine = chaine[:-1] + ')'
        return chaine

    def __len__(self):
        i = 0
        noeud = self.sommet

        while noeud != None:
            i += 1
            noeud = noeud.suivant
            
        return i

# ----- File ----- #

class File:
    def __init__(self, valeurs = []):
        self.tete = None
        self.enfiler(valeurs)

    def vider(self, valeurs = []):
        self.__init__(valeurs)

    def enfiler(self, valeurs):
        if not isinstance(valeurs, Iterable):
            valeurs = [valeurs]
        elif not valeurs:
            return

        if self.tete == None:
            self.tete = Noeud(valeurs[0])
            valeurs = valeurs[1:]

        noeud = self.tete
        while noeud.suivant != None:
            noeud = noeud.suivant

        for valeur in valeurs:
            noeud.suivant = Noeud(valeur)
            noeud = noeud.suivant

    def defiler(self, quantite = 1):
        if quantite < 1:
            return

        if quantite > len(self):
            raise IndexError
        
        elements = []
        i = 0

        while i < quantite:
            elements.append(self.tete.valeur)
            self.tete = self.tete.suivant
            i += 1

        if quantite == 1:
            return elements[0]
                
        return elements

    def est_vide(self):
        return len(self) == 0

    # par default

    def __repr__(self):
        return str(self)

    def __str__(self):
        chaine = ''
        noeud = self.tete

        while noeud != None:
            chaine = f' {noeud.valeur},' + chaine
            noeud = noeud.suivant

        chaine = ('(File:' + chaine)[:-1] + ')'
        return chaine

    def __len__(self):
        i = 0
        noeud = self.tete

        while noeud != None:
            noeud = noeud.suivant
            i += 1

        return i

# ----- ABR ----- #
    

class ABR:
    def __init__(self, valeurs = []):
        self.racine = None
        self.inserer(valeurs)
        
    def vider(self, valeurs = []):
        self.__init__(valeurs)

    def inserer(self, valeurs = []):
        if not isinstance(valeurs, Iterable):
            valeurs = [valeurs]
        elif not valeurs:
            return
        
        if self.racine == None:
            self.racine = NoeudBinaire(valeurs[0])
            valeurs = valeurs[1:]
            
        for valeur in valeurs:
            noeud = self.racine

            while True:
                if valeur < noeud.valeur:
                    
                    if noeud.gauche == None:
                        noeud.gauche = NoeudBinaire(valeur)
                        break

                    else:
                        noeud = noeud.gauche
                        continue

                if valeur > noeud.valeur:

                    if noeud.droit == None:
                        noeud.droit = NoeudBinaire(valeur)
                        break

                    else:
                        noeud = noeud.droit
                        continue
                break

    def est_vide(self):
        return self.racine == None

    def taille(self):

        def interne(noeud):
            if noeud == None:
                return 0

            return interne(noeud.gauche) + interne(noeud.droit) + 1
        
        return interne(self.racine)

    def hauteur(self):

        def interne(noeud):
            if noeud == None:
                return 0

            return max(interne(noeud.gauche), interne(noeud.droit)) + 1

        return interne(self.racine)

    def parcours_prefixe(self, fonction = lambda x : print(x)):

        def interne(noeud, fonction):
            fonction(noeud.valeur)
            
            if noeud.gauche != None:
                interne(noeud.gauche, fonction)

            if noeud.droit != None:
                interne(noeud.droit, fonction)

        if not self.est_vide():
            interne(self.racine, fonction)            

    def parcours_infixe(self, fonction):

        def interne(noeud, fonction):
            if noeud.droit != None:
                interne(noeud.droit, fonction)
                
            fonction(noeud.valeur)

            if noeud.gauche != None:
                interne(noeud.gauche, fonction)

        if not self.est_vide():
            interne(self.racine, fonction)

    def parcours_suffixe(self, fonction):

        def interne(noeud, fonction):
            if noeud.gauche != None:
                interne(noeud.gauche, fonction)

            if noeud.droit != None:
                interne(noeud.droit, fonction)
            
            fonction(noeud.valeur)

        if not self.est_vide():
            interne(self.racine, fonction)

    def parcours_largeur(self, fonction):
        file = File(self.racine)
        
        while not file.est_vide():
            noeud = file.defiler()
            fonction(noeud.valeur)
                
            if noeud.gauche != None:
                file.enfiler(noeud.gauche)

            if noeud.droit != None:
                file.enfiler(noeud.droit)

    def rechercher(self, valeur):
        profondeur = 0
        noeud = self.racine
        
        while noeud != None:
            profondeur += 1
            if valeur == noeud.valeur:
                return profondeur
            if valeur < noeud.valeur:
                noeud = noeud.gauche
            else:
                noeud = noeud.droit

        return profondeur

    def afficher(self):
        def vide(ligne):
            for caractere in ligne:
                if caractere != ' ':
                    return False
            return True


        def decalage(profondeur, cache = [1]):
            if len(cache) > profondeur:
                return cache[profondeur]

            cache.append(sum([decalage(i) for i in range(profondeur)])+profondeur)
            return cache[profondeur]

        def inserer(source, destination, emplacement):
            if len(destination) < emplacement + len(source):
                destination += ' ' * (emplacement+len(source)-len(destination))
            
            return destination[:emplacement] + source + destination[emplacement+len(source):] 

        def dessiner(noeud, rang, colone, profondeur, hauteur, tableau):
            tableau[rang] = inserer(str(noeud.valeur), tableau[rang], colone)
            
            if noeud.droit != None:
                suivant = colone + decalage(hauteur-profondeur-1)
                r = rang
                c = colone

                while c < suivant:
                    c += 1
                    r -= 1
                    tableau[r] = inserer('/', tableau[r], c)
                   
                dessiner(noeud.droit, r-1, c+1, profondeur+1, hauteur, tableau)
                
            if noeud.gauche != None:
                suivant = colone + decalage(hauteur-profondeur-1)
                r = rang
                c = colone

                while c < suivant:
                    c += 1
                    r += 1
                    tableau[r] = inserer('\\', tableau[r], c)

                dessiner(noeud.gauche, r+1, c+1, profondeur+1, hauteur, tableau)
            
            
        valeurs = []
        self.parcours_infixe(lambda valeur : valeurs.append(valeur))
        
        hauteur = self.hauteur()

        if hauteur == 0:
            return
        if hauteur == 1:
            print(self.racine)
            return

        lignes = decalage(hauteur)
        tableau = [""] * lignes

        dessiner(self.racine, lignes//2, 0, 1, hauteur, tableau)

        for ligne in tableau:
            if not vide(ligne):
                print(ligne)
                
