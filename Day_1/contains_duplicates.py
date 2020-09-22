class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # -------------------------------------------------
        
        # FIRST SOLUTION -- O(n^2) -- complete -- too slow
        # loop through the list starting from the 0th index
        # loop through the list starting from the 1st index
        # compare the first loop to the second loop 
        # if they equal each other return true else false
        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         # print(nums[i], nums[j])
        #         if nums[i] == nums[j]:
        #             return True
                
        # return False
    
        # -------------------------------------------------
        
        # SECOND SOLUTION -- O(n) -- complete -- very fast
        # remove all dups from the list
        # if the remove_dup set is less than 
        
        remove_dups = set(nums)
        
        if len(remove_dups) < len(nums):
            return True
        else: 
            return False
        
                
            