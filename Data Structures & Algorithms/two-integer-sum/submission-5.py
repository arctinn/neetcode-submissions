class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
 
        
        for i in range(len(nums) - 1):
            left, right = i, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] != target:
                    right -= 1
                else:
                    return [left, right]
        
       
    