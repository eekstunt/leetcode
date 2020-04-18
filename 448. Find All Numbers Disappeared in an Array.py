#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        nums = set(nums)
        for i in range(1, n + 1):
            if i not in nums:
                result.append(i)
        return result
        
