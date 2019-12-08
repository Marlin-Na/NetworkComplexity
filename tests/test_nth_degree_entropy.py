import networkcomplexity as nxc
import networkx as nx

def test_eq_first_degree():

    graph = nx.generators.scale_free_graph(100)
    # Remove self loops and parallel edges
    graph.remove_edges_from(list(graph.selfloop_edges()))
    graph = nx.Graph(graph)

    assert nxc.degree_entropy(graph) == nxc.nth_degree_entropy(graph, 1)
