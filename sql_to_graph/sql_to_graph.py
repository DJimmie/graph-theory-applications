
import networkx as nx
import matplotlib.pyplot as plt
import logging

from networkx.classes.function import neighbors

logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.INFO)
logging.info('start log')

class Graphs():
    
    def __init__(self,graph_type=None):

        self.G=nx.DiGraph() if graph_type == 'dig' else nx.Graph()
        
    def node(self,data):
        self.data=data
        self.G.add_nodes_from(self.data)
        logging.info(f'node{self.G.nodes()}')

        write_graph(self.G)

        GraphPlot(self.G)

class GraphPlot():
    """Undirected graph"""
    def __init__(self,G):
        self.G=G
        self.edge_attr=nx.get_edge_attributes(self.G,"Lab_ID")
        self.pos=nx.spring_layout(self.G)
        self.draw_the_graph()
    
    def draw_the_graph(self):

        plt.clf()
        nx.draw(self.G,self.pos,with_labels=True,node_color='white',edge_color='b')
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels = self.edge_attr)
        plt.show()



def write_graph(G):
    print(nx.node_link_data(G))
