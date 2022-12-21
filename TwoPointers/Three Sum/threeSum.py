def threeSum(self, nums: List[int]) -> List[List[int]]:
      res = []
      nums.sort()
      len_nums = len(nums)
      if len(nums) < 3:
          return res
      for i, a in enumerate(nums):
          print(i, a)
          if i > 0 and a == nums[i - 1]:
              continue
          l = i + 1
          r = len_nums - 1
          while l < r:
              sums = a + nums[l] + nums[r]
              if sums > 0:
                  r -= 1
              elif sums < 0:
                  l += 1
              else:
                  res.append([a, nums[l], nums[r]])
                  l += 1
                  while l < r and nums[l] == nums[l-1]:
                      l += 1
      return res
