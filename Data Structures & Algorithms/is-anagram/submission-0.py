class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic = {}
        for letter in s:
            if letter in sdic:
                sdic[letter] += 1
            else:
                sdic[letter] = 1

        tdic = {}
        for letter in t:
            if letter in tdic:
                tdic[letter] += 1
            else:
                tdic[letter] = 1
        
        if sdic == tdic:
            return True
        else:
            return False