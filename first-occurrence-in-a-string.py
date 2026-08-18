class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
  
        len_hay=len(haystack)
        len_need=len(needle)

        for i in range(len_hay-len_need +1):
            if haystack[ i: i + len_need]  == needle:
               return i
        
        return -1
           
