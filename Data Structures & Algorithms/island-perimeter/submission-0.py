class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        n = len(grid[0])
        m = len(grid)
        """[    j = 0, j = 1, j = 2
        i=0    [(0,0), (0,1), (0,2)]
        i=1    [(1,0), (1,1), (1,2)]
        ]"""

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            # base case: out of bounds:
            if i >= m or i < 0: return 1
            if j >= n or j < 0: return 1
            # base case: hit water, increment 1
            if grid[i][j] == 0: return 1
            if (i,j) in visited: return 0

            visited.add((i, j))

            perimeter = 0

            for i2, j2 in directions:
                print(i+i2, j+j2)
                perimeter += dfs(i + i2, j + j2)

            return perimeter

        # find the first piece of land:
        i, j = 0,0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: break
            if grid[i][j] == 1: break

        return dfs(i, j)
        



