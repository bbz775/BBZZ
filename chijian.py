import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

DG = nx.DiGraph()

# 添加节点1-23
for i in range(1, 136):
    DG.add_node(i, desc=str(i))

d = list(range(1, 135))
d1 = list(range(9, 64, 3))
d2 = list(range(72, 127, 3))
# print(d1)
# print(d2)
d1.extend(d2)
# print(d1)
point1 = [x for x in d if x not in d1]
# print(point1)
for i in range(0, 96):
    node2 = point1[i]
    DG.add_edge(node2, node2 + 1)
    DG.add_edge(node2+ 1, node2 )

point2 = list(range(2, 126, 3))
# print(point2)
for i in range(0,41):
    node2 = point2[i]
    DG.add_edge(node2, node2 + 9)
    DG.add_edge(node2+ 9, node2 )

a = [(1,14)]
for i in range(14,-1,-1):
    for j in range(1,10):
        a.append((j,i))
pos =a

colors = ['gray','gray','gray','gray','gray','gray','gray','gray','gray',
          'pink','gray','pink','pink','gray','pink','pink','gray','pink',
          'pink','gray','pink','pink','gray','pink','pink','gray','pink',
          'pink','gray','pink','pink','gray','pink','pink','gray','pink',
          'pink','gray','pink','pink','gray','pink','pink','gray','pink',
          'pink','gray','pink','pink','gray','pink','pink','gray','pink',
          'pink','gray','pink','pink','gray','pink','pink','gray','pink',
          'gray','gray','gray','gray','gray','gray','gray','gray','gray',
          'pink','gray','pink','pink','gray','pink','pink','gray','pink',
          'pink','gray','pink','pink','gray','pink','pink','gray','pink',
          'pink','gray','pink','pink','gray','pink','pink','gray','pink',
          'pink','gray','pink','pink','gray','pink','pink','gray','pink',
          'pink','gray','pink','pink','gray','pink','pink','gray','pink',
          'pink','gray','pink','pink','gray','pink','pink','gray','pink',
          'gray','gray','gray','gray','gray','gray','gray','gray','gray']
nx.draw_networkx(DG, pos, with_labels=None, node_color=colors , node_size =100)
node_labels = nx.get_node_attributes(DG, 'desc')
nx.draw_networkx_labels(DG, pos, labels=node_labels)
# 画出边权值
edge_labels = nx.get_edge_attributes(DG, 'name')
nx.draw_networkx_edge_labels(DG, pos, edge_labels=edge_labels, )

plt.title('map', fontsize=10)  # 标题
plt.savefig("ACT_map1.jpg")    # 储存图像
plt.show()