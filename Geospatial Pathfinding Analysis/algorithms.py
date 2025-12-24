from collections import deque
import heapq

# Directions: up, down, left, right
DIRS = [(-1,0),(1,0),(0,-1),(0,1)]

def is_valid(r, c, rows, cols, grid):
    return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0


# ---------------- BFS ----------------
def bfs(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited = set([start])
    parent = {}

    while queue:
        r, c = queue.popleft()

        if (r, c) == end:
            return reconstruct_path(parent, start, end)

        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc, rows, cols, grid) and (nr, nc) not in visited:
                visited.add((nr, nc))
                parent[(nr, nc)] = (r, c)
                queue.append((nr, nc))

    return None


# ---------------- DIJKSTRA ----------------
def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    pq = [(0, start)]
    dist = {start: 0}
    parent = {}

    while pq:
        cost, (r, c) = heapq.heappop(pq)

        if (r, c) == end:
            return reconstruct_path(parent, start, end)

        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc, rows, cols, grid):
                new_cost = cost + 1
                if (nr, nc) not in dist or new_cost < dist[(nr, nc)]:
                    dist[(nr, nc)] = new_cost
                    parent[(nr, nc)] = (r, c)
                    heapq.heappush(pq, (new_cost, (nr, nc)))

    return None


def reconstruct_path(parent, start, end):
    path = []
    cur = end
    while cur != start:
        path.append(cur)
        cur = parent[cur]
    path.append(start)
    return path[::-1]
