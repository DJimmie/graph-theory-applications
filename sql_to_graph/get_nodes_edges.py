
import sql_to_graph as stg

def get_node_data(df,column_name,graph_filename,**kwargs):

    col_index=list(df.columns).index(column_name)
    node_list=[]
    for row_index,row in df.iterrows():
        t=(row[col_index],{'DESCRIPTION':row['DESCRIPTION']})
        node_list.append(t)

    a=stg.Graphs(graph_filename=graph_filename)     # instantiate empty graph

    a.node(node_list)   # add specified nodes to graph

    
    

def get_edge_data(df,u,v,graph_filename,**kwargs):
    
    u_col_index=list(df.columns).index(u)
    v_col_index=list(df.columns).index(v)

    edge_list=[]
    for row_index,row in df.iterrows():
        t=(row[u_col_index],row[v_col_index],{'MN':row['MODEL_NUMBER']})

        edge_list.append(t)

    a=stg.Graphs(graph_filename=graph_filename,graph_type='dig')     # instantiate empty graph

    a.edge(edge_list)

    a.graph_metrics()

    a.subgraph()

  

