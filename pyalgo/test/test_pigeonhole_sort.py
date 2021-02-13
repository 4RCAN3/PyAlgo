
'''
module for testing
sort.pigeonhole_sort.py from
pyalgo math module
'''

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import unittest
from sort.pigeonhole_sort import pigeonhole_sort

class TestPigeonholesort(unittest.TestCase):

    def test_pigeonhole_sort(self):
        result = pigeonhole_sort([3, 5, 4, 1, 2])

        self.assertEqual(result, [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()

'''
PyAlgo
Devansh Singh, 2021
'''
