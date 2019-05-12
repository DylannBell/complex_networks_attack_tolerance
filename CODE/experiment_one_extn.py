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

def diameter(G):
    return nx.average_shortest_path_length(G)

def remove_random_nodes(G, node_list, nodes_deleted, remove_amount, diameters):
    print("------------------------------------------------")
    delete_node = node_list.pop(0)
    G_updated = G.copy()
    G_updated.remove_node(delete_node)

    if nodes_deleted > 81306 * 0.01:
        return diameters

    if nx.is_connected(G_updated) == True:
        print("Remove node")
        nodes_deleted = nodes_deleted + 1
        if nodes_deleted in remove_amount:
            diameter = diameter(G_updated)
            diameters.append(diameter)
            print("Diameter Appended : " + diameter)
        remove_random_nodes(G, node_list, nodes_deleted, remove_amount, diameters)

    if nx.is_connected(G_updated) == False:
        print("Don't remove node")
        remove_random_nodes(G, node_list, nodes_deleted, remove_amount, diameters)    



# internet topology graph - retrieved from SNAP
print("Reading Graph....")
twitter = read_graph('twitter_combined.txt.gz')
print("Remove nodes...")
remove_nodes_list = random.sample(list(twitter.nodes()), round(0.1* float(len(twitter.nodes))))
remove_amount = [0.005 * float(len(twitter.nodes())), 0.01 * float(len(twitter.nodes()))]
print(remove_random_nodes(twitter, remove_nodes_list, 0, remove_amount, []))




