
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

data={'018-21': {'2021-06-01': {'attr': 'hasStartDate', 'color': ''}, '2021-06-15': {'attr': 'hasStopDate', 'color': ''}, 'CELL13': {'attr': 'hasTestLocation', 'color': ''}, 'Jim Dowd': {'attr': 'hasTechnician', 'color': ''}, 'Ramsis II': {'attr': 'hasEngineer', 'color': ''}, 'Approved': {'attr': 'hasStatus', 'color': ''}, 'Pending': {'attr': 'hasTestPhase', 'color': ''}, 'Subsea': {'attr': 'hasProductGroup', 'color': ''}, 
'20 KSI': {'attr': 'hasWorkingPressure', 'color': ''}, '500°F': {'attr': 'hasMaxTemp', 'color': ''}, '20KSI-123456': {'attr': 'hasPressureSensor', 'color': ''}, '20KSI-987654': {'attr': 'hasPressureSensor', 'color': ''}, 'TP-01 Wireline': {'attr': 'hasTestProcedure', 'color': ''}, 'ASSY-01 Wireline': {'attr': 'hasAssyProcedure', 'color': ''}, '018-21 Binder': {'attr': 'hasDocumentation', 'color': ''}, 'Safety Hazards': {'attr': 'hasA', 'color': ''}}, '2021-06-01': {}, '2021-06-15': {}, 'CELL13': {}, 'Jim Dowd': {}, 'Ramsis II': {}, 'Approved': {}, 'Pending': {}, 'Subsea': {}, '20 KSI': {}, '500°F': {}, '20KSI-123456': {'20 KSI': {'attr': 'hasWorkingPressure', 'color': ''}, 'Pressure Transducer': {'attr': 'isA', 'color': ''}}, '20KSI-987654': {'20 KSI': {'attr': 'hasWorkingPressure', 'color': ''}, 'Pressure Transducer': {'attr': 'isA', 'color': ''}}, 'TP-01 Wireline': {'018-21 Binder': {'attr': 'isLocatedIn', 'color': ''}}, 'ASSY-01 Wireline': {'018-21 Binder': {'attr': 'isLocatedIn', 'color': ''}}, '018-21 Binder': {}, 'Safety Hazards': {'018-21 Binder': {'attr': 'isLocatedIn', 'color': ''}}, 'Pressure Transducer': {}}

H=get_from_dict(data, graph_type='ug')

ug.GraphPlot(H)
    
# %%

# H=nx.MultiGraph()


# %%

# %%
