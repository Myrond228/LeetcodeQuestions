class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        unreachable = 0
        visited = set()
        closed_visit = set()

        def isClosed(r, c):
            nonlocal area
            if grid[r][c] == 0 or (r, c) in visited:
                return True
            if r<=0 or r>=rows-1 or c<=0 or c>=cols-1:
                return False

            area += 1
            visited.add((r, c))

            left = isClosed(r, c-1)
            right = isClosed(r, c+1)
            up = isClosed(r-1, c)
            down = isClosed(r+1, c)

            return True and left and right and up and down

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c):
                    area = 0
                    if isClosed(r, c):
                        unreachable += area

        return unreachable

