"""Query database for nodes and their attributes
THIS IS THE LAUNCH MODULE"""


from support_pkg import sqlite_database_interface as sdi

import support_pkg.file_access as fac

import get_nodes_edges as gne

# query database

server=fac.sensor_server     # get the database server (path)

# the_sql_query='Select * from hctc_sensors WHERE Output="4 to 20 mA" and Asset_Description="10 KSI"'   # sql statement
# the_sql_query='Select * from hctc_sensors WHERE Output="3 mV/V" and Asset_Description="10 KSI"'   # sql statement
the_sql_query='Select * from hctc_sensors WHERE Output="Type K" and Asset_Description="TYPE K - FLEX" and Location Like "CELL%"'   # sql statement

df=sdi.SqliteDB(server).query_the_database(the_sql_command=the_sql_query)   # sql data as a dataframe 

# df=df.head(900)

print(df.head())

# graph_filename='press_Transmitter'
# graph_filename='press_Transducer'
graph_filename='thermocouple'

# gne.get_node_data(df.sample(10),'Lab_ID',graph_filename=graph_filename,tag='PressureTransmitter')
# gne.get_node_data(df.sample(10),'Lab_ID',graph_filename=graph_filename,tag='PressureTransducer')
relations_dict={'Location': [],'Document': []}
gne.get_node_data(df.sample(10),'Lab_ID',graph_filename=graph_filename,tag='Thermocouple',relations=relations_dict)


# gne.get_edge_data(df,'Serial_No','Model',graph_filename=graph_filename)
# gne.get_edge_data(df,'Serial_No','Asset_Type',graph_filename=graph_filename)



# graph_filename='emrData3'
# graph_filename='hctc_bom.json'
# gne.get_node_data(df,'HCTC_ID',graph_filename=graph_filename)
# gne.get_edge_data(df,'HCTC_ID','MODEL_NUMBER',graph_filename=graph_filename)
# gne.get_edge_data(df,'HCTC_ID','EQUIPMENT_CLASSIFICATION',graph_filename=graph_filename)
# gne.get_edge_data(df,'MODEL_NUMBER','PARENT_SYSTEM',graph_filename=graph_filename)
# gne.get_edge_data(df,'HCTC_ID','TECHNOLOGY',graph_filename=graph_filename)

