import random
import networkx as nx
import delete
import get
import numpy as np

# reads in file and generates a graph line by line
def read_graph(filename):
    G = nx.Graph()
    array = np.loadtxt(filename, dtype=int)
    G.add_edges_from(array)
    return G

def nodes_connected(G, u, v):
    return u in G.neighbors(v)

# average path length
def sample_path_lengths(G, nodes=None, trials=1000):
    if nodes is None:
        nodes = list(G)
    else:
        nodes = list(nodes)
        
    pairs = np.random.choice(nodes, (trials, 2)) 
    
    print(len(pairs))

    connected_pairs = []
    for pair in pairs:
        [u, v] = pair
        if nodes_connected(G, u, v):
            connected_pairs.append(pair)

    print(len(connected_pairs))

    lengths = [nx.shortest_path_length(G, *pair) 
               for pair in pairs]
    


    # lengths = []
    # for pair in pairs:
    #     [u, v] = pair
    #     if nodes_connected(G, u, v):
    #         lengths.append(nx.shortest_path_length(G, *pair))
    
    return lengths

# averages the average path length
def estimate_path_length(G, nodes=None, trials=1000):
    return np.mean(sample_path_lengths(G, nodes, trials))

# deletes random nodes
def random_nodes(G, f):
    G_local = G.copy()

    N = len(G_local.nodes)
    delete_amount = int(N * f)
    remove_nodes_list = random.sample(list(G_local.nodes()), delete_amount)

    for node in remove_nodes_list:
        G_local.remove_node(node)
    
    return G_local

# delete connected nodes
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

def generate_failure(G, remove_range):
    diameters = []

    for f in remove_range:
        print("--------------------------")
        print("F = " + str(f))
        print("NODES BEFORE DELETE " + str(len(G.nodes())))
        deleted_graph = random_nodes(G, f)
        print("NODES AFTER DELETE " + str(len(deleted_graph.nodes())))
        recalculated_diameter = estimate_path_length(deleted_graph, deleted_graph.nodes())
        print("RECALCULATED DIAMETER " + str(recalculated_diameter))
        diameters.append(recalculated_diameter)

    return diameters

def generate_attack(G, remove_range):
    connected_nodes_list = get.most_connected_nodes(G) 
    diameters = []

    for f in remove_range:
        print("--------------------------")
        print("F = " + str(f))
        print("NODES BEFORE DELETE " + str(len(G.nodes())))
        modified_graph = connected_nodes(G, f, connected_nodes_list)
        print("NODES AFTER DELETE " + str(len(modified_graph.nodes())))
        recalculated_diameter = estimate_path_length(modified_graph, modified_graph.nodes())
        print("RECALCULATED DIAMETER " + str(recalculated_diameter))
        diameters.append(recalculated_diameter)

    return diameters

# internet topology graph - retrieved from SNAP
print("Reading Graph...")
facebook = read_graph('facebook_combined.txt.gz')

# error tolerance
remove_range = list(np.arange(0.005, 0.055, 0.005))

# print("Error Tolerance...")
# facebook_failure_diameters = generate_failure(facebook, remove_range)
# print(facebook_failure_diameters)

print("Attack Tolerance...")
print("PATH LENGTH : " + str(estimate_path_length(facebook)))
# facebook_attack_diameters = generate_attack(facebook, remove_range)
# print(facebook_attack_diameters)