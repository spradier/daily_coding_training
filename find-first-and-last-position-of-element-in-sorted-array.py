class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        
        if len(nums) == 0:
            return [-1, -1]
        
        while (low < high):
            mid = low + ((high - low)//2)
            
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
                
        if target == nums[low]:
            i = nums.count(target)
            return [low, low+i-1]
        
        else:
            return [-1, -1]