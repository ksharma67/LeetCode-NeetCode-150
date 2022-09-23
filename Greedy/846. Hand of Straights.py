class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        d={}
        for i in hand:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        while d:
            mn=min(d.keys())
            for i in range(groupSize):
                if (mn+i) in d:
                    if d[mn+i]==1:
                        del d[mn+i]
                    else:
                        d[mn+i]-=1
                else:
                    return False
        return True
