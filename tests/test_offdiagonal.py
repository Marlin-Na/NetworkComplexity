import networkcomplexity as nxc
import networkx as nx

def test_periodic_grid():
    ## A lattice should have value zero
    graph = nx.generators.grid_2d_graph(10, 10, periodic=True)
    value = nxc.offdiagonal(graph)
    assert value == 0

def test_clique():
    ## Fully connected graph should have value zero
    graph = nx.generators.complete_graph(100)
    value = nxc.offdiagonal(graph)
    assert value == 0
