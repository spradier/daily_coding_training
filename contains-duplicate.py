class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashset = set()
        for el in nums:
            if el in hashset:
                return True
            hashset.add(el)
        return False