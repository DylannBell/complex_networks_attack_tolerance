from networkx import nx

import create
import get
import delete

def testCreate():
    N = 100
    ER = create.ER_graph(N, 0.1)
    SF = create.SF_graph(N)

    assert len(ER.nodes) == N, "ER Graph is not created properly"
    assert len(SF.nodes) == N, "SF Graph is not created properly"

def testGet(): 
    ER = create.ER_graph(100, 0.1)
    ER_diameter = nx.average_shortest_path_length(ER)

    SF = create.SF_graph(100)
    SF_diameter = nx.average_shortest_path_length(SF)

    assert get.diameter(ER) == ER_diameter, "Diameter is not measured correctly for ER graph"
    assert get.diameter(SF) == SF_diameter, "Diameter is not measured correctly for SF graph"

def testDelete():
    N = 100
    r = 0.5
    delete_amount = r * N
    remaining_nodes = N - delete_amount

    ER = create.ER_graph(N, 0.1)
    ER = delete.random_nodes(ER, r)
    assert remaining_nodes == len(ER.nodes), "Random nodes are not being correctly deleted for ER graph"

    SF = create.SF_graph(N)
    SF = delete.random_nodes(SF, r)
    assert remaining_nodes == len(SF.nodes), "Random nodes are not being correctly deleted for SF graph"


testCreate()
testGet()
testDelete()