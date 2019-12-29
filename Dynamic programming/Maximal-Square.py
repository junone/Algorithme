class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        largestSquare=0
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        dp=[[0 for j in range(len(matrix[0]))]for i in range(len(matrix))]
        print(matrix)
        for j in range(len(matrix[0])):
            dp[0][j]=int(matrix[0][j])
        for k in range(len(matrix)):
            dp[k][0]=int(matrix[k][0])
        largestSquare=max(max(dp))*max(max(dp))
        if len(matrix)==1 or len(matrix[0])==1:
            return max(max(dp))
        else:
            for i in range(1,len(matrix)):
                for j in range(1,len(matrix[0])):
                    if int(matrix[i][j])==1:
                        dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+int(matrix[i][j])
                        largestSquare=max(largestSquare,dp[i][j]*dp[i][j])
        return largestSquare
# the transfer function for this problem is easy to understand
#dp is the array used to save the side length of square.
#matrix[i][j] represent the right bottom corner of the square.dp[i][j] is its side length.
# We only need to consider the item on its left(the square on the left ),
# on its top(square on the top) and on its top left(the square on the top left).
# if matrix[i][j] is one then the side length for the square  
#will be the mininum side length of those square plus one.
# if matrix[i][j] is zero, there will be no square.

#for example if dp[i-1][j-1],dp[i][j-1],and dp[i-1][j] are all 1. It means that there are three square whose side length is 1 around matrix[i][j]. 
#If matrix[i][j] is one, dp[i][j] will be 1+1=2,  there exist a Square whose side length=2.