from typing import List
from domain.Node import Node
from domain.Edge import Edge
from infrastructure.metta_reader import read_metta_file
def process_edges(edge_path: str, nodes: List[Node],descriptors: List[Edge],id: str) -> List[Edge]:
    edges_raw = read_metta_file(edge_path)
    print(nodes)
    edge = {}
    list_of_edges = []
    count = 1
    for i in edges_raw:
        temp_edge = i.strip()[1:-1].split()
        if len(temp_edge) == 7:
            for j in nodes:
                if j.props[id] == temp_edge[3][:-1]:
                    for k in descriptors:
                        if k.props[id] == temp_edge[5][:-2]:
                            print(j)
                            print(k)
                            edge['node'] = j
                            edge['descriptor'] = k
                            edge['value'] = temp_edge[-1][:-1]
                            list_of_edges.append(Edge(**edge))
                            edge = {}
        count+=1                
    return list_of_edges

def process_edges_one(edge_path: str,process_str: str,nodes: List[Node],descriptors: List[Edge],id: str):
    edges_raw = read_metta_file(edge_path)
    print(nodes)
    edges_raw.pop()
    edge = {}
    node = Node()
    edges_list = []
    # for i in edges_raw:
    #     temp_edge = i.strip()[1:-1].split()
    #     for j in nodes:
    #         if process_str == j.props[id]:
    #             node.props = j.props
    #             break
    #     if node.props == {}:
    #         raise Exception("The node doesn't exist")
    #     for k in temp_edge:
    for j in nodes:
        if j.props[id] == process_str:
            print("hi", j)
            node.props = j.props
    print("This the node props", node.props)
    if node.props == {}:
        raise Exception("The node doesn't exist")
    for j in edges_raw:
        temp_edge = j.strip()[1:-1].split()
        print(temp_edge)
        print("This is a temp_edge", temp_edge[3][:-1])
        print("this is node props id", node.props[id])
        if temp_edge[3][:-1] == node.props[id]:
            print("hello how")
            for i in descriptors:
                if str(temp_edge[5][:-2]) == str(i.props[id]):
                    edge_prop = {}
                    edge_prop['node'] = node
                    edge_prop['descriptor'] = i
                    edge_prop['value'] = temp_edge[-1][:-1]
                    edges_list.append(Edge(**edge_prop))
    return edges_list
            
            
            
                
                
        
        
        
    
    

                
                            
                        
                    
                    
            
            
            
            
            
        
        
        
        
    
    
    
