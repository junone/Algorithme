class Solution:    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        largestRectangle=0
        for k in range(len(matrix)):
            heightList=[0 for i in range(len(matrix[0]))]
            for j in range(len(matrix[0])):
                if  matrix[k][j]=="0":
                    heightList[j]=0
                else:
                    i=k
                    while matrix[i][j]!="0" and i>=0:
                        heightList[j]+=1
                        i-=1
            print(heightList)
            stack=[]
            heightList.append(0)
            for i in range(len(heightList)):
                while(len(stack) and heightList[stack[-1]]>=heightList[i]):
                    cur=stack[-1] # the top element of the stack
                    stack.pop()
                    if len(stack):
                        largestRectangle=max(largestRectangle, heightList[cur] * (i - stack[-1]- 1))
                    else:
                        largestRectangle=max(largestRectangle, heightList[cur] * i)
                stack.append(i) 
        return largestRectangle

#Each row and all rows above it can be treated as a histgrom. We can solve this problem by using the function of largest rectangle row by row.
#At first heights of the histgrom start from each row to the top will be calculated.
#if we have 5 rows in the matrix we will have 5 height lists. 
#During the process of calculating histgroms' height,  the most tricky part we met is that there should not have zero in histgroms.Which means that histgroms are made up of continues 1.
# if the bottom of the column is zero than the height of it will be zero, Otherwise, we will adding 1 to the height by checking the column row by row,from the bottom to the top, until we meet the first zero. 
#The second part of the program is calculate the largest Rectangle in the histgrom, we can use the function from leetcode 84 directly
