def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minNum = float("infinity")
        while l <= r:
            if nums[l] < nums[r] and nums[l] < minNum:
                minNum = nums[l]
                return minNum
            mid = (l + r) // 2    
            if nums[mid] < minNum:
                minNum = nums[mid] 
            print(minNum)
            if nums[l] <= nums[mid]:
                l = mid + 1
            else: r = mid - 1
        return minNum
