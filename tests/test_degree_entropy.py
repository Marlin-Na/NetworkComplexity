import networkcomplexity as nxc
import networkx as nx

def test_clique():
    ## Fully connected graph should have value zero
    graph = nx.generators.complete_graph(100)
    nxc.degree_entropy(graph)
    assert value == 0

def test_simple():
    graph = nx.Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    res = nxc.degree_entropy(graph)
    ## degree are [1,1,2], counts [2,1]
    from math import log2
    assert float(res) - float(log2(3) - (log2(1)*1/3 + log2(2)*2/3)) < 0.00000000001
