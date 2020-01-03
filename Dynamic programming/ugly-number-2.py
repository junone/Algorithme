class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i=0
        j=0
        k=0
        uglyNumberList=[1]
        while len(uglyNumberList)<n:
            minValue=min(uglyNumberList[i]*2,uglyNumberList[j]*3,uglyNumberList[k]*5)
            if minValue not in uglyNumberList:
                uglyNumberList.append(minValue)
            if minValue==uglyNumberList[i]*2:
                i+=1
            elif minValue==uglyNumberList[j]*3:
                j+=1
            else:
                k+=1
        return  uglyNumberList[-1]

#The transfer function for this problem is a little bit complex.
#we need three index representing the index of the ugly number used to compute the new ugly number for each factor.
#for example index i represent the index for factor 2. If the mininum value is uglyNumberList[i]*2 then 1 will be added to 1
#which means next ugly number times 2 will be used in the comperation
#The minValue calcualted from those three factors will be the next ugly number