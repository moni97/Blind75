def productExceptSelf(self, nums: List[int]) -> List[int]:
      len_list = len(nums)
      result = [1] * len_list
      postfix = 1
      prefix = 1
      for i in range(0, len_list):
          result[i] = prefix
          prefix *= nums[i]
      for i in range(len_list - 1, -1, -1):
          result[i] *= postfix
          postfix *= nums[i]
      return result
