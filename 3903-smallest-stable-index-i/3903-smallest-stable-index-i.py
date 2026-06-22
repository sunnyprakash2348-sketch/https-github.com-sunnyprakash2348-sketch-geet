class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        z=len(nums)
        b=0
        if z==1:
            return 0
        else:
            for a in range(z):
                if a==0:
                    if nums[0]-min(nums[1:])<=k:
                        return 0
                        break
                    else:
                        pass
                elif max(nums[:a])-min((nums[a:]))<=k:
                    b=a
                    break
            if b==0:
                return -1
            else:
                return b
                