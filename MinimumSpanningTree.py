import unittest
from ClassWeightedGraph import *
from UnionFind import UnionFind

def MinimumSpanningTree(G):
    # Kruskal's algorithm: sort edges by weight, and add them one at a time.
    # We use Kruskal's algorithm, first because it is very simple to
    # implement once UnionFind exists, and second, because the only slow
    # part (the sort) is sped up by being built in to Python.
    subtrees = UnionFind()
    tree = []
    for W,u,v in sorted((G[u][v],u,v) for u in G for v in G[u]):
        if subtrees[u] != subtrees[v]:
            tree.append((u,v))
            subtrees.union(u,v)
    return tree


def GetMinimumSpanningTree(graph):
    subtrees = UnionFind()
    spanningTree = WeightedGraph()
    sorted_weighted_edges_list = sorted(
        (graph[u][v], u, v) for u in graph for v in graph[u]
    )
    for W, u, v in sorted_weighted_edges_list:
        if subtrees[u] != subtrees[v]:
            spanningTree.AddEdge(u, v, W)
            subtrees.union(u, v)
    return spanningTree
