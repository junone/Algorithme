class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        else:
            dp=[1 for i in range(len(nums))]
            for i in range(0,len(nums)):
                for j in range(i):
                    if nums[i]>nums[j]:
                        dp[i]=max(dp[i],dp[j]+1)
            return max(dp)
#dp is an list used to save the length of each subsequence.
# dp[i] will be equal to dp[j]+1 when dp[j]<dp[i]. This is the transfer function and will cover every conditon from the bottom to the top
# of the list.