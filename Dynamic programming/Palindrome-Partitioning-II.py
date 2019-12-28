class Solution:
    def minCut(self, s: str) -> int:
        if len(s)==0:
            return 0
        else:
            dp=[-2 for i in range(len(s)+1)]
            #-2 is a sign of initializing
            dp[0]=-1
            for i in range(len(s)):
                #odd
                l=0
                while i+l<len(s) and i-l>=0 and s[i+l]==s[i-l]:
                    if dp[i+l+1]==-2:
                        dp[i+l+1]=1+dp[i-l]
                    else:
                        dp[i+l+1]=min(dp[i+l+1],1+dp[i-l])
                    l+=1
                #even
                l=0
                while i+l+1<len(s) and i-l>=0 and s[i+1+l]==s[i-l]:
                    if dp[i+l+2]==-2:
                        dp[i+l+2]=1+dp[i-l]
                    else:
                        dp[i+l+2]=min(dp[i+l+2],1+dp[i-l])
                    l+=1
        return dp[len(s)]
# the most difficult part of this problem is to find the transfer function
# at first we initialize the dp array ,whose length is n+1, with -2 it is a sign of initialize.
# The first item is -1, suppose that there is only one charactor in the string. there will be only one palindorme string and we do not need to cut the string
# The result will be -1 +1=0. In a word, the -1 was used to Offset extra strings.
# we will use this array to save how many times we need to cut the original string.
# We treat every item in the orignal string as the middel charactor of a palindrome substring.
# There are two conditions for transfer function:
# The first conditon is the palindrome substring's length is odd :
# the dp array will be updated by using the index i+1+1.Index i is index of the middle charactor of 
#a palindrome substring, if the substring from s[i-l] to s[i+l] is palindrome string then we get to know the numbers of cuts will be either 1+dp[i-l] or unchanged
#(dp[i-l] represent the minimum cuts of string from s[0] to s[i-l]).Why the dp[i+l+1]'s value sometime will not be changed, beacuse
# we may already update its value in the past process, and it is small then 1+dp[i-l].
# The second condition is the palindrome substring's length is even:
# the process is similar to the process above for odd length palindrome substring.
# After checking the original string from the first item to the last item, the last item of dp array will be returned by  the function
# It represent the minium cuts for the orignal string.