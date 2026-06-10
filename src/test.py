import unittest
from selection_sort import selection_sort

class TestCases(unittest.TestCase):
    def test(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(selection_sort(arr), expected)
    
    def test_empty(self):
        arr = []
        expected = []
        self.assertEqual(selection_sort(arr), expected)

    def test_single_element(self):
        arr = [42]
        expected = [42]
        self.assertEqual(selection_sort(arr), expected)

    def test_sorted(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(selection_sort(arr), expected)

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(selection_sort(arr), expected)

if __name__ == '__main__':
    unittest.main()