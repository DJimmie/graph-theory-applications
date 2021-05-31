"""Query database for nodes and their attributes"""


from support_pkg import sqlite_database_interface as sdi

import support_pkg.file_access as fac

import get_nodes_edges as gne

# query database

server=fac.database_servers()
the_sql_query='Select * from hctc_sensors'
df=sdi.SqliteDB(server).query_the_database(the_sql_command=the_sql_query)

df=df.head(900)

print(df.head())



# print(list(df.columns).index('Serial_No'))

graph_filename='j3.json'

# gne.get_node_data(df,'Location',graph_filename=graph_filename)

# gne.get_edge_data(df,'Serial_No','Model',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Asset_Type',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Asset_Description',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Status',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Make',graph_filename=graph_filename)
gne.get_edge_data(df,'Serial_No','Model',graph_filename=graph_filename)




