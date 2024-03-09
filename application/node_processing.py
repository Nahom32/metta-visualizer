from typing import List
from ..domain.Node import Node
from ..infrastructure.metta_reader import read_metta_file
def change_to_nodes(file_path):
    raw_nodes = read_metta_file(file_path)
    types = set()
    lis_of_nodes = []
    curr_id = ''
    node = {}
    for i in raw_nodes:
        temp_list = i.strip()[1:-1].split()
        if len(temp_list) == 2 and temp_list[0] not in types:
            types.add(temp_list[0])
            curr_id = temp_list[1]
        
            
        
        
        
        
    
    
    