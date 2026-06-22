class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        b=[]
        for a in range(1,n+1):
            if a%3==0 and a%5==0:
                b.append("FizzBuzz")
            elif a%3==0:
                b.append("Fizz")
            elif a%5==0:
                b.append("Buzz")
            else:
                b.append(str(a))
        return b