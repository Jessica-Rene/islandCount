oceans = (
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1]
)

def count_islands(oceans):
    rows = len(oceans)
    cols = len(oceans[0])
    visited = set()

    # 8 directions 
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    def dfs(r, c):
        visited.add((r, c))
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                oceans[nr][nc] == 1 and (nr, nc) not in visited):
                dfs(nr, nc)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if oceans[r][c] == 1 and (r, c) not in visited:
                dfs(r, c)
                islands += 1

    return islands

print(count_islands(oceans))
