import unittest
import collections

from UnionFind import UnionFind
from ClassWeightedGraph import WeightedGraph
from MinimumSpanningTree import GetMinimumSpanningTree


class TestSpanningTree(unittest.TestCase):
    
    def setUp(self):
        self.graph = WeightedGraph()
        self.graph.AddEdge(0, 1, 11)
        self.graph.AddEdge(0, 2, 13)
        self.graph.AddEdge(0, 3, 12)
        self.graph.AddEdge(0, 0, 11)
        self.graph.AddEdge(1, 3, 14)
        self.graph.AddEdge(2, 0, 13)
        self.graph.AddEdge(2, 3, 10)
        self.graph.AddEdge(3, 0, 12)
        self.graph.AddEdge(3, 1, 14)
        self.graph.AddEdge(3, 2, 10)


    def test_generated_proper_minimum_spaning_tree(self):
        expected_result = {0: {1: 11, 3: 12}, 1: {0: 11}, 2: {3: 10}, 3: {0: 12, 2: 10}}
        minimum_spaning_tree = GetMinimumSpanningTree(self.graph)
        self.assertEqual(minimum_spaning_tree, expected_result)

    def test_type_of_result_graph_is_weighted_graph(self):
        minimum_spaning_tree = GetMinimumSpanningTree(self.graph)
        self.assertIsInstance(minimum_spaning_tree, WeightedGraph)

    def test_generated_mst_has_proper_total_length(self):
        expected_result = 34
        minimum_spaning_tree = GetMinimumSpanningTree(self.graph)
        self.assertEqual(minimum_spaning_tree.totalLengthUpperBound, expected_result)


class TestWeightedGraph(unittest.TestCase):

    def test_initial_total_graph_length_is_one(self):
        graph = WeightedGraph()
        expected_result = 1
        self.assertEqual(graph.totalLengthUpperBound, expected_result)

    def test_initial_set_of_vertices_is_empty(self):
        graph = WeightedGraph()
        expected_result = []
        self.assertEqual(list(graph.Vertices()), expected_result)

    def test_set_vertex_is_added_to_graph(self):
        graph = WeightedGraph()
        expected_result = [42]
        graph.AddVertex(42)
        self.assertEqual(list(graph.Vertices()), expected_result)

    def test_has_vertex_returns_proper_result(self):
        graph = WeightedGraph()
        graph.AddVertex(42)
        self.assertTrue(graph.HasVertex(42))

    def test_has_edge_returns_proper_result(self):
        graph = WeightedGraph()
        graph.AddEdge(1, 2, 42)
        self.assertTrue(graph.HasEdge(1, 2))

    def test_edge_length_returns_proper_result(self):
        graph = WeightedGraph()
        expected_result = 42
        graph.AddEdge(1, 2, 42)
        self.assertEqual(graph.EdgeLength(1, 2), expected_result)

    def test_vertices_returns_proper_set(self):
        graph = WeightedGraph()
        graph.AddVertex(1)
        graph.AddVertex(2)
        graph.AddVertex(3)
        expected_result = [1, 2, 3]
        self.assertEqual(list(graph.Vertices()), expected_result)

    def test_adjacent_vertices_returns_proper_set(self):
        graph = WeightedGraph()
        graph.AddEdge(1, 2, 10)
        graph.AddEdge(1, 3, 11)
        graph.AddEdge(1, 4, 12)
        expected_result = [2, 3, 4]
        adjacent_vertices = list(graph.AdjacentVertices(1))
        self.assertEqual(adjacent_vertices, expected_result)

    def test_total_length_upper_bound_returns_proper_result(self):
        graph = WeightedGraph()
        graph.AddEdge(1, 2, 10)
        graph.AddEdge(2, 4, 20)
        expected_result = 31
        self.assertEqual(graph.totalLengthUpperBound, expected_result)


class TestUnionFind(unittest.TestCase):

    def test_proper_initial_params(self):
        union_find = UnionFind()
        self.assertEqual(union_find.weights, {})
        self.assertEqual(union_find.parents, {})

    def test_getitem_when_object_not_in_set(self):
        union_find = UnionFind()
        new_object = 'Test_item'        
        self.assertEqual(union_find[new_object], new_object)
        self.assertEqual(union_find.parents, {new_object: new_object})
        self.assertEqual(union_find.weights, {new_object: 1})

    def test_getitem_returns_proper_root(self):
        union_find = UnionFind()
        union_find.union('parent', 'first_child')
        union_find.union('first_child', 'last_child')
        self.assertEqual(union_find['parent'], 'parent')
        self.assertEqual(union_find['first_child'], 'parent')
        self.assertEqual(union_find['last_child'], 'parent')

    def test_check_if_instance_is_iterable(self):
        union_find = UnionFind()
        self.assertIsInstance(union_find, collections.Iterable)

    def test_union(self):
        union_find = UnionFind()
        union_find = UnionFind()
        union_find.union('parent', 'child')
        self.assertEqual(union_find['parent'], 'parent')
        self.assertEqual(union_find['child'], 'parent')        


if __name__ == '__main__':
    unittest.main()
