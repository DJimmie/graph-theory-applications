import networkx as nx
import matplotlib.pyplot as plt

class Graphs():
    """Undirected graph"""
    def __init__(self):
        self.G=nx.Graph()
        
    def node(self,name):
        self.name=name
        self.G.add_node(self.name)
        print(self.G.nodes())

        # GraphPlot(self.G)

    def node_with_attributes(self,parameters):
        self.G.add_nodes_from(parameters)

    def edges(self,e):
        self.e=e
        self.G.add_edges_from(self.e)
        
    def graph_metrics(self):
        print(f'Number of edges:{self.G.number_of_edges()}\nNumber of nodes:{self.G.number_of_nodes()}')
        GraphPlot(self.G)

    def get_node_attributes(self):
        print(self.G.nodes)

    def get_edge_attributes(self):
        print(self.G.edges(data=True))

    def add_node_attribute(self,n,k,v):
        self.G.nodes[n][k]=v
        print(list(self.G.nodes(data=True)))

    def neigbors(self):
        pass


    def graph_reporting(self,n):

        print(f'{self.G.__contains__(n)}\n{list(self.G.neighbors(n))}')

        print(self.G.degree)




class GraphPlot():
    """Undirected graph"""
    def __init__(self,G):
        self.G=G
        self.draw_the_graph()

    def draw_the_graph(self):
        nx.draw(self.G,with_labels=True,node_color='r',edge_color='b')
        plt.show()


## MAIN:::::::::::::::::::::::::::MAIN:::::::::::::::::::::::::::MAIN

a=Graphs()

a.node('Jim')

a.node_with_attributes([
    (4, {"color": "red"}),
    (5, {"color": "green"}),])

a.edges([(1,2),('A','B'),(2,5)])

a.edges([('C','D',{'color':'purple'})])

a.graph_metrics()

a.get_node_attributes()
a.get_edge_attributes()

a.add_node_attribute('Jim','age',56)

a.get_edge_attributes()

a.add_node_attribute('Jim','Home','TX')
a.add_node_attribute(1,'color','blue')
a.get_edge_attributes()

a.graph_reporting(2)



