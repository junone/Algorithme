class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        else:
            list1=nums[:len(nums)-1]
            list2=nums[1:len(nums)]
            maxSum1=list1[0]
            maxSum2=max(list1[0],list1[1])
            for i in range(2,len(nums)-1):
                temp=maxSum2
                maxSum2=max(maxSum1+list1[i],maxSum2)
                maxSum1=temp
            max1=maxSum2
            maxSum1=list2[0]
            maxSum2=max(list2[0],list2[1])
            for i in range(2,len(nums)-1):
                temp=maxSum2
                maxSum2=max(maxSum1+list2[i],maxSum2)
                maxSum1=temp
            max2=maxSum2
            return max(max1,max2)
            
# This question is a upgrade of the qusetion house robber, the first house and the last house should not be robbered
#at the same time.
#There are two conditions.The list without the first value and the list without the last value
#We can solve this problem by finding the maxinum value of the list without the last house and compare the value with the
#maxinum value of the list without the first house
#the larger one will be the answer to the qusetion