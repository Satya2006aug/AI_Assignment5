# knowledge graph example

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("Alice")
G.add_node("AI")
G.add_node("Machine Learning")

G.add_edge("Alice",
           "AI",
           relation="studies")

G.add_edge("AI",
           "Machine Learning",
           relation="related_to")

pos = nx.spring_layout(G)

nx.draw(G,
        pos,
        with_labels=True,
        node_size=3000)

labels = nx.get_edge_attributes(G,
                                'relation')

nx.draw_networkx_edge_labels(G,
                             pos,
                             edge_labels=labels)

plt.show()
