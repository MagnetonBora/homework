import unittest
from ClassWeightedGraph import *
from MinimumSpanningTree import *

# https://www.ics.uci.edu/~eppstein/PADS/MinimumSpanningTree.py


class TestSpanningTree(unittest.TestCase):
    
    def setUp(self):
        self.graph = WeightedGraph()
        #TODO initialize the graph as you like
        # and add what you want


    def test_something(self):
        G = {
                0: {1:11, 2:13, 3:12},
                1: {0:11, 3:14},
                2: {0:13, 3:10},
                3: {0:12, 1:14, 2:10}
            }
        T = [(2, 3), (0, 1), (0, 3)]

        minimum_spaning_tree = GetMinimumSpanningTree(G)

        print(minimum_spaning_tree)
        for e, f in zip(minimum_spaning_tree, T):
            print(e, f)

        self.assertEqual(
            minimum_spaning_tree,
            {0: {1: 11, 3: 12}, 1: {0: 11}, 2: {3: 10}, 3: {0: 12, 2: 10}}
        )

    def test_something_else(self):
        pass


if __name__ == '__main__':
    unittest.main()
