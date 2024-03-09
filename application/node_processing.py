from typing import List
from domain.Node import Node
from infrastructure.metta_reader import read_metta_file
def change_to_nodes(file_path):
    raw_nodes = read_metta_file(file_path)
    values = set()
    lis_of_nodes = []
    node = {}
    for i in raw_nodes:
        temp_list = i.strip()[1:-1].split()
        if len(temp_list) == 2 and temp_list[1] not in values:
            node['typeData'] = temp_list[0]
            lis_of_nodes.append(Node(**node))
            node = {}
            values.add(temp_list[1])
        elif len(temp_list) > 2:
            if type(temp_list[-1]) == str and temp_list[-1][0]=="\"" and temp_list[-1][-1] == "\"":
                temp_list[-1] = temp_list[-1][1:-1]   
            node[temp_list[0]] = temp_list[-1]
    lis_of_nodes.pop(0)
    return lis_of_nodes
def change_to_node_from_mult_files(*paths):
    nodes = []
    for i in paths:
        nodes.extend(change_to_nodes(i))
    return nodes

    
            
        
            
        
        
        
        
    
    
    