import search
import sort
import unittest
import recursion
import graphs
import util


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


class TestGraph(unittest.TestCase):

    def test_bfs(self):
        graph = {
            'ja': ['tomasz', 'ewa'],
            'tomasz': ['natalia', 'adrian'],
            'ewa': ['madzia', 'karol'],
            'madzia': ['karol', 'natalia', 'adrian'],
            'adrian': ['mietek'],
            'natalia': [],
            'mietek': [],
            'karol': []
        }
        self.assertIs(graphs.bfs(graph, 'ja'), 'mietek')

    def test_dijkstra(self):
        graph = {
            'start': {
                'A': 5,
                'B': 2,
            },
            'A': {
                'C': 4,
                'D': 2,
            },
            'B': {
                'A': 8,
                'D': 7,
            },
            'C': {
                'D': 6,
                'Meta': 3,
            },
            'D': {
                'Meta': 1,
            },
            'Meta': {}
        }
        costs = {
            'A': 5,
            'B': 2,
            'C': float('inf'),
            'D': float('inf'),
            'Meta': float('inf'),
        }
        parents = {
            'A': 'Start',
            'B': 'Start',
            'C': None,
            'D': None,
            'Meta': None,
        }
        self.assertEqual(graphs.dijsktra(graph=graph, costs=costs, parents=parents)['Meta'], 8)


class TestUtil(unittest.TestCase):

    def find_smallest(self):
        arr = [5, 3, 8, 2, 10]
        self.assertEqual(util.find_smallest(arr), 3)

    def test_find_lowest_cost_node(self):
        costs = {
            'A': 5,
            'B': 2,
            'C': 4,
            'D': float('inf'),
        }
        self.assertEqual(util.find_lowest_cost_node(costs), 'B')

if __name__ == '__main__':
    unittest.main()
