def dfs(a, b, path):
    if (a, b) in path: return
    path.append((a, b))
    if a == 2 or b == 2:
        print(path)
        return True
    for s in [(4,b),(a,3),(0,b),(a,0),
              (a-min(a,3-b),b+min(a,3-b)),
              (a+min(b,4-a),b-min(b,4-a))]:
        if dfs(*s, path[:]): return True

dfs(0, 0, [])
