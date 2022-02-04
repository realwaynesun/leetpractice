class Solution:
    def ispalidnrome(self,x:int):
        if x < 0:
            return False
        reversedNum, tmp = 0, x
        while tmp:
            reversedNum = reversedNum*10 + tmp%10 # Get individual digits from right and put into correct postion in reversed number
            tmp //= 10 # Get the next last digit
        return x == tmp