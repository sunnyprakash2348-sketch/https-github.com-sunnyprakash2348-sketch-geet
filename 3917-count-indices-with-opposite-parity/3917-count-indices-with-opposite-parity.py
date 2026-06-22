class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        y=nums
        n=len(nums)
        x=[]
        for a in range(n):
            if nums[a]%2==0:
                c=0
                for b in y:
                    if b%2!=0:
                        c+=1
                x.append(c)
                y=y[1:]
            else:
                c=0
                for b in y:
                    if b%2==0:
                        c+=1
                x.append(c)
                y=y[1:]
        return(x)