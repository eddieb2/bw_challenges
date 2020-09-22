class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ----------------------------------------------- #
        #           Solution 1: Brute Force  O(n^2)       #
        # ----------------------------------------------- #
        
        # NOTES:
        # 2 nested loops. 
        # first loops starts from the 0th index
        # second loops start from the 1st index
        # calc sum for each pair, if it equals the target return the indicies
        # [2,7,11,15] => 2,7 => 2,11 => 2,15 => 7,11 => 7,15 => 11,15
        
        # for i in range(len(nums)):
        #     for x in range(i+1,len(nums)):
        #         sum = nums[i] + nums[x]
        #         if sum == target:
        #             return [i,x]
                
        # ----------------------------------------------- #
        #        Solution 2: Two-pass Hash Table O(n)     #
        # ----------------------------------------------- #
        
        # NOTES:
        # store all values of the list into a hash table
        # loop through list and check if it's compliment exists in the hash table
#         hash = {}
                
#         for index, val in enumerate(nums):
#             if val not in hash:
#                 hash[val] = index
        
#         for index, val in enumerate(nums):
#             # find complement for the cur itr
#             complement = target - nums[index]
#             # check if complement is in the hash
#             if complement in hash:
#                 # check that the complement's index isn't cur itr's index
#                 if hash[complement] != index:
#                     return [index, hash[complement]]
                
        # ----------------------------------------------- #
        #        Solution 3: One-pass Hash Table O(n)     #
        # ----------------------------------------------- #
        
        hash = {}
        
        for index, val in enumerate(nums):
            complement = target - nums[index]
            
            if val not in hash:
                hash[val] = index
            
            if complement in hash: 
                if hash[complement] != index:
                    return [index, hash[complement]]