import networkx as nx
import numpy as np

__all__ = ['degree_entropy']

def degree_entropy(graph):
    """
    First degree-based entropy
    https://link.springer.com/article/10.1007/s12190-018-1168-x
    """
    assert isinstance(graph, nx.Graph)
    degrees = [degree for node, degree in nx.degree(graph)]
    from collections import Counter
    degree_counts = list(Counter(degrees).values())

    def entropy_from_count(counts):
        p_counts = counts/np.sum(counts)
        return - np.sum(p_counts * np.log2(p_counts))

    return entropy_from_count(degree_counts)
