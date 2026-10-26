import heapq

s = (1,2,3,4,0,6,7,5,8)
g = (1,2,3,4,5,6,7,8,0)

def h(a):
    return sum(abs(i//3-(x-1)//3)+abs(i%3-(x-1)%3)
               for i,x in enumerate(a) if x)

q = [(h(s), s)]
v = set()

while q:
    _, a = heapq.heappop(q)
    print(a)
    if a == g:
        print("Goal Found")
        break
    if a in v:
        continue
    v.add(a)
    i = a.index(0)

    for j in [i-3, i+3, i-1, i+1]:
        if 0 <= j < 9 and not (abs(i-j)==1 and i//3 != j//3):
            b = list(a)
            b[i], b[j] = b[j], b[i]
            b = tuple(b)
            if b not in v:
                heapq.heappush(q, (h(b), b))
