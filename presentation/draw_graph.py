from igraph import Graph
import igraph as ig
import matplotlib.pyplot as plt
def draw_graph(g: Graph):
    fig, ax = plt.subplots()
    layout = g.layout('kk')
    ig.plot(g, layout=layout, target=ax)
    plt.show()
    
    