class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        y=nums[::-1]
        nums=nums+y
        return(nums)