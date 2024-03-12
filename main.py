
from application.node_processing import change_to_node_from_mult_files
from application.edge_processing import process_edges
import igraph as ig



value = change_to_node_from_mult_files("test_files/compound_nodes.metta")
value2 = change_to_node_from_mult_files("test_files/descriptor_nodes.metta")
print(value2)
edges = process_edges("test_files/compound_edges.metta",value, value2,"id")
for i in edges:
    print(i)
    
