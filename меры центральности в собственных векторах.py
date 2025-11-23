import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_nodes_from([1,2,3,4,5,6,7])
G.add_edges_from([(1,2),(2,3),(2,4),(2,5),(4,5),(4,6),(4,7),(5,7)])
nx.draw(G, node_size = 500, with_labels=True)
plt.show()
print(nx.degree_centrality(G))
DC = nx.degree_centrality(G)
for i in DC.keys():
    print('The node {} measurement center value {:.4f}'.format(i, DC[i]))
    print(nx.eigenvector_centrality(G))#特征向量的中心性

#2
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_edges_from([(1,2), (1,3), (1,4), (2,3), (2,4), (3,4), (3,5), (4,6),(5,6)])
nx.draw(G, node_size = 500, with_labels=True)
plt.show()
print(nx.degree_centrality(G))
DC = nx.degree_centrality(G)
for i in DC.keys():
    print('The node {} measurement center value {:.4f}'.format(i, DC[i]))
    print(nx.eigenvector_centrality(G))#特征向量的中心性


