import random as rd

class Jeu:
    """
    Classe représentant un jeu de devinette.

    Parameters
    ----------
    m : INT -> nombre maximum à choisir
    n : INT -> nombre d'essais maximum
    """

    def __init__(self, m, n):
        """
        Initialise un jeu avec un nombre à deviner aléatoire et un nombre d'essais.

        Parameters
        ----------
        m : INT -> nombre max à choisir 
        n : INT -> nombre d'essais

        Returns
        -------
        None

        Example
        -------
        >>> jeu = Jeu(10, 4)
        """
        self.k = rd.randint(0, m)
        self.n = n

    def test(self, k):
        """
        Compare le nombre deviné avec le nombre à deviner.

        Parameters
        ----------
        k : INT

        Returns
        -------
        booléen: True si les nombres sont égaux, False sinon

        Example
        -------
        >>> jeu = Jeu(10, 4)
        >>> jeu.k = 5
        >>> jeu.test(6)
        Trop Grand
        False
        >>> jeu.test(2)
        Trop Petit
        False
        >>> jeu.test(5)
        Tu as gagné
        True
        """
        if k != self.k:        
            if k < self.k:
                print('Trop Petit')
            if k > self.k:
               print("Trop Grand")
            return False
        else:
            print("Tu as gagné")
            return True
    
    def jouer(self):
        """
        Lance le jeu en permettant au joueur de deviner jusqu'à ce qu'il gagne ou qu'il atteigne le nombre d'essais maximum.
        """
        n = 0
        while n < self.n:
            try:
                k = int(input('Entre un nombre : '))
                if self.test(k):
                    break
                n += 1
            except ValueError:
                print("Ceci n'est pas un entier")
        else:
            print("Désolé, tu as épuisé tous tes essais.")


if __name__ == '__main__':  
    import doctest
    doctest.testmod()
    jeu = Jeu(10, 4)
    jeu.jouer()
