class Solution(object):
    def search(self, nums, target):
        
        high = len(nums)-1
        low = 0
        mid = 0
        while high >= low:
            mid = (high+low)//2
            if nums[mid] > target:
                high = mid -1
            elif nums[mid] < target:
                low = mid +1
            else:
                return mid
        return -1
    
        