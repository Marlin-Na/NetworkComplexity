import networkcomplexity as nxc
import networkx as nx
import numpy as np

def test_get_topology():
    from networkcomplexity.topological_info_content import _get_topology
    graph = nx.generators.connected_caveman_graph(3, 3)
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

def test_get_orbits():
    from networkcomplexity.topological_info_content import _get_topology, _get_orbits
    #graph = nx.generators.connected_caveman_graph(3, 3)
    #graph = nx.generators.cycle_graph(10)
    #graph = nx.generators.complete_graph(10)
    #graph = nx.generators.grid_2d_graph(3, 3, periodic=True)
    graph = nx.generators.scale_free_graph(100)
    orbits = _get_orbits(_get_topology(graph))
    assert len(graph) == sum([len(x) for x in orbits])
