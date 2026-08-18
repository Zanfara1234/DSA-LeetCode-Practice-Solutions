class Solution(object):
    def lengthOfLastWord(self, s):
        length=0
        for i in reversed(range(len(s))):
            if s[i] != ' ':
                length+=1
            elif length >0:
                return length

        return length
        
