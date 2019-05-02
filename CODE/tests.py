from networkx import nx
import random
import numpy as np

import create
import get
import delete

# set seed
# networkx uses a combination of random and numpy.random libraries for random number generation
seed = 123
random.seed(seed)
np.random.seed(seed)

# NEED TO REDO : create.SF_graph(N, seed) -> create.SF_graph(N, M, seed)

def init():
    N = 50
    ER = create.ER_graph(N, 0.1, seed)
    SF = create.SF_graph(N, seed)
    
    testCreate(N, ER, SF)

    testGet(N, ER, SF)

    testDelete()

def testCreate(N, ER, SF):    
    assert len(ER.nodes) == N, "ER Graph is not created properly"
    assert len(SF.nodes) == N, "SF Graph is not created properly"

def testGet(N, ER, SF): 
    
    ER_diameter = nx.average_shortest_path_length(ER)
    SF_diameter = nx.average_shortest_path_length(SF)

    # diameter
    assert get.diameter(ER) == ER_diameter, "Diameter is not measured correctly for ER graph"
    assert get.diameter(SF) == SF_diameter, "Diameter is not measured correctly for SF graph"

    # most connected nodes - assum N = 50, may differ across machines (rand. isn't going to be the same across different hardware)
    ER_most_connected = [(0, 9), (1, 9), (7, 9), (20, 8), (6, 7), (11, 7), (14, 7), 
                        (18, 7), (24, 7), (30, 7), (8, 6), (15, 6), (16, 6), (26, 6), 
                        (29, 6), (31, 6), (33, 6), (43, 6), (46, 6), (47, 6), (2, 5), 
                        (9, 5), (10, 5), (17, 5), (19, 5), (22, 5), (25, 5), (28, 5), 
                        (37, 5), (39, 5), (42, 5), (44, 5), (48, 5), (4, 4), (5, 4), 
                        (13, 4), (21, 4), (23, 4), (32, 4), (35, 4), (41, 4), (45, 4), 
                        (49, 4), (3, 3), (27, 3), (34, 3), (36, 3), (38, 3), (40, 3), (12, 2)]
    assert get.most_connected_nodes(ER) == ER_most_connected

    SF_most_connected = [(0, 33), (2, 25), (1, 16), (3, 8), (4, 6), (5, 6), (14, 6), 
                        (9, 5), (13, 5), (10, 4), (6, 3), (17, 3), (23, 3), (24, 3), (30, 3), 
                        (34, 3), (38, 3), (12, 2), (15, 2), (16, 2), (18, 2), (20, 2), (21, 2), 
                        (25, 2), (27, 2), (7, 1), (8, 1), (11, 1), (19, 1), (22, 1), (26, 1), 
                        (28, 1), (29, 1), (31, 1), (32, 1), (33, 1), (35, 1), (36, 1), (37, 1), 
                        (39, 1), (40, 1), (41, 1), (42, 1), (43, 1), (44, 1), (45, 1), (46, 1), 
                        (47, 1), (48, 1), (49, 1)]
    assert get.most_connected_nodes(SF) == SF_most_connected

    # largest cluster - not sure if implementation is correct
    # print(get.largest_cluster(ER))
    # print(get.largest_cluster(ER))

    # average size cluster - not sure if implementation is correct
    # print(get.average_size_cluster(ER))

def testDelete():
    N = 100
    M = 5
    r = 0.5
    delete_amount = r * N
    remaining_nodes = N - delete_amount

    ER = create.ER_graph(N, 0.1, seed)
    SF = create.SF_graph(N, M, seed)
    
    ER_list = get.most_connected_nodes(ER)[1:5]
    ER_deleted = delete.connected_nodes(ER, ER_list)
    ER_nodes = len(ER)   
    ER_remaining_nodes = len(ER_deleted)
    assert ER_nodes - 4 == ER_remaining_nodes, "Connected nodes has not been correctly implemented" 
   
    SF_list = get.most_connected_nodes(SF)[1:5]
    SF_deleted = delete.connected_nodes(SF, SF_list)
    SF_nodes = len(SF)   
    SF_remaining_nodes = len(SF_deleted)
    assert SF_nodes - 4 == SF_remaining_nodes, "Connected nodes has not been correctly implemented" 

    ER = create.ER_graph(N, 0.1, seed)
    SF = create.SF_graph(N, seed)

    ER_random_delete = delete.random_nodes(ER, r)
    assert remaining_nodes == len(ER_random_delete.nodes), "Random nodes are not being correctly deleted for ER graph"
    SF_random_delete = delete.random_nodes(SF, r)
    assert remaining_nodes == len(SF_random_delete.nodes), "Random nodes are not being correctly deleted for SF graph"

init()
