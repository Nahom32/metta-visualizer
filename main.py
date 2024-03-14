
from application.node_processing import change_to_node_from_mult_files
from application.edge_processing import process_edges_one,process_edges
from application.graph_processing import get_graph
from presentation.draw_graph import draw_graph
import igraph as ig

nodes = change_to_node_from_mult_files("test_files/compound_nodes.metta")
descriptors = change_to_node_from_mult_files("test_files/descriptor_nodes.metta")

edges = process_edges_one("test_files/compound_edges.metta","CID2499094",nodes, descriptors,"id")
print("This are the edges: ", edges)
graph = get_graph(edges)
draw_graph(graph)




