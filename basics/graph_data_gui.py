
# GUI for entering graph data (u,v) and attributes
# %%

import PySimpleGUI as sg
from numpy.lib.function_base import append
import undirected_graphs as ug

import networkx as nx

# Define the window's contents
layout = [[sg.Text("u")],
          [sg.Input(key='-INPUT-0')],
          [sg.Text("v")],
          [sg.Input(key='-INPUT-1')],
          [sg.Text("attr:")],
          [sg.Input(key='-INPUT-2')],
          [sg.Text("color:")],
          [sg.Input(key='-INPUT-3')],

          [sg.Text(size=(40,1), key='-OUTPUT-1')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# %%

G=ug.Graphs(graph_type='dig')
edge_list=[]
# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    edge_dict={
        'attr': values['-INPUT-2'],
        'color': values['-INPUT-3'],
    }
    data=(values['-INPUT-0'],values['-INPUT-1'],edge_dict)
    window['-OUTPUT-1'].update(f"graph edge is    {data}")
    # window['-OUTPUT-1'].update('Hello ' + values['-INPUT-0'] + "! Thanks for trying PySimpleGUI")

    a=values['-INPUT-0']
    # print(f'a={a}')

    edge_list.append(data)

    G.edges(edge_list)
    G.graph_metrics()

    


# Finish up by removing from the screen
window.close()



# %%

print(G.G.adj)
print(list(G.G.adjacency()))

# traverse all edges of a graph is via the neighbors
a='attr'
for n, nbrsdict in G.G.adjacency():
    for nbr, eattr in nbrsdict.items():
        if a in eattr:
        # Do something useful with the edges
            print(eattr)
        




# %%
