"""Query database for nodes and their attributes
THIS IS THE LAUNCH MODULE"""


from support_pkg import sqlite_database_interface as sdi

import support_pkg.file_access as fac

import get_nodes_edges as gne

# query database

server=fac.sensor_server     # get the database server (path)
the_sql_query='Select * from hctc_sensors WHERE Output="3 mV/V" and Asset_Description="10 KSI"'   # sql statement
df=sdi.SqliteDB(server).query_the_database(the_sql_command=the_sql_query)   # sql data as a dataframe 

# df=df.head(900)

print(df.head())


graph_filename='press_transducers'
gne.get_node_data(df.head(10),'Lab_ID',graph_filename=graph_filename,tag='PressureTransducer')
# gne.get_edge_data(df,'Serial_No','Model',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Asset_Type',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Asset_Description',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Status',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Make',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Model',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Output',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Location',graph_filename=graph_filename)



# graph_filename='emrData3'
# graph_filename='hctc_bom.json'
# gne.get_node_data(df,'HCTC_ID',graph_filename=graph_filename)
# gne.get_edge_data(df,'HCTC_ID','MODEL_NUMBER',graph_filename=graph_filename)
# gne.get_edge_data(df,'HCTC_ID','EQUIPMENT_CLASSIFICATION',graph_filename=graph_filename)
# gne.get_edge_data(df,'MODEL_NUMBER','PARENT_SYSTEM',graph_filename=graph_filename)
# gne.get_edge_data(df,'HCTC_ID','TECHNOLOGY',graph_filename=graph_filename)

