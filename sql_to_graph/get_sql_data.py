"""Query database for nodes and their attributes
THIS IS THE LAUNCH MODULE"""


from support_pkg import sqlite_database_interface as sdi

import support_pkg.file_access as fac

import get_nodes_edges as gne

# query database

server=fac.emr_server      # get the database server (path)
the_sql_query='Select * from csp_table_1'   # sql statement
df=sdi.SqliteDB(server).query_the_database(the_sql_command=the_sql_query)   # sql data as a dataframe 

# df=df.head(900)

print(df.head())


# graph_filename='press_sensors.json'
# gne.get_node_data(df,'Location',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Model',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Asset_Type',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Asset_Description',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Status',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Make',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Model',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Output',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Location',graph_filename=graph_filename)



graph_filename='csp_table.json'
# gne.get_node_data(df,'HCTC_ID',graph_filename=graph_filename)
# gne.get_edge_data(df,'HCTC_ID','MODEL_NUMBER',graph_filename=graph_filename)
gne.get_edge_data(df,'HCTC_ID','EQUIPMENT_CLASSIFICATION',graph_filename=graph_filename)

