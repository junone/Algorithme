class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[False for i in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0]=True
        # * can match empty string if * is the first char
        for j in range(1,len(p)+1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='?'or s[i-1]==p[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=(dp[i][j-1] or dp[i-1][j])
                else:
                    dp[i][j]=False
        return dp[len(s)][len(p)]
#https://www.youtube.com/watch?v=DSJ9kFsA_gs

                    