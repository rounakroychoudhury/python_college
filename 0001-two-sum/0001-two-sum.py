class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            a=i
            for j in range (i+1, len(nums)):
                b=j
                if (nums[a]+nums[b]) == target:
                    return [a,b]
        return (-1,-1)