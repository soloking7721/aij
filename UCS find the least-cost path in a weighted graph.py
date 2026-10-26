import heapq

g = {'A': [('B', 1), ('C', 4)],
     'B': [('C', 2), ('D', 5)],
     'C': [('D', 1)], 'D': []}

q = [(0, 'A', ['A'])]
while q:
    c, n, p = heapq.heappop(q)
    if n == 'D':
        print("Path:", p, "Cost:", c)
        break
    for x, w in g[n]:
        heapq.heappush(q, (c+w, x, p+[x]))
