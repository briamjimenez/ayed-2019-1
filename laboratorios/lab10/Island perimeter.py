class Solution(object):
    def islandPerimeter(self, grid):
        recount=0
        sum=0
        n=len(grid)
        m=len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    sum=sum+1
                    if i-1>=0:
                        if grid[i-1][j]==1 :recount+=1
                    if j - 1 >= 0:
                        if grid[i][j-1] == 1: recount+= 1
                    if i + 1 < n:
                        if grid[i + 1][j] == 1: recount += 1
                    if j+1 < m:
                        if grid[i][1+j] == 1: recount+=1
        print(sum,recount)
        return sum*4-recount

s=Solution()
print(s.islandPerimeter([[1,1,0],[1,0,0], [1,1,0]]))

