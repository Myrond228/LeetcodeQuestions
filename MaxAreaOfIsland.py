class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        visited = set()

        def getArea(r, c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            
            left = getArea(r, c-1)
            right = getArea(r, c+1)
            top = getArea(r-1, c)
            down = getArea(r+1, c)

            return 1 + left + right + top + down

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    current_area = getArea(r, c)
                    max_area = max(max_area, current_area)

        return max_area
