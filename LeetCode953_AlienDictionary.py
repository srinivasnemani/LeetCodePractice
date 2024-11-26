from typing import List

words = ["hello", "leetcode"],
order = "hlabcdefgijkmnopqrstuvwxyz"


def isAlienSorted(words, order):
    alien_dict = {char: num for num, char in enumerate(order)}
    print(alien_dict)

    def compare_words(word1, word2):
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                return alien_dict[c1] - alien_dict[c2]
        return len(word1) - len(word2)

    for i in range(len(words) - 1):
        if compare_words(words[i], words[i + 1]) > 0:
            return False
    return True

ans = isAlienSorted(words, order)
print(ans)