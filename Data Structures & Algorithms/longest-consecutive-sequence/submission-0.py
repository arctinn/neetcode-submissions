class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        sortednums = sorted(list(set(nums)))
        maxcounter = 1
        counter = 1
        for i in range(len(sortednums) - 1):
            if sortednums[i + 1] == sortednums[i] + 1:
                counter += 1
            else:
                counter = 1
            if counter > maxcounter:
                maxcounter = counter
        return maxcounter