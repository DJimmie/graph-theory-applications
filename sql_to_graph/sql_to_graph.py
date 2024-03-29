
import networkx as nx
import matplotlib.pyplot as plt
import logging
import json

from networkx.classes.function import neighbors

logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.INFO)
logging.info('start log')

import support_pkg.file_access as fac

class Graphs():
    
    def __init__(self,graph_filename=None,graph_type=None):

        if graph_filename==None:
            self.G=nx.DiGraph() if graph_type == 'dig' else nx.Graph()

        else:
            try:
                # check if file exist
                graph_file=f'{fac.graph_file_location}{graph_filename}'
                print(f'the graph file is: {graph_file}')
                with open(graph_file, "r") as read_file:
                    data_dict = json.load(read_file)
                
                data_dict['directed']=True if graph_type == 'dig' else False

                self.G=nx.node_link_graph(data_dict, directed=True, multigraph=True, attrs=None)
                # print(f'G:{type(G)}')
                # self.G=nx.to_directed(G) if graph_type == 'dig' else G
                # self.G=nx.to_directed(G) if graph_type == 'dig' else nx.node_link_graph(data_dict, directed=False, multigraph=True, attrs=None)
                # print(f'self.G:{type(self.G)}')
                GraphPlot(self.G)

                print(f'Is Graph Frozen?:{nx.is_frozen(self.G)}')
            except Exception as err:
                # make an empty dictionary to make an empty Graph
                print(err)
                print('Creating empty graph')
                graph_file=f'{fac.graph_file_location}{graph_filename}'
                self.G=nx.DiGraph() if graph_type == 'dig' else nx.Graph()
                data_dict=nx.node_link_data(self.G)
                with open(graph_file,'w') as f: 
                    json.dump(data_dict, f, indent=4)
                self.G=nx.node_link_graph(data_dict, directed=False, multigraph=True, attrs=None)
                GraphPlot(self.G)

                

        self.graph_filename=graph_filename
            
        
    def node(self,data):
        self.data=data
        self.G.add_nodes_from(self.data)
        logging.info(f'node{self.G.nodes()}')
        write_graph(self.G,self.graph_filename)

        GraphPlot(self.G)


    def edge(self,data):
        self.data=data
        self.G.add_edges_from(self.data)
        logging.info(f'edge{self.G.edges()}')
        write_graph(self.G,self.graph_filename)

        GraphPlot(self.G)

    def graph_metrics(self):
        # logging.info(f'node{nx.degree_histogram(self.G)}')
        logging.info(f'info {nx.info(self.G)}')

        logging.info(f'degree {nx.degree(self.G,"20 KSI")}')


    def subgraph(self):
        view=nx.subgraph_view(self.G,filter_node='20 KSI')
        GraphPlot(view)


class GraphPlot():
    """Plot the graph"""
    def __init__(self,G):
        self.G=G
        self.edge_attr=nx.get_edge_attributes(self.G,"MN")
        self.pos=nx.spring_layout(self.G)
        self.draw_the_graph()
    
    def draw_the_graph(self):

        plt.clf()
        nx.draw(self.G,self.pos,with_labels=True,node_color='white',edge_color='b',font_size=6)
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels = self.edge_attr,font_size=6)
        plt.show()



def write_graph(G,graph_filename):
    
    data_dict=nx.node_link_data(G)
    print(data_dict)
    graph_file=f'{fac.graph_file_location}{graph_filename}'
    with open(graph_file,'w') as f: 
        json.dump(data_dict, f, indent=4) 

# Graphs()