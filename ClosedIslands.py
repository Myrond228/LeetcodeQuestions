class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        closed = 0
        visited = set()

        def onPerimeter(r, c):
            return r == 0 or r == (rows-1) or c==0 or c==(cols-1)
                

        def isClosed(r, c):
            if grid[r][c] == 1 or (r, c) in visited:
                return True
            if onPerimeter(r, c):
                return False

            visited.add((r, c))

            left = isClosed(r, c-1)
            right = isClosed(r, c+1)
            up = isClosed(r-1, c)
            down = isClosed(r+1, c)

            return True and left and right and up and down

        for r in range(1, rows):
            for c in range(1, cols):
                if grid[r][c] == 0 and (r, c) not in visited:
                    if isClosed(r, c):
                        closed += 1

        return closed
