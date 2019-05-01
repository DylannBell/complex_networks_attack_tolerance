from networkx import nx
import numpy as np

def diameter(G):
    return nx.average_shortest_path_length(G)
    # return np.mean(sample_path_lengths(G))

# average path length - taken from the book - need to redo
def sample_path_lengths(G, nodes=None, trials=100000):
    if nodes is None:
        nodes = list(G)
    else:
        nodes = list(nodes)
        
    pairs = np.random.choice(nodes, (trials, 2))
    lengths = [nx.shortest_path_length(G, *pair) 
               for pair in pairs]
    return lengths


def most_connected_nodes(G):
    degrees = list(G.degree)
    degrees.sort(key=lambda tup: tup[1], reverse=True)
    return degrees

# The below two functions are wrong...
def largest_cluster(G):
    l = most_connected_nodes(G)
    return l[0]

def average_size_cluster(G):
    avg_clusters = most_connected_nodes(G)[1:]
   
    avg_cluster_size = len(avg_clusters)
    avg_cluster_sum = sum([cluster[1] for cluster in avg_clusters])

    return float(avg_cluster_sum/avg_cluster_size)