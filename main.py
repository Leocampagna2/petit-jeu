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
        0 <= m <=10

        """
        self.k = rd.randint(0, m)


if __name__ == '__main__':  
    import doctest
    doctest.testmod()
   
