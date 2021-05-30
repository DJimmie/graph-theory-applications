"""Query database for nodes and their attributes"""


from support_pkg import sqlite_database_interface as sdi

import support_pkg.file_access as fac

import get_nodes_edges as gne



# query database

server=fac.database_servers()
the_sql_query='Select * from hctc_sensors'
df=sdi.SqliteDB(server).query_the_database(the_sql_command=the_sql_query)

df=df.head(20)

# print(df.head())

gne.get_node_data(df,'Serial_No')



