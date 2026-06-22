class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        x = len(s)
        y = False
        for a in range(x - 1):
            if abs(int(s[a]) - int(s[a+1])) <= 2:
                y = True
            else:
                y = False
                break

        if y:
            return True
        else:
            return False