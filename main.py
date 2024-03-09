
from application.node_processing import change_to_nodes

value = change_to_nodes("test_files/compound_nodes.metta")
for i in value:
    print(i)
