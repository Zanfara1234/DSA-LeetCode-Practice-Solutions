class Solution(object):
    def isPalindrome(self, x):
        reversed_num=0
        a=x

        if x<0:
           return False

        while x:
            digit=x % 10
            reversed_num=(reversed_num*10) +digit
            x=x//10

        return a==reversed_num
        
