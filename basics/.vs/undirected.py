
"""Undirected graph basics"""
import networkx as nx
import matplotlib.pyplot as plt


def plot_graph(g):
    nx.draw(G,with_labels=True)
    plt.show()


G=nx.Graph()
# Nodes
a=G.add_node(1)
b=G.add_node("Hello")


print(G.number_of_nodes())

plot_graph(G)

# Examining elements of a graph

print(G.nodes)

# create edges

G.add_edges_from([G.nodes])

plot_graph(G)