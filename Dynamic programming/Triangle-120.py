class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle)==0:
            return 0
        else:
            if len(triangle)==1:
                return max(triangle[0])
            else:
                pathSumOld=triangle[0]
                for i in range(1,len(triangle)):
                    pathSumNew=triangle[i]
                    pathSumNew[0]=pathSumNew[0]+pathSumOld[0]
                    pathSumNew[-1]=pathSumNew[-1]+pathSumOld[-1]
                    for j in range(1,len(triangle[i])-1):
                        pathSumNew[j]=min(pathSumOld[j-1]+pathSumNew[j],pathSumNew[j]+pathSumOld[j])
                    pathSumOld=pathSumNew
                return min(pathSumOld)
#two list will be used to save sum of each path. They are pathSumOld and pathSumNew
#The program will browse the triangle from the top to the bottom and calculate every path's sum.
#Finally, we only need to return the min value of the latest path list(which means reach the bottom of the triangle).
#The most difficult part of this problem is when we update the first item and the last item of the pathSumNew. We should calculate 
#the value sepretarly because the old list only one path to the first item and the last item of the new pathSum list.