
# GUI for entering graph data (u,v) and attributes
# %%

import PySimpleGUI as sg
from numpy.lib.function_base import append
import undirected_graphs as ug

import networkx as nx
import json
import sys

from graphviz import Digraph
import graphviz

# file_location='C:/Users/dowdj/OneDrive/Documents/GitHub/graph-theory-applications/basics/data/'
file_location='C:/Users/JDowd/OneDrive - Schlumberger/Programming/graph-theory-applications/basics/data/'

dot_off=False

def the_dot_display(G,G_edge_list,data=None):
    dot = Digraph(
        comment='The Round Table',
        engine='circo',
        node_attr={'color': 'white', 'style': 'filled'},
        graph_attr={'rankdir':'LR',
              'landscape':'False',
              'size':'20,16',
              'splines':'polyline'}
        )
    dot.attr('node', shape='plaintext')
    for i in G_edge_list:
        edge_label=G[i[0]][i[1]]['attr']
        dot.edge(i[0],i[1],edge_label)

    if data != None:
        dot.edge(data[0],data[1],label=data[2]['attr'])

    dot.render('test-output/round-table.gv', view=True)
    print(dot.source) 

def write_graph(G,graph_filename):

    graph_filename=graph_filename
    
    graph_file_location=file_location
    data_dict=nx.node_link_data(G)
    print(data_dict)
    graph_file=f'{graph_file_location}{graph_filename}'
    with open(graph_file,'w') as f: 
        json.dump(data_dict, f, indent=4) 




pop_up=[[sg.Text("File Name")],
          [sg.Input(key='-INPUT-0')],
          [sg.Button('Ok'), sg.Button('Quit')]]

pop_up_window=sg.Window('Window Title', pop_up)

while True:
    event, values = pop_up_window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED  or event == 'Quit':
        # break
        sys.exit()
    elif event == 'Ok':
        graph_filename=f"{values['-INPUT-0']}"
        print(graph_filename)
        break

# Define the window's contents
layout = [[sg.Text("u")],
          [sg.Input(key='-INPUT-1')],
          [sg.Text("v")],
          [sg.Input(key='-INPUT-2')],
          [sg.Text("attr:")],
          [sg.Input(key='-INPUT-3')],
          [sg.Text("amount:")],
          [sg.Input(key='-INPUT-4')],
          [sg.Text("filename:")],
          [sg.Input(key='-INPUT-5')],


          [sg.Text(size=(40,1), key='-OUTPUT-1')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# %%


# G=ug.Graphs(graph_type='ug')
graph_file_location=file_location


# graph_type='ug'
graph_type='dig'
try:
    # check if file exist
    graph_file=f'{graph_file_location}{graph_filename}'
    print(graph_file)
    with open(graph_file, "r") as read_file:
        data_dict = json.load(read_file)

    directed=True if graph_type=='dig' else False
        
    G=nx.node_link_graph(data_dict, directed=directed, multigraph=True, attrs=None)
    ug.GraphPlot(G)
    if not dot_off:
        the_dot_display(G,list(G.edges))
except FileNotFoundError:
    # raise
    # make an empty dictionary to make an empty Graph
    print('Creating empty graph')
    graph_file=f'{graph_file_location}{graph_filename}'
    G=nx.DiGraph() if graph_type == 'dig' else nx.Graph()
    # data_dict=nx.node_link_data(G)
    data_dict={}
    with open(graph_file,'w') as f: 
        json.dump(data_dict, f, indent=4)
    
    # ug.GraphPlot(G)

    
edge_list=[]

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    edge_dict={
        'attr': values['-INPUT-3'],
        'amount': values['-INPUT-4'],
    }
    data=(values['-INPUT-1'],values['-INPUT-2'],edge_dict)
    window['-OUTPUT-1'].update(f"graph edge is    {data}")
    # window['-OUTPUT-1'].update('Hello ' + values['-INPUT-0'] + "! Thanks for trying PySimpleGUI")

    # a=values['-INPUT-0']
    # # print(f'a={a}')

    edge_list.append(data)

    G.add_edges_from(edge_list)
    ug.GraphPlot(G)

    print(list(G.edges))

    if not dot_off:
        the_dot_display(G,list(G.edges),data=data)
        

 
# Finish up by removing from the screen
window.close()





# %%



write_graph(G,graph_filename=graph_filename)





# %%
