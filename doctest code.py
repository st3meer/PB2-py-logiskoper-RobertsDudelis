from doctest import testmod
def parbaudit_koordinati(koord_x: float) -> bool:
    # sourcery skip: assign-if-exp, boolean-if-exp-identity, remove-unnecessary-cast
    """
    funkcija parbauda vai x pieder (3.9, +bezgaliba) diapazonam
    >>> parbaudit_koordinati(1.3)
    False
    >>> parbaudit_koordinati(3.9)
    False
    >>> parbaudit_koordinati(9)
    True
    """
    
    if koord_x > 3.9:
        return True
    else:
        return False
testmod(verbose=True)
vertiba = float(input())
if parbaudit_koordinati(vertiba):
    print('ir ')
else:
    print('nav')