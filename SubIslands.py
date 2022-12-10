class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        subs = 0
        visited = set()

        def isSub(r, c):
            if r<0 or c<0 or r==rows or c==cols or grid2[r][c] == 0 or (r, c) in visited:
                return True 
            if grid1[r][c] == 0:
                return False

            visited.add((r, c))

            left = isSub(r, c-1)
            right = isSub(r, c+1)
            up = isSub(r-1, c)
            down = isSub(r+1, c)

            return True and left and right and up and down

        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and (r, c) not in visited and isSub(r, c):
                    subs += 1

        return subs
