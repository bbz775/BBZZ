import networkx as nx
import matplotlib.pyplot as plt

# 创建一个有向图对象
DG = nx.DiGraph()

# 添加节点
DG.add_node(1)
DG.add_node(2)
DG.add_node(3)

# 添加边
DG.add_edge(1, 2)
DG.add_edge(2, 3)

# 定义节点位置信息
pos = {1: (0, 0), 2: (1, 1), 3: (2, 0)}

# 定义节点标签
node_labels = {1: 'Node 1', 2: 'Node 2', 3: 'Node 3'}

# 绘制网络图
nx.draw_networkx(DG, pos, with_labels=False)
nx.draw_networkx_labels(DG, pos, labels=node_labels)

# 显示图形
plt.show()
