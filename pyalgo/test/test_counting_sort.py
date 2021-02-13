
'''
module for testing
sort.counting_sort.py from
pyalgo math module
'''

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from sort.counting_sort import counting_sort

class TestCountingsort(unittest.TestCase):

    def test_counting_sort(self):
        result = counting_sort([3, 5, 4, 1, 2])

        self.assertEqual(result, [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()

'''
PyAlgo
Devansh Singh, 2021
'''
