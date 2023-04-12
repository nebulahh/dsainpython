# Time complexity: O(n)
# nums = [100,4,200,1,3,2]

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    # the list will be partly "sorted" when passed to set()
    numSet = set(nums)
    longest = 0
    # iterate over the set once: the first num   
    for x in numSet:
      if x - 1 not in numSet:
        # if first integer minus 1 not in numSet
        y = x + 1
        while y in numSet:
          y += 1
        longest = max(longest, y - x)
    return longest
