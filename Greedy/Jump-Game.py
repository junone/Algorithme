class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)<=1:
            return True
        else:
            maxReach=1+nums[0]
            i=0
            while i<maxReach and i<len(nums):
                maxReach=max(maxReach,i+1+nums[i])
                i+=1
            return (maxReach>=len(nums))

# The program will browsing the list from the bottom to the end and calculating the maxinum index step by step
# when the index for search reached the maxinum index. the search process will stop and return the maxinum index can be reached.