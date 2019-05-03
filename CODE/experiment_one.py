import numpy as np
import itertools
import matplotlib.pyplot as plt

import create
import get
import delete

def init(seed):
    N = 300
    M = 7
    P = 0.1

    # need to ensure both the below have the same number of links
    ER_graph = create.ER_graph(N, P, seed)
    SF_graph = create.SF_graph(N, M, seed)

    # error tolerance
    remove_range = list(np.arange(0.005, 0.055, 0.005))

    # ER Failure
    ER_failure_diameters = generate_failure(ER_graph, remove_range)
   
    # ER Attack
    ER_attack_diameters = generate_attack(ER_graph, remove_range)
    
    # SF Failure
    SF_failure_diameters = generate_failure(SF_graph, remove_range)

    # SF Attack
    SF_attack_diameters = generate_attack(SF_graph, remove_range)

    graph_data = [ER_failure_diameters, ER_attack_diameters, SF_failure_diameters, SF_attack_diameters]
    generate_graph(remove_range, graph_data)

def generate_failure(G, remove_range):
    diameters = []

    for f in remove_range:
        modified_graph = delete.random_nodes(G, f)
        recalculated_diameter = get.diameter(modified_graph)
        diameters.append(recalculated_diameter)

    return diameters

def generate_attack(G, remove_range):
    connected_nodes_list = get.most_connected_nodes(G) 
    diameters = []

    for f in remove_range:
        modified_graph = delete.connected_nodes(G, f, connected_nodes_list)
        recalculated_diameter = get.diameter(modified_graph)
        diameters.append(recalculated_diameter)

    return diameters

def generate_graph(x, graph_data):    
    
    plt.plot(x, graph_data[0], marker='^', label="ER Failure", color="b")
    plt.plot(x, graph_data[1], marker='D', label="ER Attack", color="r")
    plt.plot(x, graph_data[2], marker='s', label="SF Failure",color="b")
    plt.plot(x, graph_data[3], marker='o', label="SF Attack",color="r")   
    plt.xlabel('Fraction f of nodes removed')
    plt.ylabel('Diameter d')
    plt.legend(loc='upper right')
    plt.title("Failure & Attack On SF & ER Graph")
    plt.show()
