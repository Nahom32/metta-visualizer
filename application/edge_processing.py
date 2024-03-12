from typing import List
from domain.Node import Node
from domain.Edge import Edge
from infrastructure.metta_reader import read_metta_file
def process_edges(edge_path: str, nodes: List[Node],descriptors: List[Edge],id: str) -> List[Edge]:
    edges_raw = read_metta_file(edge_path)
    print(edges_raw)
    edge = {}
    list_of_edges = []
    for i in edges_raw:
        temp_edge = i.strip()[1:-1].split()
        if len(temp_edge) == 7:
            for j in nodes:
                if j.props[id] == temp_edge[3][:-1]:
                    for k in descriptors:
                        if k.props[id] == temp_edge[5][:-2]:
                            edge['node'] = j
                            edge['descriptor'] = k
                            edge['value'] = temp_edge[-1][:-1]
                            list_of_edges.append(Edge(**edge))
                            edge = {}
                    
    return list_of_edges

                
                            
                        
                    
                    
            
            
            
            
            
        
        
        
        
    
    
    
