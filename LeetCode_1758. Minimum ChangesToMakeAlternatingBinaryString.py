class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        exp_char_start_with_1 = '1'
        exp_char_start_with_0 = '0'
        counter_1 = 0
        counter_0 = 0
        for char in s:

            if not char == exp_char_start_with_1:
                counter_1 += 1

            if not char == exp_char_start_with_0:
                counter_0 += 1

            exp_char_start_with_1 = '0' if exp_char_start_with_1 == '1' else '1'
            exp_char_start_with_0 = '0' if exp_char_start_with_0 == '1' else '1'

        min_changes = min(counter_1, counter_0)
        return min_changes
                
