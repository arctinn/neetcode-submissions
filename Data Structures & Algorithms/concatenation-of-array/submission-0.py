class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        dupnums = nums
        newnums = nums + dupnums
        return newnums