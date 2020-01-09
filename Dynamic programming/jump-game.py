class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(list(nums))<=1:
            return True
        dp=[0 for i in range(len(nums))]
        for i in range(1,len(nums)):
            dp[i]=max(dp[i-1]-1,nums[i-1]-1)
        if min(dp)==-1:
            return False
        else:
            return True
# The transfer function is used to calculate the remain jump length for each position
# If the remain jump length for either position is negative. we can not reach the last position
# The remain jump length for current positoin is related with the jump length of the positon before current positon and 
# current position's jump length