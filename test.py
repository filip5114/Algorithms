import search
import sort
import unittest
import recursion


class TestSearch(unittest.TestCase):

    def test_binary_search_exist(self):
        item_list = range(100)
        item = 33
        index = search.binary_search(item_list=item_list, item=item)
        self.assertEqual(item_list[index], item)

    def test_binary_search_null(self):
        item_list = range(100)
        item = 200
        self.assertIsNone(search.binary_search(item_list=item_list, item=item))


class TestSort(unittest.TestCase):

    def test_selection_sort(self):
        sorted_list = sort.selection_sort([5, 3, 8, 1, 10, 22, 15])
        self.assertTrue(all(sorted_list[i] <= sorted_list[i + 1] for i in range(len(sorted_list) - 1)))


class TestRecursion(unittest.TestCase):

    def test_sum_array(self):
        array = [1, 2, 3, 4, 5, 6]
        self.assertEqual(recursion.sum_array(array), 21)

    def test_sum_array_empty(self):
        self.assertEqual(recursion.sum_array([]), 0)

    def test_count_array(self):
        array = [1, 1, 2, 3, 4, 4, 5, 6]
        self.assertEqual(recursion.count_array(array), 8)

    def test_count_array_empty(self):
        self.assertEqual(recursion.count_array([]), 0)

    def test_find_lagerst_nr(self):
        array = [1, 6, 2, 8, 2, 2, 10, 5]
        self.assertEqual(recursion.find_largest_nr(array), 10)

    def test_find_largest_nr_empty(self):
        self.assertEqual(recursion.find_largest_nr([]), 0)

if __name__ == '__main__':
    unittest.main()
