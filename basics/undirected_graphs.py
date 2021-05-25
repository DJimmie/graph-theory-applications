import networkx as nx
import matplotlib.pyplot as plt
import logging

from networkx.classes.function import neighbors

logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.INFO)
logging.info('start log')

class Graphs():
    """Undirected graph"""
    def __init__(self, graph_type=None):

        self.G=nx.DiGraph() if graph_type == 'dig' else nx.Graph()
        
    def node(self,name):
        self.name=name
        self.G.add_node(self.name)
        # print(self.G.nodes())
        logging.info(f'node{self.G.nodes()}')

        # GraphPlot(self.G)

    def node_with_attributes(self,parameters):
        self.G.add_nodes_from(parameters)

    def edges(self,e):
        self.e=e
        self.G.add_edges_from(self.e)
        
    def graph_metrics(self):
        # print(f'Number of edges:{self.G.number_of_edges()}\nNumber of nodes:{self.G.number_of_nodes()}')
        logging.info(f'Number of edges:{self.G.number_of_edges()}-----Number of nodes:{self.G.number_of_nodes()}')
        GraphPlot(self.G)

    def get_node_attributes(self):
        # print(self.G.nodes)
        logging.info(f'get_node_attributes{self.G.nodes}')

    def get_edge_attributes(self):
        # print(self.G.edges(data=True))
        logging.info(f'get_edge_attributes{self.G.edges(data=True)}')

    def add_node_attribute(self,n,k,v):
        self.G.nodes[n][k]=v
        logging.info(f'add node attrs{list(self.G.nodes(data=True))}')

    def neigbors(self,n):
        logging.info(list(nx.neighbors(self.G,n)))

        return list(nx.neighbors(self.G,n))

    
    def query(self,node_list):
        q_list=[]

        for i in node_list:
            q_list.append(self.neigbors(i))
            
        logging.info(q_list)

        s=[set(x) for x in q_list]
        print(s)

        print(s[0].intersection(s[1]))

    def get_from_dict(self,data_dict):
        self.G=nx.from_dict_of_dicts(data_dict,create_using=self.G)




    def graph_reporting(self,n):

        logging.info(f'{self.G.__contains__(n)}\n{list(self.G.neighbors(n))}')

        logging.info(self.G.degree)




class GraphPlot():
    """Undirected graph"""
    def __init__(self,G):
        self.G=G
        self.edge_attr=nx.get_edge_attributes(self.G,"attr")
        self.edge_color=nx.get_edge_attributes(self.G,"color")
        self.pos=nx.spring_layout(self.G)
        self.draw_the_graph()
    
    def draw_the_graph(self):

        plt.clf()
        nx.draw(self.G,self.pos,with_labels=True,node_color='white',edge_color='b')
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels = self.edge_attr)
        plt.show()









## MAIN:::::::::::::::::::::::::::MAIN:::::::::::::::::::::::::::MAIN

# a=Graphs()

# a.node('Jim')

# a.node_with_attributes([
#     ('Donna', {"color": "red"}),
#     ('Fluffy', {"color": "green"}),])

# # a.edges([(1,2),('A','B'),(2,5)])

# a_list=[
#     ('Jim','warm-blooded',{'color':'isA'}),
#     ('Donna','warm-blooded',{'color':'isA'}),
#     ('Jack','warm-blooded',{'color':'isA'}),
#     ('Donna','V',{'color':'hasA'}),
#     ('Jack','P',{'color':'hasA'}),
#     ('Jim','P',{'color':'hasA'}),
#     ('Fluffy','P',{'color':'hasA'}),
#     ('Lexi','V',{'color':'hasA'})
#     ]

# b_list=[
#     ('Jim','biped',{'color':'isA'}),
#     ('Donna','biped',{'color':'isA'}),
#     ('Jack','biped',{'color':'isA'}),
#     ('Lexi','quadped',{'color':'isA'}),
#     ('Fluffy','quadped',{'color':'isA'}),
#     ('Fluffy','tail',{'color':'hasA'}),
#     ('Lexi','tail',{'color':'hasA'}),
#     ('Fluffy','warm-blooded',{'color':'isA'}),
#     ('Lexi','warm-blooded',{'color':'isA'})
#     ]

# c_list=[('Jim','vertebrae',{'color':'hasA'}),
#     ('Donna','vertebrae',{'color':'hasA'}),
#     ('Jack','vertebrae',{'color':'hasA'}),
#     ('Fluffy','vertebrae',{'color':'hasA'}),
#     ('Lexi','vertebrae',{'color':'hasA'}),
#     ('Creamy','vertebrae',{'color':'hasA'}),
#     ('Creamy','P',{'color':'hasA'}),
#     ('Creamy','quadped',{'color':'isA'}),
#     ('Creamy','warm-blooded',{'color':'isA'}),
#     ('Creamy','tail',{'color':'hasA'})
#     ]

# a.edges(a_list+b_list+c_list)

# a.neigbors('warm-blooded')
# a.neigbors('biped')

# a.neigbors('P')
# a.neigbors('V')

# # a.graph_metrics()

# a.query(['vertebrae','warm-blooded'])

# K3 = nx.Graph([('Lisa','warm-blooded' ), (1, 2), (2, 0)])

# a.G.add_edge('Lisa','warm-blooded')

# # print(list(K3.adjacency()))

# print(K3.nodes())

# a.graph_metrics()

# print(a.node)


# a.get_node_attributes()
# a.get_edge_attributes()

# a.add_node_attribute('Jim','age',56)

# a.get_edge_attributes()

# a.add_node_attribute('Jim','Home','TX')
# a.add_node_attribute(1,'color','blue')
# a.get_edge_attributes()

# a.graph_reporting(2)



