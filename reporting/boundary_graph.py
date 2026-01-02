import networkx as nx
import matplotlib.pyplot as plt


def plot_boundary(boundary_record):
    G = nx.DiGraph()
    G.add_node("Dynamics")

    for a in boundary_record.assumption_context:
        G.add_node(a)
        G.add_edge("Dynamics", a)

    nx.draw(G, with_labels=True, node_color="lightcoral")
    plt.title("Epistemic Boundary Localization")
    plt.show()
