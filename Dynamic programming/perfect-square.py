class Solution:
    def numSquares(self, n: int) -> int:
        dp=[5 for i in range(n+1)]
        dp[0]=0
        for i in range(n):
            j=1
            while j*j+i<=n:
                dp[i+j*j]=min(dp[i+j*j],dp[i]+1)
                j=j+1
        return dp[n]
# the transfer function for this problem is dp[i+j*j]=dp[i]+1
#every integer can be made up of at most 4 square numbers so we can initialize the dp list with number 5