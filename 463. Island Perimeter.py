class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total = 0
        for n, i in enumerate(grid):
            for m, j in enumerate(i):
                if j == 1:
                    total += 4
                    if m > 0 and i[m-1] == 1: # left
                        total -= 2
                    if n > 0 and grid[n-1][m] == 1: # on
                        total -= 2
        return total