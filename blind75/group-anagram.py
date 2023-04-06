# Time Complexity: n log n 

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)

    for val in strs:
      key = "".join(sorted(list(val)))
      res[key].append(val)

    return [l for l in res.values()]
