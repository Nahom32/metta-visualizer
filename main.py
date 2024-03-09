
from application.node_processing import change_to_node_from_mult_files
import igraph as ig



value = change_to_node_from_mult_files("test_files/compound_nodes.metta")
for i in value:
    print(i)
    
