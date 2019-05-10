import numpy as np
import itertools
import matplotlib.pyplot as plt

import create
import get
import delete

def init(seed):
    N = 1000
    M = 7
    #M = 2
    P = 0.002
    # need to ensure both the below have the same number of links
    ER_graph_big_S = create.ER_graph(N, P, seed)
    #SF_graph_big_S = create.SF_graph(N, M, seed)
    ER_graph_small_s = create.ER_graph(N, P, seed)
    #SF_graph_small_s = create.SF_graph(N, M, seed)

    # error tolerance
    remove_range = list(np.arange(0.0, 1, 0.01))
    
    # GRAPH #1
    ER_system_size = len(ER_graph_big_S)
    # ER Failure -> Finding S
    ER_Failure_big_S = generate_failure_big_S(ER_graph_big_S, remove_range, ER_system_size)
    ER_Failure_small_s = generate_failure_small_s(ER_graph_small_s, remove_range)

    # ER Attack -> Finding S
    ER_Attack_big_S = generate_attack_big_S(ER_graph_big_S, remove_range, ER_system_size)
    ER_Attack_small_s = generate_attack_small_s(ER_graph_small_s, remove_range)
    
    plt.plot(remove_range, ER_Failure_big_S, marker='^', linestyle = 'None', label="ER Failure S", color="b", markerfacecolor='none')
    plt.plot(remove_range, ER_Attack_big_S, marker='D', linestyle = 'None', label="ER Attack S", color="r", markerfacecolor='none')
    plt.plot(remove_range, ER_Failure_small_s, marker='^', linestyle = 'None', label="ER Failure <s>", color="b",)
    plt.plot(remove_range, ER_Attack_small_s, marker='D', linestyle = 'None', label="ER Attack <s>", color="r")
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

def generate_attack_big_S(G, remove_range, system_size):
    connected_nodes_list = get.most_connected_nodes(G) 
    S = []

    for f in remove_range:
        modified_graph = delete.connected_nodes(G, f, connected_nodes_list)
        size_of_lg_cluster = get.largest_cluster_len(modified_graph)
        fraction_of_system = size_of_lg_cluster/system_size
        S.append(fraction_of_system)
    
    return S

def generate_failure_big_S(G, remove_range, system_size):
    S = []

    for f in remove_range:
        modified_graph = delete.random_nodes(G, f)
        size_of_lg_cluster = get.largest_cluster_len(modified_graph)
        fraction_of_system = size_of_lg_cluster/system_size
        S.append(fraction_of_system)

    return S 

def generate_attack_small_s(G, remove_range):
    connected_nodes_list = get.most_connected_nodes(G) 
    S = []

    for f in remove_range:
        modified_graph = delete.connected_nodes(G, f, connected_nodes_list)
        avg_isolated_cluster = get.isolated_clusters_len(modified_graph)
        S.append(avg_isolated_cluster)
    
    return S

def generate_failure_small_s(G, remove_range):
    S = []
    N = len(G.nodes)

    for i, f in enumerate(remove_range):
        delete_amount = int(N * f)
        
        if i == 0:
            modifed_graph = delete.random_nodes(G, delete_amount)
        else:
            modifed_graph = delete.random_nodes(modified_graph, delete_amount)

        avg_isolated_cluster = get.isolated_clusters_len(modified_graph)
        S.append(avg_isolated_cluster)

    return S 