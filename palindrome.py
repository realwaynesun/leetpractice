class Solution:
    def ispalidnrome(self,x:int):
        if x < 0:
            return False
        reversedNum, tmp = 0, x
        while tmp:
            reversedNum = reversedNum*10 + tmp%10
            tmp //= 10
        return x == tmp