from networkx import nx
import random

def random_nodes(G, f, L):
    G_local = G.copy()

    N = len(G_local.nodes)
    delete_amount = int(N * f)
    count = 1

    for node in L:
        G_local.remove_node(node)

        if count >= delete_amount:
            break
        else:
            count = count + 1
    
    return G_local
 

def connected_nodes(G, f, L):          
    G_local = G.copy()

    N = len(G_local.nodes)
    delete_amount = int(N * f)
    count = 1

    for (node, _) in L:
        G_local.remove_node(node)
            
        if count >= delete_amount:
            break
        else:
            count = count + 1

    return G_local