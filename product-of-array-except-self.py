class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)
        curr = 1

        for i in range(len(nums)):
            out[i] = curr
            curr *= nums[i]

        curr = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] *= curr
            curr *= nums[i]

        return out