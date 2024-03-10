from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        lp, rp, la = 0, 1, len(fruits)  # left ptr, right ptr, length of array
        cv = set()  # current varieties bw lp and rp
        if la < 2:
            return la

        max_len = 0
        current_len = 1
        cv.add(fruits[lp])
        while rp < la:

            rpe = fruits[rp]
            if len(cv) < 2 or (rpe in cv):
                current_len = rp - lp + 1
                rp = rp + 1
                cv.add(rpe)
            elif len(cv) == 2 and (rpe not in cv):
                cv.clear()
                cv.add(rpe)
                lp = rp - 1
                cv.add(fruits[rp-1])
                while (lp-1 >= 0) and (fruits[lp-1] in cv):
                    lp = lp - 1

                current_len = rp - lp + 1

            max_len = max(current_len, max_len)

        return max_len


s = Solution()
nums = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
val = s.totalFruit(nums)
print(val)
