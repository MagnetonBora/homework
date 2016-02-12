import unittest

from UnionFind import UnionFind
from ClassWeightedGraph import WeightedGraph


def GetMinimumSpanningTree(graph):
    subtrees = UnionFind()
    spanningTree = WeightedGraph()
    sorted_weighted_edges_list = sorted(
        [(u, v, graph[u][v]) for u in graph for v in graph[u]],
        key=lambda item: item[-1]
    )
    for u, v, w in sorted_weighted_edges_list:
        if subtrees[u] != subtrees[v]:
            spanningTree.AddEdge(u, v, w)
            subtrees.union(u, v)
    return spanningTree
