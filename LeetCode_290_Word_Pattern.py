class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        chars = list(map(str, pattern))
        pw = s.split(" ")

        if not len(pattern) == len(pw):
            return False

        if not len(set(pattern)) == len(set(pw)):
            return False

        pd = {}

        for idx, char in enumerate(chars):
            matching_word = pd.get(char)
            if matching_word is None:
                pd[char] = pw[idx]
            else:
                if matching_word == pw[idx]:
                    continue
                else:
                    print("Not correct")
                    return False
        return True        
