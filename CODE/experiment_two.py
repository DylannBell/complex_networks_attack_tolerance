import numpy as np
import itertools
import matplotlib.pyplot as plt
import random

import create
import get
import delete

def init(seed):
    N = 1000
    M = 7
    # M = 2
    P = 0.002
    remove_range = list(np.arange(0.0, 1, 0.01))

    # ER
    # ER = create.ER_graph(N, P, seed)
    # ER_system_size = len(ER)

    # ER_Failure_big_S = generate_failure_big_S(ER, remove_range, ER_system_size)
    # ER_Attack_big_S = generate_attack_big_S(ER, remove_range, ER_system_size)
    # ER_Failure_small_s = generate_failure_small_s(ER, remove_range)
    # ER_Attack_small_s = generate_attack_small_s(ER, remove_range)
    # generate_graph("ER Graph", remove_range, ER_Failure_big_S, ER_Attack_big_S, ER_Failure_small_s, ER_Attack_small_s)
    
    # SF
    # SF = create.SF_graph(N, M, seed)
    # SF_system_size = len(SF)

    # SF_Failure_big_S = generate_failure_big_S(SF, remove_range, SF_system_size)
    # SF_Attack_big_S = generate_attack_big_S(SF, remove_range, SF_system_size)
    # SF_Failure_small_s = generate_failure_small_s(SF, remove_range)
    # SF_attack_small_s = generate_attack_small_s(SF, remove_range)
    # generate_graph("SF Graph", remove_range, SF_Failure_big_S, SF_Attack_big_S, SF_Failure_small_s, SF_attack_small_s)


def generate_graph(name, remove_range, Failure_big_S, Attack_big_S, Failure_small_s, Attack_small_s):
    plt.plot(remove_range, Failure_big_S, marker='^', linestyle = 'None', label="ER Failure S", color="b", markerfacecolor='none')
    plt.plot(remove_range, Attack_big_S, marker='D', linestyle = 'None', label="ER Attack S", color="r", markerfacecolor='none')
    plt.plot(remove_range, Failure_small_s, marker='^', linestyle = 'None', label="ER Failure <s>", color="b",)
    plt.plot(remove_range, Attack_small_s, marker='D', linestyle = 'None', label="ER Attack <s>", color="r")
    plt.xlabel('Fraction f of nodes removed')
    plt.ylabel('S')
    plt.legend(loc='upper right')
    plt.title(name)
    plt.show()

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
        G_random_nodes = list(G.nodes())
        random.shuffle(G_random_nodes)
        modified_graph = delete.random_nodes(G, f, G_random_nodes)
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

    for f in remove_range:
        G_random_nodes = list(G.nodes())
        random.shuffle(G_random_nodes)
        modified_graph = delete.random_nodes(G, f, G_random_nodes)
        avg_isolated_cluster = get.isolated_clusters_len(modified_graph)
        S.append(avg_isolated_cluster)
    
    return S