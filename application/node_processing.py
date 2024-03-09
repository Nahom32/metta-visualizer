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
            lis_of_nodes.append(node)
            node = {}
            values.add(temp_list[1])
        elif len(temp_list) > 2:
            node[temp_list[0]] = temp_list[-1]
    lis_of_nodes.pop(0)
    return lis_of_nodes
            
        
            
        
        
        
        
    
    
    