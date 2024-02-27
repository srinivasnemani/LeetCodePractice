from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        maxa = 0

        seen = set()
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1 and (r, c) not in seen:
                    cur_island = list()
                    cur_island.append((r, c))
                    seen.add((r, c))
                    ca = 1

                    while len(cur_island) > 0:
                        u, v = cur_island.pop(0)
                        for i, j in (u + 1, v), (u, v + 1), (u - 1, v), (u, v - 1):
                            if (0 <= i < nr) and (0 <= j < nc):
                                if grid[i][j] == 1:
                                    if (i, j) not in seen:
                                        seen.add((i, j))
                                        ca = ca + 1
                                        cur_island.append((i, j))
                    maxa = max(maxa, ca)
        return maxa


s = Solution()
grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

ni = s.numIslands(grid)
print("--------------------")
print(ni)
print("--------------------")
