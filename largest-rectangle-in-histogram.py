class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largestRectangle=0
        stack=[]
        heights.append(0)
        for i in range(len(heights)):
            while(len(stack) and heights[stack[-1]]>=heights[i]):
                cur=stack[-1] # the top element of the stack
                stack.pop()
                if len(stack):
                    largestRectangle=max(largestRectangle, heights[cur] * (i - stack[-1]- 1))
                else:
                    largestRectangle=max(largestRectangle, heights[cur] * i)
            stack.append(i)
        return (largestRectangle)


# monotone stack will be used to save the index of heights,once the next height is lower than stack's top's height
# the index saved in the stack will be poped until the top's height is bigger or equal to the next height. The area of the rectangle will be caluclated
# at the same time. The largestRectangle's area will be saved.
# the current height is higher than the top's height is a sign of poping out 
# By using the stack, the program will use less memory