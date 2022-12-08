class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfsIsland(r, c):
            if r<0 or r>=rows or c<0 or c>=cols or (r, c) in visited or grid[r][c] == "0":
                return

            visited.add((r, c))

            dfsIsland(r, c-1)
            dfsIsland(r, c+1)
            dfsIsland(r-1, c)
            dfsIsland(r+1, c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfsIsland(r, c)
                    islands += 1

        return islands
