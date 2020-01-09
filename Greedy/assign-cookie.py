class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        contentNumber=0
        g.sort()
        s.sort()
        i=0
        j=0
        while s and g and j<len(s) and i<len(g):
            if s[j]>=g[i]:
                i+=1
                j+=1
                contentNumber+=1
            else:
                j+=1
        return contentNumber
# The program will always assgin the shortest cookie to the child 
#having the minimum size of greed factor at first
