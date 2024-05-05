from typing import List
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))  # R, L, T, D
        visted = set()
        minHeap = [[0, 0, 0]]  # diff, r, c
        nr, nc = len(heights), len(heights[0])

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r, c) in visted:
                continue
            visted.add((r, c))
            if (r, c) == (nr - 1, nc - 1):
                return diff

            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if (newR < 0 or newR == nr) or (newC < 0 or newC == nc) or (newR, newC) in visted:
                    continue
                newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))
                heapq.heappush(minHeap, [newDiff, newR, newC])


heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
sol = Solution()
val = sol.minimumEffortPath(heights)
print(val)
