poured = 34
query_row = 6
query_glass = 1
tower = [[0] * query_row for i in range(query_row)]


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Initialize a 2D list with enough space for all rows
        tower = [[0] * (r + 1) for r in range(query_row + 1)]
        tower[0][0] = poured

        # Iterate through each row up to query_row
        for r in range(query_row):
            for c in range(r + 1):
                if tower[r][c] > 1:
                    excess = tower[r][c] - 1
                    tower[r][c] = 1
                    tower[r + 1][c] += excess / 2
                    tower[r + 1][c + 1] += excess / 2

        # Return the amount in the specified glass, capped at 1
        return min(1, tower[query_row][query_glass])
