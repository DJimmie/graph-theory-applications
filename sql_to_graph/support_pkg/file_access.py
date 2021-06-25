""" Central location for File pathways needed by the various program(s)"""


import os

graph_file_location='C:/Users/dowdj/OneDrive/Documents/GitHub/graph-theory-applications/sql_to_graph/data/'
emr_server=r'C:\Users\dowdj\OneDrive\Documents\GitHub\EM-Database\emr_database.db'
sensor_server=r'C:\Users\dowdj\OneDrive\Documents\GitHub\Sensor-Inventory-Database\database.db'

def database_servers():

    server=r'C:\Users\dowdj\OneDrive\Documents\GitHub\Sensor-Inventory-Database\database.db' 
    return server


def urls():
    pass



def access_document(path,document):
        """Opens selected document"""

        doc=path+'\\'+document
        print(doc)
        os.startfile(doc)
        # subprocess.run(doc)