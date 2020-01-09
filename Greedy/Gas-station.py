class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sumAll=0
        sumfromStart=0
        start=0
        for i in range(len(gas)):
            sumAll=sumAll+gas[i]-cost[i]
            sumfromStart=sumfromStart+gas[i]-cost[i]
            if sumfromStart<0:
                start=i+1
                sumfromStart=0
        if sumAll<0:
            return -1
        else:
            return start
#the only thing need to consider is that the total sum of gas should be larger or equal to the total sum of cost
# and the point from where we can go to the end of the list will be the start point