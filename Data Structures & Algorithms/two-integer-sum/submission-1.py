class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for index, value in enumerate(nums):
            for j , v in enumerate(nums):
                if index != j and (value + v == target):
                    return [index, j]    
