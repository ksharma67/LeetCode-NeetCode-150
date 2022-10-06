class Solution:
    def mergeTriplets(self, e: List[List[int]], target: List[int]) -> bool:
        t=[]
        for i in range(len(e)):
            if(e[i][0]>target[0] or e[i][1]>target[1] or e[i][2]>target[2]):
                    pass
            else:
                t.append([e[i][0],e[i][1],e[i][2]])
                
        if(len(t)>0):        
            p1=t[0][0]
            p2=t[0][1]
            p3=t[0][2]
            for i in range(len(t)):    
                p1=max(t[i][0],p1)
                p2=max(t[i][1],p2)
                p3=max(t[i][2],p3)
                ok=[p1,p2,p3]
                if(ok==target):
                    return True
        return False
