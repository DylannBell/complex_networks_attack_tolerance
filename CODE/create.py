from networkx import nx

def ER_graph(N, p):
    return nx.erdos_renyi_graph(N, p)

def SF_graph(N):
    return nx.scale_free_graph(N).to_undirected()
