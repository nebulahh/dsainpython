class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    res = {}
    
    for idx, val in enumerate(nums):
      diff = target - val
      if diff in res:
        return [res[diff], idx]
      else:
        res[val] = idx
