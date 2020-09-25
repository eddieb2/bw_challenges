class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # ------------------------------------ #
        #       SOLUTION 1:  O(n^2)            #
        # ------------------------------------ #

        # NOTES:
        # sort nums
        # nested for loops
        # track prev
        # make prev 1 step behind the inner for loop
        # if prev == nums[x], return the number

        #         nums.sort()
        #         print(nums)

        #         for i in range(len(nums)):
        #             prev = None
        #             for x in range(i+1, len(nums)):
        #                 prev = nums[x-1]
        #                 if prev == nums[x]:
        #                     return nums[x]

        # ------------------------------------ #
        #       SOLUTION 2:  O(n)              #
        # ------------------------------------ #

        # add all items to a hash map
        # key = num, value = count, index
        hash_map = {}

        # O(n)
        # Loop over nums
        for i in range(len(nums)):
            # O(1)
            # If num isn't in the hash map, add it as a key, with count and index as the value
            if nums[i] not in hash_map:
                hash_map[nums[i]] = [0, i]
            # O(1)
            # If the num is in the hash map, increment the count
            if nums[i] in hash_map:
                hash_map[nums[i]][0] += 1
                # O(1)
                # If the count is 2, there is a duplicate, return the num from nums which is the key's value's 1st index
                # nums[hash_map[nums[i]][1]]
                #      hash key=^num ->  ^nums index
                if hash_map[nums[i]][0] == 2:
                    return nums[hash_map[nums[i]][1]]
