import heapq

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def manhattan(state):
    distance = 0
    for i, value in enumerate(state):
        if value != 0:
            target = value - 1
            distance += abs(i // 3 - target // 3)
            distance += abs(i % 3 - target % 3)
    return distance

def astar(start, goal):
    pq = [(manhattan(start), 0, start, [start])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path

        if state in visited:
            continue
        visited.add(state)

        zero = state.index(0)
        r, c = divmod(zero, 3)

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new_zero = nr * 3 + nc
                new_state = list(state)
                new_state[zero], new_state[new_zero] = (
                    new_state[new_zero], new_state[zero]
                )
                new_state = tuple(new_state)

                if new_state not in visited:
                    heapq.heappush(
                        pq,
                        (g + 1 + manhattan(new_state),
                         g + 1, new_state, path + [new_state])
                    )

    return None

path = astar(start, goal)

if path:
    for step, state in enumerate(path):
        print("Step", step)
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()

    print("Total moves:", len(path) - 1)
else:
    print("No solution found")