from networkx import nx

def ER_graph(N, p, seed):
    return nx.erdos_renyi_graph(N, p, seed)

def SF_graph(N, M, seed):
    return nx.barabasi_albert_graph(N, M, seed)