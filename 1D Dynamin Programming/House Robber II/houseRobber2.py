def rob(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 0:
        return 0
    def houseRob(nums):
        rob1, rob2 = 0, 0
        for n in nums:
            tmp = max(rob1 + n, rob2)
            rob1, rob2 = rob2, tmp
        return rob2
    print(nums[:len(nums)-1])
    return max(houseRob(nums[:len(nums)-1]), houseRob(nums[1:]))
