class Solution:
    def integerBreak(self, n: int) -> int:
        if n==1:
            return 0
        else:
            dp=[1 for i in range(n+1)]
            dp[0]=0
            for i in range(n+1):
                for j in range(n+1-i):
                        dp[i+j]=max(dp[i]*j,dp[i+j],i*j)
        return dp[n]
#the transfer function for this problem is easy to understand
#dp[i+j] is the max product of number i+j. it must be the maxinum value of dp[i]*j or i*j or its original value
# the transfer function will cover every possible condition
#  the last item of dp list is the value we want to return it represent the maxinum product for current number