class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s)==0:
            return 0
        sumAll=0
        for i in range(len(s)):
            # odd
            n=i
            m=i
            while n>=0 and m<len(s) and s[m]==s[n]:
                m+=1
                n-=1
                sumAll+=1
            #even
            x=i
            y=i+1
            while x>=0 and  y<len(s) and s[x]==s[y]:
                x-=1
                y+=1
                sumAll+=1
        return sumAll
#Every charactor in the string will be treated as the middle charactor of a palindromic string. 
#Then the program will check charactors on both side of that middle item. 
#There are two condition:
#odd :One charactor can be a palindromic string, if characotrs on both side of it are equal, the they can be treated as palindormic string
#even : if two charactors are close to each other and they are equal, They are palindormic string. the program will check 
#both side of the palindormic string.
#By checking the string from left to right and take odd and even palindromic string into consideration. The program will cover every condition.