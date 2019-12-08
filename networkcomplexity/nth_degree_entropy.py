import networkx as nx
import numpy as np

__all__ = ['nth_degree_entropy']

def nth_degree_entropy(graph, nth):
    """
    n-th degree-based entropy
    https://link.springer.com/article/10.1007/s12190-018-1168-x
    """
    assert isinstance(graph, nx.Graph)

    # distance matrix
    dist = nx.algorithms.floyd_warshall_numpy(graph)
    dist = np.array(dist, dtype=np.int)
    max_dist = int(np.max(dist))

    from collections import Counter
    degree_byorder_bynode = list()
    for one_dist in dist:
        degree_byorder = Counter(one_dist)
        degree_byorder_bynode.append(degree_byorder)
    
    nth = int(nth)
    nth_degrees = [d[nth] for d in degree_byorder_bynode]
    nth_degree_counts = list(Counter(nth_degrees).values())

    return entropy_from_count(nth_degree_counts)

def entropy_from_count(counts):
    p_counts = counts/np.sum(counts)
    return - np.sum(p_counts * np.log2(p_counts))
    
