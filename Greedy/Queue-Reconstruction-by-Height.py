# -*- coding: utf-8 -*-
# @Author: junone
# @Date:   2020-01-22 10:38:00
# @Last Modified by:   junone
# @Last Modified time: 2020-01-22 11:12:18
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=(lambda x:[x[0],-x[1]]),reverse=True)
        newList=[]
        for item in people:
            newList.insert(item[1],item)
        return newList
#At first we sorted the sequence by people's height. Higher person will be placed in the front. If two peoples' height ara the same.
#the person with lower K value will be placed in the front.
#Then we just need to construct a new new list. And insert person by using each person's k value as the index.