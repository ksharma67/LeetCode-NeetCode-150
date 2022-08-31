def genP(n, stack, s, ans, openingPCount):
    # check if length of generated parentheses string is greater than n
	if len(s) >= n:
	    # if stack is empty then the string is valid parentheses combination
        if not stack:
		    # add to ans array if string is valid
            ans.append(s)
        return
		
	# irrespective of the last elemnt added, we can add opening parenthesis to the string and stack 
	# only the count of opening parenthesis shouldn't be greater than half of n
	# a valid string will have equal number of opening and closing brackets equal to half of n
	if openingPCount < n//2:
		genP(n, stack+["("], s+"(", ans, openingPCount+1)
	
	# pop the last element from the stack
    p = stack.pop() if stack else None
	
	# if popped elemnt is None or ) then adding another ) to it would generate an invalid string, so we avoid it here
    if p and p == "(":
        genP(n, stack, s+")", ans, openingPCount)
        
        

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
		# pass 2*n as n to genP function
        genP(2*n, [], "", ans, 0)
        return ans
