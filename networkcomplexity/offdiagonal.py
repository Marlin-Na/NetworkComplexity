import networkx as nx
import numpy as np

__all__ = ['offdiagonal']

def offdiagonal(graph):
    # Reference:
    # - https://github.com/cran/QuACN/blob/master/R/offdiagonal.R
    # - https://www.sciencedirect.com/science/article/pii/S0378437108000319
    # - https://reader.elsevier.com/reader/sd/pii/S0378437106009484
    
    assert isinstance(graph, nx.Graph)

    deg = np.array(list(dict(graph.degree()).values()))
    n = len(graph)
    M = nx.adjacency_matrix(graph)

    nr = max(deg) + 1
    # the degree correlation matrix
    c_nodecor = np.zeros((nr, nr))
    for l in range(n):
        for p in range(n):
            if M[l, p] != 0 and deg[p] >= deg[l]:
                c_nodecor[deg[l], deg[p]] += 1

    # sum over upper-triangle "parallels" to the main diagonal
    a_offdiag = []
    for delta in range(nr):
        value = np.sum(c_nodecor[(range(0,(nr-delta)), range(delta,nr))])
        a_offdiag.append(value)
    a_offdiag = np.array(a_offdiag)

    prob_a = a_offdiag/np.sum(a_offdiag)

    where_not_zero = prob_a != 0
    sum_prob = np.sum(prob_a * np.log(prob_a, where=where_not_zero))
    return -sum_prob/np.log(n-1)


#graph = nx.generators.grid_2d_graph(40, 40)
#graph = nx.generators.random_regular_graph(5, 1000)
#graph = nx.generators.random_lobster(100, 0.2, 0.2)
#type(graph.adj)
#
#offdiagonal(graph)


"""
This idea is based on the observation that a straightforward quantification of the
node-degree-distribution heterogeneity would favor the equidistribution instead of
a power law.
"""