from networkx import nx
import random

def random_nodes(G, f):
    N = len(G.nodes)
    delete_amount = int(N * f)
    remove_nodes_list = random.sample(range(N - 1), delete_amount)

    for node in remove_nodes_list:
        G.remove_node(node)
    
    return G

# def connected_nodes(G, L):
    