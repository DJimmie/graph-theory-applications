""" Central location for File pathways needed by the various program(s)"""


import os


def database_servers():

    
    server=r'C:\Users\dowdj\OneDrive\Documents\GitHub\Sensor-Inventory-Database\database.db'  #production database
    

    return server


def urls():
    pass



def access_document(path,document):
        """Opens selected document"""

        doc=path+'\\'+document
        print(doc)
        os.startfile(doc)
        # subprocess.run(doc)