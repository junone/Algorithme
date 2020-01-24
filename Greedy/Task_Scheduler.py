# -*- coding: utf-8 -*-
# @Author: junone
# @Date:   2020-01-22 11:58:32
# @Last Modified by:   junone
# @Last Modified time: 2020-01-24 10:10:41
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskSet=list(set(tasks))
        countList=[]
        countMax=0
        for item in taskSet:
            countList.append(tasks.count(item))
        maxLength=max(countList)
        countMax=countList.count(maxLength)
        empty=(maxLength-1)*(n-countMax+1)
        remain=len(tasks)-countMax*(maxLength)
        if remain>empty:
            return (maxLength-1)*(n+1)+countMax+remain-empty
        else:
            return (maxLength-1)*(n+1)+countMax
#At first how many times the most frequent task's will run is calculated. Other task wich the same frequence will also be counted
#It helped us to calculated the empty places we have between thest high frequency tasks
#if the number of empty place is lower than remain tasks, we just need to add the number of tasks that id minused by number of empty places
#Or we just need to return the frequence of the most frequent tasks times n.
