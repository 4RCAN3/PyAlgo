'''
module for implementation
of binary search
algorithm
'''

def binary_search(arr: list, start: None, end: None, key):

    '''
    Binary search implementation
    using iterative method
    '''

    if start == None:
        start = 0

    if end == None:
        end = len(arr)

    while (start <= end):

        mid = int(start + ((end - start) / 2))

        if (arr[mid] < key):
            start = mid + 1

        elif arr[mid] > key:
            end = mid - 1

        else:
            return mid

    return -1

'''
PyAlgo
Neemesh Yadav, 2021
'''