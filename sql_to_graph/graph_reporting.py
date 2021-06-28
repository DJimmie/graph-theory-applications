
# %%
import networkx as nx
import json
import sys

from networkx import exception

# import undirected_graphs as ug

from sql_to_graph import GraphPlot as gp
import support_pkg.file_access as fac



# %%
graph_file_location=fac.graph_file_location
graph_filename='press_sensors.json'
graph_filename='press_ctrl_sensors.json'
graph_filename='emrData3.json'

# graph_type='ug'
graph_type='dig'
try:
    # check if file exist
    graph_file=f'{graph_file_location}{graph_filename}'
    print(graph_file)
    with open(graph_file, "r") as read_file:
        data_dict = json.load(read_file)

    directed=True if graph_type=='dig' else False
        
    G=nx.node_link_graph(data_dict, directed=directed, multigraph=False, attrs=None)
    gp(G)
except FileNotFoundError:
    print('You Need A File')


def node_neigbors(H,node):

    # for nbr in H[node]:
    #     print(nbr)

    return [x for x in H[node]]

def analysis_of_graph(G):
    try:
        print(f'Connected Components:\n{list(nx.connected_components(G))}\n')
    except Exception as err:
        print(err)

    node=['HYP Chamber Lid Seals']
    # print(list(G.predecessors(node)))
    # print(f'Count of {node}: {len(list(G.predecessors(node)))}')

    # print([f'Count of {x}: {len(list(G.predecessors(x)))}' for x in node])
    print(nx.info(G))

    # print(f'Clustering:\n{nx.clustering(G)}\n')
    # print(f'Clustering Histogram:\n{nx.degree_histogram(G)}\n')

    a='HYP Chamber Lid Seals'
    print(f'{a}:\n{list(G.successors(a))}')
    
    print([f'Count of {x}: {len(list(G.successors(x)))}' for x in node])

    
# %%

# %%

analysis_of_graph(G)

node_neigbors(G,'Pneumatic Valve Assembly (60KSI Needle Valve)')



# %%