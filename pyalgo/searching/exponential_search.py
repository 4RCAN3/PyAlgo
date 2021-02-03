'''
module for implementation
of exponential search
algorithm
'''

from binary_search import *

def exponential_search(arr: list, start: None, end: None, key):

    '''
    Exponential search method
    using iterative moethod
    '''

    if start == None:
        start = 0

    if end == None:
        end = len(arr)

    if (end - start <= 0):

        return -1

    num = 1

    while (num < end - start):
        
        if (arr[num] < key):
            num *= 2

        else:
            break

    return binary_search(arr, num // 2, num, key)

'''
PyAlgo
Devansh Singh, 2021
'''