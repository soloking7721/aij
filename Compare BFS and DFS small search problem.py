g = {1:[2,3], 2:[4], 3:[5], 4:[], 5:[]}

def search(q, bfs):
    v = []
    while q:
        p = q.pop(0) if bfs else q.pop()
        n = p[-1]
        if n == 5:
            print(p)
            return
        if n not in v:
            v.append(n)
            q += [p+[x] for x in g[n]]

print("BFS:"); search([[1]], True)
print("DFS:"); search([[1]], False)
