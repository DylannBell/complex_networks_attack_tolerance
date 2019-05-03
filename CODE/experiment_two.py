import numpy as np
import itertools
import matplotlib.pyplot as plt

import create
import get
import delete

def init(seed):
    N = 1000
    M = 7
    P = 0.3

    # need to ensure both the below have the same number of links
    ER_graph = create.ER_graph(N, P, seed)
    SF_graph = create.SF_graph(N, M, seed)

    # error tolerance
    remove_range = list(np.arange(0.0, 0.55, 0.01))
    
    # GRAPH #1
    ER_system_size = len(ER_graph)
    # ER Failure -> Finding S
    ER_Failure_S = generate_failure_S(ER_graph, remove_range, ER_system_size)
    # ER Attack -> Finding S
    ER_Attack_S = generate_attack_S(ER_graph, remove_range, ER_system_size)

    plt.plot(remove_range, ER_Failure_S, marker='^', label="ER Failure", color="b")
    plt.plot(remove_range, ER_Attack_S, marker='D', label="ER Attack", color="r")
    plt.xlabel('Fraction f of nodes removed')
    plt.ylabel('S')
    plt.legend(loc='upper right')
    plt.title("ER Graph")
    plt.show()


    # GRAPH #2
    # SF_system_size = len(SF_graph)
    # SF Failure -> Finding S
    # SF_Failure_S = generate_failure_S(SF_graph, remove_range, SF_system_size)
    # SF Attack -> Finding S
    # SF_Failure_S = generate_attack_S(SF_graph, remove_range, SF_system_size)

def generate_attack_S(G, remove_range, system_size):
    connected_nodes_list = get.most_connected_nodes(G) 
    S = []

    for f in remove_range:
        modified_graph = delete.connected_nodes(G, f, connected_nodes_list)
        size_of_lg_cluster = get.largest_cluster_len(modified_graph)
        fraction_of_system = size_of_lg_cluster/system_size
        S.append(fraction_of_system)
    
    return S

def generate_failure_S(G, remove_range, system_size):
    S = []

    for f in remove_range:
        modified_graph = delete.random_nodes(G, f)
        size_of_lg_cluster = get.largest_cluster_len(modified_graph)
        fraction_of_system = size_of_lg_cluster/system_size
        S.append(fraction_of_system)

    return S 

