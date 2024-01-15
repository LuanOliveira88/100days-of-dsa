from typing import List 

#Brute Force implementation
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    break


if __name__ == '__main__':
    case1 = {'nums': [2,7,11,15], 'target': 9, 'output': [0,1]}
    case2 = {'nums': [3, 2, 4], 'target': 6, 'output': [1,2]}
    case3 = {'nums': [3,3], 'target': 6, 'output': [0,1]}
    cases = [case1, case2, case3]

    for case in cases:
        assert Solution().twoSum(nums=case['nums'], target=case['target']) == case['output']