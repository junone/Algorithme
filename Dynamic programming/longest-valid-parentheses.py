class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        stack.append(-1)
        longest=0;
        for i in range(len(s)):
            if i==0:
                stack.append(i)
            else:
                if s[stack[-1]]=="(" and s[i]==")" and stack[-1]!=-1:
                    stack.pop()
                else:
                    stack.append(i)
                longest=max(i-stack[-1],longest)
        return longest



#In order to solve this problem with in O(n)'s time. A stack wiil be used to store the index of char.if the last char is "(" and the 
# New char is ")" the index of the last char will be poped from the stack. Otherwise the new char's index will be pushed into the stack.
#The index right now minus the last number saved in the stack means the longest vaid parenthesis up to now. 
#The problem will be solved in one pass.
# -1 in the stack represent the stack is empty.