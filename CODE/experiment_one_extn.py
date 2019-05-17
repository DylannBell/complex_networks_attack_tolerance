import random
import networkx as nx
import delete
import get
import numpy as np

def init():
    facebook = read_graph('facebook_combined.txt.gz')
    fb_connected_nodes = get_most_connected_nodes(facebook)
    fb_connected_nodes = fb_connected_nodes[20:30]

    diameters = []
    recursive_attack(facebook, fb_connected_nodes, diameters)
    print(diameters)

def recursive_attack(G, connected_nodes, diameters):
        
    if len(connected_nodes) == 0:
        print("RETURNING NOW....")
        print(diameters)
        return diameters
    
    print("-----------------------")
    (node, _) = connected_nodes.pop(0)
    print("NODE : " + str(node))
    print("NO. OF NODES BEFORE : " + str(len(G.nodes())))
    G.remove_node(node)
    print("NO. OF NODES AFTER : " + str(len(G.nodes())))
    L = estimate_path_length(G)
    print("L : " + str(L))
    diameters.append(L) 
    print(diameters)

    recursive_attack(G, connected_nodes, diameters)


# average path length
def sample_path_lengths(G, trials=1000):
    nodes = list(G)

    pairs = np.random.choice(nodes, (trials, 2)) 

    lengths = [nx.shortest_path_length(G, *pair) 
               for pair in pairs]
    
    return lengths

# averages the average path length
def estimate_path_length(G, trials=1000):
    return np.mean(sample_path_lengths(G, trials))

def remove_node(G, n):
    G_local = G.copy()
    G_local.remove_node(n)
    return G_local

def get_most_connected_nodes(G):
    degrees = list(G.degree)
    degrees.sort(key=lambda tup: tup[1], reverse=True)
    return degrees    

# reads in file and generates a graph line by line
def read_graph(filename):
    G = nx.Graph()
    array = np.loadtxt(filename, dtype=int)
    G.add_edges_from(array)
    return G


init()