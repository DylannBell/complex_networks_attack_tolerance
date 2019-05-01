from networkx import nx

def ER_graph(N, p, seed):
    return nx.erdos_renyi_graph(N, p, seed)

def SF_graph(N, seed):
    return nx.scale_free_graph(N).to_undirected()
