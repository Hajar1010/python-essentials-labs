def numCells(grid):
    n, m = len(grid), len(grid[0])
    count = 0
    for r in range(n):
        for c in range(m):
            val = grid[r][c]
            neighbors = [
                grid[i][j]
                for i in range(max(0, r-1), min(n, r+2))
                for j in range(max(0, c-1), min(m, c+2))
                if (i, j) != (r, c)
            ]
            if val > max(neighbors):
                count += 1
        
    return count