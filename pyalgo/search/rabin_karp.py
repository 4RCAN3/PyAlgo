'''
module for implementation
of Rabin Karp algorithm
for pattern searching
'''

CHAR = 256

def rabin_karp(pattern: str, text: str):

    '''
    searches all occurences
    of pattern in text, returns
    list of indexes
    '''

    prime = 101

    len_pat     = len(pattern)
    len_txt     = len(text)
    hash_pat    = 0
    hash_txt    = 0
    num         = 1
    result      = []

    for i in range (len_pat - 1):
        num = (num * CHAR) % prime

    for i in range (len_pat):
        hash_pat = (CHAR * hash_pat + ord(pattern[i])) % prime
        hash_txt = (CHAR * hash_txt + ord(text[i])) % prime

    for i in range (len_txt - len_pat + 1):

        if (hash_pat == hash_txt):

            for j in range (len_pat):

                if (text[i + j] != pattern[j]):
                    break

                else:
                    j += 1

            if (j == len_pat):
                result.append(i)

        if (i < len_txt - len_pat):

            hash_txt = (CHAR * (hash_txt - ord(text[i]) * num)) + ord(text[i + len_pat]) % prime

            if (hash_txt < 0):
                hash_txt += prime

    return result

'''
PyAlgo
Devansh Singh, 2021
'''