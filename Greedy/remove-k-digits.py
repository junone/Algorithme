class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k>=len(num):
            return '0'
        while k>0:
            for i in range(1,len(num)):
                if num[i-1]>num[i]:
                    num=num[:i-1]+num[i:]
                    break
                if i==len(num)-1:
                    num=num[:i]
            k-=1
            if num[0]=='0':
                if len(num)==1:
                    return '0'
                else:
                    num=num[1:]
        return num
#We only need  to check the charactor from left to right 
#if the current number is larger than the number on it's right, we will remove that number
