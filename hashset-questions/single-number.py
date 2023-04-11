class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      uniqueList = set()
      
      for val in nums:
        if val in hashSet:
          uniqueList.discard(val)
        else:
          uniqueList.add(val)
      return list(uniqueList)[0]
          
