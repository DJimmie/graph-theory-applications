
import sql_to_graph as stg

def get_node_data(df,column_name,**kwargs):
    node_list=[]
    for row_index,row in df.iterrows():
        t=(row[4],{'Lab_ID':row['Lab_ID']})
        node_list.append(t)

    # print (node_list)

    # return node_list

   
    a=stg.Graphs()
    a.node(node_list)


    print(a.G.nodes['1704866']['Lab_ID'])
    

