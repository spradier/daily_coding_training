class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exp_val = []
        for i in range(len(nums)):
            if nums[i] in exp_val:
                out = [exp_val.index(nums[i]), i]
            else:
                exp_val.append(target-nums[i])
                
        return out