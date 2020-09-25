class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # ------------------------------------ #
        #         SOLUTION 1: Linear Search    #
        # ------------------------------------ #

        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1

        # ------------------------------------ #
        #         SOLUTION 1: Binary Search    #
        # ------------------------------------ #