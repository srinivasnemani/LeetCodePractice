class Solution:
    def firstUniqChar(self, s: str) -> int:
        uc = {}

        # Better start enumerate at -1 as first char is logged as -1 and duplicates are also marked as -1
        for pos, char in enumerate(s, 1):
            if char in uc.keys():
                uc[char] = -1
            else:
                uc[char] = pos-1
        print(uc)

        # Note sorted always returns a list. Convert this back to dictionary.
        uc_sorted = dict(sorted(uc.items(), key=lambda x:x[1]))
  

        for key, value in uc_sorted.items():
            if value == -1:
                continue
            else:
                return value
        return -1

        
