class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        remove=0
        intervals.sort()
        last=0
        for i in range(1,len(intervals)):
            if intervals[last][1]>intervals[i][0]:
                remove+=1
                if intervals[last][1]>intervals[i][1]:
                    last=i
            else:
                last=i
        return remove

#at first we sort the interval list and check the interval from bottom to the top.
#if the end of current interval  is larger than the start of next interval
# we will delete the interval with the higher end. last is used to save the interval with lower end.

