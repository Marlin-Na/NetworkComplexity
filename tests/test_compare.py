import networkcomplexity as nxc
import networkx as nx
from networkcomplexity import *
from collections import namedtuple

def second_degree_entropy(graph):
    return nxc.nth_degree_entropy(graph, 2)

Result = namedtuple("Result",
    ["DegreeEntropy", "SecondDegreeEntropy",
     "TopologicalInfoContent", "Offdiagonal"])
def report(graph):
    return Result(
        degree_entropy(graph),
        second_degree_entropy(graph),
        topological_info_content(graph),
        offdiagonal(graph)
    )

def test_clique():
    graph = nx.generators.complete_graph(10)
    report(graph)

def test_grid():
    graph = nx.generators.grid_graph([5,5,5], periodic=True)
    report(graph)

    graph = nx.generators.grid_graph([3,3,3], periodic=True)
    report(graph)

def no_test_Gnp():
    file = open("compare_gnp_data.txt", "w")
    file.write("N\tp\t")
    file.write("\t".join(Result._fields))
    file.write("\n")
    def report_and_write_res(N, p):
        graph = nx.generators.gnp_random_graph(N, p)
        res = report(graph)
        file.write("{}\t{}\t".format(N, p))
        file.write("\t".join(str(r) for r in tuple(res)))
        file.write("\n")
        return res
    def report_and_write_ten_times(N, p):
        for i in range(10):
            res = report_and_write_res(N, p)
        return res # last res
    
    for N in (50, 100, 150, 200):
        for p in (0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5):
            report_and_write_ten_times(N, p)

def no_test_preferential_attach():
    #g = nx.generators.gnp_random_graph(200, 0.05)
    #len(g.edges())

    #graph = nx.generators.barabasi_albert_graph(200, int(212/100))
    #len(graph.edges())
    file = open("compare_preferential_attach_data.txt", "w")
    file.write("N\tseed_p\tm\tseed_n_edge\tn_edge\t")
    file.write("\t".join(Result._fields))
    file.write("\n")

    def report_ten_with_n_p(N, p):
        g = nx.generators.gnp_random_graph(N, p)
        seed_n_edge = len(g.edges())
        m = int(seed_n_edge/N)
        graph = nx.generators.barabasi_albert_graph(N, m)
        n_edge = len(graph.edges())

        for i in range(10):
            graph = nx.generators.barabasi_albert_graph(N, m)
            res = report(graph)
            # N seed_p m seed_n_edge n_edge
            file.write("{}\t{}\t{}\t{}\t{}\t".format(N, p, m, seed_n_edge, n_edge))
            file.write("\t".join(str(r) for r in tuple(res)))
            file.write("\n")
            file.flush()
    
    # only run 200
    for N in [200]:
        for p in (0.05, 0.15, 0.25, 0.35, 0.45):
            report_ten_with_n_p(N, p)
