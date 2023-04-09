class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # create 2d array: [[], [], [], [], [], [], []]
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
          if n not in count:
            count[n] = 1
          else:
            count[n] += 1

        for val, count in count.items():
            freq[count].append(val)

        res = []
        # looping backward
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
