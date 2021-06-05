
# GUI for entering graph data (u,v) and attributes
# %%

import PySimpleGUI as sg
from numpy.lib.function_base import append
import undirected_graphs as ug

import networkx as nx
import json
import sys

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
graph_file_location='C:/Users/dowdj/OneDrive/Documents/GitHub/graph-theory-applications/basics/data/'


graph_type='ug'
try:
    # check if file exist
    graph_file=f'{graph_file_location}{graph_filename}'
    print(graph_file)
    with open(graph_file, "r") as read_file:
        data_dict = json.load(read_file)
    G=nx.node_link_graph(data_dict, directed=False, multigraph=True, attrs=None)
    ug.GraphPlot(G)
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
    # G=nx.node_link_graph(data_dict, directed=False, multigraph=True, attrs=None)
    ug.GraphPlot(G)



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

 
# Finish up by removing from the screen
window.close()

def write_graph(G,graph_filename):

    graph_filename=graph_filename
    
    graph_file_location='C:/Users/dowdj/OneDrive/Documents/GitHub/graph-theory-applications/basics/data/'
    data_dict=nx.node_link_data(G)
    print(data_dict)
    graph_file=f'{graph_file_location}{graph_filename}'
    with open(graph_file,'w') as f: 
        json.dump(data_dict, f, indent=4) 

# %%



write_graph(G,graph_filename=graph_filename)



# traverse all edges of a graph is via the neighbors
# a='attr'
# for n, nbrsdict in G.G.adjacency():
#     for nbr, eattr in nbrsdict.items():
#         if a in eattr:
#         # Do something useful with the edges
#             print(eattr)
        




# %%
