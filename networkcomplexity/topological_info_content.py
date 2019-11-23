import networkx as nx
import numpy as np
from collections import deque

__all__ = ['topological_info_content']

def topological_info_content(graph):
    """
    The structural information content Ig(X) of a graph X is defined as the
    entropy of the finite probability scheme constructed from the orbits of
    its automorphism group G(X).
    - https://link.springer.com/article/10.1007/BF02476948

    The equivalence classes of the vertices of a graph G under the action of
    the automorphisms are called vertex orbits.
    - http://www.cs.columbia.edu/~cs4203/files/GT-Lec2.pdf

    R source code:
    - https://github.com/cran/QuACN/blob/master/R/topologicalInfoContent.R
    """
    assert isinstance(graph, nx.Graph)

    top = _get_topology(graph)
    orbits = _get_orbits(top)
    On = np.array([len(x) for x in orbits]) # orbits
    pis = On/np.sum(On)
    Iorb = - np.sum(pis * np.log2(pis)) # entropy
    return Iorb

def _get_topology(graph):
    assert isinstance(graph, nx.Graph)

    # distance matrix
    dist = nx.algorithms.floyd_warshall_numpy(graph)
    # degree
    deg = np.array(list(dict(graph.degree()).values()))

    nodes = graph.nodes()
    ans = []
    for vi in range(len(nodes)):
        dist_vi = np.asarray(dist[vi, ]).reshape(-1)
        max_dist = np.max(dist_vi)
        idx_nonzero_dist = dist_vi != 0
        dist_vi = dist_vi[idx_nonzero_dist]
        deg_vi = deg[idx_nonzero_dist]

        joined = np.rec.fromarrays([dist_vi, deg_vi], names=["dist", "deg"])
        joined.sort(order=["dist", "deg"]) # sort by dist then deg
        ans.append(joined)
    return dict(zip(nodes, ans))

def _get_orbits(topology):
    rest = deque(topology.keys()) # The nodes
    #top = list(topology.values())
    erg = []
    while len(rest):
        rem = []
        vi = rest.popleft()
        erg_tmp = [vi]
        for j in reversed(range(len(rest))):
            if np.all(topology[vi] == topology[rest[j]]):
                erg_tmp.append(rest[j])
                del rest[j]
        erg_tmp.sort()
        erg.append(erg_tmp)
    return erg
