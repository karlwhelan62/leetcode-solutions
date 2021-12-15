from typing import List

class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:

        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]

        return k + 1   
    


def main():
    test_obeject = Solution()
    print(test_obeject.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

if __name__ == "__main__":
    main()