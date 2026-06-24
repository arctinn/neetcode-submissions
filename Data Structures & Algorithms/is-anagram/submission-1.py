from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic = Counter(s)
        tdic = Counter(t)

        if sdic == tdic:
            return True
        return False