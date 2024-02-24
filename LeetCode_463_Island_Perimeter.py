class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        nr = len(grid)
        nc = len(grid[0])
        total_counter = 0

        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 1:
                    counter = 4
                    top = [max(i - 1, 0), j]
                    bottom = [min(i + 1, nr - 1), j]
                    left = [i, max(j - 1, 0)]
                    right = [i, min(j + 1, nc - 1)]

                    if grid[top[0]][top[1]] == 1 and not ([i, j] == top):
                        counter = counter - 1

                    if grid[bottom[0]][bottom[1]] == 1 and not ([i, j] == bottom):
                        counter = counter - 1

                    if grid[right[0]][right[1]] == 1 and not ([i, j] == right):
                        counter = counter - 1

                    if grid[left[0]][left[1]] == 1 and not ([i, j] == left):
                        counter = counter - 1

                    total_counter = total_counter + counter       
        return total_counter