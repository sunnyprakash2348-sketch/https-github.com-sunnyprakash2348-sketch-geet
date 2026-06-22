class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        x=str(n)
        x=x[::-1]
        x=int(x)
        c=0
        if n==0:
            c=0
        elif n>x:
            for a in range(x,n+1):
                d=0
                for b in range(2,a//2+1):
                    if a%b==0:
                        d+=1
                        break
                if d==0 and a!=1:
                    c+=a
                else:
                    pass
        else:
            for a in range(n,x+1):
                d=0
                for b in range(2,a//2+1):
                    if a%b==0:
                        d+=1
                        break
                if d==0 and a!=1:
                    c+=a
                else:
                    pass
        return(c)