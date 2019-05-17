import random
import networkx as nx
import delete
import get
import numpy as np
import matplotlib.pyplot as plt

def init():
    facebook = read_graph('facebook_combined.txt.gz')
    N = len(facebook.nodes())

    # ATTACK
    facebook_attack = facebook.copy()
    fb_connected_nodes = get_most_connected_nodes(facebook_attack)
    update_connected_nodes(facebook_attack, N, fb_connected_nodes)
    filtered_connected_nodes = fb_connected_nodes[0:20]

    facebook_attack_diameters = []
    recursive_attack(facebook_attack, filtered_connected_nodes, facebook_attack_diameters)
    print(facebook_attack_diameters)

    # FAILURE
    facebook_failure = facebook.copy()
    fb_nodes = list(facebook_failure.nodes())[0:20]
    random.shuffle(fb_nodes)

    facebook_failure_diameters = []
    recursive_failure(facebook_failure, fb_nodes, facebook_failure_diameters)
    print(facebook_failure_diameters)

    # facebook_attack_diameters = [4.188, 4.608, 4.896, 5.16, 5.501, 5.549, 5.431, 5.355, 5.43, 5.652, 5.578, 5.499, 5.468, 5.516, 5.439, 5.466, 5.457, 5.614, 5.563, 5.426]
    # facebook_failure_diameters = [3.948, 3.899, 3.916, 4.037, 3.965, 3.925, 3.959, 4.078, 3.881, 4.082, 3.942, 4.018, 3.914, 3.958, 4.002, 3.951, 4.019, 3.941, 3.988, 3.907]
    # x = range(0, len(facebook_attack_diameters))
    # generate_graph(facebook_attack_diameters, facebook_failure_diameters, x)
    
def generate_graph(attack, failure, x):
    plt.plot(x, failure, marker='^', label="Facebook Failure", color="b")
    plt.plot(x, attack, marker='D', label="Facebook Attack", color="r")
    plt.xlabel('X')
    plt.ylabel('Diameter d Of Largest Subgraph')
    plt.legend(loc='upper right')
    plt.title("Failure & Attack On Facebook Graph")
    plt.show()

def recursive_failure(G, random_nodes, diameters):
    # break recursion
    if len(random_nodes) == 0:
        return diameters
    
    # remove node
    node = random_nodes.pop(0)
    G.remove_node(node)

    subgraphs = nx.connected_component_subgraphs(G)  
    subgraph_diameters = []

    for subgraph in subgraphs:
        L = estimate_path_length(subgraph)
        if L != 0.0:
            subgraph_diameters.append(L)

    L = max(subgraph_diameters)
    diameters.append(L) 

    # continue recursion
    recursive_failure(G, random_nodes, diameters)

def recursive_attack(G, connected_nodes, diameters):
    # break recursion
    if len(connected_nodes) == 0:
        return diameters
    
    # remove node
    (node, _) = connected_nodes.pop(0)
    G.remove_node(node)

    subgraphs = nx.connected_component_subgraphs(G)  
    subgraph_diameters = []

    for subgraph in subgraphs:
        L = estimate_path_length(subgraph)
        if L != 0.0:
            subgraph_diameters.append(L)

    L = max(subgraph_diameters)
    diameters.append(L)

    # continue recursion
    recursive_attack(G, connected_nodes, diameters)

# filter the connected nodes for only those within a certain lower and upperbound
# Maybe able to delete
def filter_connected_nodes(connected_nodes, lower_bound, upper_bound):
    filtered_connected_nodes = []

    for (node, f) in connected_nodes:
        if lower_bound <= f <= upper_bound:
            print("ADDING : " + str((node, f)))
            filtered_connected_nodes.append((node, f))

    return filtered_connected_nodes

def update_connected_nodes(G, N, connected_nodes):
    for index, (node, links) in enumerate(connected_nodes):
        fraction = round(links/N, 4)
        connected_nodes[index] = (node, fraction)


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