class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        m_sum = nums[0]
        curr = 0
        for n in nums:
            if curr < 0:
                curr = 0
            curr += n
            m_sum = max(curr, m_sum)
        return m_sum