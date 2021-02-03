'''
module for implementation
of interpolation search
algorithm
'''

def interpolation_search(arr: list, start: None, end: None, key):

    '''
    Interpolation search using
    iterative method
    '''

    if start == None:
        start = 0

    if end == None:
        end = len(arr)

    while (start <= end and key >= arr[start] and key <= arr[end]):

        dist        = key - arr[start]
        valRange    = arr[end] - arr[start]
        frac        = dist / valRange
        indexRange  = end - start
        num         = start + int(frac * indexRange)

        if (arr[num] == key):
            return num

        if (arr[num] < key):
            start = num + 1

        else:
            end = num - 1

    return -1

'''
PyAlgo
Devansh Singh, 2021
'''