# Time complexity: O(n)

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    unique = set()

    for x in nums:
      if x in unique:
        return True
      else:
        unique.add(x)
    return False
