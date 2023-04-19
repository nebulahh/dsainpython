# Time complexity: O(n squared)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lo = 1
        hi = len(nums)-1
        res = []
        
        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx -1]:
                continue
            lo = idx +1
            hi = len(nums) -1
            
            while lo < hi:
                summ = val + nums[lo] + nums[hi]
                if summ > 0:
                    hi -= 1
                elif summ < 0:
                    lo += 1
                else:
                    res.append([val, nums[lo], nums[hi]])
                    lo += 1
                    while nums[lo] == nums[lo - 1] and lo < hi:
                        lo += 1
        return res   
