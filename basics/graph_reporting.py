
# %%
import networkx as nx
import json
import sys

from networkx import exception

import undirected_graphs as ug

# %%
graph_file_location='C:/Users/dowdj/OneDrive/Documents/GitHub/graph-theory-applications/basics/data/'
graph_filename='instru'

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
    ug.GraphPlot(G)
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


    print(f'Clustering:\n{nx.clustering(G)}\n')

    print(f'Clustering Histogram:\n{nx.degree_histogram(G)}\n')

    
# %%

# %%

analysis_of_graph(G)



# %%