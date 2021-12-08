from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_dict = {}
        for index, value in enumerate(nums):
            my_dict[value] = index

        
        i = 0
        while target - nums[i] not in my_dict or my_dict[target-nums[i]] == i:
            i += 1

        return [i, my_dict[target - nums[i]]]
