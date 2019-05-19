from networkx import nx
import numpy as np

def diameter(G):
    return nx.average_shortest_path_length(G)

def most_connected_nodes(G):
    degrees = list(G.degree)
    degrees.sort(key=lambda tup: tup[1], reverse=True)
    return degrees

def largest_cluster_len(G):
    sub_graphs_sorted = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)
    largest_cluster = sub_graphs_sorted[0]
    return len(largest_cluster)

def isolated_clusters_len(G):
    sub_graphs_sorted = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)
    
    if len(sub_graphs_sorted) == 1:
        return 0

    largest_cluster = sub_graphs_sorted[0]
    sub_graphs_sorted.remove(largest_cluster)

    subgraph_sizes = []
    for subgraph in sub_graphs_sorted:
        subgraph_size = len(subgraph)
        subgraph_sizes.append(subgraph_size)

    return np.mean(subgraph_sizes)