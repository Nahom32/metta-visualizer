
from application.node_processing import change_to_nodes
import igraph as ig
import  matplotlib.pyplot as plt
g = ig.Graph.Famous("petersen")
fig, ax = plt.subplots()
ig.plot(g, target=ax)
plt.show()


# value = change_to_nodes("test_files/compound_nodes.metta")
# for i in value:
#     print(i)
    
