from igraph import Graph
def get_graph(list_edges):

    graph_to_return = Graph()
    for i in list_edges:
        print(i)
        print(graph_to_return)
        
        graph_to_return.add_vertex(i.edges['node'].props['id'])
        for j in graph_to_return.vs:
            print(j.attributes())
        graph_to_return.add_vertex(i.edges['descriptor'].props['id'])
        graph_to_return.add_edges([(i.edges['node'].props['id'],i.edges['descriptor'].props['id'])])
    return graph_to_return

