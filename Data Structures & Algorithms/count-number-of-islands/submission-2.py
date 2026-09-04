class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        d=[[1, 0], [-1, 0], [0, 1], [0, -1]]
        r, c=len(grid), len(grid[0])
        islands=0

        def dfs(i, j):
            if i<0 or j<0 or i>=r or j>=c or grid[i][j]=="0":
                return
            grid[i][j]="0"
            for a, b in d:
                dfs(i+a, j+b)
            
        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1":
                    dfs(i, j)
                    islands+=1
        return islands