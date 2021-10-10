
import sql_to_graph as stg

def get_node_data(df,column_name,graph_filename,**kwargs):

    col_index=list(df.columns).index(column_name)
    node_list=[]
    node_to_tag_list=[]
    a=stg.Graphs(graph_filename=graph_filename)     # instantiate empty graph
    for row_index,row in df.iterrows():
        t=(row[col_index],{
        'facilityAddress': 'N/A',
        'assetNum': row['Lab_ID'],
        'model_num': row['Model'],
        'serial_num': row['Serial_No'],
        'status': row['Status'],
        'uniqueID': row['Lab_ID'],
        'description': row['Asset_Description'],
        'manufacturer': row['Make'],
        'model': row['Model'],
        'serialNumber': row['Serial_No'],
        'RecertDate': row['Recert_Date'],
        'EnterDate': row['Entry_Date'],
        'barcodeString': row['Notes'],
        'PO_Number': 'N/A'})

        if 'tag' in kwargs:
            e=(t[0],kwargs['tag'],{'attr':'Is A'})
            node_to_tag_list.append(e)
            if 'relations' in kwargs:
                e2=(t[0],row['Location'],{'attr':'hasLocation'})
                kwargs['relations']['Location'].append(e2)
            # print(e)
            print(e2)
        node_list.append(t)
    a.node(node_list)

    if 'tag' in kwargs:
        tag_nodes(node_to_tag_list,graph_filename)
        tag_nodes(kwargs['relations']['Location'],graph_filename)

def tag_nodes(edge_list,graph_filename):
    a=stg.Graphs(graph_filename=graph_filename)
    a.edge(edge_list)


   

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

  

