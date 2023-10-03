from doctest import testmod



def parbaudit(koord_x:float) -> bool:
    """
    >>> parbaudit(3.9)
    False
    >>> parbaudit(4)
    True
    >>> parbaudit(3)
    False

    """
        
    if koord_x > 3.9:
        print(True)
    else:
        print(False)


testmod(verbose=True) 
parbaudit(float(input("ievadiet skaitli: ")))

