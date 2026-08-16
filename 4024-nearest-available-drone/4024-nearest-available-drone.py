class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        a=[]
        
        for x in drones:
            if((abs(x[0]-target[0])+abs(x[1]-target[1]))<=x[2]):
                a.append(abs(x[0]-target[0])+abs(x[1]-target[1]))
            else:
                a.append(-1)
        b=max(a)
        for x in a:
            if(x==-1):
                a[a.index(x)]=b+1
            else:
                pass
        if(b+1 in a):
            if(a.count(max(a))==len(a)):
                return(-1)
            else:
               return(a.index(min(a))) 
        else:
            return(a.index(min(a)))