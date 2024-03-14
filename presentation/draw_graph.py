import numpy as np
import igraph as ig
import matplotlib.pyplot as plt

def draw_graph(g: ig.Graph):
    layout = np.array(g.layout("kk"))
    vertex_names = [v["name"] for v in g.vs]
    edges = g.get_edgelist()
    fig, ax = plt.subplots(figsize=(8, 6))
    for edge in edges:
        v1, v2 = edge
        x = [layout[v1][0], layout[v2][0]]
        y = [layout[v1][1], layout[v2][1]]
        ax.plot(x, y, 'k-', alpha=0.5)
    
    scatter = ax.scatter(layout[:, 0], layout[:, 1], s=100, c='b')
    
    def update_annot(ind):
        pos = scatter.get_offsets()[ind["ind"][0]]
        annot.xy = pos
        text = f"Name: {vertex_names[ind['ind'][0]]}"
        annot.set_text(text)
        annot.get_bbox_patch().set_alpha(0.4)
    
    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            cont, ind = scatter.contains(event)
            if cont:
                update_annot(ind)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()
    
    fig.canvas.mpl_connect("motion_notify_event", hover)
    
    ax.set_title('Metta Graph Visualizer')
    
    ax.set_xlim(min(layout[:, 0]) - 0.1, max(layout[:, 0]) + 0.1)
    ax.set_ylim(min(layout[:, 1]) - 0.1, max(layout[:, 1]) + 0.1)
    
    ax.axis('off')
    
    annot = ax.annotate("", xy=(0, 0), xytext=(-20, 20), textcoords="offset points",
                         bbox=dict(boxstyle="round", fc="w"),
                         arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)
    
    plt.show()