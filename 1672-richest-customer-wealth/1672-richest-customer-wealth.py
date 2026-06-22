class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        b=0
        for a in accounts:
            if b>=sum(a):
                pass
            else:
                b=sum(a)
        return b