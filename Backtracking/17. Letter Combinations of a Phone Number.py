class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        number = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        
        ans = [""]
        
        for i in digits:
            temp = []
            for j in ans:
                for k in number[i]:
                    temp.append(j+k)
            ans = temp
        
        return ans
