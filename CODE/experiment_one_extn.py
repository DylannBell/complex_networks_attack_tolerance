import random
import networkx as nx
import delete
import get
import numpy as np
import matplotlib.pyplot as plt

def init():
    facebook = read_graph('facebook_combined.txt.gz')
    N = len(facebook.nodes())
    remove_range = list(np.arange(0.00, 0.055, 0.005))

    # ATTACK
    facebook_attack_diameters = generate_attack(facebook, N, remove_range)
    print(facebook_attack_diameters)

    # FAILURE
    facebook_failure_diameters = generate_failure(facebook, N, remove_range)
    print(facebook_failure_diameters)

    # GRAPHING
    generate_graph(facebook_attack_diameters, facebook_failure_diameters, remove_range)

def generate_graph(attack, failure, x):
    plt.plot(x, failure, marker='s', label="Facebook Failure", color="b")
    plt.plot(x, attack, marker='o', label="Facebook Attack", color="r")
    plt.xlabel('Fraction of nodes removed')
    plt.ylabel('Diameter d Of Largest Subgraph')
    plt.legend(loc='upper right')
    plt.title("Failure & Attack On Facebook Graph")
    plt.show()

def generate_failure(G, num_nodes, range):
    diameters = []

    for f in range:
        G_random_nodes = list(G.nodes())
        random.shuffle(G_random_nodes)

        G_modified = delete.random_nodes(G, f, G_random_nodes)
        diameter = max_subgraph_diameter(G_modified)
        diameters.append(diameter)
    
    return diameters

def generate_attack(G, num_nodes, range):
    diameters = []

    for f in range:
        G_connected_nodes = get.most_connected_nodes(G)
        G_modified = delete.connected_nodes(G, f, G_connected_nodes)
        diameter = max_subgraph_diameter(G_modified)
        diameters.append(diameter)

    return diameters


def max_subgraph_diameter(G):
    subgraphs = nx.connected_component_subgraphs(G)
    subgraph_diameters = []
    
    for subgraph in subgraphs:
        L = estimate_path_length(subgraph)
        if L != 0.0:
            subgraph_diameters.append(L)

    L = max(subgraph_diameters)
    return L

def read_graph(filename):
    G = nx.Graph()
    array = np.loadtxt(filename, dtype=int)
    G.add_edges_from(array)
    return G

def sample_path_lengths(G, trials=1000):
    nodes = list(G)

    pairs = np.random.choice(nodes, (trials, 2)) 

    lengths = [nx.shortest_path_length(G, *pair) 
               for pair in pairs]
    
    return lengths

def estimate_path_length(G, trials=1000):
    return np.mean(sample_path_lengths(G, trials))


init()