import unittest, search, sort


class TestSearch(unittest.TestCase):

    def test_binary_search_exist(self):
        itemList = range(100)
        item = 33
        index = search.binary_search(itemList=itemList, item=item)
        self.assertEqual(itemList[index], item)

    def test_binary_search_null(self):
        itemList = range(100)
        item = 200
        self.assertIsNone(search.binary_search(itemList=itemList, item=item))


class TestSort(unittest.TestCase):

    def test_selection_sort(self):
        sortedList = sort.selectionSort([5, 3, 8, 1, 10, 22, 15])
        self.assertTrue(all(sortedList[i] <= sortedList[i+1] for i in range(len(sortedList) - 1)))

if __name__ == '__main__':
    unittest.main()
