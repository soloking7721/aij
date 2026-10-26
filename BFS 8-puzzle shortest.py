from collections import deque

s = (1,2,3,4,0,6,7,5,8)
g = (1,2,3,4,5,6,7,8,0)
q = deque([(s, [])])
v = {s}

while q:
    a, p = q.popleft()
    if a == g:
        print(p + [a])
        break
    i = a.index(0)
    for j in [i-3, i+3, i-1, i+1]:
        if 0 <= j < 9 and not (abs(i-j)==1 and i//3 != j//3):
            b = list(a)
            b[i], b[j] = b[j], b[i]
            b = tuple(b)
            if b not in v:
                v.add(b)
                q.append((b, p+[a]))
