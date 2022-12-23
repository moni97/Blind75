def search(self, nums: List[int], target: int) -> int:
        move, mid = 0, -1

        while move + 1 < len(nums) and nums[move] < nums[move + 1]:
            move += 1
        
        l, r = 0, 0
        if move == len(nums) - 1:
            l = 0
            r = move
        elif nums[0] <= target <= nums[move]:
            l = 0
            r = move
        elif nums[move + 1] <= target <= nums[len(nums) - 1]:
            l = move + 1
            r = len(nums) - 1
        
        while l < len(nums) and r < len(nums) and l <= r:
            mid = (r + l) // 2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid
        return -1
