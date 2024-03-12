from igraph import Graph
def get_graph(list_edges):

    graph_to_return = Graph()
    for i in list_edges:    
        graph_to_return.add_vertex(i.edges['node'].props['id']) 
        graph_to_return.add_vertex(i.edges['descriptor'].props['id'])
        graph_to_return.add_edges([(i.edges['node'].props['id'],i.edges['descriptor'].props['id'])])
    return graph_to_return

