import random
import numpy as np
import matplotlib.pyplot as plt

import create
import get
import delete

seed = 123
random.seed(seed)
np.random.seed(seed)

def experiment_one():
    N = 1000
    P = 0.5

    # need to ensure both the below have the same number of links
    ER_graph = create.ER_graph(N, P, seed)
    SF_graph = create.SF_graph(N, seed)

    # error tolerance
    remove_range = list(np.arange(0.005, 0.055, 0.005))

    # ISSUES - 
    # need to fix get diameter : don't think it's working properly
    # need to ensure graphs are being generated properly

    # ER Failure
    # ER_failure_diameters = generate_failure(ER_graph, remove_range)
    # graph(remove_range, ER_failure_diameters, 'Failure')

    # ER Attack
    # ER_attack_diameters = generate_attack(ER_graph, remove_range)
    # graph(remove_range, ER_attack_diameters, 'Attack')

def graph(x, y, title):
    plt.plot(x, y, marker='o')
    plt.xlabel('Fraction f of nodes removed')
    plt.ylabel('Diameter d')
    plt.title(title)
    plt.show()

def generate_attack(G, remove_range):
    connected_nodes_list = get.most_connected_nodes(G) 
    diameters = []

    for f in remove_range:
        modified_graph = delete.connected_nodes(G, f, connected_nodes_list)
        recalculated_diameter = get.diameter(modified_graph)
        diameters.append(recalculated_diameter)

    return diameters

def generate_failure(G, remove_range):
    diameters = []

    for f in remove_range:
        deleted_graph = delete.random_nodes(G, f)
        recalculated_diameter = get.diameter(deleted_graph)
        diameters.append(recalculated_diameter)

    return diameters

experiment_one()