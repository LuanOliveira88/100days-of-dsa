from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        expectedNums = []
        auxList = []
        for num in nums:
            if num not in expectedNums:
                expectedNums.append(num)
            else:
                auxList.append(num)
        nums = expectedNums + auxList
        k = len(expectedNums)
        return k
    

if __name__ == '__main__':
    Solution().removeDuplicates([1,1,2])
