
from ascii_graph import Pyasciigraph
from ascii_graph.colors import *

import networkx as nx
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.pyplot as plt

topology = {'node-1x1': {'links': ['node-2x1', 'node-1x2']}, 'node-1x2': {'links': ['node-2x2', 'node-1x1', 'node-1x3']}, 'node-1x3': {'links': ['node-2x3', 'node-1x2']}, 'node-2x1': {'links': ['node-1x1', 'node-3x1', 'node-2x2']}, 'node-2x2': {'links': ['node-1x2', 'node-3x2', 'node-2x1', 'node-2x3']}, 'node-2x3': {'links': ['node-1x3', 'node-3x3', 'node-2x2']}, 'node-3x1': {'links': ['node-2x1', 'node-3x2']}, 'node-3x2': {'links': ['node-2x2', 'node-3x1', 'node-3x3']}, 'node-3x3': {'links': ['node-2x3', 'node-3x2']}}
G = nx.Graph()

# Add nodes to the graph
for node in topology:
    G.add_node(node)

# Add edges to the graph
for node, connections in topology.items():
    for neighbor in connections['links']:
        G.add_edge(node, neighbor)

# Plot the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold')
plt.show()


'''
G = nx.DiGraph(
    [
        ("f", "a"),
        ("a", "b"),
        ("a", "e"),
        ("b", "c"),
        ("b", "d"),
        ("d", "e"),
        ("f", "c"),
        ("f", "g"),
        ("h", "f"),
    ]
)

for layer, nodes in enumerate(nx.topological_generations(G)):
    # `multipartite_layout` expects the layer as a node attribute, so add the
    # numeric layer value as a node attribute
    for node in nodes:
        G.nodes[node]["layer"] = layer

# Compute the multipartite_layout using the "layer" node attribute
pos = nx.multipartite_layout(G, subset_key="layer")

fig, ax = plt.subplots()
nx.draw_networkx(G, pos=pos, ax=ax)
ax.set_title("DAG layout in topological order")
fig.tight_layout()
plt.show()

from pyvis.network import Network
import networkx as nx
nx_graph = nx.cycle_graph(10)
nx_graph.nodes[1]['title'] = 'Number 1'
nx_graph.nodes[1]['group'] = 1
nx_graph.nodes[3]['title'] = 'I belong to a different group!'
nx_graph.nodes[3]['group'] = 10
nx_graph.add_node(20, size=20, title='couple', group=2)
nx_graph.add_node(21, size=15, title='couple', group=2)
nx_graph.add_edge(20, 21, weight=5)
nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)
nt = Network('500px', '500px')
# populates the nodes and edges data structures
nt.from_nx(nx_graph)
nt.show('nx.html')

'''