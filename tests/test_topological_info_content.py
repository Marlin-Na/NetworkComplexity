import networkcomplexity as nxc
import networkx as nx
import numpy as np

def test_get_topology():
    from networkcomplexity.topological_info_content import _get_topology

    def test_local(graph):
        topology = _get_topology(graph)
        assert isinstance(topology, dict)
        nodes = iter(list(graph.nodes()))
        for key in topology.keys():
            assert key == next(nodes)
        try:
            next(nodes)
            assert False
        except StopIteration:
            assert True
    
        assert isinstance(topology[0], np.recarray)

        for top_each_node in topology.values():
            assert len(top_each_node) == len(graph) - 1

    graph = nx.generators.connected_caveman_graph(3, 3)
    test_local(graph)

    graph = nx.generators.scale_free_graph(100)
    test_local(graph)


def test_vertex_orbits():
    from networkcomplexity.topological_info_content import vertex_orbits

    def test_local(graph):
        orbits = vertex_orbits(graph)
        assert len(graph) == sum([len(x) for x in orbits])

    graph = nx.generators.connected_caveman_graph(3, 3)
    test_local(graph)

    graph = nx.generators.cycle_graph(10)
    test_local(graph)

    graph = nx.generators.complete_graph(10)
    test_local(graph)

    graph = nx.generators.grid_2d_graph(3, 3, periodic=True)
    test_local(graph)

    graph = nx.generators.grid_2d_graph(3, 3, periodic=False)
    test_local(graph)

    graph = nx.generators.scale_free_graph(100)
    test_local(graph)
