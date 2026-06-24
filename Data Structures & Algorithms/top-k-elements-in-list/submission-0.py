from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = Counter(nums)
        numSort = sorted(numCount, key = lambda x : numCount[x], reverse = True)
        slicenum = numSort[:k]
        return slicenum