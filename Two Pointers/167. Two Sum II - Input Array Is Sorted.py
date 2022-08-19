class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        while(start<end):
            if(numbers[start]+numbers[end]>target):
                end -= 1
            elif(numbers[start]+numbers[end]<target):
                start += 1
            else:
                return [start+1,end+1]
        return []        
        
