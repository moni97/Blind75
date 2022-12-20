def longestConsecutive(self, nums: List[int]) -> int:
    setNums = set(nums)
    maxLen = 0
    for n in nums:
        if (n - 1) not in setNums:
            length = 1
            while (n + length) in setNums:
                length += 1
            maxLen = max(length, maxLen)
    return maxLen
