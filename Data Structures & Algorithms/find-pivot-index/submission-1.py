class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left, leftsum = 0, 0
        for i in range(len(nums)):
            total -= nums[left]
            if leftsum == total:
                return left
            else:
                leftsum += nums[left]
                left += 1
                
        return -1
        