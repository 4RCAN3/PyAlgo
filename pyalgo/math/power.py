'''
module for calculating
x to the power y (x ** y)
efficiently
'''

def big_power(x: int, y: int, MOD = None):

    '''
    For calculating powers where
    x and y are large numbers
    '''

    result = 1

    if MOD is None:

        while (y > 0):
            if (y & 1):
                result *= x
            x *= x
            y >>= 1

    else:

        while (y > 0):
            if (y & 1):
                result *= x
            x *= x
            y >>= 1

        result %= MOD

    return result

def mod_power(x: int, y:int, MOD: int):

    '''
    For calculating powers where
    modular arithmetic is used
    '''

    result = ((x % MOD) ** (y % MOD)) % MOD
    return result

'''
PyAlgo
Devansh Singh, 2021
'''