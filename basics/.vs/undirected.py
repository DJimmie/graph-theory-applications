
"""Undirected graph basics"""
import networkx as nx
import matplotlib.pyplot as plt




class graph(nx.Graph):
    """Undirected graph"""
    def __init__(self):
        super().__init__()
        
    def node(self,name):

        self.name=name
        self.n=self.add_node(self.name)

    
    def node_with_attributes(self,parameters):
    
        self.n=self.add_nodes_from(parameters)

    # def edges(self,e):
    #     self.edge=self.add_edge(e)


    def edges(self,e):
        self.e=e
        self.edge=self.add_edges_from(self.e)

    def graph_metrics(self):
        
        print(f'Number of edges:{self.number_of_edges()}\nNumber of nodes:{self.number_of_nodes()}')


class GraphPlot(nx.draw):
    """Undirected graph"""
    def __init__(self):
        super().__init__()

    def draw_the_graph(self,G):
        self.draw(G)
        plt.show




# def plot_graph(G):
#     nx.draw(G,with_labels=True)
#     plt.show()

## MAIN:::::::::::::::::::::::::::MAIN:::::::::::::::::::::::::::MAIN

a=graph()

a.node('Jim')

a.node_with_attributes([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])


a.edges([(1, 2), (1, 3)])

a.edges([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])

a.graph_metrics()



p=GraphPlot()

p.draw_the_graph(a)