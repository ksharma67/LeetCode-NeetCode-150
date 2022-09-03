class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtracking(nums,target,path):
            if target<0:
                return
            if target==0:
                res.append(path)
                return 
            for i in range(len(nums)):
				# this is step is very important , to prevent 1,2,5 1,2,5 for several times
                if i>0 and nums[i]==nums[i-1]:
                    continue
                backtracking(nums[i+1:],target-nums[i],path+[nums[i]])
        
        res=[]
        backtracking(sorted(candidates),target,[])
        return res
