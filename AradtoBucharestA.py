import heapq

graph = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Oradea', 71), ('Arad', 75)],
    'Oradea': [('Sibiu', 151), ('Zerind', 71)],
    'Sibiu': [('Fagaras', 99), ('Rimnicu Vilcea', 80), ('Arad', 140), ('Oradea', 151)],
    'Fagaras': [('Bucharest', 211), ('Sibiu', 99)],
    'Rimnicu Vilcea': [('Pitesti', 97), ('Craiova', 146), ('Sibiu', 80)],
    'Pitesti': [('Bucharest', 101), ('Rimnicu Vilcea', 97), ('Craiova', 138)],
    'Timisoara': [('Lugoj', 111), ('Arad', 118)],
    'Lugoj': [('Mehadia', 70), ('Timisoara', 111)],
    'Mehadia': [('Drobeta', 75), ('Lugoj', 70)],
    'Drobeta': [('Craiova', 120), ('Mehadia', 75)],
    'Craiova': [('Pitesti', 138), ('Rimnicu Vilcea', 146), ('Drobeta', 120)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Urziceni', 85), ('Giurgiu', 90)],
    'Urziceni': [('Vaslui', 142), ('Hirsova', 98), ('Bucharest', 85)],
    'Vaslui': [('Iasi', 92), ('Urziceni', 142)],
    'Iasi': [('Neamt', 87), ('Vaslui', 92)],
    'Neamt': [('Iasi', 87)],
    'Hirsova': [('Eforie', 86), ('Urziceni', 98)],
    'Eforie': [('Hirsova', 86)],
    'Giurgiu': [('Bucharest', 90)]
}

h = {
    'Arad': 366, 'Zerind': 374, 'Oradea': 380,
    'Sibiu': 253, 'Fagaras': 176, 'Rimnicu Vilcea': 193,
    'Pitesti': 100, 'Timisoara': 329, 'Lugoj': 244,
    'Mehadia': 241, 'Drobeta': 242, 'Craiova': 160,
    'Bucharest': 0, 'Urziceni': 80, 'Vaslui': 199,
    'Iasi': 226, 'Neamt': 234, 'Hirsova': 151,
    'Eforie': 161, 'Giurgiu': 77
}

pq = [(h['Arad'], 0, 'Arad', ['Arad'])]
best = {'Arad': 0}

while pq:
    f, cost, city, path = heapq.heappop(pq)

    if cost != best[city]:
        continue

    if city == 'Bucharest':
        print("Path:", path)
        print("Total distance:", cost, "km")
        break

    for next_city, distance in graph[city]:
        new_cost = cost + distance

        if new_cost < best.get(next_city, float('inf')):
            best[next_city] = new_cost
            heapq.heappush(
                pq, (new_cost + h[next_city], new_cost,
                     next_city, path + [next_city])
            )