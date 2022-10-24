class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        total = len(A)+len(B)
        half = total//2
        if(len(B)<len(A)):
            A,B = B,A
        l,r = 0,len(A)-1
        ans = 0
        while(True):
            i = (l+r)//2
            j = half - i - 2
            Aleft = A[i] if i>=0 else float('-inf')
            Aright = A[i+1] if i+1<len(A) else float('inf')
            Bleft = B[j] if j>=0 else float('-inf')
            Bright = B[j+1] if j+1<len(B) else float('inf')
            print(i,j,Aleft,Aright,Bleft,Bright)
            if(Aleft<=Bright and Bleft<=Aright):
                if(total%2==0):
                    ans = (max(Aleft,Bleft) + min(Aright,Bright))/2
                    return ans
                else:
                    ans = min(Aright,Bright)
                    return ans
            elif(Aleft>Bright):
                r = i-1
            else:
                l = i+1
