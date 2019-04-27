from networkx import nx

def diameter(G):
    return nx.average_shortest_path_length(G)

def most_connected_nodes(G):
    degrees = list(G.degree)
    return degrees.sort(key=lambda tup: tup[1], reverse=True)

def largest_cluster(G):
    return max(nx.connected_component_subgraphs(G), key=len)

# def average_size_cluster(G):
