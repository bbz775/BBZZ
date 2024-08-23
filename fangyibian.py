a = [(1,14)]
for i in range(14,-1,-1):
    for j in range(1,9):
        a.append((j,i))

pos =a

point1 = [1, 2, 3, 4, 5, 6, 7, 57, 58, 59, 60, 61, 62, 63, 113, 114, 115, 116, 117, 118, 119]
for i in range(0, 21):
    node1 = point1[i]
    DG.add_edge(node1, node1 + 1)

point1 = [1, 2, 3, 4, 5, 6, 7, 57, 58, 59, 60, 61, 62, 63, 113, 114, 115, 116, 117, 118, 119]
for i in range(0, 21):
    node1 = point1[i]
    DG.add_edge(node1+1, node1)
