from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        valid_seq_nums = []
        for i in range(1, 9):
            new_number = i
            last_digit = i
            while last_digit < 9:
                new_number = (new_number * 10) + (last_digit + 1)
                last_digit = last_digit + 1
                if low <= new_number <= high:
                    valid_seq_nums.append(new_number)
                else:
                    continue
                if new_number > high:
                    break
        valid_seq_nums.sort()
        return valid_seq_nums

low = 10
high = 100

s1 = Solution()
s1.sequentialDigits(low, high)
