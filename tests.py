import unittest

from HeapSort import HeapSort


class HeapSortTests(unittest.TestCase):

    def test_empty_arr(self):
        hs = HeapSort()
        arr = ['']
        arr2 = arr.copy()
        arr2.sort()
        self.assertEqual(hs.sort(arr), arr2)

    def test_string(self):
        hs = HeapSort()
        arr = ['arr', 'data', 'string', 'heap_sort', 'sort']
        arr2 = arr.copy()
        arr2.sort()
        self.assertEqual(hs.sort(arr), arr2)

    def test_integer(self):
        hs = HeapSort()
        arr = [1, 2, 3, 11, 12, 13, 111, 913, 25]
        arr2 = arr.copy()
        arr2.sort()
        self.assertEqual(hs.sort(arr), arr2)

    def test_negative_integer(self):
        hs = HeapSort()
        arr = [-1, -23, -25, -11, -543, -32, -5234, -111111]
        arr2 = arr.copy()
        arr2.sort()
        self.assertEqual(hs.sort(arr), arr2)

    def test_dif_case_string(self):
        hs = HeapSort()
        arr = ['A', 'B', 'a', 'b', 'AA']
        arr2 = arr.copy()
        arr2.sort()
        self.assertEqual(hs.sort(arr), arr2)