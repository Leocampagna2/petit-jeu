import random as rd

class Jeu:
    """
    Parameters
    ----------
    elle sert à activer le jeu

    """

    def __init__(self, m):
        """
       

        Parameters
        ----------
        m : INT
            DESCRIPTION.

        Returns
        -------
        None.

        Example
        -------
        >>> jeu = Jeu(10)

        """
        self.k = rd.randint(0, m)


    def test(self, k):
        """
        Compare le nombre deviné  avec le nombre à deviner
       

        Parameters
        ----------
        k : INT

        Returns*
        --------
        booléen: True si les nombres sont égaux et False dans le cas contraire

        Example
        -------
        >>> jeu = Jeu(10)
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
                return False
            if k > self.k:
               print("Trop Grand")
               return False
        print("Tu as gagné")
        return True


if __name__ == '__main__':  
    import doctest
    doctest.testmod()
    jeu = Jeu(10)
    jeu.test(4)

