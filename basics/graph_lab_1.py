
# %%
import networkx as nx
import matplotlib.pyplot as plt
import logging

from networkx.classes.function import neighbors

import undirected_graphs as ug
# %%

def get_from_dict(data_dict,graph_type):

        h=nx.from_dict_of_dicts(data_dict,create_using=nx.DiGraph) if graph_type=='dig' else nx.from_dict_of_dicts(data_dict,create_using=nx.Graph)       
        return nx.from_dict_of_dicts(data_dict,h)


# %%
# H=ug.Graphs(graph_type='dig')
# %%

data={'CELL': {'console': {'attr': 'HasA', 'color': ''}}, 'console': {'monitor': {'attr': 'HasA', 'color': ''}, 'PC': {'attr': 'HasA', 'color': ''}, 'UPS': {'attr': 'HasA', 'color': ''}}, 'monitor': {}, 'PC': {}, 'UPS': {}, 'cameraPC': {'PC': {'attr': 'IsA', 'color': ''}}, 'daqPC': {'PC': {'attr': 'IsA', 'color': ''}}, 'cameraMonitor': {'monitor': {'attr': 'IsA', 'color': ''}}, 'daqMonitor': {'monitor': {'attr': 'IsA', 'color': ''}}}
H=get_from_dict(data, graph_type='dig')
    
# %%



# %%
